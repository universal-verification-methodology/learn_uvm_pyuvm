# Module 3: UVM Basics

This directory contains all examples, exercises, and test cases for Module 3, focusing on UVM (Universal Verification Methodology) fundamentals including class hierarchy, phases, reporting, configuration database, factory pattern, and objection mechanism.

## Directory Structure

```
module3/
├── examples/              # pyuvm examples for each topic
│   ├── class_hierarchy/   # UVM class hierarchy examples
│   │   └── class_hierarchy_example.py
│   ├── phases/           # UVM phases examples
│   │   └── phases_example.py
│   ├── reporting/        # UVM reporting examples
│   │   └── reporting_example.py
│   ├── configdb/         # ConfigDB examples
│   │   └── configdb_example.py
│   ├── factory/          # Factory pattern examples
│   │   └── factory_example.py
│   └── objections/       # Objection mechanism examples
│       └── objections_example.py
├── dut/                   # Verilog Design Under Test modules
│   └── simple_blocks/     # Simple blocks for UVM testing
│       └── adder.v        # 8-bit adder
├── tests/                 # Testbenches
│   └── pyuvm_tests/      # pyuvm testbenches
│       └── test_simple_uvm.py
└── exercises/            # Exercise solutions (if any)
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

## UVM Examples

### 1. Class Hierarchy (`examples/class_hierarchy/class_hierarchy_example.py`)

Demonstrates UVM class hierarchy and component structure:

**Key Concepts:**
- `uvm_object` - Base class for all UVM objects (transactions, sequences)
- `uvm_component` - Base class for all UVM components (drivers, monitors, agents)
- Component hierarchy: Test → Environment → Agent → Driver/Monitor
- Component creation using factory pattern (`create()`)
- Phase implementation in components

**UVM Classes Demonstrated:**

1. **Transaction (`MyTransaction`)**
   - Extends `uvm_sequence_item`
   - Contains test data (data, address)
   - Demonstrates `uvm_object` hierarchy

2. **Driver (`MyDriver`)**
   - Extends `uvm_driver`
   - Implements `build_phase()`, `connect_phase()`, `run_phase()`
   - Uses `uvm_seq_item_pull_port` for transaction communication

3. **Monitor (`MyMonitor`)**
   - Extends `uvm_monitor`
   - Implements `build_phase()`, `run_phase()`
   - Uses `uvm_analysis_port` for data forwarding

4. **Agent (`MyAgent`)**
   - Extends `uvm_agent`
   - Contains driver, monitor, and sequencer
   - Demonstrates component composition

5. **Environment (`MyEnv`)**
   - Extends `uvm_env`
   - Contains agent instances
   - Top-level verification environment

6. **Test (`ClassHierarchyTest`)**
   - Extends `uvm_test`
   - Top-level test class
   - Orchestrates test execution

**Running the example:**

```bash
# Via module script
./scripts/module3.sh --class-hierarchy

