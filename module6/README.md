# Module 6: Complex Testbenches

This directory contains all examples, exercises, and test cases for Module 6, focusing on complex testbench construction including multi-agent environments, protocol verification, protocol checkers, multi-channel scoreboards, and layered testbench architectures.

## Directory Structure

```
module6/
├── examples/              # pyuvm examples for each topic
│   ├── multi_agent/       # Multi-agent environment examples
│   │   └── multi_agent_example.py
│   ├── protocol/          # Protocol verification examples
│   │   └── protocol_example.py
│   ├── protocol_checkers/ # Protocol checker examples
│   │   └── protocol_checker_example.py
│   ├── scoreboards/       # Multi-channel scoreboard examples
│   │   └── multi_channel_scoreboard_example.py
│   └── architecture/      # Testbench architecture examples
│       └── architecture_example.py
├── dut/                   # Verilog Design Under Test modules
│   └── protocols/         # Protocol modules for testing
│       └── axi4_lite_slave.v
├── tests/                 # Testbenches
│   └── pyuvm_tests/       # pyuvm testbenches
│       └── test_complex_testbench.py
└── exercises/             # Exercise solutions (if any)
```

## Prerequisites

Before running the experiments, ensure you have:

- **Python 3.8+** - Required for cocotb and pyuvm
- **Verilator 5.036+** - Required for simulation (5.044 recommended)
- **cocotb 2.0+** - Installed in virtual environment
- **pyuvm 4.0+** - Installed in virtual environment
- **Make** - For building and running tests

To verify your environment:

```bash
python3 --version        # Should be 3.8+
verilator --version      # Should be 5.036+
python3 -c "import cocotb; print(cocotb.__version__)"
python3 -c "import pyuvm; print(pyuvm.__version__)"
```

## Complex Testbench Examples

### 1. Multi-Agent Environment (`examples/multi_agent/multi_agent_example.py`)

Demonstrates multi-agent environment with agent coordination:

**Key Concepts:**
- Multiple agent instantiation
- Agent coordination using virtual sequences
- Multi-agent scoreboard integration
- Parallel agent execution
- Agent-specific transactions

**Multi-Agent Components:**

1. **MultiAgentAgent**
   - Agent with driver, monitor, and sequencer
   - Contains `agent_id` for identification
   - Generates agent-specific transactions
   - Connected to scoreboard

2. **MultiAgentScoreboard**
   - Scoreboard for multiple agents
   - Contains subscribers for each agent
   - Tracks transactions per agent
   - Reports agent-specific statistics

3. **MultiAgentSubscriber**
   - Subscriber for individual agent
   - Receives transactions from agent monitor
   - Forwards to parent scoreboard
   - Maintains agent-specific state

4. **MultiAgentVirtualSequence**
   - Virtual sequence coordinating multiple agents
   - Starts sequences on multiple sequencers in parallel
   - Uses `cocotb.start_soon()` for parallel execution
   - Waits for all sequences to complete

**Multi-Agent Patterns:**

**Agent Creation:**
```python
# Create multiple agents
self.agents = []
for i in range(3):
    agent = MultiAgentAgent.create(f"agent_{i}", self)
    agent.agent_id = i
    self.agents.append(agent)
```

**Scoreboard Connection:**
```python
# Connect each agent's monitor to scoreboard
for i, agent in enumerate(self.agents):
    agent.monitor.ap.connect(self.scoreboard.subscribers[i].analysis_export)
```

**Parallel Sequence Execution:**
```python
# Start sequences on multiple agents in parallel
tasks = []
for i, seqr in enumerate(self.agent_seqrs):
    seq = MultiAgentSequence(f"seq_agent_{i}", agent_id=i, num_items=3)
    task = cocotb.start_soon(seq.start(seqr))
    tasks.append(task)

# Wait for all sequences to complete
for task in tasks:
    await task
```

**Running the example:**

```bash
# Via module script
./scripts/module6.sh --multi-agent

# Or directly from example directory
cd module6/examples/multi_agent
make SIM=verilator TEST=multi_agent_example
```

**Expected Output:**
- Multiple agent creation and connection
- Parallel sequence execution
- Multi-agent coordination
- Agent-specific transaction tracking

