# Module 2: cocotb Fundamentals

This directory contains all examples, exercises, and test cases for Module 2, focusing on cocotb fundamentals including clock generation, signal access, triggers, reset patterns, and common verification patterns.

## Directory Structure

```
module2/
├── examples/              # cocotb examples for each topic
│   ├── signal_access/     # Signal reading and writing
│   │   └── signal_access_example.py
│   ├── clock_generation/  # Clock generation patterns
│   │   └── clock_generation_example.py
│   ├── triggers/         # Trigger usage examples
│   │   └── triggers_example.py
│   ├── reset_patterns/   # Reset sequences
│   │   └── reset_patterns_example.py
│   └── common_patterns/  # Common verification patterns
│       └── common_patterns_example.py
├── dut/                   # Verilog Design Under Test modules
│   ├── registers/         # Register modules
│   │   ├── simple_register.v    # Basic register with enable
│   │   └── shift_register.v     # 8-bit shift register
│   ├── fifos/            # FIFO modules
│   │   └── simple_fifo.v        # 16-entry FIFO
│   └── state_machines/   # State machine modules
│       └── simple_fsm.v         # 4-state FSM
├── tests/                 # Testbenches
│   └── cocotb_tests/     # cocotb testbenches
│       ├── test_simple_register.py
│       └── test_shift_register.py
└── exercises/            # Exercise solutions (if any)
```

## Prerequisites

Before running the experiments, ensure you have:

- **Python 3.8+** - Required for cocotb and pyuvm
- **Verilator 5.036+** - Required for simulation (5.044 recommended)
- **cocotb 2.0+** - Installed in virtual environment
- **Make** - For building and running tests

To verify your environment:

```bash
python3 --version        # Should be 3.8+
verilator --version      # Should be 5.036+
python3 -c "import cocotb; print(cocotb.__version__)"
```

## cocotb Examples

### 1. Signal Access (`examples/signal_access/signal_access_example.py`)

Demonstrates how to access and manipulate DUT signals in cocotb:

**Key Concepts:**
- Accessing DUT signals via `dut.signal_name`
- Reading signal values using `.value` attribute
- Signal value representations: `.integer`, `.binstr`
- Signal properties: `_name`, `_path`, width (`len(signal)`)
- Different value assignments (integer, binary literals)

**Test Cases:**

1. `test_signal_access_basic` - Basic signal access
   - Demonstrates reading initial signal values
   - Shows different value representations (integer, binary)
   - Verifies signal updates after clock edges

2. `test_signal_types` - Signal type exploration
   - Single-bit vs multi-bit signals
   - Signal width determination
   - Different assignment methods (hex, binary)

3. `test_signal_properties` - Signal properties and methods
   - Signal metadata access (`_name`, `_path`)
   - Value representation methods
   - Signal introspection capabilities

**Running the example:**

```bash
# Via module script
./scripts/module2.sh --signal-access

# Or directly from example directory
cd module2/examples/signal_access
make SIM=verilator TEST=signal_access_example
```

**Expected Output:**
- Signal values displayed in different formats
- Demonstration of signal width and properties
- Verification of signal read/write operations

### 2. Clock Generation (`examples/clock_generation/clock_generation_example.py`)

Demonstrates various clock generation patterns:

**Key Concepts:**
- Using `Clock` class for standard clock generation
- Starting clocks with `cocotb.start_soon()`
- Multiple clock domain handling
- Clock gating patterns
- Clock division techniques

**Test Cases:**

1. `test_clock_class` - Basic Clock class usage
   - Creating clocks with specified periods
   - Starting clocks in background
   - Waiting for clock edges

2. `test_multiple_clocks` - Multiple clock domains
   - Demonstrates handling different clock frequencies
   - Fast and slow clock patterns

3. `test_clock_gating` - Clock gating pattern
   - Simulating clock enable/disable
   - Clock hold patterns

4. `test_clock_stopping` - Clock control
   - Clock lifecycle management
   - Patterns for controlled clock stopping