# Or directly from example directory
cd module3/examples/class_hierarchy
make SIM=verilator TEST=class_hierarchy_example
```

**Expected Output:**
- Component hierarchy creation and connection
- Phase execution in hierarchical order
- Transaction creation and manipulation

### 2. Phases (`examples/phases/phases_example.py`)

Demonstrates UVM phase execution and implementation:

**Key Concepts:**
- UVM phase execution order
- Build-time phases (synchronous)
- Run-time phases (asynchronous)
- Cleanup phases

**UVM Phases Demonstrated:**

**Build-Time Phases (Top-down):**
1. `build_phase()` - Component construction
2. `connect_phase()` - Component connections
3. `end_of_elaboration_phase()` - Final setup

**Run-Time Phases (Bottom-up):**
4. `pre_reset_phase()` - Before reset
5. `reset_phase()` - Reset sequence
6. `post_reset_phase()` - After reset
7. `pre_configure_phase()` - Before configuration
8. `configure_phase()` - Configuration
9. `post_configure_phase()` - After configuration
10. `pre_main_phase()` - Before main test
11. `main_phase()` - Main test execution
12. `post_main_phase()` - After main test
13. `pre_shutdown_phase()` - Before shutdown
14. `shutdown_phase()` - Shutdown sequence
15. `post_shutdown_phase()` - After shutdown

**Cleanup Phases (Bottom-up):**
16. `extract_phase()` - Extract results
17. `check_phase()` - Final checks
18. `report_phase()` - Generate reports
19. `final_phase()` - Final cleanup

**Running the example:**

```bash
./scripts/module3.sh --phases
# or
cd module3/examples/phases
make SIM=verilator TEST=phases_example
```

**Phase Execution Order:**
- Build-time phases execute top-down (parent before children)
- Run-time phases execute bottom-up (children before parent)
- Cleanup phases execute bottom-up (children before parent)

### 3. Reporting (`examples/reporting/reporting_example.py`)

Demonstrates UVM reporting system with severity and verbosity levels:

**Key Concepts:**
- Severity levels: INFO, WARNING, ERROR, FATAL
- Verbosity levels: UVM_LOW, UVM_MEDIUM, UVM_HIGH, UVM_FULL, UVM_DEBUG
- Message formatting and context
- Hierarchical reporting with component names

**Test Cases:**

1. `test_reporting` - Basic reporting demonstration
   - Severity level examples
   - Message formatting with data
   - Component context information
   - Verbosity level explanation

2. `test_hierarchical_reporting` - Hierarchical reporting
   - Reporting from different components
   - Component name inclusion in messages

**Reporting Methods:**
- `self.logger.info()` - Informational messages
- `self.logger.warning()` - Warning messages
- `self.logger.error()` - Error messages
- `self.logger.fatal()` - Fatal errors (stops simulation)

**Running the example:**

```bash
./scripts/module3.sh --reporting
# or
cd module3/examples/reporting
make SIM=verilator TEST=reporting_example
```

**Expected Output:**
- Messages with different severity levels
- Formatted messages with data values
- Component context in messages
- Hierarchical component reporting

### 4. ConfigDB (`examples/configdb/configdb_example.py`)

Demonstrates UVM configuration database for passing configuration:

**Key Concepts:**
- Setting configuration values in ConfigDB
- Getting configuration values from ConfigDB
- Hierarchical configuration lookup
- Configuration objects vs scalar values
- Component-specific configuration

**Test Cases:**

1. `test_configdb` - Basic ConfigDB usage
   - Setting configuration objects
   - Setting scalar configuration values
   - Getting configuration from ConfigDB
   - Hierarchical configuration paths

2. `test_configdb_hierarchy` - Hierarchical configuration
   - Configuration at different hierarchy levels
   - Global vs component-specific configuration
   - Configuration lookup priority

**Configuration Patterns:**

**Setting Configuration:**
```python
ConfigDB().set(None, "", "config_name", value)  # Global
ConfigDB().set(self, "env.agent", "config_name", value)  # Specific path
```

**Getting Configuration:**
```python
config = None
success = ConfigDB().get(None, "", "config_name", config)
if success and config is not None:
    # Use config
```

**Configuration Object Example:**
```python
class AgentConfig(uvm_object):
    def __init__(self, name="AgentConfig"):
        super().__init__(name)
        self.active = True
        self.has_coverage = False
        self.address_width = 32
```

**Running the example:**

```bash
./scripts/module3.sh --configdb
# or
cd module3/examples/configdb
make SIM=verilator TEST=configdb_example
```

**Configuration Hierarchy:**
- Configuration is looked up starting from the component's hierarchy path
- Falls back to more global configuration if not found
- Enables flexible test configuration without code changes

### 5. Factory (`examples/factory/factory_example.py`)

Demonstrates UVM factory pattern for object creation and overrides:

**Key Concepts:**
- Factory registration for classes
- Factory-based object creation
- Type overrides for substituting classes
- Instance overrides for specific instances
- Component vs object factory

**Test Cases:**

1. `test_factory` - Basic factory usage
   - Factory registration
   - Factory-based object creation
   - Creating transactions and components

2. `test_factory_override` - Factory overrides
   - Type override: `BaseDriver` → `ExtendedDriver`
   - Override affects all instances of the base type
   - Enables test customization without code changes

**Factory Patterns:**

**Object Creation:**
```python
# Create component using factory
driver = MyDriver.create("driver", self)

