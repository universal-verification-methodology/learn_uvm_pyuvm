        # Narration script — Module 7: Real-World Applications

        **Target length:** ~35 minutes (71 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 7 | 0:25 | Welcome to module 7, Real-World Applications. In this module you will apply uvm to real-world verification scenarios. |
| 2 | Learning objectives | 0:16 | Here is what you will learn in this module. Apply UVM to real-world verification scenarios |
| 3 | Prerequisites | 0:16 | Before you start, make sure you have these prerequisites. See module README |
| 4 | Learning path | 0:22 | Learning path. Apply UVM to real-world verification scenarios |
| 5 | Overview | 0:16 | Overview. This module applies all learned concepts to real-world verification scenarios. You'll work on complete verification projects, learn... |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:32 | Follow this learning path. Read the guides before running the labs. Module 6 multi-agent protocol env is baseline — Module 7 applies it to DMA and UART IP blocks Review module7/dut/dma/simple_dma.v register map and descriptor flow before DMA examples Study module7/dut/protocols/uart.v framing (start bit, data, stop) for serial agent labs VIP example packages reusable agents — focus on... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. Real-world DUT blocks | 0:34 | 1. Real-world DUT blocks. module7/dut/dma/simple_dma.v — DMA controller with channel descriptors module7/dut/protocols/uart.v — serial framing for protocol agent labs Blocks represent IP-style interfaces students will see in SoC verification Refer to the diagram on the right. |
| 10 | 2. Verification IP (VIP) architecture | 0:38 | 2. Verification IP (VIP) architecture. Reusable agents package protocol knowledge (transactions, sequences, checkers) Env composes DMA + UART (or other) agents with shared config and scoreboard fabric Best-practices example shows directory layout, naming, and review-friendly TB structure VIP boundaries separate protocol expertise from scenario tests Refer to the diagram on the right. |
| 11 | 3. Execution pipeline | 0:28 | 3. Execution pipeline. Build: Verilator compiles DMA and/or UART RTL; env builds VIP agents and shared infrastructure Connect: register bus agent + DMA status monitors + UART analysis paths into system scoreboard Sim: software-visible register writes program DMA; UART sequences inject serial traffic concurrently Check: DMA transfer completion flags, memory content, UART frame integrity —... |
| 12 | 4. Integration view | 0:28 | 4. Integration view. Software-visible registers drive DMA; UART provides async serial path Scoreboard and coverage span multiple IPs in one regression Exercises push toward production-style reuse and documentation Module 8 utilities (CLP, recorders) plug into this env style in capstone work |
| 13 | DUT — simple DMA controller | 0:28 | DUT — simple DMA controller. Review the code on screen and match it to files in the repository. |
| 14 | VIP-style agent reuse | 0:28 | VIP-style agent reuse. Review the code on screen and match it to files in the repository. |
| 15 | Key files to study | 0:08 | Next section: Key files to study. |
| 16 | Open these in the repo | 0:36 | Open these in the repo. module7/dut/dma/simple_dma.v — DMA controller with channel descriptors and status module7/dut/protocols/uart.v — UART TX/RX serial interface for protocol agent labs module7/examples/dma/dma_example.py — descriptor programming and transfer completion module7/examples/protocols/uart_example.py — baud/framing stimulus and loopback checks module7/examples/vip/vip_example.py... |
| 17 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 18 | 1. Application-level test methods | 0:34 | 1. Application-level test methods. DMA tests: descriptor programming, transfer completion, interrupt/status flags UART tests: baud framing, TX/RX loops, error injection in exercises VIP tests encapsulate protocol rules so tests focus on scenarios not bit toggling Refer to the diagram on the right. |
| 19 | 2. Regression and sign-off practices | 0:24 | 2. Regression and sign-off practices. ./scripts/module7.sh runs DMA, protocol, VIP, and best-practices demos Layered regressions: smoke (short), nightly (full EXAMPLES), release (with coverage goals) Waveforms and transaction logs for post-mortem on failures |
| 20 | 3. Step-by-step lab execution | 0:32 | 3. Step-by-step lab execution. 1. DMA block: ./scripts/module7.sh --dma — program descriptor, confirm completion 2. UART protocol: ./scripts/module7.sh --protocols — framing and loopback 3. VIP packaging: ./scripts/module7.sh --vip — study reusable agent layout 4. Best practices: ./scripts/module7.sh --best-practices — review TB structure checklist 5. Integrated: ./scripts/module7.sh... |
| 21 | 4. Closure | 0:24 | 4. Closure. ./scripts/module7.sh --pyuvm-tests; assessment covers VIP reuse, protocols, and integration Prepares for Module 8 utilities used in production regressions (CLP, recorders) Articulate which checks live in VIP vs scenario test vs scoreboard |
| 22 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 23 | 1. DMA Verification (1/4) | 0:36 | 1. DMA Verification (1/4). DMA Controller Overview DMA concepts DMA controller architecture DMA transfer types DMA verification challenges |
| 24 | 1. DMA Verification (2/4) | 0:36 | 1. DMA Verification (2/4). Register interface agent Memory interface agent DMA monitor Scoreboard design Coverage model |
| 25 | 1. DMA Verification (3/4) | 0:36 | 1. DMA Verification (3/4). Simple transfers Scatter-gather transfers Multiple channel transfers Error scenarios Performance verification |
| 26 | 1. DMA Verification (4/4) | 0:28 | 1. DMA Verification (4/4). Test scenarios Sequence design Coverage closure Regression testing |
| 27 | 2. Protocol Verification (Industry Standards) (1/4) | 0:36 | 2. Protocol Verification (Industry Standards) (1/4). UART Verification UART protocol UART agent design UART testbench UART verification |
| 28 | 2. Protocol Verification (Industry Standards) (2/4) | 0:36 | 2. Protocol Verification (Industry Standards) (2/4). SPI protocol SPI agent design Master-slave coordination SPI testbench I2C Verification |
| 29 | 2. Protocol Verification (Industry Standards) (3/4) | 0:36 | 2. Protocol Verification (Industry Standards) (3/4). I2C agent design Multi-master scenarios I2C testbench AXI Verification AXI protocol details |
| 30 | 2. Protocol Verification (Industry Standards) (4/4) | 0:20 | 2. Protocol Verification (Industry Standards) (4/4). AXI testbench AXI compliance |
| 31 | 3. Best Practices and Patterns (1/4) | 0:36 | 3. Best Practices and Patterns (1/4). Code Organization Project structure File organization Naming conventions Documentation standards |
| 32 | 3. Best Practices and Patterns (2/4) | 0:36 | 3. Best Practices and Patterns (2/4). Component reuse Sequence reuse Environment reuse VIP (Verification IP) creation Documentation |
| 33 | 3. Best Practices and Patterns (3/4) | 0:36 | 3. Best Practices and Patterns (3/4). Test documentation User guides API documentation Maintenance Code maintenance |
| 34 | 3. Best Practices and Patterns (4/4) | 0:20 | 3. Best Practices and Patterns (4/4). Version management Change management |
| 35 | 4. Advanced Topics (1/4) | 0:36 | 4. Advanced Topics (1/4). Performance Optimization Testbench optimization Simulation speed Memory optimization CPU utilization |
| 36 | 4. Advanced Topics (2/4) | 0:36 | 4. Advanced Topics (2/4). Coverage strategies Coverage analysis Coverage improvement Coverage metrics Regression Testing |
| 37 | 4. Advanced Topics (3/4) | 0:36 | 4. Advanced Topics (3/4). Test selection Test execution Result analysis Continuous Integration CI/CD setup |
| 38 | 4. Advanced Topics (4/4) | 0:20 | 4. Advanced Topics (4/4). Result reporting Notification systems |
| 39 | 5. Verification IP (VIP) Development (1/3) | 0:36 | 5. Verification IP (VIP) Development (1/3). VIP Overview What is VIP? VIP components VIP structure VIP benefits |
| 40 | 5. Verification IP (VIP) Development (2/3) | 0:36 | 5. Verification IP (VIP) Development (2/3). VIP design VIP implementation VIP testing VIP documentation VIP Integration |
| 41 | 5. Verification IP (VIP) Development (3/3) | 0:24 | 5. Verification IP (VIP) Development (3/3). VIP configuration VIP usage VIP maintenance |
| 42 | 6. System-Level Verification (1/2) | 0:36 | 6. System-Level Verification (1/2). System Verification System architecture System testbench System scenarios System verification |
| 43 | 6. System-Level Verification (2/2) | 0:28 | 6. System-Level Verification (2/2). SoC architecture SoC testbench SoC scenarios SoC verification |
| 44 | 7. Advanced Debugging (1/2) | 0:36 | 7. Advanced Debugging (1/2). Complex Debugging Multi-component debugging Transaction flow debugging Timing debugging Configuration debugging |
| 45 | 7. Advanced Debugging (2/2) | 0:28 | 7. Advanced Debugging (2/2). Waveform tools Log analysis tools Coverage tools Performance tools |
| 46 | 8. Test Planning and Strategy (1/2) | 0:36 | 8. Test Planning and Strategy (1/2). Test Planning Test strategy Test scenarios Test coverage Test execution plan |
| 47 | 8. Test Planning and Strategy (2/2) | 0:28 | 8. Test Planning and Strategy (2/2). Verification approach Verification metrics Verification closure Sign-off criteria |
| 48 | 9. Industry Patterns (1/2) | 0:36 | 9. Industry Patterns (1/2). Common Patterns Industry patterns Pattern libraries Pattern reuse Pattern best practices |
| 49 | 9. Industry Patterns (2/2) | 0:28 | 9. Industry Patterns (2/2). Verification patterns Architecture patterns Implementation patterns Testing patterns |
| 50 | 10. Project: Build Your Own VIP (1/3) | 0:36 | 10. Project: Build Your Own VIP (1/3). Project Requirements Choose protocol Design VIP Implement VIP Test VIP |
| 51 | 10. Project: Build Your Own VIP (2/3) | 0:36 | 10. Project: Build Your Own VIP (2/3). VIP Components Complete agent Protocol checker Coverage model Scoreboard |
| 52 | 10. Project: Build Your Own VIP (3/3) | 0:20 | 10. Project: Build Your Own VIP (3/3). Documentation Test suite |
| 53 | Command reference highlights | 0:08 | Next section: Command reference highlights. |
| 54 | IP block examples | 0:24 | IP block examples. ./scripts/module7.sh --dma — DMA descriptor and completion drills ./scripts/module7.sh --protocols — UART (and related protocol) agent examples ./scripts/module7.sh --vip --best-practices — reusable VIP layout and review-friendly structure Full detail in docs/MODULE7.md command reference. |
| 55 | Integrated tests | 0:24 | Integrated tests. ./scripts/module7.sh --pyuvm-tests — integrated pyuvm regressions under module7/tests/ cd module7/tests/pyuvm_tests && make SIM=verilator — direct Make when debugging env wiring ./scripts/module7.sh — full example sweep plus tests for module sign-off Full detail in docs/MODULE7.md command reference. |
| 56 | Layered regression mindset | 0:24 | Layered regression mindset. Smoke: ./scripts/module7.sh --dma only — fast sanity after tool changes Nightly: all example flags — catches cross-IP integration regressions Use transaction logs and waves for UART timing vs DMA memory content failures Full detail in docs/MODULE7.md command reference. |
| 57 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 58 | Module 7 orchestrator | 0:45 | Module 7 orchestrator. Watch the terminal output and confirm you see the expected pass message. |
| 59 | Demo: DMA Verification | 0:45 | Demo: DMA Verification. Watch the terminal output and confirm you see the expected pass message. |
| 60 | Demo: UART Protocol | 0:45 | Demo: UART Protocol. Watch the terminal output and confirm you see the expected pass message. |
| 61 | Demo: SPI Protocol | 0:45 | Demo: SPI Protocol. Watch the terminal output and confirm you see the expected pass message. |
| 62 | Demo: I2C Protocol | 0:45 | Demo: I2C Protocol. Watch the terminal output and confirm you see the expected pass message. |
| 63 | Demo: VIP Development | 0:45 | Demo: VIP Development. Watch the terminal output and confirm you see the expected pass message. |
| 64 | Demo: Best Practices | 0:45 | Demo: Best Practices. Watch the terminal output and confirm you see the expected pass message. |
| 65 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 66 | What you should know (1/3) | 0:36 | By now you should be able to explain the following. Verify complex designs (DMA, protocols) Apply industry best practices Create reusable verification IP Optimize testbench performance Achieve coverage closure From MODULE7 Learning Outcomes. |
| 67 | What you should know (2/3) | 0:36 | By now you should be able to explain the following. Debug complex issues Maintain production testbenches Apply industry patterns Create complete verification solutions Register model From MODULE7 Learning Outcomes. |
| 68 | What you should know (3/3) | 0:28 | By now you should be able to explain the following. Scatter-gather support Performance monitoring Coverage model Scoreboard From MODULE7 Learning Outcomes. |
| 69 | Exercises | 0:32 | Exercises. DMA Verification Protocol VIP Best Practices Coverage Closure Final Project |
| 70 | Assessment checklist | 0:36 | Assessment checklist. Can verify complex designs Understands best practices Can create reusable VIP Can optimize performance Can achieve coverage closure |
| 71 | Summary & next steps | 0:28 | In summary: Apply UVM to real-world verification scenarios Next up: Next module in course. Apply UVM to real-world verification scenarios Complete module7/CHECKLIST.md Review module7/EXAMPLES.md and run each lab Next: Next module in course |

        ## Section narration (edit for TTS)

        - **How to learn:** Module 6 multi-agent protocol env is baseline — Module 7 applies it to DMA and UART IP blocks Then Review `module7/dut/dma/simple_dma.v` register map and descriptor flow before DMA examples Then Study `module7/dut/protocols/uart.v` framing (start bit, data, stop) for serial agent labs Then VIP example packages reusable agents — focus on directory layout and naming for reuse.
- **Design architecture (Real-world DUT blocks, Verification IP (VIP) architecture, Execution pipeline, Integration view):** Walk through the block diagram, then relate each block to files under module7/examples/.
- **Verification (Application-level test methods, Regression and sign-off practices, Step-by-step lab execution, Closure):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 10 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module7/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE7.md` and `module7/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 7`