5. `test_clock_division` - Clock division
   - Creating divided clocks from base clock
   - Divide-by-N clock generation

**Running the example:**

```bash
./scripts/module2.sh --clock-generation
# or
cd module2/examples/clock_generation
make SIM=verilator TEST=clock_generation_example
```

**Key Patterns:**
- `Clock(dut.clk, 10, units="ns")` - Create 10ns period clock
- `cocotb.start_soon(clock.start())` - Start clock in background
- `await RisingEdge(dut.clk)` - Wait for clock edge

### 3. Triggers (`examples/triggers/triggers_example.py`)

Demonstrates cocotb trigger mechanisms for synchronization:

**Key Concepts:**
- Edge triggers: `RisingEdge`, `FallingEdge`, `Edge`
- Timer triggers: `Timer(duration, units)`
- ReadOnly trigger: Wait for end of time step
- Combined triggers: `Combine`, `First`
- Parallel trigger handling

**Test Cases:**

1. `test_edge_triggers` - Edge detection
   - Rising edge detection
   - Falling edge detection
   - Any edge detection

2. `test_timer_trigger` - Time-based triggers
   - Absolute time delays
   - Sequential timing patterns

3. `test_readonly_trigger` - ReadOnly phase trigger
   - Waiting for signal stabilization
   - Reading stable values after propagation

4. `test_combine_trigger` - Combined conditions
   - Waiting for multiple conditions simultaneously
   - AND-style trigger combinations

5. `test_first_trigger` - First-occurrence trigger
   - Waiting for first of multiple events
   - OR-style trigger combinations

6. `test_timeout_handling` - Timeout patterns
   - Timeout exception handling
   - SimTimeoutError usage

7. `test_parallel_triggers` - Parallel coroutines
   - Multiple simultaneous coroutines
   - Coordinated trigger handling

**Running the example:**

```bash
./scripts/module2.sh --triggers
# or
cd module2/examples/triggers
make SIM=verilator TEST=triggers_example
```

**Common Triggers:**
- `RisingEdge(signal)` - Wait for rising edge
- `FallingEdge(signal)` - Wait for falling edge
- `Timer(time, units="ns")` - Wait for time period
- `ReadOnly()` - Wait for end of time step
- `Combine(trigger1, trigger2)` - Wait for all triggers
- `First(trigger1, trigger2)` - Wait for first trigger

### 4. Reset Patterns (`examples/reset_patterns/reset_patterns_example.py`)

Demonstrates reset sequence implementation:

**Key Concepts:**
- Asynchronous reset sequences
- Synchronous reset patterns
- Reset verification techniques
- Reset initialization patterns
- Propagation delay handling

**Test Cases:**

1. `test_async_reset` - Asynchronous reset
   - Reset assertion and deassertion
   - Reset duration control
   - Propagation delay handling

2. `test_sync_reset` - Synchronous reset pattern
   - Clock-synchronized reset
   - Multi-cycle reset hold
   - Reset release timing

3. `test_reset_verification` - Comprehensive reset verification
   - Reset during operation
   - Reset release timing verification
   - Post-reset state verification

4. `test_reset_initialization` - Post-reset initialization
   - Signal initialization after reset
   - Validating post-reset behavior

**Reset Helper Functions:**

- `async_reset(dut, duration_ns, propagation_delay_ns)` - Async reset sequence
- `sync_reset(dut, clock_period_ns, reset_cycles)` - Sync reset sequence

**Running the example:**

```bash
./scripts/module2.sh --reset-patterns
# or
cd module2/examples/reset_patterns
make SIM=verilator TEST=reset_patterns_example
```

**Reset Patterns:**
- **Async Reset**: Assert immediately, wait duration, deassert, wait propagation
- **Sync Reset**: Assert, hold for N clock cycles, deassert on clock edge
- Always wait for propagation delay after reset deassertion

### 5. Common Patterns (`examples/common_patterns/common_patterns_example.py`)

Demonstrates common verification patterns:

**Key Concepts:**
- Sequential stimulus patterns
- Random stimulus generation
- Scoreboard implementation
- Reference model pattern
- Transaction-level modeling

**Test Cases:**

1. `test_sequential_pattern` - Sequential stimulus
   - Linear test data sequences
   - Systematic value progression

2. `test_random_pattern` - Random stimulus
   - Random data generation
   - Reproducible randomness (seeded)

3. `test_scoreboard_pattern` - Scoreboard verification
   - Expected vs actual comparison
   - Mismatch tracking
   - Statistics collection

4. `test_reference_model` - Reference model pattern
   - Python-based behavior model
   - DUT vs reference comparison
   - Golden reference validation

5. `test_transaction_level` - Transaction-level modeling
   - Transaction objects
   - High-level operation abstraction
   - Transaction-based verification

**Running the example:**

```bash
./scripts/module2.sh --common-patterns
# or
cd module2/examples/common_patterns
make SIM=verilator TEST=common_patterns_example
```

**Pattern Examples:**

**Scoreboard Class:**
- Tracks expected and actual values
- Detects mismatches
- Provides statistics

**Reference Model:**
- Python implementation of expected DUT behavior
- Used for comparison and validation
- Enables high-level verification

## Design Under Test (DUT)

### Simple Register (`dut/registers/simple_register.v`)

A basic 8-bit register with clock, reset, and enable control.

**Module Interface:**
```verilog
module simple_register (
    input  wire       clk,     // Clock signal
    input  wire       rst_n,   // Active-low reset
    input  wire       enable,  // Register enable
    input  wire [7:0] d,       // Data input
    output reg  [7:0] q        // Data output
);
```

**Functionality:**
- Resets to 0x00 when `rst_n` is low
- Updates `q` with `d` on positive clock edge when `enable` is high
- Holds current value when `enable` is low
- Asynchronous reset (sensitive to `rst_n` edge)

**Characteristics:**
- 8-bit data width
- Synchronous operation with async reset
- Enable-controlled updates

### Shift Register (`dut/registers/shift_register.v`)

An 8-bit shift register with serial input/output and parallel output.

**Module Interface:**
```verilog
module shift_register (
    input  wire       clk,        // Clock signal
    input  wire       rst_n,      // Active-low reset
    input  wire       shift,      // Shift enable
    input  wire       data_in,    // Serial data input
    output reg        data_out,   // Serial data output (MSB)
    output reg  [7:0] q           // Parallel output
);
```

**Functionality:**
- Resets to all zeros when `rst_n` is low
- Shifts left (MSB out, LSB in) on positive clock edge when `shift` is high
- `data_out` provides MSB (q[7])
- Parallel output `q` shows current register contents

**Shift Operation:**
- `q <= {q[6:0], data_in}` - Shift left, insert `data_in` at LSB
- `data_out <= q[7]` - Output MSB before shift

**Characteristics:**
- Serial-to-parallel and parallel-to-serial conversion
- MSB-first shifting (first bit shifted becomes MSB)
- 8-bit internal storage

### Simple FIFO (`dut/fifos/simple_fifo.v`)

A 16-entry FIFO (First-In-First-Out) buffer with read/write pointers.

**Module Interface:**
```verilog
module simple_fifo (
    input  wire       clk,       // Clock signal
    input  wire       rst_n,     // Active-low reset
    input  wire       write_en,  // Write enable
    input  wire       read_en,   // Read enable
    input  wire [7:0] data_in,   // Write data
    output reg  [7:0] data_out,  // Read data
    output reg        full,      // FIFO full flag
    output reg        empty      // FIFO empty flag
);
```

**Functionality:**
- Resets to empty state when `rst_n` is low
- Writes `data_in` when `write_en` is high and FIFO is not full
- Reads `data_out` when `read_en` is high and FIFO is not empty
- Maintains `full` and `empty` status flags
- 16-entry capacity (addresses 0-15)

**FIFO Behavior:**
- Write pointer increments on write (wraps at 16)
- Read pointer increments on read (wraps at 16)
- Count tracks number of entries
- `full` when count == 16
- `empty` when count == 0