### 2. Protocol Verification (`examples/protocol/protocol_example.py`)

Demonstrates AXI4-Lite protocol verification agent:

**Key Concepts:**
- AXI4-Lite protocol implementation
- Protocol-specific transaction classes
- Protocol-specific drivers and monitors
- Write and read transaction handling
- Protocol verification patterns

**AXI4-Lite Components:**

1. **AXI4LiteTransaction**
   - Transaction for AXI4-Lite operations
   - Fields: `addr`, `data`, `is_write`, `prot`, `strb`
   - Supports both read and write operations
   - Simplified for demonstration

2. **AXI4LiteDriver**
   - Implements AXI4-Lite protocol in driver
   - Handles write transactions (address, data, response channels)
   - Handles read transactions (address, data channels)
   - Demonstrates protocol timing and handshaking

3. **AXI4LiteMonitor**
   - Monitors AXI4-Lite protocol signals
   - Creates transactions from monitored signals
   - Broadcasts via analysis port
   - Supports write and read monitoring

4. **AXI4LiteSequence**
   - Generates AXI4-Lite transactions
   - Creates write and read sequences
   - Demonstrates protocol usage patterns

**AXI4-Lite Protocol:**

**Write Transaction:**
- Write Address Channel: `AWVALID`, `AWREADY`, `AWADDR`, `AWPROT`
- Write Data Channel: `WVALID`, `WREADY`, `WDATA`, `WSTRB`
- Write Response Channel: `BVALID`, `BREADY`, `BRESP`

**Read Transaction:**
- Read Address Channel: `ARVALID`, `ARREADY`, `ARADDR`, `ARPROT`
- Read Data Channel: `RVALID`, `RREADY`, `RDATA`, `RRESP`

**Protocol Implementation:**
```python
async def write_transaction(self, txn):
    """Implement AXI4-Lite write protocol."""
    # Write Address Channel
    await Timer(5, unit="ns")
    
    # Write Data Channel
    await Timer(5, unit="ns")
    
    # Write Response Channel
    await Timer(5, unit="ns")
```

**Running the example:**

```bash
./scripts/module6.sh --protocol
# or
cd module6/examples/protocol
make SIM=verilator TEST=protocol_example
```

**Protocol Verification Benefits:**
- Standard protocol compliance
- Reusable protocol agents
- Protocol-specific test patterns
- Industry-standard verification

### 3. Protocol Checker (`examples/protocol_checkers/protocol_checker_example.py`)

Demonstrates protocol compliance checking:

**Key Concepts:**
- Protocol rule checking
- Error detection and reporting
- Protocol compliance monitoring
- Protocol state tracking
- Protocol violation detection

**Protocol Checker Components:**

1. **ProtocolChecker**
   - Extends `uvm_subscriber`
   - Receives transactions from monitor
   - Checks protocol rules
   - Tracks errors and warnings
   - Reports protocol compliance

2. **ProtocolMonitor**
   - Monitors protocol signals
   - Generates protocol transactions
   - Broadcasts to protocol checker
   - Provides transaction timestamps

**Protocol Rules:**

**Rule 1: Valid/Ready Handshaking**
- `valid` should not change while `ready` is asserted
- Violation: `valid` changes during handshake

**Rule 2: Ready/Valid Handshaking**
- `ready` should not change while `valid` is asserted
- Violation: `ready` changes during handshake

**Rule 3: Data Validity**
- Data should be valid when `valid` and `ready` are both high
- OK: Valid handshake with data transfer

**Rule 4: Valid Without Ready**
- Warning if `valid` asserted without `ready`
- Warning: Protocol may be inefficient

**Protocol Checking:**
```python
def write(self, txn):
    """Check protocol compliance."""
    # Check rule violations
    if self.prev_ready and self.prev_valid and txn.valid != self.prev_valid:
        error = "Protocol violation: valid changed while ready asserted"
        self.errors.append(error)
        self.logger.error(error)
    
    # Track state
    self.prev_valid = txn.valid
    self.prev_ready = txn.ready
```

**Running the example:**

```bash
./scripts/module6.sh --protocol-checkers
# or
cd module6/examples/protocol_checkers
make SIM=verilator TEST=protocol_checker_example
```