# Create object (manual)
txn = BaseTransaction("txn_name")
```

**Type Override:**
```python
# Set override in build_phase
uvm_factory().set_type_override(BaseDriver, ExtendedDriver)
```

**Running the example:**

```bash
./scripts/module3.sh --factory
# or
cd module3/examples/factory
make SIM=verilator TEST=factory_example
```

**Factory Benefits:**
- Centralized object creation
- Easy substitution of implementations
- Test customization without modifying base code
- Supports inheritance hierarchies

### 6. Objections (`examples/objections/objections_example.py`)

Demonstrates UVM objection mechanism for controlling test execution:

**Key Concepts:**
- Raising objections to keep simulation running
- Dropping objections to allow phase completion
- Multiple objections per component
- Objection tracking across hierarchy
- Simulation ends when all objections dropped

**Test Cases:**

1. `test_objection` - Basic objection mechanism
   - Raising objections in test and components
   - Dropping objections when work completes
   - Simulation control via objections

2. `test_objection_timing` - Objection timing
   - Multiple components with different objection lifetimes
   - Coordinated objection dropping
   - Ensuring all components complete before test ends

**Objection Methods:**
- `self.raise_objection()` - Raise objection (keeps simulation running)
- `self.drop_objection()` - Drop objection (may allow phase completion)

**Objection Behavior:**
- Each component can raise multiple objections
- Phase completes only when all objections are dropped
- Objections are tracked per phase
- Simulation ends when run_phase objections are all dropped

**Running the example:**

```bash
./scripts/module3.sh --objections
# or
cd module3/examples/objections
make SIM=verilator TEST=objections_example
```

**Objection Best Practices:**
- Always raise objection at start of `run_phase()` if doing work
- Drop objection when work completes
- Coordinate objections across components
- Use objections only in run-time phases (async phases)

## Design Under Test (DUT)

### Adder (`dut/simple_blocks/adder.v`)

An 8-bit adder with carry output for UVM testing.

**Module Interface:**
```verilog
module adder (
    input  wire       clk,     // Clock signal
    input  wire       rst_n,   // Active-low reset
    input  wire [7:0] a,       // Operand A
    input  wire [7:0] b,       // Operand B
    output reg  [7:0] sum,     // Sum output (8-bit)
    output reg        carry    // Carry output
);
```

**Functionality:**
- Resets to all zeros when `rst_n` is low
- Computes `{carry, sum} = a + b` on positive clock edge
- Handles 8-bit addition with overflow detection
- Carry bit indicates overflow (sum > 255)

**Characteristics:**
- Synchronous operation with async reset
- 8-bit unsigned arithmetic
- Overflow detection via carry flag
- Simple design for UVM testbench demonstration

**Truth Table Examples:**
| a   | b   | sum | carry |
|-----|-----|-----|-------|
| 0x00 | 0x00 | 0x00 | 0 |
| 0x01 | 0x01 | 0x02 | 0 |
| 0xFF | 0x01 | 0x00 | 1 |
| 0x80 | 0x80 | 0x00 | 1 |

## Testbenches

### pyuvm Tests (`tests/pyuvm_tests/`)

#### Simple UVM Test (`test_simple_uvm.py`)

Complete UVM testbench demonstrating all core concepts:

**UVM Components:**

1. **Transaction (`AdderTransaction`)**
   - Extends `uvm_sequence_item`
   - Contains operands (a, b) and expected results
   - Used for stimulus and checking

2. **Sequence (`AdderSequence`)**
   - Extends `uvm_sequence`
   - Generates test vectors for the adder
   - Creates and sends transactions to sequencer

3. **Driver (`AdderDriver`)**
   - Extends `uvm_driver`
   - Receives transactions from sequencer
   - Drives DUT inputs (pattern shown, not connected in example)

4. **Monitor (`AdderMonitor`)**
   - Extends `uvm_monitor`
   - Observes DUT outputs
   - Forwards transactions via analysis port

5. **Scoreboard (`AdderScoreboard`)**
   - Extends `uvm_subscriber`
   - Receives transactions from monitor
   - Compares expected vs actual results

6. **Agent (`AdderAgent`)**
   - Extends `uvm_agent`
   - Contains driver, monitor, and sequencer
   - Connects components in `connect_phase()`

7. **Environment (`AdderEnv`)**
   - Extends `uvm_env`
   - Contains agent and scoreboard
   - Connects monitor to scoreboard

8. **Test (`AdderTest`)**
   - Extends `uvm_test`
   - Top-level test class
   - Creates environment, starts sequence, checks results

**Test Flow:**
1. `build_phase()` - Create environment and components
2. `connect_phase()` - Connect components (driver-sequencer, monitor-scoreboard)
3. `run_phase()` - Start sequence, generate transactions
4. `check_phase()` - Verify results in scoreboard
5. `report_phase()` - Generate test report

**Running the test:**

```bash
# Via module script
./scripts/module3.sh --pyuvm-tests