**Characteristics:**
- Circular buffer implementation
- Status flag management
- Overflow/underflow prevention

### Simple FSM (`dut/state_machines/simple_fsm.v`)

A 4-state finite state machine with start/done control.

**Module Interface:**
```verilog
module simple_fsm (
    input  wire       clk,     // Clock signal
    input  wire       rst_n,   // Active-low reset
    input  wire       start,   // Start signal
    output reg        done,    // Done signal
    output reg  [1:0] state    // Current state output
);
```

**State Encoding:**
- `IDLE` (2'b00) - Initial/idle state
- `START` (2'b01) - Start state
- `WORK` (2'b10) - Working state
- `DONE` (2'b11) - Done state

**State Transitions:**
- `IDLE` → `START`: When `start` signal is asserted
- `START` → `WORK`: Automatic transition on next clock
- `WORK` → `DONE`: Automatic transition on next clock
- `DONE` → `IDLE`: Automatic transition, asserts `done`

**Functionality:**
- Resets to `IDLE` state when `rst_n` is low
- `done` signal asserted only in `DONE` state
- State transitions on positive clock edge
- External control via `start` signal

**Characteristics:**
- 4-state Moore machine (outputs depend only on state)
- Simple control flow demonstration
- State visibility via `state` output

## Testbenches

### cocotb Tests (`tests/cocotb_tests/`)

#### Simple Register Test (`test_simple_register.py`)

Comprehensive testbench for the simple register module:

**Test Cases:**

1. `test_register_reset` - Reset functionality
   - Verifies register resets to 0x00
   - Tests reset sequence with propagation delay

2. `test_register_write` - Write functionality
   - Verifies data can be written to register
   - Tests enable-controlled write operation

3. `test_register_enable` - Enable control
   - Tests register update when enable is high
   - Verifies register holds value when enable is low

4. `test_register_all_values` - Boundary value testing
   - Tests critical 8-bit values: 0x00, 0x01, 0x7F, 0x80, 0xFE, 0xFF
   - Validates all value ranges

**Key Features:**
- Reusable `reset_dut()` helper function
- Clock generation using `Clock` class
- Proper timing with `RisingEdge` and `Timer`
- Comprehensive value coverage

**Running the test:**

```bash
# Via module script
./scripts/module2.sh --cocotb-tests

# Directly from test directory
cd module2/tests/cocotb_tests
make SIM=verilator TEST=test_simple_register
```

**Expected Results:**
- 4 test cases, all passing
- All register functionality verified
- Boundary conditions tested

#### Shift Register Test (`test_shift_register.py`)

Testbench for the shift register module:

**Test Cases:**

1. `test_shift_register_reset` - Reset functionality
   - Verifies register resets to 0x00
   - Verifies `data_out` resets to 0

2. `test_shift_register_operation` - Shift operation
   - Shifts in 8 bits of data
   - Verifies parallel output matches expected value
   - Tests MSB-first shifting behavior

3. `test_shift_register_serial_out` - Serial output
   - Loads data into register
   - Verifies serial output during shifting
   - Tests serial-to-parallel conversion

**Key Features:**
- Bit-by-bit serial input generation
- Expected value calculation for verification
- Serial output monitoring
- Comprehensive shift operation testing

**Running the test:**

```bash
# Via module script
./scripts/module2.sh --cocotb-tests

# Directly from test directory
cd module2/tests/cocotb_tests
make SIM=verilator TEST=test_shift_register
```

**Expected Results:**
- 3 test cases, all passing
- Serial and parallel operations verified
- Shift direction and bit ordering validated

## Running Examples and Tests

### Using the Module Script

The `module2.sh` script provides a convenient way to run all examples and tests:

```bash
# Run everything (all examples + all tests)
./scripts/module2.sh

# Run only examples
./scripts/module2.sh --all-examples

# Run only tests
./scripts/module2.sh --cocotb-tests

# Run specific examples
./scripts/module2.sh --signal-access
./scripts/module2.sh --clock-generation
./scripts/module2.sh --triggers
./scripts/module2.sh --reset-patterns
./scripts/module2.sh --common-patterns

# Combine options
./scripts/module2.sh --signal-access --clock-generation --cocotb-tests
```

### Running Individual Examples

#### Direct Execution from Example Directory

```bash
# Activate virtual environment
source .venv/bin/activate

# Change to example directory
cd module2/examples/signal_access

# Run example
make SIM=verilator TEST=signal_access_example

# Clean build artifacts
make clean
```

#### Running All Examples Sequentially

```bash
cd module2/examples

# Signal access
cd signal_access && make SIM=verilator TEST=signal_access_example && cd ..

# Clock generation
cd clock_generation && make SIM=verilator TEST=clock_generation_example && cd ..

# Triggers
cd triggers && make SIM=verilator TEST=triggers_example && cd ..

# Reset patterns
cd reset_patterns && make SIM=verilator TEST=reset_patterns_example && cd ..

# Common patterns
cd common_patterns && make SIM=verilator TEST=common_patterns_example && cd ..
```

### Running cocotb Tests

```bash
# Activate virtual environment
source .venv/bin/activate

# Change to test directory
cd module2/tests/cocotb_tests

# Run simple register tests
make SIM=verilator TEST=test_simple_register

# Run shift register tests
make SIM=verilator TEST=test_shift_register

# Clean build artifacts
make clean
```

## Test Results

When tests complete successfully, you should see output similar to:

### Example Test Output

```
** TEST                                        STATUS  SIM TIME (ns)  REAL TIME (s)  RATIO (ns/s) **
** test_signal_access_basic                        PASS          50.00           0.00      12345.67  **
** test_signal_types                               PASS          80.00           0.00      23456.78  **
** test_signal_properties                          PASS          70.00           0.00      34567.89  **
** TESTS=3 PASS=3 FAIL=0 SKIP=0                                 200.00           0.00      23456.78  **
```

### Expected Test Counts

- **Signal Access example**: 3 tests
- **Clock Generation example**: 5 tests
- **Triggers example**: 7 tests
- **Reset Patterns example**: 4 tests
- **Common Patterns example**: 5 tests
- **Simple Register tests**: 4 tests
- **Shift Register tests**: 3 tests
- **Total**: 31 tests across all examples and testbenches

## Troubleshooting

### Common Issues

#### 1. Verilator Version Error

**Error:** `cocotb requires Verilator 5.036 or later, but using 5.020`

**Solution:** Upgrade Verilator to 5.036 or later:

```bash
./scripts/install_verilator.sh --from-submodule --force
```

#### 2. Module Not Found Errors

**Error:** `ModuleNotFoundError: No module named 'cocotb'`

**Solution:** Activate the virtual environment:

```bash
source .venv/bin/activate
```

#### 3. TOPLEVEL Mismatch

**Error:** `Can not find root handle 'simple_register'`

**Solution:** Clean the build directory between tests with different TOPLEVELs:

```bash
cd module2/tests/cocotb_tests
make clean
make SIM=verilator TEST=test_simple_register
```

The module script automatically cleans between tests.

#### 4. Signal Access Errors

**Error:** `AttributeError: 'cocotb.handle.ModifiableObject' object has no attribute 'value'`

**Solution:** Ensure you're accessing signals correctly:
- Use `dut.signal_name.value` for reading/writing
- Use `dut.signal_name.value.integer` for integer representation
- Check that signal names match the Verilog module ports exactly

#### 5. Clock Not Running

**Error:** Test hangs waiting for clock edge

**Solution:** Ensure clock is started before waiting for edges:

```python
clock = Clock(dut.clk, 10, units="ns")
cocotb.start_soon(clock.start())  # Must start clock first
await RisingEdge(dut.clk)  # Then wait for edge
```

#### 6. Reset Not Working

**Error:** DUT doesn't reset properly

**Solution:** 
- Verify reset signal polarity (active-low `rst_n` vs active-high `rst`)
- Wait for propagation delay after deasserting reset
- Check reset is held for sufficient duration

### Debugging Tips

1. **Check Verilator Version:**
   ```bash
   verilator --version
   ```

2. **Verify Virtual Environment:**
   ```bash
   which python3  # Should point to .venv/bin/python3
   python3 -c "import cocotb; print(cocotb.__version__)"
   ```

3. **Check Build Directory:**
   ```bash
   ls -la module2/examples/*/sim_build/
   ls -la module2/tests/cocotb_tests/sim_build/
   ```

4. **View Detailed Logs:**
   ```bash
   # Check log files created by module script
   tail -f /tmp/cocotb_signal_access.log
   tail -f /tmp/cocotb_clock_generation.log
   ```

5. **Run Tests with Verbose Output:**
   ```bash
   make SIM=verilator TEST=test_simple_register V=1
   ```

6. **Inspect Signal Values:**
   ```python
   print(f"Signal value: {dut.q.value}")
   print(f"Signal integer: {dut.q.value.integer}")
   print(f"Signal binary: {dut.q.value.binstr}")
   print(f"Signal width: {len(dut.q)}")
   ```

## Topics Covered

1. **Signal Access** - Reading and writing DUT signals in cocotb
2. **Clock Generation** - Creating and managing clock signals
3. **Triggers** - Using triggers for synchronization (edges, timers, combined)
4. **Reset Patterns** - Implementing async and sync reset sequences
5. **Common Patterns** - Sequential, random, scoreboard, reference model patterns
6. **cocotb Architecture** - Understanding cocotb structure and integration
7. **Simulator Integration** - Working with Verilator and other simulators
8. **Test Structure** - Organizing cocotb tests effectively
9. **Debugging Techniques** - Debugging cocotb testbenches
10. **Verification Patterns** - Best practices for hardware verification

## Next Steps

After completing Module 2, proceed to:

- **Module 3**: UVM Concepts - Phases, factory, configuration database, objections
- **Module 4**: UVM Components - Agents, sequencers, monitors, drivers, TLM
- **Module 5**: Advanced UVM - Callbacks, coverage, register model, virtual sequences

## Additional Resources

- [cocotb Documentation](https://docs.cocotb.org/)
- [cocotb Tutorials](https://docs.cocotb.org/en/stable/coding_style.html)
- [Verilator Documentation](https://verilator.org/)
- [Python Async/Await Guide](https://docs.python.org/3/library/asyncio.html)

## File Descriptions

### Examples

| File | Description | Tests |
|------|-------------|-------|
| `signal_access_example.py` | Signal access and manipulation | 3 test functions |
| `clock_generation_example.py` | Clock generation patterns | 5 test functions |
| `triggers_example.py` | Trigger usage and synchronization | 7 test functions |
| `reset_patterns_example.py` | Reset sequence implementation | 4 test functions |
| `common_patterns_example.py` | Common verification patterns | 5 test functions |

### DUT Modules

| File | Description | Ports |
|------|-------------|-------|
| `simple_register.v` | 8-bit register with enable | `clk`, `rst_n`, `enable`, `d[7:0]`, `q[7:0]` |
| `shift_register.v` | 8-bit shift register | `clk`, `rst_n`, `shift`, `data_in`, `data_out`, `q[7:0]` |
| `simple_fifo.v` | 16-entry FIFO | `clk`, `rst_n`, `write_en`, `read_en`, `data_in[7:0]`, `data_out[7:0]`, `full`, `empty` |
| `simple_fsm.v` | 4-state FSM | `clk`, `rst_n`, `start`, `done`, `state[1:0]` |

### Testbenches

| File | Framework | Description | Tests |
|------|-----------|-------------|-------|
| `test_simple_register.py` | cocotb | Simple register testbench | 4 test functions |
| `test_shift_register.py` | cocotb | Shift register testbench | 3 test functions |

---

For questions or issues, refer to the main project README or check the test logs for detailed error messages.