**Expected Output:**
- Protocol rule checking
- Error and warning detection
- Protocol compliance reporting
- Protocol state tracking

**Protocol Checker Benefits:**
- Automatic protocol compliance checking
- Early error detection
- Protocol debugging support
- Compliance reporting

### 4. Multi-Channel Scoreboard (`examples/scoreboards/multi_channel_scoreboard_example.py`)

Demonstrates multi-channel scoreboard implementation:

**Key Concepts:**
- Multiple channel checking
- Channel coordination
- Time-based matching
- Channel-specific scoreboarding
- Multi-channel verification

**Multi-Channel Scoreboard Components:**

1. **MultiChannelScoreboard**
   - Scoreboard for multiple channels
   - Contains subscribers for each channel
   - Tracks expected and actual per channel
   - Matches transactions per channel
   - Reports channel-specific statistics

2. **ChannelSubscriber**
   - Subscriber for individual channel
   - Receives transactions for specific channel
   - Forwards to parent scoreboard
   - Maintains channel-specific state

3. **ChannelMonitor**
   - Monitor for a channel
   - Generates channel-specific transactions
   - Broadcasts via analysis port
   - Maintains channel ID

**Multi-Channel Patterns:**

**Scoreboard Creation:**
```python
# Create scoreboard with multiple channels
self.scoreboard = MultiChannelScoreboard.create("scoreboard", self)
self.scoreboard.num_channels = 3

# Create subscribers for each channel
for i in range(self.num_channels):
    subscriber = ChannelSubscriber(f"subscriber_channel_{i}", self, i)
    self.subscribers.append(subscriber)
```

**Channel-Specific Matching:**
```python
def receive_transaction(self, txn, channel_id):
    """Match transaction for specific channel."""
    if len(self.expected[channel_id]) > 0:
        exp_txn = self.expected[channel_id].pop(0)
        if txn.actual == exp_txn.expected:
            self.matched[channel_id].append((exp_txn, txn))
        else:
            self.mismatches[channel_id].append((exp_txn, txn))
```

**Running the example:**

```bash
./scripts/module6.sh --scoreboards
# or
cd module6/examples/scoreboards
make SIM=verilator TEST=multi_channel_scoreboard_example
```

**Expected Output:**
- Multi-channel scoreboard creation
- Channel-specific transaction tracking
- Channel-specific matching
- Multi-channel verification reports

**Multi-Channel Scoreboard Benefits:**
- Channel-specific verification
- Parallel channel checking
- Channel coordination
- Scalable verification

### 5. Testbench Architecture (`examples/architecture/architecture_example.py`)

Demonstrates layered testbench architecture and reusable components:

**Key Concepts:**
- Layered architecture patterns
- Layer communication
- Abstraction levels
- Component reuse
- Parameterization

**Architecture Components:**

1. **Layered Architecture:**
   - **Layer 0**: Lowest abstraction level (signal-level)
   - **Layer 1**: Middle abstraction level (transaction-level)
   - **Layer 2**: Highest abstraction level (application-level)

2. **Layer Components:**
   - **Layer0Component**: Signal-level processing
   - **Layer1Component**: Transaction-level processing
   - **Layer2Component**: Application-level processing

3. **Reusable Components:**
   - **ReusableComponent**: Configurable component
   - Supports `enabled` and `mode` configuration
   - Demonstrates component reuse patterns

**Layered Architecture Patterns:**

**Layer Communication:**
```python
# Connect layers: Layer0 -> Layer1 -> Layer2
self.layer0.ap.connect(self.layer1.subscriber.analysis_export)
self.layer1.ap_out.connect(self.layer2.subscriber.analysis_export)
```

**Layer Processing:**
```python
# Layer 0: Signal-level
txn.layer = 0
self.ap.write(txn)

# Layer 1: Transaction-level
processed_txn.data = txn.data + 0x10
processed_txn.layer = 1
self.ap_out.write(processed_txn)

# Layer 2: Application-level
self.received.append(txn)
```

**Reusable Component Patterns:**

**Component Configuration:**
```python
# Create reusable component with configuration
self.comp1 = ReusableComponent.create("comp1", self)
self.comp1.config = {'enabled': True, 'mode': 'normal'}
self.comp1.enabled = True
self.comp1.mode = 'normal'
```