# Directly from test directory
cd module3/tests/pyuvm_tests
make SIM=verilator TEST=test_simple_uvm
```

**Expected Results:**
- 1 test case passing
- All UVM phases executed successfully
- Transaction generation and processing demonstrated
- Scoreboard verification completed

## Running Examples and Tests

### Using the Module Script

The `module3.sh` script provides a convenient way to run all examples and tests:

```bash
# Run everything (all examples + all tests)
./scripts/module3.sh

# Run only examples
./scripts/module3.sh --all-examples

# Run only tests
./scripts/module3.sh --pyuvm-tests

# Run specific examples
./scripts/module3.sh --class-hierarchy
./scripts/module3.sh --phases
./scripts/module3.sh --reporting
./scripts/module3.sh --configdb
./scripts/module3.sh --factory
./scripts/module3.sh --objections

# Combine options
./scripts/module3.sh --phases --factory --pyuvm-tests
```

### Running Individual Examples

#### Direct Execution from Example Directory

```bash
# Activate virtual environment
source .venv/bin/activate

# Change to example directory
cd module3/examples/phases

# Run example
make SIM=verilator TEST=phases_example

# Clean build artifacts
make clean
```

#### Running All Examples Sequentially

```bash
cd module3/examples

# Class hierarchy
cd class_hierarchy && make SIM=verilator TEST=class_hierarchy_example && cd ..

# Phases
cd phases && make SIM=verilator TEST=phases_example && cd ..

# Reporting
cd reporting && make SIM=verilator TEST=reporting_example && cd ..

# ConfigDB
cd configdb && make SIM=verilator TEST=configdb_example && cd ..

# Factory
cd factory && make SIM=verilator TEST=factory_example && cd ..

# Objections
cd objections && make SIM=verilator TEST=objections_example && cd ..
```

### Running pyuvm Tests

```bash
# Activate virtual environment
source .venv/bin/activate

# Change to test directory
cd module3/tests/pyuvm_tests

# Run test
make SIM=verilator TEST=test_simple_uvm

