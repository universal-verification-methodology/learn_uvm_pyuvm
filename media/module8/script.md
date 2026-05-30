        # Narration script — Module 8: UVM Miscellaneous Utilities

        **Target length:** ~42 minutes (85 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 8 | 0:25 | Welcome to module 8, UVM Miscellaneous Utilities. In this module you will master uvm utility classes and helper functions. |
| 2 | Learning objectives | 0:16 | Here is what you will learn in this module. Master UVM utility classes and helper functions |
| 3 | Prerequisites | 0:16 | Before you start, make sure you have these prerequisites. See module README |
| 4 | Learning path | 0:22 | Learning path. Master UVM utility classes and helper functions |
| 5 | Overview | 0:16 | Overview. This module covers the miscellaneous utilities provided by UVM that support verification environments. These utilities include... |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:32 | Follow this learning path. Read the guides before running the labs. Modules 4–7 env patterns should be fresh — utilities attach to analysis ports and phase hooks you already built No new large DUT focus; module8/dut/dma/simple_dma.v reuses DMA block as a lightweight integration anchor Run CLP example first — plusargs configure tests without recompilation Study comparators and recorders on... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. Utility layer in the testbench | 0:38 | 1. Utility layer in the testbench. No new large DUT focus — utilities plug into existing envs from prior modules CLP (uvm_cmdline_processor) configures tests without recompilation Comparators, recorders, pools, queues support analysis and debug infrastructure String/math/random helpers reduce boilerplate in checks and stimulus Refer to the diagram on the right. |
| 10 | 2. How utilities attach | 0:38 | 2. How utilities attach. Comparators sit on analysis ports beside scoreboards Recorders log transactions to files for offline review Pools/queues manage recycled objects and ordered work lists CLP reads plusargs before build/run to select tests and verbosity Refer to the diagram on the right. |
| 11 | 3. Execution pipeline | 0:28 | 3. Execution pipeline. Build: standard Verilator compile; utilities instantiate during env build like other components Connect: comparators/recorders tap monitor analysis ports alongside scoreboard Sim: CLP-selected sequences run; recorders flush on phase boundaries; pools recycle transaction objects Check: comparators flag ordering/equality violations; logs + UVM report provide offline audit... |
| 12 | 4. Integration architecture | 0:28 | 4. Integration architecture. module8/examples/integration/ wires multiple utilities in one mini-env Tests under module8/tests/pyuvm_tests/ prove utilities under simulation Pattern: configure via CLP → run sequence → compare → record → report Reuse utilities in Module 6/7 style envs for capstone projects |
| 13 | Comparator on analysis port | 0:28 | Comparator on analysis port. Review the code on screen and match it to files in the repository. |
| 14 | Key files to study | 0:08 | Next section: Key files to study. |
| 15 | Open these in the repo | 0:36 | Open these in the repo. module8/examples/clp/clp_example.py — uvm_cmdline_processor plusarg parsing module8/examples/comparators/comparator_example.py — equal/less/greater compare policies module8/examples/recorders/recorder_example.py — transaction logging to files module8/examples/pools/pool_example.py and queues/queue_example.py — object reuse and ordered work... |
| 16 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 17 | 1. Utility-focused test methods | 0:34 | 1. Utility-focused test methods. Comparator tests: equal/less/greater policies on transaction streams Recorder tests: verify log format and flush on phase boundaries CLP tests: plusargs override seed, verbosity, and test name Refer to the diagram on the right. |
| 18 | 2. Efficiency and reuse | 0:24 | 2. Efficiency and reuse. Object pools cut allocation churn in high-transaction regressions Queues order deferred checks or secondary stimulus Random/string/math utils keep constraints readable in sequences |
| 19 | 3. Step-by-step lab execution | 0:32 | 3. Step-by-step lab execution. 1. CLP: ./scripts/module8.sh --clp — exercise plusarg overrides 2. Compare/record: ./scripts/module8.sh --comparators --recorders 3. Pools/queues: ./scripts/module8.sh --pools --queues 4. Helpers: ./scripts/module8.sh --string-utils --math-utils --random-utils 5. Capstone: ./scripts/module8.sh --integration --pyuvm-tests — full utility integration pass |
| 20 | 4. Closure | 0:24 | 4. Closure. ./scripts/module8.sh --pyuvm-tests across all utility examples Assessment: CLP, comparators, recorders, pools, queues, integration Capstone: combine utilities with Module 6/7 style envs in your own project |
| 21 | CLP plusarg configuration | 0:28 | CLP plusarg configuration. Review the code on screen and match it to files in the repository. |
| 22 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 23 | 1. UVM Command Line Processor (CLP) (1/4) | 0:36 | 1. UVM Command Line Processor (CLP) (1/4). Command Line Processor Overview What is CLP? Why use CLP? CLP benefits CLP vs manual argument parsing |
| 24 | 1. UVM Command Line Processor (CLP) (2/4) | 0:36 | 1. UVM Command Line Processor (CLP) (2/4). Getting command-line arguments Argument types (string, int, bit, time) Default values Argument validation CLP Methods |
| 25 | 1. UVM Command Line Processor (CLP) (3/4) | 0:36 | 1. UVM Command Line Processor (CLP) (3/4). get_arg_values() - Get multiple values get_arg_count() - Get argument count has_arg() - Check if argument exists CLP Patterns Test configuration via command line |
| 26 | 1. UVM Command Line Processor (CLP) (4/4) | 0:20 | 1. UVM Command Line Processor (CLP) (4/4). Simulation control via command line Best practices |
| 27 | 2. UVM Comparators (1/5) | 0:36 | 2. UVM Comparators (1/5). Comparator Overview What are comparators? Comparator purpose When to use comparators Comparator types |
| 28 | 2. UVM Comparators (2/5) | 0:36 | 2. UVM Comparators (2/5). uvm_in_order_comparator - In-order comparison uvm_algorithmic_comparator - Algorithmic comparison Comparator characteristics Comparator selection In-Order Comparator |
| 29 | 2. UVM Comparators (3/5) | 0:36 | 2. UVM Comparators (3/5). Transaction matching Comparison logic Error reporting Algorithmic Comparator Custom comparison algorithms |
| 30 | 2. UVM Comparators (4/5) | 0:36 | 2. UVM Comparators (4/5). Comparison functions Use cases Comparator Implementation Creating comparators Connecting comparators |
| 31 | 2. UVM Comparators (5/5) | 0:16 | 2. UVM Comparators (5/5). Using comparators in scoreboards |
| 32 | 3. UVM Recorders (1/5) | 0:36 | 3. UVM Recorders (1/5). Recorder Overview What are recorders? Recorder purpose Transaction recording Recording benefits |
| 33 | 3. UVM Recorders (2/5) | 0:36 | 3. UVM Recorders (2/5). uvm_text_recorder - Text recording uvm_tr_database - Transaction database Recording formats Recording selection Recorder Usage |
| 34 | 3. UVM Recorders (3/5) | 0:36 | 3. UVM Recorders (3/5). Recording transactions Recording configuration Recording analysis Transaction Recording Recording sequence items |
| 35 | 3. UVM Recorders (4/5) | 0:36 | 3. UVM Recorders (4/5). Recording timing Recording relationships Recorder Implementation Creating recorders Connecting recorders |
| 36 | 3. UVM Recorders (5/5) | 0:16 | 3. UVM Recorders (5/5). Analyzing recordings |
| 37 | 4. UVM Pools (1/5) | 0:36 | 4. UVM Pools (1/5). Object Pool Overview What are pools? Pool purpose Object reuse Performance benefits |
| 38 | 4. UVM Pools (2/5) | 0:36 | 4. UVM Pools (2/5). uvm_pool - Generic object pool Pool characteristics Pool operations Pool use cases Pool Usage |
| 39 | 4. UVM Pools (3/5) | 0:36 | 4. UVM Pools (3/5). Adding objects to pools Getting objects from pools Pool management Pool Implementation Pool creation |
| 40 | 4. UVM Pools (4/5) | 0:36 | 4. UVM Pools (4/5). Object deallocation Pool cleanup Pool Patterns Transaction pooling Sequence item pooling |
| 41 | 4. UVM Pools (5/5) | 0:16 | 4. UVM Pools (5/5). Memory management |
| 42 | 5. UVM Queues (1/5) | 0:36 | 5. UVM Queues (1/5). Queue Overview What are queues? Queue purpose Queue vs list Queue benefits |
| 43 | 5. UVM Queues (2/5) | 0:36 | 5. UVM Queues (2/5). uvm_queue - Generic queue Queue characteristics Queue operations Queue use cases Queue Usage |
| 44 | 5. UVM Queues (3/5) | 0:36 | 5. UVM Queues (3/5). Adding items to queues Removing items from queues Queue management Queue Implementation Queue creation |
| 45 | 5. UVM Queues (4/5) | 0:36 | 5. UVM Queues (4/5). Queue iteration Queue cleanup Queue Patterns Transaction queues Scoreboard queues |
| 46 | 5. UVM Queues (5/5) | 0:16 | 5. UVM Queues (5/5). Queue best practices |
| 47 | 6. UVM String Utilities (1/3) | 0:36 | 6. UVM String Utilities (1/3). String Utility Overview String manipulation needs UVM string utilities Utility benefits When to use utilities |
| 48 | 6. UVM String Utilities (2/3) | 0:36 | 6. UVM String Utilities (2/3). String formatting String conversion String manipulation String comparison String Utility Methods |
| 49 | 6. UVM String Utilities (3/3) | 0:24 | 6. UVM String Utilities (3/3). Formatting functions Conversion functions Utility patterns |
| 50 | 7. UVM Math Utilities (1/3) | 0:36 | 7. UVM Math Utilities (1/3). Math Utility Overview Mathematical operations UVM math utilities Utility benefits When to use utilities |
| 51 | 7. UVM Math Utilities (2/3) | 0:36 | 7. UVM Math Utilities (2/3). Random number generation Statistical functions Mathematical utilities Math patterns Math Utility Methods |
| 52 | 7. UVM Math Utilities (3/3) | 0:24 | 7. UVM Math Utilities (3/3). Random functions Statistical functions Utility patterns |
| 53 | 8. UVM Random Utilities (1/3) | 0:36 | 8. UVM Random Utilities (1/3). Random Utility Overview Random number generation UVM random utilities Randomization support Random patterns |
| 54 | 8. UVM Random Utilities (2/3) | 0:36 | 8. UVM Random Utilities (2/3). Random value generation Constrained random Random seeds Random control Random Utility Methods |
| 55 | 8. UVM Random Utilities (3/3) | 0:24 | 8. UVM Random Utilities (3/3). Seed management Random state Utility patterns |
| 56 | 9. UVM Primitives (1/3) | 0:36 | 9. UVM Primitives (1/3). Primitive Overview What are primitives? Primitive purpose Primitive types Primitive use cases |
| 57 | 9. UVM Primitives (2/3) | 0:36 | 9. UVM Primitives (2/3). Common primitives Primitive operations Primitive characteristics Primitive selection Primitive Usage |
| 58 | 9. UVM Primitives (3/3) | 0:24 | 9. UVM Primitives (3/3). Primitive patterns Primitive best practices Primitive examples |
| 59 | 10. UVM Macros (Python Context) (1/2) | 0:36 | 10. UVM Macros (Python Context) (1/2). Macro Overview Macros in SystemVerilog vs Python Python alternatives Utility functions Helper decorators |
| 60 | 10. UVM Macros (Python Context) (2/2) | 0:28 | 10. UVM Macros (Python Context) (2/2). Macro alternatives Utility functions Decorator patterns Helper classes |
| 61 | 11. Utility Integration (1/3) | 0:36 | 11. Utility Integration (1/3). Using Utilities in Testbenches When to use utilities Utility selection Utility integration Utility patterns |
| 62 | 11. Utility Integration (2/3) | 0:36 | 11. Utility Integration (2/3). Utility usage guidelines Performance considerations Memory management Utility organization Common Utility Patterns |
| 63 | 11. Utility Integration (3/3) | 0:24 | 11. Utility Integration (3/3). Transaction comparison Transaction recording Object management |
| 64 | Command reference highlights | 0:08 | Next section: Command reference highlights. |
| 65 | Core utilities | 0:24 | Core utilities. ./scripts/module8.sh --clp --comparators --recorders — configure, compare, and log infrastructure ./scripts/module8.sh --pools --queues — allocation efficiency and ordered deferred work ./scripts/module8.sh --string-utils --math-utils --random-utils — helper libraries for checks/stimulus Full detail in docs/MODULE8.md command reference. |
| 66 | Integration and tests | 0:24 | Integration and tests. ./scripts/module8.sh --integration — combined utility mini-env ./scripts/module8.sh --pyuvm-tests — test_utilities.py regression cd module8/tests/pyuvm_tests && make SIM=verilator TEST=test_utilities Full detail in docs/MODULE8.md command reference. |
| 67 | CLP-driven runs | 0:24 | CLP-driven runs. Pass plusargs through Makefile/SIM_ARGS where examples support seed, verbosity, test name overrides Re-run same binary with different plusargs — demonstrates no-recompile test selection ./scripts/module8.sh — full utility sweep for module completion Full detail in docs/MODULE8.md command reference. |
| 68 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 69 | Module 8 orchestrator | 0:45 | Module 8 orchestrator. Watch the terminal output and confirm you see the expected pass message. |
| 70 | Demo: Command Line Processor | 0:45 | Demo: Command Line Processor. Watch the terminal output and confirm you see the expected pass message. |
| 71 | Demo: Comparators | 0:45 | Demo: Comparators. Watch the terminal output and confirm you see the expected pass message. |
| 72 | Demo: Recorders | 0:45 | Demo: Recorders. Watch the terminal output and confirm you see the expected pass message. |
| 73 | Demo: Pools | 0:45 | Demo: Pools. Watch the terminal output and confirm you see the expected pass message. |
| 74 | Demo: Queues | 0:45 | Demo: Queues. Watch the terminal output and confirm you see the expected pass message. |
| 75 | Demo: String Utilities | 0:45 | Demo: String Utilities. Watch the terminal output and confirm you see the expected pass message. |
| 76 | Demo: Math Utilities | 0:45 | Demo: Math Utilities. Watch the terminal output and confirm you see the expected pass message. |
| 77 | Demo: Random Utilities | 0:45 | Demo: Random Utilities. Watch the terminal output and confirm you see the expected pass message. |
| 78 | Demo: Utility Integration | 0:45 | Demo: Utility Integration. Watch the terminal output and confirm you see the expected pass message. |
| 79 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 80 | What you should know (1/3) | 0:36 | By now you should be able to explain the following. Use UVM Command Line Processor Implement and use comparators Use recorders for transaction recording Use pools for object management Use queues for data structures From MODULE8 Learning Outcomes. |
| 81 | What you should know (2/3) | 0:36 | By now you should be able to explain the following. Use random utilities effectively Integrate utilities into testbenches Apply utility best practices Choose appropriate utilities for tasks CLP usage From MODULE8 Learning Outcomes. |
| 82 | What you should know (3/3) | 0:16 | By now you should be able to explain the following. Configuration via command line From MODULE8 Learning Outcomes. |
| 83 | Exercises | 0:32 | Exercises. Command Line Processor Comparator Implementation Recorder Usage Pool and Queue Usage Utility Integration |
| 84 | Assessment checklist | 0:36 | Assessment checklist. Can use Command Line Processor Can implement and use comparators Can use recorders effectively Can use pools for object management Can use queues for data structures |
| 85 | Summary & next steps | 0:28 | In summary: Master UVM utility classes and helper functions Next up: Next module in course. Master UVM utility classes and helper functions Complete module8/CHECKLIST.md Review module8/EXAMPLES.md and run each lab Next: Next module in course |

        ## Section narration (edit for TTS)

        - **How to learn:** Modules 4–7 env patterns should be fresh — utilities attach to analysis ports and phase hooks you already built Then No new large DUT focus; `module8/dut/dma/simple_dma.v` reuses DMA block as a lightweight integration anchor Then Run CLP example first — plusargs configure tests without recompilation Then Study comparators and recorders on analysis ports before pools/queues efficiency labs.
- **Design architecture (Utility layer in the testbench, How utilities attach, Execution pipeline, Integration architecture):** Walk through the block diagram, then relate each block to files under module8/examples/.
- **Verification (Utility-focused test methods, Efficiency and reuse, Step-by-step lab execution, Closure):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 11 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module8/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE8.md` and `module8/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 8`