**Component Reuse:**
```python
# Create multiple instances with different configs
comp1: enabled=True, mode='normal'
comp2: enabled=True, mode='debug'
comp3: enabled=False, mode='normal'
```

**Running the example:**

```bash
./scripts/module6.sh --architecture
# or
cd module6/examples/architecture
make SIM=verilator TEST=architecture_example
```

**Expected Output:**
- Layered architecture demonstration
- Layer communication
- Reusable component usage
- Configuration-based component reuse

**Architecture Benefits:**
- Clear abstraction levels
- Reusable components
- Scalable architecture
- Configuration-based customization

## Design Under Test (DUT)

### AXI4-Lite Slave (`dut/protocols/axi4_lite_slave.v`)

A simplified AXI4-Lite slave for protocol verification.

**Module Interface:**
```verilog
module axi4_lite_slave (
    input  wire        ACLK,      // Clock signal
    input  wire        ARESETn,   // Active-low reset
    
    // Write Address Channel
    input  wire        AWVALID,   // Write address valid
    output reg         AWREADY,   // Write address ready
    input  wire [31:0] AWADDR,    // Write address
    input  wire [2:0]  AWPROT,    // Write protection type
    
    // Write Data Channel
    input  wire        WVALID,    // Write data valid
    output reg         WREADY,    // Write data ready
    input  wire [31:0] WDATA,     // Write data
    input  wire [3:0]  WSTRB,     // Write strobe
    
    // Write Response Channel
    output reg         BVALID,    // Write response valid
    input  wire        BREADY,    // Write response ready
    output reg  [1:0]  BRESP,     // Write response
    
    // Read Address Channel
    input  wire        ARVALID,   // Read address valid
    output reg         ARREADY,   // Read address ready
    input  wire [31:0] ARADDR,    // Read address
    input  wire [2:0]  ARPROT,    // Read protection type
    
    // Read Data Channel
    output reg         RVALID,    // Read data valid
    input  wire        RREADY,    // Read data ready
    output reg  [31:0] RDATA,     // Read data
    output reg  [1:0]  RRESP      // Read response
);
```

**Functionality:**
- 4KB memory (1024 words × 32 bits)
- Write transactions: Address → Data → Response
- Read transactions: Address → Data
- State machines for write and read operations
- Handshaking on all channels
- Response codes: OKAY (00), EXOKAY (01), SLVERR (10), DECERR (11)

**Characteristics:**
- Simplified AXI4-Lite implementation
- Synchronous operation with async reset
- Separate state machines for write and read
- Memory-based storage
- Suitable for protocol verification

**Protocol Support:**
- Write Address Channel handshaking
- Write Data Channel handshaking
- Write Response Channel handshaking
- Read Address Channel handshaking
- Read Data Channel handshaking

## Testbenches

### pyuvm Tests (`tests/pyuvm_tests/`)

#### Complex Testbench Test (`test_complex_testbench.py`)

Complete UVM testbench demonstrating complex testbench construction:

**UVM Components:**

1. **Transaction (`ComplexTransaction`)**
   - Contains `data`, `address`, and `channel` fields
   - Used for complex testbench testing

2. **Sequence (`ComplexSequence`)**
   - Generates test transactions
   - Creates and sends transactions

3. **Driver (`ComplexDriver`)**
   - Receives transactions from sequencer
   - Drives DUT inputs (pattern shown)

4. **Monitor (`ComplexMonitor`)**
   - Samples DUT outputs
   - Creates transactions from sampled data
   - Broadcasts via analysis port

5. **Scoreboard (`ComplexScoreboard`)**
   - Extends `uvm_subscriber`
   - Receives transactions from monitor
   - Tracks received transactions

6. **Agent (`ComplexAgent`)**
   - Contains driver, monitor, and sequencer
   - Connects components

7. **Environment (`ComplexEnv`)**
   - Contains agent and scoreboard
   - Connects monitor to scoreboard

8. **Test (`ComplexTestbenchTest`)**
   - Top-level test class
   - Creates environment and runs test
   - Starts sequence and checks results

**Test Flow:**
1. `build_phase()` - Create all components
2. `connect_phase()` - Connect components
3. `run_phase()` - Start sequence, generate transactions
4. `check_phase()` - Verify results
5. `report_phase()` - Generate test report

