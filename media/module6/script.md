        # Narration script — Module 6: Complex Testbenches

        **Target length:** ~32 minutes (67 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 6 | 0:25 | Welcome to module 6, Complex Testbenches. In this module you will build complex multi-agent testbenches with protocol verification. |
| 2 | Learning objectives | 0:16 | Here is what you will learn in this module. Build complex multi-agent testbenches with protocol verification |
| 3 | Prerequisites | 0:16 | Before you start, make sure you have these prerequisites. See module README |
| 4 | Learning path | 0:22 | Learning path. Build complex multi-agent testbenches with protocol verification |
| 5 | Overview | 0:16 | Overview. This module focuses on building complex verification environments with multiple agents, protocol verification, advanced testbench... |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:32 | Follow this learning path. Read the guides before running the labs. Module 5 multi-agent and virtual sequence patterns carry forward — AXI adds real protocol timing Read module6/dut/protocols/axi4_lite_slave.v AW/W/B/AR/R channel interfaces before stimulus Run --multi-agent and --protocol examples before --protocol-checkers and scoreboard labs Understand initiator vs slave roles: DUT is slave... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. Protocol DUT architecture | 0:34 | 1. Protocol DUT architecture. module6/dut/protocols/axi4_lite_slave.v — five-channel AXI4-Lite slave + memory interface Separate address/write/read response channels exercise real protocol timing Multi-agent TB can attach initiator agents while DUT acts as slave Refer to the diagram on the right. |
| 10 | 2. Complex testbench architecture | 0:38 | 2. Complex testbench architecture. Multiple agents (e.g., master, memory, low-speed peripheral) under one uvm_env Protocol checkers validate handshake rules independent of scoreboard Layered scoreboards: per-agent checks + system-level consistency Architecture example documents reusable env patterns and package boundaries Refer to the diagram on the right. |
| 11 | 3. Execution pipeline | 0:28 | 3. Execution pipeline. Build: Verilator compiles AXI slave RTL; env instantiates master/memory/peripheral agents and checkers Connect: each agent monitor feeds protocol checker and scoreboard analysis ports Sim: virtual sequences configure agents then launch concurrent read/write traffic to slave Check: protocol checker asserts channel rules; scoreboard correlates addr/data/response across ports |
| 12 | 4. Data flow | 0:28 | 4. Data flow. Virtual sequences coordinate cross-agent scenarios (config then traffic) Monitors on each interface feed checkers and coverage Reference models optional for memory content golden checks System scoreboard ties master observations to slave memory updates |
| 13 | DUT — AXI4-Lite slave | 0:28 | DUT — AXI4-Lite slave. Review the code on screen and match it to files in the repository. |
| 14 | Multi-agent testbench | 0:28 | Multi-agent testbench. Review the code on screen and match it to files in the repository. |
| 15 | Key files to study | 0:08 | Next section: Key files to study. |
| 16 | Open these in the repo | 0:36 | Open these in the repo. module6/dut/protocols/axi4_lite_slave.v — five-channel AXI4-Lite slave with memory port module6/examples/protocol/protocol_example.py — directed AXI4-Lite transactions module6/examples/multi_agent/multi_agent_example.py — multiple agents under one env module6/examples/protocol_checkers/protocol_checker_example.py — handshake rule assertions... |
| 17 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 18 | 1. Protocol verification methods | 0:34 | 1. Protocol verification methods. Protocol checker asserts AW/W/B/AR/R channel rules and ordering Directed AXI transactions in protocol_example.py and test_complex_testbench Multi-agent tests verify concurrent masters do not violate slave assumptions Refer to the diagram on the right. |
| 19 | 2. System-level checking | 0:24 | 2. System-level checking. Scoreboard correlates transactions across ports (address, data, response) Architecture tests validate env wiring before long regressions Debug: transaction logs, UVM verbosity, Verilator waveforms |
| 20 | 3. Step-by-step lab execution | 0:32 | 3. Step-by-step lab execution. 1. Multi-agent wiring: ./scripts/module6.sh --multi-agent 2. Directed protocol: ./scripts/module6.sh --protocol 3. Protocol checkers: ./scripts/module6.sh --protocol-checkers 4. Scoreboards/architecture: ./scripts/module6.sh --scoreboards --architecture 5. System regression: ./scripts/module6.sh --pyuvm-tests — full complex testbench pass |
| 21 | 4. Closure | 0:24 | 4. Closure. ./scripts/module6.sh --pyuvm-tests; exercises extend multi-agent and protocol checkers Assessment: multi-agent envs, protocol verification, complex scoreboards, architecture patterns Explain how checker failures differ from scoreboard data mismatches |
| 22 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 23 | 1. Multi-Agent Environments (1/3) | 0:36 | 1. Multi-Agent Environments (1/3). Environment Architecture Multiple agent coordination Agent communication Environment hierarchy Environment patterns |
| 24 | 1. Multi-Agent Environments (2/3) | 0:36 | 1. Multi-Agent Environments (2/3). Master-slave agents Peer-to-peer agents Multi-channel agents Agent synchronization Environment Patterns |
| 25 | 1. Multi-Agent Environments (3/3) | 0:24 | 1. Multi-Agent Environments (3/3). Hierarchical environments Flat environments Mixed environments |
| 26 | 2. Protocol Verification (1/4) | 0:36 | 2. Protocol Verification (1/4). Protocol Verification Overview What is protocol verification? Protocol compliance Protocol checking Protocol coverage |
| 27 | 2. Protocol Verification (2/4) | 0:36 | 2. Protocol Verification (2/4). AXI protocol basics AXI4-Lite agent AXI4 agent AXI protocol checker Custom Protocol Verification |
| 28 | 2. Protocol Verification (3/4) | 0:36 | 2. Protocol Verification (3/4). Protocol agent creation Protocol checker implementation Protocol coverage Protocol Checkers Checker implementation |
| 29 | 2. Protocol Verification (4/4) | 0:20 | 2. Protocol Verification (4/4). Error detection Protocol compliance |
| 30 | 3. Testbench Architecture Patterns (1/3) | 0:36 | 3. Testbench Architecture Patterns (1/3). Layered Testbench Abstraction layers Layer communication Layer organization Layer patterns |
| 31 | 3. Testbench Architecture Patterns (2/3) | 0:36 | 3. Testbench Architecture Patterns (2/3). Component design Component reuse Component libraries Component patterns Testbench Templates |
| 32 | 3. Testbench Architecture Patterns (3/3) | 0:24 | 3. Testbench Architecture Patterns (3/3). Template customization Template patterns Template best practices |
| 33 | 4. Debugging and Analysis (1/4) | 0:36 | 4. Debugging and Analysis (1/4). UVM Debugging Techniques Phase debugging Component debugging Transaction debugging Configuration debugging |
| 34 | 4. Debugging and Analysis (2/4) | 0:36 | 4. Debugging and Analysis (2/4). Transaction logging Transaction tracing Transaction replay Transaction analysis Waveform Analysis |
| 35 | 4. Debugging and Analysis (3/4) | 0:36 | 4. Debugging and Analysis (3/4). Waveform viewing Signal tracing Timing analysis Log Analysis Log parsing |
| 36 | 4. Debugging and Analysis (4/4) | 0:20 | 4. Debugging and Analysis (4/4). Performance analysis Coverage analysis |
| 37 | 5. Multi-Channel Verification (1/2) | 0:36 | 5. Multi-Channel Verification (1/2). Channel Coordination Multiple channels Channel synchronization Channel independence Channel patterns |
| 38 | 5. Multi-Channel Verification (2/2) | 0:28 | 5. Multi-Channel Verification (2/2). Master-slave interfaces Bidirectional agents Interface coordination Interface patterns |
| 39 | 6. Performance Verification (1/2) | 0:36 | 6. Performance Verification (1/2). Performance Monitoring Performance metrics Performance collection Performance analysis Performance reporting |
| 40 | 6. Performance Verification (2/2) | 0:28 | 6. Performance Verification (2/2). Throughput measurement Bandwidth analysis Latency measurement Performance optimization |
| 41 | 7. Error Injection and Recovery (1/2) | 0:36 | 7. Error Injection and Recovery (1/2). Error Injection Error scenarios Error injection mechanisms Error patterns Error testing |
| 42 | 7. Error Injection and Recovery (2/2) | 0:28 | 7. Error Injection and Recovery (2/2). Recovery scenarios Recovery verification Recovery patterns Recovery testing |
| 43 | 8. Testbench Integration (1/2) | 0:36 | 8. Testbench Integration (1/2). Component Integration Integration strategies Integration testing Integration patterns Integration best practices |
| 44 | 8. Testbench Integration (2/2) | 0:28 | 8. Testbench Integration (2/2). System-level integration Integration verification Integration patterns Integration challenges |
| 45 | 9. Advanced Scoreboarding (1/2) | 0:36 | 9. Advanced Scoreboarding (1/2). Multi-Channel Scoreboards Multiple channel checking Channel coordination Scoreboard patterns Scoreboard optimization |
| 46 | 9. Advanced Scoreboarding (2/2) | 0:28 | 9. Advanced Scoreboarding (2/2). Temporal matching Time windows Matching algorithms Matching patterns |
| 47 | 10. Testbench Maintenance (1/2) | 0:36 | 10. Testbench Maintenance (1/2). Code Organization File organization Class organization Namespace management Documentation |
| 48 | 10. Testbench Maintenance (2/2) | 0:28 | 10. Testbench Maintenance (2/2). Git workflows Branching strategies Code review Release management |
| 49 | Command reference highlights | 0:08 | Next section: Command reference highlights. |
| 50 | Protocol and agent examples | 0:24 | Protocol and agent examples. ./scripts/module6.sh --multi-agent --protocol — agent fabric and directed AXI traffic ./scripts/module6.sh --protocol-checkers — independent protocol rule validation ./scripts/module6.sh --scoreboards --architecture — layered checking and env packaging Full detail in docs/MODULE6.md command reference. |
| 51 | Complex testbench regression | 0:24 | Complex testbench regression. ./scripts/module6.sh --pyuvm-tests — test_complex_testbench full env cd module6/tests/pyuvm_tests && make SIM=verilator TEST=test_complex_testbench ./scripts/module6.sh --skip-examples --pyuvm-tests — system test when components are validated Full detail in docs/MODULE6.md command reference. |
| 52 | Debug concurrent traffic | 0:24 | Debug concurrent traffic. Transaction logs plus UVM verbosity — trace AW/W ordering vs W data beats Protocol checker failures often precede scoreboard mismatches — fix checker errors first Waveforms on awvalid/awready, wvalid/wready for handshake stalls Full detail in docs/MODULE6.md command reference. |
| 53 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 54 | Module 6 orchestrator | 0:45 | Module 6 orchestrator. Watch the terminal output and confirm you see the expected pass message. |
| 55 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 56 | Demo: Multi-Agent Environment | 0:45 | Demo: Multi-Agent Environment. Watch the terminal output and confirm you see the expected pass message. |
| 57 | Demo: Protocol Verification | 0:45 | Demo: Protocol Verification. Watch the terminal output and confirm you see the expected pass message. |
| 58 | Demo: Protocol Checker | 0:45 | Demo: Protocol Checker. Watch the terminal output and confirm you see the expected pass message. |
| 59 | Demo: Multi-Channel Scoreboard | 0:45 | Demo: Multi-Channel Scoreboard. Watch the terminal output and confirm you see the expected pass message. |
| 60 | Demo: Testbench Architecture | 0:45 | Demo: Testbench Architecture. Watch the terminal output and confirm you see the expected pass message. |
| 61 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 62 | What you should know (1/3) | 0:36 | By now you should be able to explain the following. Design multi-agent environments Implement protocol verification Apply testbench architecture patterns Debug complex testbenches Analyze simulation results From MODULE6 Learning Outcomes. |
| 63 | What you should know (2/3) | 0:36 | By now you should be able to explain the following. Monitor performance Integrate components Maintain testbenches Apply industry best practices Multiple agents From MODULE6 Learning Outcomes. |
| 64 | What you should know (3/3) | 0:16 | By now you should be able to explain the following. Environment structure From MODULE6 Learning Outcomes. |
| 65 | Exercises | 0:32 | Exercises. Multi-Agent Environment Protocol Verification Testbench Architecture Debugging Performance Analysis |
| 66 | Assessment checklist | 0:36 | Assessment checklist. Can design multi-agent environments Can implement protocol verification Understands architecture patterns Can debug complex testbenches Can analyze simulation results |
| 67 | Summary & next steps | 0:28 | In summary: Build complex multi-agent testbenches with protocol verification Next up: Next module in course. Build complex multi-agent testbenches with protocol verification Complete module6/CHECKLIST.md Review module6/EXAMPLES.md and run each lab Next: Next module in course |

        ## Section narration (edit for TTS)

        - **How to learn:** Module 5 multi-agent and virtual sequence patterns carry forward — AXI adds real protocol timing Then Read `module6/dut/protocols/axi4_lite_slave.v` AW/W/B/AR/R channel interfaces before stimulus Then Run `--multi-agent` and `--protocol` examples before `--protocol-checkers` and scoreboard labs Then Understand initiator vs slave roles: DUT is slave; TB agents play masters/memory/peripheral.
- **Design architecture (Protocol DUT architecture, Complex testbench architecture, Execution pipeline, Data flow):** Walk through the block diagram, then relate each block to files under module6/examples/.
- **Verification (Protocol verification methods, System-level checking, Step-by-step lab execution, Closure):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 10 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module6/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE6.md` and `module6/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 6`
