        # Narration script — Module 3: UVM Basics

        **Target length:** ~38 minutes (78 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 3 | 0:25 | Welcome to module 3, UVM Basics. In this module you will master uvm class hierarchy and phases. |
| 2 | Learning objectives | 0:16 | Here is what you will learn in this module. Master UVM class hierarchy and phases |
| 3 | Prerequisites | 0:16 | Before you start, make sure you have these prerequisites. See module README |
| 4 | Learning path | 0:22 | Learning path. Master UVM class hierarchy and phases |
| 5 | Overview | 0:16 | Overview. This module introduces the Universal Verification Methodology (UVM) and its implementation in pyuvm. You'll learn the fundamental UVM... |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:32 | Follow this learning path. Read the guides before running the labs. Solid cocotb skills from Module 2 — you will reuse trigger timing inside pyuvm drivers later Read module3/dut/simple_blocks/adder.v — combinational operands a, b, output sum Step through module3/examples/phases/ and class_hierarchy/ before integrated test_simple_uvm.py Understand UVM phase order: build → connect → run (with... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. RTL and interfaces | 0:34 | 1. RTL and interfaces. Primary DUT: module3/dut/simple_blocks/adder.v — combinational operands and sum Clock/reset scaffolding for pyuvm tests that mirror industry TB hooks Flat block; no protocol channels — focus stays on UVM structure, not bus complexity Refer to the diagram on the right. |
| 10 | 2. UVM testbench architecture | 0:38 | 2. UVM testbench architecture. Hierarchy: uvm_test → uvm_env → uvm_agent (driver, monitor, sequencer) → DUT uvm_sequence_item / uvm_sequence carry transactions; driver converts items to pin wiggles ConfigDB publishes virtual interfaces and parameters before build_phase Factory + objections control creation and phase lifetime Refer to the diagram on the right. |
| 11 | 3. Execution pipeline | 0:28 | 3. Execution pipeline. Build: Verilator compiles adder RTL; pyuvm build_phase constructs test/env/agent/component tree Connect: TLM ports linked in connect_phase; ConfigDB delivers virtual interface handles to driver/monitor Sim/run: sequences start on sequencer; driver applies operands; objections hold run phase until sequences finish Check/report: monitor samples sum; UVM report phase... |
| 12 | 4. Module layout | 0:28 | 4. Module layout. module3/examples/ — isolated API demos (phases, reporting, configdb, factory, objections) module3/tests/pyuvm_tests/ — integrated make SIM=verilator TEST=test_simple_uvm flows Each example directory has its own Makefile for incremental learning Assessment maps each example topic to integrated test behaviors |
| 13 | DUT — 8-bit adder | 0:28 | DUT — 8-bit adder. Review the code on screen and match it to files in the repository. |
| 14 | UVM transaction item | 0:28 | UVM transaction item. Review the code on screen and match it to files in the repository. |
| 15 | Key files to study | 0:08 | Next section: Key files to study. |
| 16 | Open these in the repo | 0:36 | Open these in the repo. module3/dut/simple_blocks/adder.v — primary combinational DUT for UVM structure labs module3/examples/phases/phases_example.py — phase callbacks and simulation lifetime module3/examples/configdb/configdb_example.py — virtual interface and parameter publishing module3/examples/factory/factory_example.py — type overrides without hierarchy edits... |
| 17 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 18 | 1. Phase-based test execution | 0:34 | 1. Phase-based test execution. build → connect → end_of_elaboration → start_of_simulation → run → extract → report Objections in run phase prevent premature finish until sequences complete Reporting verbosity filters debug vs error messages Refer to the diagram on the right. |
| 19 | 2. Stimulus and checking | 0:24 | 2. Stimulus and checking. Directed sequences on adder operands; monitor samples outputs for scoreboard hooks Factory overrides swap test/agent types without editing hierarchy code ConfigDB sets agent active/passive and interface handles |
| 20 | 3. Step-by-step lab execution | 0:32 | 3. Step-by-step lab execution. 1. API drills: ./scripts/module3.sh --class-hierarchy --phases --configdb 2. Factory/objections: ./scripts/module3.sh --factory --objections 3. Integrated test: ./scripts/module3.sh --pyuvm-tests (or make TEST=test_simple_uvm) 4. Confirm simulation log shows phase progression and no UVM_ERROR/FATAL 5. Optional: factory override exercise from examples, re-run... |
| 21 | 4. Closure | 0:24 | 4. Closure. ./scripts/module3.sh --pyuvm-tests and per-topic flags (--phases, --factory, …) Pass when simulation report shows UVM TEST PASSED and no fatal errors Assessment: class hierarchy, phases, configdb, factory, objections |
| 22 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 23 | 1. Introduction to UVM (1/3) | 0:36 | 1. Introduction to UVM (1/3). What is UVM? Universal Verification Methodology Industry standard for verification Methodology vs library History and evolution |
| 24 | 1. Introduction to UVM (2/3) | 0:36 | 1. Introduction to UVM (2/3). Reusability Standardization Scalability Maintainability UVM in Python (pyuvm) |
| 25 | 1. Introduction to UVM (3/3) | 0:20 | 1. Introduction to UVM (3/3). Advantages over SystemVerilog UVM Compatibility and features |
| 26 | 2. UVM Class Hierarchy (1/4) | 0:36 | 2. UVM Class Hierarchy (1/4). Base Classes uvm_object - Base for all UVM objects uvm_component - Base for all UVM components Differences and use cases Component Classes |
| 27 | 2. UVM Class Hierarchy (2/4) | 0:36 | 2. UVM Class Hierarchy (2/4). uvm_env - Environment container uvm_agent - Agent (driver, monitor, sequencer) uvm_driver - Drives transactions to DUT uvm_monitor - Monitors DUT signals uvm_sequencer - Manages sequences |
| 28 | 2. UVM Class Hierarchy (3/4) | 0:36 | 2. UVM Class Hierarchy (3/4). Object Classes uvm_sequence_item - Transaction objects uvm_sequence - Sequence of transactions uvm_config_object - Configuration objects Class Relationships |
| 29 | 2. UVM Class Hierarchy (4/4) | 0:20 | 2. UVM Class Hierarchy (4/4). Composition patterns Factory pattern |
| 30 | 3. UVM Phases (1/6) | 0:36 | 3. UVM Phases (1/6). Phase Overview Why phases exist Phase execution order Phase synchronization Phase types |
| 31 | 3. UVM Phases (2/6) | 0:36 | 3. UVM Phases (2/6). build_phase() - Component construction connect_phase() - Component connections end_of_elaboration_phase() - Final setup Run Phases run_phase() - Main test execution |
| 32 | 3. UVM Phases (3/6) | 0:36 | 3. UVM Phases (3/6). reset_phase() - Reset sequence post_reset_phase() - After reset pre_configure_phase() - Before configuration configure_phase() - Configuration post_configure_phase() - After configuration |
| 33 | 3. UVM Phases (4/6) | 0:36 | 3. UVM Phases (4/6). main_phase() - Main test execution post_main_phase() - After main test pre_shutdown_phase() - Before shutdown shutdown_phase() - Shutdown sequence post_shutdown_phase() - After shutdown |
| 34 | 3. UVM Phases (5/6) | 0:36 | 3. UVM Phases (5/6). extract_phase() - Extract results check_phase() - Final checks report_phase() - Generate reports final_phase() - Final cleanup Phase Implementation |
| 35 | 3. UVM Phases (6/6) | 0:24 | 3. UVM Phases (6/6). Asynchronous phases (run phases) Phase methods Phase ordering |
| 36 | 4. UVM Reporting System (1/5) | 0:36 | 4. UVM Reporting System (1/5). Reporting Overview UVM messaging system Severity levels Verbosity levels Message formatting |
| 37 | 4. UVM Reporting System (2/5) | 0:36 | 4. UVM Reporting System (2/5). UVM_FATAL - Fatal errors UVM_ERROR - Errors UVM_WARNING - Warnings UVM_INFO - Informational UVM_DEBUG - Debug messages |
| 38 | 4. UVM Reporting System (3/5) | 0:36 | 4. UVM Reporting System (3/5). UVM_NONE - No messages UVM_LOW - Low verbosity UVM_MEDIUM - Medium verbosity UVM_HIGH - High verbosity UVM_FULL - Full verbosity |
| 39 | 4. UVM Reporting System (4/5) | 0:36 | 4. UVM Reporting System (4/5). Using Reporting self.logger.info() self.logger.warning() self.logger.error() self.logger.fatal() |
| 40 | 4. UVM Reporting System (5/5) | 0:16 | 4. UVM Reporting System (5/5). Verbosity control |
| 41 | 5. UVM Configuration Database (ConfigDB) (1/4) | 0:36 | 5. UVM Configuration Database (ConfigDB) (1/4). ConfigDB Overview What is ConfigDB? Why use ConfigDB? Configuration hierarchy Setting Configuration |
| 42 | 5. UVM Configuration Database (ConfigDB) (2/4) | 0:36 | 5. UVM Configuration Database (ConfigDB) (2/4). Configuration paths Configuration objects Scalar configuration Getting Configuration ConfigDB().get() |
| 43 | 5. UVM Configuration Database (ConfigDB) (3/4) | 0:36 | 5. UVM Configuration Database (ConfigDB) (3/4). Default values Configuration checking Configuration Patterns Agent configuration Environment configuration |
| 44 | 5. UVM Configuration Database (ConfigDB) (4/4) | 0:16 | 5. UVM Configuration Database (ConfigDB) (4/4). Hierarchical configuration |
| 45 | 6. Factory Pattern (1/2) | 0:36 | 6. Factory Pattern (1/2). Factory Overview What is the factory? Why use factory? Factory benefits Factory Usage |
| 46 | 6. Factory Pattern (2/2) | 0:24 | 6. Factory Pattern (2/2). Object creation Override mechanism Factory patterns |
| 47 | 7. First UVM Test Class (1/3) | 0:36 | 7. First UVM Test Class (1/3). Test Structure Test class definition Inheriting from uvm_test Required methods Test organization |
| 48 | 7. First UVM Test Class (2/3) | 0:36 | 7. First UVM Test Class (2/3). Creating environment Environment hierarchy Component instantiation Test Execution run_phase() implementation |
| 49 | 7. First UVM Test Class (3/3) | 0:20 | 7. First UVM Test Class (3/3). Test flow Completion |
| 50 | 8. Environment Structure (1/3) | 0:36 | 8. Environment Structure (1/3). Environment Basics What is environment? Environment purpose Environment structure Environment Components |
| 51 | 8. Environment Structure (2/3) | 0:36 | 8. Environment Structure (2/3). Scoreboard instantiation Coverage instantiation Other components Environment Connections Component connections |
| 52 | 8. Environment Structure (3/3) | 0:16 | 8. Environment Structure (3/3). TLM connections |
| 53 | 9. Objection Mechanism (1/3) | 0:36 | 9. Objection Mechanism (1/3). Objections Overview What are objections? Why objections? Objection lifecycle Using Objections |
| 54 | 9. Objection Mechanism (2/3) | 0:36 | 9. Objection Mechanism (2/3). drop_objection() Objection timing Multiple objections Objection Patterns Test objections |
| 55 | 9. Objection Mechanism (3/3) | 0:20 | 9. Objection Mechanism (3/3). Component objections Best practices |
| 56 | 10. UVM Test Execution (1/3) | 0:36 | 10. UVM Test Execution (1/3). Test Flow Test startup Phase execution Test completion Cleanup |
| 57 | 10. UVM Test Execution (2/3) | 0:36 | 10. UVM Test Execution (2/3). uvm_root().run_test() Test selection Test parameters Test execution Test Organization |
| 58 | 10. UVM Test Execution (3/3) | 0:24 | 10. UVM Test Execution (3/3). Test inheritance Test libraries Test selection |
| 59 | Command reference highlights | 0:08 | Next section: Command reference highlights. |
| 60 | Isolated UVM API examples | 0:24 | Isolated UVM API examples. ./scripts/module3.sh --phases --reporting — phase and verbosity drills ./scripts/module3.sh --configdb --factory --objections — ConfigDB, factory, objection tracks ./scripts/module3.sh --class-hierarchy — component tree and TLM port basics Full detail in docs/MODULE3.md command reference. |
| 61 | Integrated pyuvm simulation | 0:24 | Integrated pyuvm simulation. ./scripts/module3.sh --pyuvm-tests — default integrated regression against adder DUT cd module3/tests/pyuvm_tests && make SIM=verilator TEST=test_simple_uvm — direct Make debug path ./scripts/module3.sh --skip-examples --pyuvm-tests — jump to integrated test when API drills are done Full detail in docs/MODULE3.md command reference. |
| 62 | Verbosity and overrides | 0:24 | Verbosity and overrides. Set PYUVM_VERBOSITY or plusargs (when supported) to filter UVM report noise during debug Factory overrides in examples swap test/agent types — mirror pattern in integrated test Re-run single example Make target under module3/examples/<topic>/ for fast iteration Full detail in docs/MODULE3.md command reference. |
| 63 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 64 | Module 3 orchestrator | 0:45 | Module 3 orchestrator. Watch the terminal output and confirm you see the expected pass message. |
| 65 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 66 | Demo: Class Hierarchy | 0:45 | Demo: Class Hierarchy. Watch the terminal output and confirm you see the expected pass message. |
| 67 | Demo: UVM Phases | 0:45 | Demo: UVM Phases. Watch the terminal output and confirm you see the expected pass message. |
| 68 | Demo: UVM Reporting | 0:45 | Demo: UVM Reporting. Watch the terminal output and confirm you see the expected pass message. |
| 69 | Demo: ConfigDB | 0:45 | Demo: ConfigDB. Watch the terminal output and confirm you see the expected pass message. |
| 70 | Demo: Factory Pattern | 0:45 | Demo: Factory Pattern. Watch the terminal output and confirm you see the expected pass message. |
| 71 | Demo: Objection Mechanism | 0:45 | Demo: Objection Mechanism. Watch the terminal output and confirm you see the expected pass message. |
| 72 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 73 | What you should know (1/3) | 0:36 | By now you should be able to explain the following. Understand UVM methodology Explain UVM class hierarchy Understand and use UVM phases Use UVM reporting effectively Use ConfigDB for configuration From MODULE3 Learning Outcomes. |
| 74 | What you should know (2/3) | 0:36 | By now you should be able to explain the following. Create UVM test classes Structure UVM environments Use objection mechanism Execute UVM tests Test class definition From MODULE3 Learning Outcomes. |
| 75 | What you should know (3/3) | 0:16 | By now you should be able to explain the following. Objection mechanism From MODULE3 Learning Outcomes. |
| 76 | Exercises | 0:32 | Exercises. Test Class Creation Environment Structure Reporting Configuration Phase Understanding |
| 77 | Assessment checklist | 0:36 | Assessment checklist. Understands UVM methodology Can explain class hierarchy Understands all UVM phases Can use UVM reporting Can use ConfigDB |
| 78 | Summary & next steps | 0:28 | In summary: Master UVM class hierarchy and phases Next up: Next module in course. Master UVM class hierarchy and phases Complete module3/CHECKLIST.md Review module3/EXAMPLES.md and run each lab Next: Next module in course |

        ## Section narration (edit for TTS)

        - **How to learn:** Solid cocotb skills from Module 2 — you will reuse trigger timing inside pyuvm drivers later Then Read `module3/dut/simple_blocks/adder.v` — combinational operands `a`, `b`, output `sum` Then Step through `module3/examples/phases/` and `class_hierarchy/` before integrated `test_simple_uvm.py` Then Understand UVM phase order: build → connect → run (with objections) → report.
- **Design architecture (RTL and interfaces, UVM testbench architecture, Execution pipeline, Module layout):** Walk through the block diagram, then relate each block to files under module3/examples/.
- **Verification (Phase-based test execution, Stimulus and checking, Step-by-step lab execution, Closure):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 10 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module3/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE3.md` and `module3/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 3`