# Clean build artifacts
make clean
```

## Test Results

When tests complete successfully, you should see output similar to:

### Example Test Output

```
** TEST                                        STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
** phases_example.test_phases                      PASS         200.00           0.00     232758.27  **
** TESTS=1 PASS=1 FAIL=0 SKIP=0                                 200.00           0.00     123000.12  **
```

### Expected Test Counts

- **Class Hierarchy example**: 1 test
- **Phases example**: 1 test
- **Reporting example**: 2 tests
- **ConfigDB example**: 2 tests
- **Factory example**: 2 tests
- **Objections example**: 2 tests
- **Simple UVM test**: 1 test
- **Total**: 11 tests across all examples and testbenches

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

#### 3. Phase Execution Errors

**Error:** `RuntimeWarning: coroutine 'Test.build_phase' was never awaited`

**Solution:** This is a known warning in pyuvm when phases are called synchronously. It doesn't affect functionality. The phases are executed correctly by the UVM phase scheduler.

#### 4. Factory Override Not Working

**Error:** Override doesn't seem to take effect

**Solution:** 
- Ensure override is set in `build_phase()` before creating components
- Use `set_type_override()` for all instances, or `set_inst_override()` for specific instances
- Verify the base class is being used in `create()` calls

#### 5. Objections Not Working

**Error:** Simulation ends too early or hangs

**Solution:**
- Ensure `raise_objection()` is called at start of `run_phase()` if doing work
- Ensure `drop_objection()` is called when work completes
- Check that all components have dropped their objections
- Objections only work in async phases (run-time phases)

#### 6. ConfigDB Lookup Fails

**Error:** Configuration not found in ConfigDB

**Solution:**
- Verify configuration is set before components try to get it
- Check hierarchy path matches exactly
- Use `None` for global configuration, component for specific paths
- Ensure configuration is set in parent's `build_phase()` before child's `build_phase()`

### Debugging Tips

1. **Check pyuvm Installation:**
   ```bash
   python3 -c "import pyuvm; print(pyuvm.__version__)"
   ```

2. **Verify Virtual Environment:**
   ```bash
   which python3  # Should point to .venv/bin/python3
   python3 -c "import cocotb; import pyuvm"
   ```

3. **Enable Verbose Logging:**
   ```python
   # Set UVM verbosity in test
   uvm_report_object.set_report_verbosity_level(UVM_DEBUG)
   ```

4. **Check Phase Execution:**
   - Add logging in each phase to verify execution order
   - Use `report_phase()` to verify test completion

5. **Inspect Component Hierarchy:**
   ```python
   # Print component hierarchy
   self.print_topology()
   ```

6. **Check Objection Count:**
   ```python
   # Check objection count
   objection_count = uvm_objection().get_objection_count()
   self.logger.info(f"Objection count: {objection_count}")
   ```

## Topics Covered

1. **UVM Introduction** - Understanding UVM methodology and benefits
2. **Class Hierarchy** - UVM base classes (uvm_object, uvm_component) and inheritance
3. **UVM Phases** - Build-time, run-time, and cleanup phases
4. **Reporting System** - Severity levels, verbosity, and message formatting
5. **ConfigDB** - Configuration database for flexible test configuration
6. **Factory Pattern** - Object creation and type/instance overrides
7. **Test Classes** - Creating and structuring UVM tests
8. **Environment Structure** - Building UVM environments with agents
9. **Objection Mechanism** - Controlling test execution and phase completion
10. **Component Communication** - TLM ports, exports, and analysis ports
11. **Sequence/Sequencer/Driver** - Transaction generation and processing
12. **Monitor and Scoreboard** - DUT observation and result checking

## Next Steps

After completing Module 3, proceed to:

- **Module 4**: UVM Components - Detailed agent, driver, monitor, sequencer implementation
- **Module 5**: Advanced UVM - Callbacks, coverage, register model, virtual sequences
- **Module 6**: Protocol Verification - Multi-agent testbenches, protocol checkers
- **Module 7**: Advanced Topics - DMA, VIP integration, best practices

## Additional Resources

- [pyuvm Documentation](https://pyuvm.readthedocs.io/)
- [UVM User's Guide](https://www.accellera.org/images/downloads/standards/uvm/UVM_Class_Reference_1.2.pdf)
- [cocotb Documentation](https://docs.cocotb.org/)
- [Verilator Documentation](https://verilator.org/)

## File Descriptions

### Examples

| File | Description | Tests |
|------|-------------|-------|
| `class_hierarchy_example.py` | UVM class hierarchy and component structure | 1 test function |
| `phases_example.py` | UVM phase implementation and execution | 1 test function |
| `reporting_example.py` | UVM reporting system | 2 test functions |
| `configdb_example.py` | UVM configuration database | 2 test functions |
| `factory_example.py` | UVM factory pattern | 2 test functions |
| `objections_example.py` | UVM objection mechanism | 2 test functions |

### DUT Modules

| File | Description | Ports |
|------|-------------|-------|
| `adder.v` | 8-bit adder with carry | `clk`, `rst_n`, `a[7:0]`, `b[7:0]`, `sum[7:0]`, `carry` |

### Testbenches

| File | Framework | Description | Tests |
|------|-----------|-------------|-------|
| `test_simple_uvm.py` | pyuvm | Complete UVM testbench for adder | 1 UVM test |

---

For questions or issues, refer to the main project README or check the test logs for detailed error messages.