**Running the test:**

```bash
# Via module script
./scripts/module6.sh --pyuvm-tests

# Directly from test directory
cd module6/tests/pyuvm_tests
make SIM=verilator TEST=test_complex_testbench
```

**Expected Results:**
- 1 test case passing
- All components created and connected
- Sequence execution demonstrated
- Scoreboard tracking demonstrated
- Complex testbench concepts integrated

## Running Examples and Tests

### Using the Module Script

The `module6.sh` script provides a convenient way to run all examples and tests:

```bash
# Run everything (all examples + all tests)
./scripts/module6.sh

# Run only examples
./scripts/module6.sh --all-examples

# Run only tests
./scripts/module6.sh --pyuvm-tests

# Run specific examples
./scripts/module6.sh --multi-agent
./scripts/module6.sh --protocol
./scripts/module6.sh --protocol-checkers
./scripts/module6.sh --scoreboards
./scripts/module6.sh --architecture

# Combine options
./scripts/module6.sh --multi-agent --protocol --pyuvm-tests
```

### Running Individual Examples

#### Direct Execution from Example Directory

```bash
# Activate virtual environment
source .venv/bin/activate

# Change to example directory
cd module6/examples/multi_agent

# Run example
make SIM=verilator TEST=multi_agent_example

# Clean build artifacts
make clean
```

#### Running All Examples Sequentially

```bash
cd module6/examples

# Multi-agent
cd multi_agent && make SIM=verilator TEST=multi_agent_example && cd ..

# Protocol
cd protocol && make SIM=verilator TEST=protocol_example && cd ..

# Protocol checkers
cd protocol_checkers && make SIM=verilator TEST=protocol_checker_example && cd ..

# Scoreboards
cd scoreboards && make SIM=verilator TEST=multi_channel_scoreboard_example && cd ..

# Architecture
cd architecture && make SIM=verilator TEST=architecture_example && cd ..
```

### Running pyuvm Tests

```bash
# Activate virtual environment
source .venv/bin/activate

# Change to test directory
cd module6/tests/pyuvm_tests

# Run test
make SIM=verilator TEST=test_complex_testbench

# Clean build artifacts
make clean
```

## Test Results

When tests complete successfully, you should see output similar to:

### Example Test Output

```
** TEST                                        STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
** multi_agent_example.test_multi_agent           PASS         200.00           0.00     123456.78  **
** TESTS=1 PASS=1 FAIL=0 SKIP=0                                 200.00           0.00      12345.67  **
```

### Expected Test Counts

- **Multi-agent example**: 1 test
- **Protocol example**: 1 test
- **Protocol checker example**: 1 test
- **Multi-channel scoreboard example**: 1 test
- **Architecture example**: 1 test
- **Complex testbench test**: 1 test
- **Total**: 6 tests across all examples and testbenches

## Troubleshooting

### Common Issues

#### 1. Verilator Version Error

**Error:** `cocotb requires Verilator 5.036 or later, but using 5.020`

**Solution:** Upgrade Verilator to 5.036 or later:

```bash
./scripts/install_verilator.sh --from-submodule --force
```

#### 2. Module Not Found Errors

**Error:** `ModuleNotFoundError: No module named 'pyuvm'` or `ModuleNotFoundError: No module named 'cocotb'`

**Solution:** Activate the virtual environment:

```bash
source .venv/bin/activate
```

#### 3. Multi-Agent Coordination Issues

**Error:** Agents don't coordinate correctly

**Solution:**
- Verify virtual sequence has references to all sequencers
- Check parallel execution uses `cocotb.start_soon()` correctly
- Ensure all sequences are awaited
- Verify scoreboard connections for all agents

#### 4. Protocol Verification Issues

**Error:** Protocol transactions fail

**Solution:**
- Verify protocol signals are connected correctly
- Check protocol timing matches specification
- Ensure handshaking signals are correct
- Verify transaction fields match protocol

#### 5. Protocol Checker Not Detecting Violations

**Error:** Protocol checker doesn't report violations

**Solution:**
- Verify monitor is generating transactions correctly
- Check protocol rules are implemented correctly
- Ensure state tracking is working
- Verify checker receives transactions from monitor

