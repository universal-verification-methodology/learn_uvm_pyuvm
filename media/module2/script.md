        # Narration script — Module 2: cocotb Fundamentals

        **Target length:** ~36 minutes (76 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 2 | 0:25 | Welcome to module 2, cocotb Fundamentals. In this module you will master cocotb for hardware verification. |
| 2 | Learning objectives | 0:16 | Here is what you will learn in this module. Master cocotb for hardware verification |
| 3 | Prerequisites | 0:16 | Before you start, make sure you have these prerequisites. See module README |
| 4 | Learning path | 0:22 | Learning path. Master cocotb for hardware verification |
| 5 | Overview | 0:16 | Overview. This module provides comprehensive coverage of cocotb, the coroutine-based testbench framework that enables Python testbenches for... |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:32 | Follow this learning path. Read the guides before running the labs. Finish Module 1 cocotb labs so clock/reset coroutine patterns are familiar Read module2/dut/registers/simple_register.v and shift_register.v port lists before writing stimulus Work through module2/examples/triggers/ — RisingEdge, FallingEdge, and Timer are core to all Module 2 tests Study module2/examples/clock_generation/ and... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. RTL portfolio architecture | 0:38 | 1. RTL portfolio architecture. simple_register.v — 8-bit register, enable, synchronous reset (primary lab DUT) shift_register.v — serial in/out, parallel tap; exercises multi-cycle behavior simple_fifo.v — 16×8 FIFO with full/empty flags (reference for extension) simple_fsm.v — IDLE/START/WORK/DONE four-state controller (optional study) Refer to the diagram on the right. |
| 10 | 2. cocotb testbench architecture | 0:38 | 2. cocotb testbench architecture. Test module → coroutines (@cocotb.test) → DUT signals via dut.signal handles Clock generators in examples decouple timing from test logic No UVM hierarchy; flat Python functions and shared fixtures via Makefile TEST= selection Concurrent coroutines use triggers to model parallel clock, reset, and stimulus threads Refer to the diagram on the right. |
| 11 | 3. Execution pipeline | 0:28 | 3. Execution pipeline. Build: Verilator compiles selected DUT under module2/dut/registers/ per Makefile top module Sim: cocotb schedules coroutines on triggers; reset coroutines establish known state before stimulus Check: Python assertions on dut.q.value / shift outputs; cocotb regression aggregates results.xml Examples path: module2.sh --triggers runs tutorial makes without full DUT regression |
| 12 | 4. Example vs test separation | 0:28 | 4. Example vs test separation. module2/examples/ — signal access, clocks, triggers, reset patterns (runnable tutorials) module2/tests/cocotb_tests/ — regression tests bound to specific DUTs Orchestrator scripts/module2.sh routes flags to examples or cocotb makes Reference FIFO/FSM RTL supports self-study; graded labs focus on register and shift register |
| 13 | DUT — simple register | 0:28 | DUT — simple register. Review the code on screen and match it to files in the repository. |
| 14 | cocotb — reset then write | 0:28 | cocotb — reset then write. Review the code on screen and match it to files in the repository. |
| 15 | Key files to study | 0:08 | Next section: Key files to study. |
| 16 | Open these in the repo | 0:36 | Open these in the repo. module2/dut/registers/simple_register.v — 8-bit register with enable and synchronous reset (primary lab DUT) module2/dut/registers/shift_register.v — serial in/out with parallel tap; multi-cycle behavior module2/examples/triggers/triggers_example.py — cocotb trigger primitives and concurrency module2/tests/cocotb_tests/test_simple_register.py — directed write/read and... |
| 17 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 18 | 1. Stimulus and observation | 0:34 | 1. Stimulus and observation. Directed writes/reads on register ports; shift tests exercise serial timing RisingEdge/FallingEdge/Timer triggers structure concurrent activity Reset tests run first in regression order to establish known state Refer to the diagram on the right. |
| 19 | 2. Regression and Makefile flow | 0:24 | 2. Regression and Makefile flow. make SIM=verilator TEST=test_simple_register selects cocotb test module Regression runner executes multiple tests; pass/fail per cocotb.regression Boundary tests (test_register_all_values) cover 0x00, 0x7F, 0x80, 0xFF |
| 20 | 3. Step-by-step lab execution | 0:32 | 3. Step-by-step lab execution. 1. Tutorials: ./scripts/module2.sh --signal-access --triggers --reset-patterns 2. Register lab: cd module2/tests/cocotb_tests && make SIM=verilator TEST=test_simple_register 3. Shift register lab: make SIM=verilator TEST=test_shift_register — verify serial-to-parallel timing 4. Full DUT regression: ./scripts/module2.sh --cocotb-tests 5. Debug failures with... |
| 21 | 4. Debug and closure | 0:24 | 4. Debug and closure. Logging via cocotb.log; VCD from simulator flags for waveform debug ./scripts/module2.sh --cocotb-tests validates key cocotb tests and example makes Assessment: clocks, triggers, reset sequences, structured cocotb tests |
| 22 | Regression Makefile | 0:28 | Regression Makefile. Review the code on screen and match it to files in the repository. |
| 23 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 24 | 1. cocotb Architecture and Concepts (1/3) | 0:36 | 1. cocotb Architecture and Concepts (1/3). What is cocotb? Coroutine-based testbench framework Python testbenches for Verilog/VHDL Simulator abstraction History and motivation |
| 25 | 1. cocotb Architecture and Concepts (2/3) | 0:36 | 1. cocotb Architecture and Concepts (2/3). Python testbench layer Simulator interface layer DUT interaction Event scheduling Key Concepts |
| 26 | 1. cocotb Architecture and Concepts (3/3) | 0:24 | 1. cocotb Architecture and Concepts (3/3). Triggers for synchronization Handles for signal access Simulation time management |
| 27 | 2. Simulator Integration (1/3) | 0:36 | 2. Simulator Integration (1/3). Supported Simulators Verilator (recommended) Icarus Verilog ModelSim/QuestaSim GHDL (VHDL) |
| 28 | 2. Simulator Integration (2/3) | 0:36 | 2. Simulator Integration (2/3). Simulator Selection Environment variables Makefile configuration Simulator-specific features Compilation Process |
| 29 | 2. Simulator Integration (3/3) | 0:24 | 2. Simulator Integration (3/3). cocotb library compilation Linking process Makefile structure |
| 30 | 3. Clock Generation and Management (1/3) | 0:36 | 3. Clock Generation and Management (1/3). Clock Generation Clock class usage Clock parameters (period, units) Starting clocks Multiple clocks |
| 31 | 3. Clock Generation and Management (2/3) | 0:36 | 3. Clock Generation and Management (2/3). Regular clocks Gated clocks Clock division Clock stopping Clock Domain Management |
| 32 | 3. Clock Generation and Management (3/3) | 0:20 | 3. Clock Generation and Management (3/3). Clock domain crossing Synchronization between domains |
| 33 | 4. Signal Access and Driving (1/4) | 0:36 | 4. Signal Access and Driving (1/4). Signal Handles Accessing DUT signals dut.signal_name syntax Signal value types Signal properties |
| 34 | 4. Signal Access and Driving (2/4) | 0:36 | 4. Signal Access and Driving (2/4). .value property Integer conversion Binary representation Signal state checking Driving Signals |
| 35 | 4. Signal Access and Driving (3/4) | 0:36 | 4. Signal Access and Driving (3/4). Integer assignment Binary string assignment High-impedance (Z) and unknown (X) Signal Types Single-bit signals |
| 36 | 4. Signal Access and Driving (4/4) | 0:20 | 4. Signal Access and Driving (4/4). Buses and arrays Bidirectional signals |
| 37 | 5. Triggers and Coroutines (1/4) | 0:36 | 5. Triggers and Coroutines (1/4). Trigger Types RisingEdge(signal) FallingEdge(signal) Edge(signal) (any edge) Timer(time, units) |
| 38 | 5. Triggers and Coroutines (2/4) | 0:36 | 5. Triggers and Coroutines (2/4). ReadWrite() (during time step) Combine(*triggers) (multiple triggers) First(*triggers) (first to occur) Coroutine Execution Defining coroutines |
| 39 | 5. Triggers and Coroutines (3/4) | 0:36 | 5. Triggers and Coroutines (3/4). cocotb.start_soon() vs await Parallel execution Coroutine Synchronization Waiting for triggers Coordinating multiple coroutines |
| 40 | 5. Triggers and Coroutines (4/4) | 0:16 | 5. Triggers and Coroutines (4/4). Exception propagation |
| 41 | 6. Test Structure and Organization (1/3) | 0:36 | 6. Test Structure and Organization (1/3). Test Function Structure @cocotb.test() decorator Test function signature DUT parameter Test organization |
| 42 | 6. Test Structure and Organization (2/3) | 0:36 | 6. Test Structure and Organization (2/3). Setup phase Test execution Cleanup phase Error handling Multiple Tests |
| 43 | 6. Test Structure and Organization (3/3) | 0:24 | 6. Test Structure and Organization (3/3). Test selection Test parameters Test fixtures |
| 44 | 7. Reset and Initialization (1/2) | 0:36 | 7. Reset and Initialization (1/2). Reset Strategies Synchronous reset Asynchronous reset Reset sequences Reset verification |
| 45 | 7. Reset and Initialization (2/2) | 0:28 | 7. Reset and Initialization (2/2). Signal initialization State initialization Configuration setup Initial conditions |
| 46 | 8. Common Verification Patterns (1/3) | 0:36 | 8. Common Verification Patterns (1/3). Stimulus Generation Sequential patterns Random patterns Constrained random File-based stimulus |
| 47 | 8. Common Verification Patterns (2/3) | 0:36 | 8. Common Verification Patterns (2/3). Immediate checking Deferred checking Reference model comparison Scoreboard patterns Transaction-Level Modeling |
| 48 | 8. Common Verification Patterns (3/3) | 0:24 | 8. Common Verification Patterns (3/3). Transaction generation Transaction execution Transaction checking |
| 49 | 9. Debugging with cocotb (1/4) | 0:36 | 9. Debugging with cocotb (1/4). Logging and Reporting cocotb logging Log levels Log formatting Debug messages |
| 50 | 9. Debugging with cocotb (2/4) | 0:36 | 9. Debugging with cocotb (2/4). VCD file generation FST file generation Waveform viewing Signal tracing Interactive Debugging |
| 51 | 9. Debugging with cocotb (3/4) | 0:36 | 9. Debugging with cocotb (3/4). Breakpoints Variable inspection Step-through debugging Common Issues Signal access errors |
| 52 | 9. Debugging with cocotb (4/4) | 0:20 | 9. Debugging with cocotb (4/4). Simulation hangs Value conversion problems |
| 53 | 10. Advanced cocotb Features (1/3) | 0:36 | 10. Advanced cocotb Features (1/3). Memory Access Memory modeling Memory initialization Memory access patterns Bus Functional Models (BFM) |
| 54 | 10. Advanced cocotb Features (2/3) | 0:36 | 10. Advanced cocotb Features (2/3). BFM implementation Reusable BFMs Performance Optimization Coroutine efficiency Trigger optimization |
| 55 | 10. Advanced cocotb Features (3/3) | 0:16 | 10. Advanced cocotb Features (3/3). Memory usage |
| 56 | 11. Integration with pytest (1/2) | 0:36 | 11. Integration with pytest (1/2). pytest Integration Using pytest with cocotb Test discovery Fixtures Parametrization |
| 57 | 11. Integration with pytest (2/2) | 0:28 | 11. Integration with pytest (2/2). Test directory structure Test naming conventions Test grouping Test execution |
| 58 | Command reference highlights | 0:08 | Next section: Command reference highlights. |
| 59 | cocotb examples (tutorial makes) | 0:24 | cocotb examples (tutorial makes). ./scripts/module2.sh --triggers — run trigger tutorial under module2/examples/triggers/ ./scripts/module2.sh --clock-generation --reset-patterns — timing and reset fixture drills ./scripts/module2.sh — all five example tracks (signal access through common patterns) Full detail in docs/MODULE2.md command reference. |
| 60 | DUT regression tests | 0:24 | DUT regression tests. ./scripts/module2.sh --cocotb-tests — register and shift-register makes via orchestrator cd module2/tests/cocotb_tests && make SIM=verilator TEST=test_simple_register make SIM=verilator TEST=test_shift_register — serial timing and parallel output checks Full detail in docs/MODULE2.md command reference. |
| 61 | Debug and waves | 0:24 | Debug and waves. make SIM=verilator TEST=test_simple_register WAVES=1 — enable VCD/FST when Makefile supports it Use cocotb.log verbosity and simulator stdout from results.xml for pass/fail triage Re-run single TEST= target after RTL or stimulus edits — faster than full example sweep Full detail in docs/MODULE2.md command reference. |
| 62 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 63 | Module 2 orchestrator | 0:45 | Module 2 orchestrator. Watch the terminal output and confirm you see the expected pass message. |
| 64 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 65 | Demo: Signal Access | 0:45 | Demo: Signal Access. Watch the terminal output and confirm you see the expected pass message. |
| 66 | Demo: Clock Generation | 0:45 | Demo: Clock Generation. Watch the terminal output and confirm you see the expected pass message. |
| 67 | Demo: Triggers | 0:45 | Demo: Triggers. Watch the terminal output and confirm you see the expected pass message. |
| 68 | Demo: Reset Patterns | 0:45 | Demo: Reset Patterns. Watch the terminal output and confirm you see the expected pass message. |
| 69 | Demo: Common Verification Patterns | 0:45 | Demo: Common Verification Patterns. Watch the terminal output and confirm you see the expected pass message. |
| 70 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 71 | What you should know (1/3) | 0:36 | By now you should be able to explain the following. Understand cocotb architecture Integrate with simulators Generate and manage clocks Access and drive signals Use triggers effectively From MODULE2 Learning Outcomes. |
| 72 | What you should know (2/3) | 0:36 | By now you should be able to explain the following. Implement reset sequences Use common verification patterns Debug cocotb testbenches Optimize testbench performance Signal handles From MODULE2 Learning Outcomes. |
| 73 | What you should know (3/3) | 0:16 | By now you should be able to explain the following. Signal types From MODULE2 Learning Outcomes. |
| 74 | Exercises | 0:32 | Exercises. Clock Management Signal Operations Trigger Patterns Test Structure Debugging |
| 75 | Assessment checklist | 0:36 | Assessment checklist. Understands cocotb architecture Can integrate with simulators Can generate and manage clocks Can access and drive signals Can use triggers effectively |
| 76 | Summary & next steps | 0:28 | In summary: Master cocotb for hardware verification Next up: Next module in course. Master cocotb for hardware verification Complete module2/CHECKLIST.md Review module2/EXAMPLES.md and run each lab Next: Next module in course |

        ## Section narration (edit for TTS)

        - **How to learn:** Finish Module 1 cocotb labs so clock/reset coroutine patterns are familiar Then Read `module2/dut/registers/simple_register.v` and `shift_register.v` port lists before writing stimulus Then Work through `module2/examples/triggers/` — `RisingEdge`, `FallingEdge`, and `Timer` are core to all Module 2 tests Then Study `module2/examples/clock_generation/` and `reset_patterns/` — shared fixtures decouple timing from test logic.
- **Design architecture (RTL portfolio architecture, cocotb testbench architecture, Execution pipeline, Example vs test separation):** Walk through the block diagram, then relate each block to files under module2/examples/.
- **Verification (Stimulus and observation, Regression and Makefile flow, Step-by-step lab execution, Debug and closure):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 11 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module2/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE2.md` and `module2/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 2`
