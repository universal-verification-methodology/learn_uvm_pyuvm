        # Narration script — Module 4: UVM Components

        **Target length:** ~42 minutes (84 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 4 | 0:25 | Welcome to module 4, UVM Components. In this module you will build complete uvm agents with driver, monitor, and sequencer. |
| 2 | Learning objectives | 0:16 | Here is what you will learn in this module. Build complete UVM agents with driver, monitor, and sequencer |
| 3 | Prerequisites | 0:16 | Before you start, make sure you have these prerequisites. See module README |
| 4 | Learning path | 0:22 | Learning path. Build complete UVM agents with driver, monitor, and sequencer |
| 5 | Overview | 0:16 | Overview. This module covers the core UVM components used to build verification environments. You'll learn how to create agents, drivers... |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:32 | Follow this learning path. Read the guides before running the labs. Module 3 UVM hierarchy and phases must be comfortable — agents bundle components you studied separately Study module4/dut/interfaces/simple_interface.v valid/ready handshake before driver labs Run examples in order: transactions → driver → monitor → sequencer → scoreboard → TLM → agents Read InterfaceTransaction field... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. DUT and interface protocol | 0:34 | 1. DUT and interface protocol. module4/dut/interfaces/simple_interface.v — valid/ready handshake, address/data/result buses Clocked, resettable interface models streaming transactions Agent maps one transaction type to one interface beat Refer to the diagram on the right. |
| 10 | 2. Agent-centric UVM architecture | 0:38 | 2. Agent-centric UVM architecture. Agent bundles driver, monitor, sequencer; env holds agent + scoreboard TLM analysis ports connect monitor → scoreboard (and optional coverage) InterfaceTransaction defines fields, copy/compare, and constraints Complete path: sequence → sequencer → driver → DUT → monitor → scoreboard Refer to the diagram on the right. |
| 11 | 3. Execution pipeline | 0:28 | 3. Execution pipeline. Build: Verilator compiles simple_interface.v; env builds agent (driver, monitor, sequencer) and scoreboard Connect: monitor ap → scoreboard exp/act analysis imports; sequencer ↔ driver TLM ports Sim: sequence items drive valid/ready beats; monitor reconstructs transactions on completed handshakes Check: scoreboard compare on monitored vs predicted streams; UVM report... |
| 12 | 4. Component responsibilities | 0:28 | 4. Component responsibilities. Driver: pull items from sequencer, drive pins per protocol Monitor: passive observation, broadcast transactions on analysis port Sequencer: arbitration and sequence execution Scoreboard: expected vs actual from monitor streams |
| 13 | Interface — valid/ready handshake | 0:28 | Interface — valid/ready handshake. Review the code on screen and match it to files in the repository. |
| 14 | Agent-centric env wiring | 0:28 | Agent-centric env wiring. Review the code on screen and match it to files in the repository. |
| 15 | Key files to study | 0:08 | Next section: Key files to study. |
| 16 | Open these in the repo | 0:36 | Open these in the repo. module4/dut/interfaces/simple_interface.v — valid/ready streaming interface with addr/data/result module4/examples/transactions/transaction_example.py — sequence item fields and compare/copy module4/examples/drivers/driver_example.py — sequencer pull loop and pin wiggling module4/examples/monitors/monitor_example.py — passive sampling and analysis port broadcast... |
| 17 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 18 | 1. Integration testing method | 0:34 | 1. Integration testing method. test_complete_agent.py — end-to-end agent, env, and test class Run: ./scripts/module4.sh --pyuvm-tests or make TEST=test_complete_agent Per-component examples (driver_example.py, …) isolate behavior before integration Refer to the diagram on the right. |
| 19 | 2. Checking strategy | 0:24 | 2. Checking strategy. Scoreboard compares monitored results to predicted model or golden vectors Analysis port fan-out allows multiple checkers without changing monitor Sequences provide repeatable stimulus; random/constrained extensions in exercises |
| 20 | 3. Step-by-step lab execution | 0:32 | 3. Step-by-step lab execution. 1. Transactions: ./scripts/module4.sh --transactions 2. Driver/monitor/sequencer: ./scripts/module4.sh --drivers --monitors --sequencers 3. Scoreboard/TLM: ./scripts/module4.sh --scoreboards --tlm 4. Agent assembly: ./scripts/module4.sh --agents 5. Capstone: ./scripts/module4.sh --pyuvm-tests — confirm scoreboard clean and UVM TEST PASSED |
| 21 | 4. Closure | 0:24 | 4. Closure. Self-check via ./scripts/module4.sh --pyuvm-tests; demo screenshots per EXAMPLES.md section Assessment: drivers, monitors, sequencers, agents, scoreboards, TLM connections You should trace one transaction from sequence item through to scoreboard compare |
| 22 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 23 | 1. UVM Agent Architecture (1/3) | 0:36 | 1. UVM Agent Architecture (1/3). Agent Overview What is an agent? Agent components Agent purpose Agent types |
| 24 | 1. UVM Agent Architecture (2/3) | 0:36 | 1. UVM Agent Architecture (2/3). Active agents (driver + sequencer + monitor) Passive agents (monitor only) When to use each Agent configuration Agent Structure |
| 25 | 1. UVM Agent Architecture (3/3) | 0:24 | 1. UVM Agent Architecture (3/3). Monitor component Sequencer component Agent container |
| 26 | 2. UVM Driver Implementation (1/4) | 0:36 | 2. UVM Driver Implementation (1/4). Driver Overview Driver purpose Driver responsibilities Driver interface Driver lifecycle |
| 27 | 2. UVM Driver Implementation (2/4) | 0:36 | 2. UVM Driver Implementation (2/4). Inheriting from uvm_driver run_phase() implementation Transaction reception Signal driving Driver-Sequencer Communication |
| 28 | 2. UVM Driver Implementation (3/4) | 0:36 | 2. UVM Driver Implementation (3/4). get_next_item() item_done() Transaction flow Signal-Level Driving DUT signal access |
| 29 | 2. UVM Driver Implementation (4/4) | 0:20 | 2. UVM Driver Implementation (4/4). Timing control Protocol implementation |
| 30 | 3. UVM Monitor Implementation (1/4) | 0:36 | 3. UVM Monitor Implementation (1/4). Monitor Overview Monitor purpose Monitor responsibilities Monitor types Monitor lifecycle |
| 31 | 3. UVM Monitor Implementation (2/4) | 0:36 | 3. UVM Monitor Implementation (2/4). Inheriting from uvm_monitor run_phase() implementation Signal sampling Transaction creation Analysis Ports |
| 32 | 3. UVM Monitor Implementation (3/4) | 0:36 | 3. UVM Monitor Implementation (3/4). Creating analysis ports Writing to analysis ports Analysis port connections Transaction Creation Sampling signals |
| 33 | 3. UVM Monitor Implementation (4/4) | 0:20 | 3. UVM Monitor Implementation (4/4). Populating transaction fields Broadcasting transactions |
| 34 | 4. UVM Sequencer and Sequences (1/5) | 0:36 | 4. UVM Sequencer and Sequences (1/5). Sequencer Overview Sequencer purpose Sequencer responsibilities Sequencer types Sequencer lifecycle |
| 35 | 4. UVM Sequencer and Sequences (2/5) | 0:36 | 4. UVM Sequencer and Sequences (2/5). Inheriting from uvm_sequencer Default sequencer usage Custom sequencer features Sequencer configuration Sequence Items |
| 36 | 4. UVM Sequencer and Sequences (3/5) | 0:36 | 4. UVM Sequencer and Sequences (3/5). Transaction definition Transaction fields Transaction methods Sequence Basics uvm_sequence base class |
| 37 | 4. UVM Sequencer and Sequences (4/5) | 0:36 | 4. UVM Sequencer and Sequences (4/5). Sequence execution Sequence lifecycle Sequence Operations start_item() finish_item() |
| 38 | 4. UVM Sequencer and Sequences (5/5) | 0:16 | 4. UVM Sequencer and Sequences (5/5). Transaction creation |
| 39 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (1/1 | 0:36 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (1/11). TLM Overview What is TLM? TLM benefits TLM abstraction levels TLM communication patterns |
| 40 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (2/1 | 0:36 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (2/11). put interface - Unidirectional blocking put get interface - Unidirectional blocking get peek interface - Unidirectional non-blocking peek transport interface - Bidirectional blocking transport Interface characteristics and use cases |
| 41 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (3/1 | 0:36 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (3/11). uvm_put_port - Put port uvm_get_port - Get port uvm_peek_port - Peek port uvm_transport_port - Transport port Port vs export vs implementation |
| 42 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (4/1 | 0:36 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (4/11). uvm_put_export - Put export uvm_get_export - Get export uvm_peek_export - Peek export uvm_transport_export - Transport export Export usage patterns |
| 43 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (5/1 | 0:36 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (5/11). uvm_put_imp - Put implementation uvm_get_imp - Get implementation uvm_peek_imp - Peek implementation uvm_transport_imp - Transport implementation Implementation requirements |
| 44 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (6/1 | 0:36 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (6/11). Analysis port concept Publisher-subscriber pattern Broadcast communication One-to-many connections uvm_analysis_port - Analysis port |
| 45 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (7/1 | 0:36 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (7/11). uvm_analysis_imp - Analysis implementation Connection patterns TLM FIFOs uvm_tlm_fifo - TLM FIFO FIFO purpose and usage |
| 46 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (8/1 | 0:36 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (8/11). FIFO connection patterns When to use FIFOs TLM Connection Patterns Direct connections (port to export) FIFO connections (port to FIFO to export) |
| 47 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (9/1 | 0:36 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (9/11). Hierarchical connections Connection best practices TLM Usage Patterns Producer-consumer pattern Request-response pattern |
| 48 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (10/ | 0:36 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (10/11). Pipeline pattern TLM vs analysis ports TLM Implementation Examples Using put/get interfaces Using transport interface |
| 49 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (11/ | 0:20 | 5. TLM (Transaction-Level Modeling) - Complete Coverage (11/11). Combining TLM types TLM debugging |
| 50 | 6. Scoreboard Implementation (1/4) | 0:36 | 6. Scoreboard Implementation (1/4). Scoreboard Overview Scoreboard purpose Scoreboard types Scoreboard responsibilities Scoreboard lifecycle |
| 51 | 6. Scoreboard Implementation (2/4) | 0:36 | 6. Scoreboard Implementation (2/4). Inheriting from uvm_component Analysis port connections Transaction storage Comparison logic Scoreboard Patterns |
| 52 | 6. Scoreboard Implementation (3/4) | 0:36 | 6. Scoreboard Implementation (3/4). Expected vs actual Transaction matching Error reporting Advanced Scoreboards Multi-channel scoreboards |
| 53 | 6. Scoreboard Implementation (4/4) | 0:20 | 6. Scoreboard Implementation (4/4). Complex comparison logic Performance optimization |
| 54 | 7. Transaction-Level Modeling (1/3) | 0:36 | 7. Transaction-Level Modeling (1/3). Transaction Concepts What are transactions? Transaction abstraction Transaction fields Transaction methods |
| 55 | 7. Transaction-Level Modeling (2/3) | 0:36 | 7. Transaction-Level Modeling (2/3). Transaction class structure Field definition Constraint definition Method implementation Transaction Operations |
| 56 | 7. Transaction-Level Modeling (3/3) | 0:24 | 7. Transaction-Level Modeling (3/3). Transaction copying Transaction comparison Transaction conversion |
| 57 | 8. Complete Agent Example (1/3) | 0:36 | 8. Complete Agent Example (1/3). Agent Structure Agent class definition Component instantiation Component connections Agent configuration |
| 58 | 8. Complete Agent Example (2/3) | 0:36 | 8. Complete Agent Example (2/3). Component creation Configuration application Active/passive selection Agent Connect Phase Driver-sequencer connection |
| 59 | 8. Complete Agent Example (3/3) | 0:16 | 8. Complete Agent Example (3/3). External connections |
| 60 | 9. Sequence Libraries (1/2) | 0:36 | 9. Sequence Libraries (1/2). Sequence Organization Base sequences Derived sequences Sequence libraries Sequence reuse |
| 61 | 9. Sequence Libraries (2/2) | 0:28 | 9. Sequence Libraries (2/2). Simple sequences Random sequences Constrained sequences Layered sequences |
| 62 | 10. Agent Integration (1/2) | 0:36 | 10. Agent Integration (1/2). Environment Integration Adding agents to environment Agent configuration Agent connections Agent coordination |
| 63 | 10. Agent Integration (2/2) | 0:28 | 10. Agent Integration (2/2). Agent instantiation Sequence execution Test coordination Result checking |
| 64 | Command reference highlights | 0:08 | Next section: Command reference highlights. |
| 65 | Per-component examples | 0:24 | Per-component examples. ./scripts/module4.sh --transactions --drivers --monitors — stimulus and observation building blocks ./scripts/module4.sh --sequencers --scoreboards --tlm — sequence flow and analysis connections ./scripts/module4.sh --agents — complete agent wiring before capstone test Full detail in docs/MODULE4.md command reference. |
| 66 | Integration test | 0:24 | Integration test. ./scripts/module4.sh --pyuvm-tests — run test_complete_agent via orchestrator cd module4/tests/pyuvm_tests && make SIM=verilator TEST=test_complete_agent ./scripts/module4.sh --skip-examples --pyuvm-tests — capstone only when components are understood Full detail in docs/MODULE4.md command reference. |
| 67 | Debug paths | 0:24 | Debug paths. Run individual example Make under module4/examples/<component>/ to isolate failures Increase UVM verbosity to trace sequence → driver → monitor transaction paths Verilator waveforms on interface valid/ready when handshake debug is needed Full detail in docs/MODULE4.md command reference. |
| 68 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 69 | Module 4 orchestrator | 0:45 | Module 4 orchestrator. Watch the terminal output and confirm you see the expected pass message. |
| 70 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 71 | Demo: Driver Implementation | 0:45 | Demo: Driver Implementation. Watch the terminal output and confirm you see the expected pass message. |
| 72 | Demo: Monitor Implementation | 0:45 | Demo: Monitor Implementation. Watch the terminal output and confirm you see the expected pass message. |
| 73 | Demo: Sequencer and Sequences | 0:45 | Demo: Sequencer and Sequences. Watch the terminal output and confirm you see the expected pass message. |
| 74 | Demo: Complete Agent | 0:45 | Demo: Complete Agent. Watch the terminal output and confirm you see the expected pass message. |
| 75 | Demo: Scoreboard Implementation | 0:45 | Demo: Scoreboard Implementation. Watch the terminal output and confirm you see the expected pass message. |
| 76 | Demo: TLM Communication | 0:45 | Demo: TLM Communication. Watch the terminal output and confirm you see the expected pass message. |
| 77 | Demo: Transaction Modeling | 0:45 | Demo: Transaction Modeling. Watch the terminal output and confirm you see the expected pass message. |
| 78 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 79 | What you should know (1/3) | 0:36 | By now you should be able to explain the following. Understand agent architecture Implement UVM drivers Implement UVM monitors Implement sequencers and sequences Use analysis ports effectively From MODULE4 Learning Outcomes. |
| 80 | What you should know (2/3) | 0:36 | By now you should be able to explain the following. Design transaction models Build complete agents Integrate agents into environments Execute sequences in tests Driver class From MODULE4 Learning Outcomes. |
| 81 | What you should know (3/3) | 0:16 | By now you should be able to explain the following. Signal driving From MODULE4 Learning Outcomes. |
| 82 | Exercises | 0:32 | Exercises. Driver Implementation Monitor Implementation Sequence Creation Agent Building Scoreboard Implementation |
| 83 | Assessment checklist | 0:36 | Assessment checklist. Understands agent architecture Can implement drivers Can implement monitors Can implement sequencers Can create sequences |
| 84 | Summary & next steps | 0:28 | In summary: Build complete UVM agents with driver, monitor, and sequencer Next up: Next module in course. Build complete UVM agents with driver, monitor, and sequencer Complete module4/CHECKLIST.md Review module4/EXAMPLES.md and run each lab Next: Next module in course |

        ## Section narration (edit for TTS)

        - **How to learn:** Module 3 UVM hierarchy and phases must be comfortable — agents bundle components you studied separately Then Study `module4/dut/interfaces/simple_interface.v` valid/ready handshake before driver labs Then Run examples in order: transactions → driver → monitor → sequencer → scoreboard → TLM → agents Then Read `InterfaceTransaction` field definitions and `copy`/`compare` before scoreboard integration.
- **Design architecture (DUT and interface protocol, Agent-centric UVM architecture, Execution pipeline, Component responsibilities):** Walk through the block diagram, then relate each block to files under module4/examples/.
- **Verification (Integration testing method, Checking strategy, Step-by-step lab execution, Closure):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 10 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module4/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE4.md` and `module4/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 4`