#### 6. Multi-Channel Scoreboard Mismatches

**Error:** Scoreboard reports mismatches incorrectly

**Solution:**
- Verify channel IDs are correct
- Check expected transactions are added for correct channels
- Ensure channel-specific matching logic is correct
- Verify subscriber connections per channel

#### 7. Architecture Layer Communication Issues

**Error:** Layers don't communicate correctly

**Solution:**
- Verify layer connections in `connect_phase()`
- Check analysis port connections between layers
- Ensure subscriber `write()` methods forward correctly
- Verify layer processing order

### Debugging Tips

1. **Check Multi-Agent Coordination:**
   ```python
   # Verify agent sequencers are set
   self.logger.info(f"Agent sequencers: {self.agent_seqrs}")
   ```

2. **Monitor Protocol Transactions:**
   ```python
   # Add logging in protocol driver
   self.logger.info(f"Protocol transaction: {txn}")
   ```

3. **Check Protocol Compliance:**
   ```python
   # Verify protocol checker receives transactions
   self.logger.info(f"Protocol checker errors: {len(self.errors)}")
   ```

4. **Inspect Multi-Channel Scoreboard:**
   ```python
   # Check channel-specific data
   self.logger.info(f"Channel {channel_id}: expected={len(self.expected[channel_id])}, actual={len(self.actual[channel_id])}")
   ```

5. **Verify Layer Connections:**
   ```python
   # Check layer connections
   self.logger.info(f"Layer0 -> Layer1: {self.layer0.ap} -> {self.layer1.subscriber}")
   ```

## Topics Covered

1. **Multi-Agent Environments** - Multiple agent coordination, parallel execution
2. **Protocol Verification** - AXI4-Lite protocol, protocol-specific agents
3. **Protocol Checkers** - Protocol compliance checking, rule validation
4. **Multi-Channel Scoreboards** - Channel-specific verification, parallel checking
5. **Testbench Architecture** - Layered architecture, reusable components
6. **Debugging and Analysis** - Advanced debugging techniques, analysis patterns
7. **Multi-Channel Verification** - Channel coordination, parallel verification
8. **Performance Verification** - Performance monitoring, throughput analysis
9. **Error Injection** - Error injection and recovery patterns
10. **Testbench Integration** - Component integration, system-level verification

## Next Steps

After completing Module 6, proceed to:

- **Module 7**: Advanced Topics - DMA, VIP integration, best practices
- **Module 8**: Advanced Utilities - CLP, comparators, pools, queues, recorders

## Additional Resources

- [pyuvm Documentation](https://pyuvm.readthedocs.io/)
- [UVM User's Guide](https://www.accellera.org/images/downloads/standards/uvm/UVM_Class_Reference_1.2.pdf)
- [AXI4 Protocol Specification](https://developer.arm.com/documentation/ihi0022/latest/)
- [cocotb Documentation](https://docs.cocotb.org/)
- [Verilator Documentation](https://verilator.org/)

## File Descriptions

### Examples

| File | Description | Tests |
|------|-------------|-------|
| `multi_agent_example.py` | Multi-agent environment coordination | 1 test function |
| `protocol_example.py` | AXI4-Lite protocol verification | 1 test function |
| `protocol_checker_example.py` | Protocol compliance checking | 1 test function |
| `multi_channel_scoreboard_example.py` | Multi-channel scoreboard | 1 test function |
| `architecture_example.py` | Layered architecture and reusable components | 1 test function |

### DUT Modules

| File | Description | Ports |
|------|-------------|-------|
| `axi4_lite_slave.v` | AXI4-Lite slave interface | `ACLK`, `ARESETn`, `AWVALID`, `AWREADY`, `AWADDR`, `AWPROT`, `WVALID`, `WREADY`, `WDATA`, `WSTRB`, `BVALID`, `BREADY`, `BRESP`, `ARVALID`, `ARREADY`, `ARADDR`, `ARPROT`, `RVALID`, `RREADY`, `RDATA`, `RRESP` |

### Testbenches

| File | Framework | Description | Tests |
|------|-----------|-------------|-------|
| `test_complex_testbench.py` | pyuvm | Complex testbench test | 1 UVM test |

---

For questions or issues, refer to the main project README or check the test logs for detailed error messages.
