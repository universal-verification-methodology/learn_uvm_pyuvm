        # Narration script — Module 5: Advanced UVM Concepts

        **Target length:** ~36 minutes (74 slides; auto-generated — edit per slide as needed)

        ## Timing table

        | Slide | Section | Duration | Narration |
|-------|---------|----------|-----------|
| 1 | Module 5 | 0:25 | Welcome to module 5, Advanced UVM Concepts. In this module you will master sequences, coverage, configuration, and virtual sequences. |
| 2 | Learning objectives | 0:16 | Here is what you will learn in this module. Master sequences, coverage, configuration, and virtual sequences |
| 3 | Prerequisites | 0:16 | Before you start, make sure you have these prerequisites. See module README |
| 4 | Learning path | 0:22 | Learning path. Master sequences, coverage, configuration, and virtual sequences |
| 5 | Overview | 0:16 | Overview. This module covers advanced UVM concepts including virtual sequences, coverage models, complex configuration, callbacks, and advanced... |
| 6 | How to learn this module | 0:08 | Next section: How to learn this module. |
| 7 | Suggested learning path | 0:32 | Follow this learning path. Read the guides before running the labs. Module 4 agent/scoreboard integration is prerequisite — multi-channel env extends the same TLM patterns Review module5/dut/advanced/multi_channel.v — multiple logical channels needing coordinated stimulus Study virtual sequencer concept before virtual_sequences/ examples — one coordinator, many agents Skim RAL terminology... |
| 8 | Design architecture | 0:08 | Next section: Design architecture. |
| 9 | 1. Advanced DUT architecture | 0:34 | 1. Advanced DUT architecture. module5/dut/advanced/multi_channel.v — multiple logical channels for coordination labs Designed for virtual sequences and multi-stream scoreboarding Register abstraction layer examples align with memory-mapped control/status Refer to the diagram on the right. |
| 10 | 2. Advanced UVM environment architecture | 0:38 | 2. Advanced UVM environment architecture. Virtual sequencers coordinate multiple agents on different channels Coverage collectors sample transaction fields and cross coverage Callbacks extend driver/monitor without subclass explosion Configuration objects centralize knobs (active/passive, timeouts, enable flags) Refer to the diagram on the right. |
| 11 | 3. Execution pipeline | 0:28 | 3. Execution pipeline. Build: multi-channel RTL plus env with multiple agents, virtual sequencer, coverage, register model Connect: per-channel monitor analysis → scoreboard/coverage; RAL adapter linked to bus sequencer Sim: virtual sequence launches child sequences in order; callbacks may alter driver/monitor behavior mid-run Check: scoreboard per channel + coverage goals + register mirror... |
| 12 | 4. Register model layer | 0:28 | 4. Register model layer. RAL-style maps: registers, fields, access policies (RW, RO, WO) Adapter links bus transactions to register reads/writes in tests Predictor/update paths keep mirror model consistent with DUT Register sequences replace raw bus wiggling for software-visible setup |
| 13 | DUT — multi-channel block | 0:28 | DUT — multi-channel block. Review the code on screen and match it to files in the repository. |
| 14 | Virtual sequencer pattern | 0:28 | Virtual sequencer pattern. Review the code on screen and match it to files in the repository. |
| 15 | Key files to study | 0:08 | Next section: Key files to study. |
| 16 | Open these in the repo | 0:36 | Open these in the repo. module5/dut/advanced/multi_channel.v — multi-stream DUT for virtual sequence coordination module5/examples/virtual_sequences/virtual_sequence_example.py — child sequences on multiple sequencers module5/examples/coverage/coverage_example.py — functional coverage sampling hooks module5/examples/register_model/register_model_example.py — RAL map, adapter, mirror updates... |
| 17 | Verification & testing methods | 0:08 | Next section: Verification & testing methods. |
| 18 | 1. Coverage-driven verification | 0:34 | 1. Coverage-driven verification. Functional coverage on transaction types, channel IDs, and corner field values Coverage goals gate regression sign-off in advanced flows Examples under module5/examples/coverage/ show sampling hooks Refer to the diagram on the right. |
| 19 | 2. Virtual sequences and configuration tests | 0:24 | 2. Virtual sequences and configuration tests. Virtual sequences start child sequences on multiple sequencers in order Config tests prove ConfigDB + config object overrides change behavior Callback tests inject errors or delays to validate robustness |
| 20 | 3. Step-by-step lab execution | 0:32 | 3. Step-by-step lab execution. 1. Virtual sequences: ./scripts/module5.sh --virtual-sequences 2. Coverage/callbacks: ./scripts/module5.sh --coverage --callbacks 3. Configuration: ./scripts/module5.sh --configuration 4. Register model: ./scripts/module5.sh --register-model 5. Integrated: ./scripts/module5.sh --pyuvm-tests — all advanced mechanisms in one regression |
| 21 | 4. Closure | 0:24 | 4. Closure. ./scripts/module5.sh --pyuvm-tests; register model and callback demos in EXAMPLES.md Assessment: virtual sequences, coverage, callbacks, configuration, register model Demonstrate register read/write through RAL adapter rather than ad-hoc pin toggling |
| 22 | Syllabus topics | 0:08 | Next section: Syllabus topics. |
| 23 | 1. Advanced Sequences (1/4) | 0:36 | 1. Advanced Sequences (1/4). Virtual Sequences What are virtual sequences? Virtual sequence purpose Multiple sequencer coordination Virtual sequence implementation |
| 24 | 1. Advanced Sequences (2/4) | 0:36 | 1. Advanced Sequences (2/4). Base sequence classes Derived sequences Sequence reuse patterns Sequence organization Sequence Arbitration |
| 25 | 1. Advanced Sequences (3/4) | 0:36 | 1. Advanced Sequences (3/4). Priority mechanisms Lock and grab Sequence coordination Layered Sequences High-level sequences |
| 26 | 1. Advanced Sequences (4/4) | 0:20 | 1. Advanced Sequences (4/4). Sequence composition Protocol layering |
| 27 | 2. UVM Coverage Models (1/4) | 0:36 | 2. UVM Coverage Models (1/4). Coverage Overview What is coverage? Coverage types Coverage goals Coverage metrics |
| 28 | 2. UVM Coverage Models (2/4) | 0:36 | 2. UVM Coverage Models (2/4). Coverage models Coverage groups Coverpoints Coverage bins Coverage Implementation |
| 29 | 2. UVM Coverage Models (3/4) | 0:36 | 2. UVM Coverage Models (3/4). Coverage sampling Coverage analysis Coverage reporting Coverage Patterns Transaction coverage |
| 30 | 2. UVM Coverage Models (4/4) | 0:20 | 2. UVM Coverage Models (4/4). State coverage Cross coverage |
| 31 | 3. Complex Configuration Objects (1/4) | 0:36 | 3. Complex Configuration Objects (1/4). Configuration Objects Configuration class design Configuration fields Configuration methods Configuration validation |
| 32 | 3. Complex Configuration Objects (2/4) | 0:36 | 3. Complex Configuration Objects (2/4). Hierarchical configuration Configuration inheritance Configuration override Configuration patterns Resource Database |
| 33 | 3. Complex Configuration Objects (3/4) | 0:36 | 3. Complex Configuration Objects (3/4). Resource types Resource lookup Resource management Configuration Callbacks Configuration callbacks |
| 34 | 3. Complex Configuration Objects (4/4) | 0:20 | 3. Complex Configuration Objects (4/4). Callback registration Callback execution |
| 35 | 4. UVM Callbacks (1/4) | 0:36 | 4. UVM Callbacks (1/4). Callback Overview What are callbacks? Callback purpose Callback types Callback benefits |
| 36 | 4. UVM Callbacks (2/4) | 0:36 | 4. UVM Callbacks (2/4). Callback class definition Callback registration Callback execution Callback patterns Pre/Post Callbacks |
| 37 | 4. UVM Callbacks (3/4) | 0:36 | 4. UVM Callbacks (3/4). Post-callbacks Callback ordering Callback control Callback Use Cases Driver callbacks |
| 38 | 4. UVM Callbacks (4/4) | 0:20 | 4. UVM Callbacks (4/4). Scoreboard callbacks Test callbacks |
| 39 | 5. UVM Register Model (Advanced) (1/5) | 0:36 | 5. UVM Register Model (Advanced) (1/5). Register Model Overview Register model purpose Register model structure Register model benefits Register model components |
| 40 | 5. UVM Register Model (Advanced) (2/5) | 0:36 | 5. UVM Register Model (Advanced) (2/5). uvm_reg_block - Register blocks uvm_reg - Registers uvm_reg_field - Register fields uvm_reg_map - Address maps Register Operations |
| 41 | 5. UVM Register Model (Advanced) (3/5) | 0:36 | 5. UVM Register Model (Advanced) (3/5). Register write Register peek/poke Register update Register Sequences Register access sequences |
| 42 | 5. UVM Register Model (Advanced) (4/5) | 0:36 | 5. UVM Register Model (Advanced) (4/5). Register model integration Register predictor Backdoor Access Backdoor read/write Backdoor vs frontdoor |
| 43 | 5. UVM Register Model (Advanced) (5/5) | 0:16 | 5. UVM Register Model (Advanced) (5/5). Backdoor implementation |
| 44 | 6. Virtual Sequences and Virtual Sequencers (1/3) | 0:36 | 6. Virtual Sequences and Virtual Sequencers (1/3). Virtual Sequencer Virtual sequencer purpose Virtual sequencer structure Multiple sequencer references Virtual sequencer implementation |
| 45 | 6. Virtual Sequences and Virtual Sequencers (2/3) | 0:36 | 6. Virtual Sequences and Virtual Sequencers (2/3). Coordinating multiple sequencers Parallel sequence execution Sequence synchronization Sequence coordination patterns Virtual Sequence Patterns |
| 46 | 6. Virtual Sequences and Virtual Sequencers (3/3) | 0:24 | 6. Virtual Sequences and Virtual Sequencers (3/3). Multi-channel coordination Protocol coordination Test coordination |
| 47 | 7. Coverage Analysis and Closure (1/3) | 0:36 | 7. Coverage Analysis and Closure (1/3). Coverage Analysis Coverage collection Coverage reporting Coverage gaps Coverage analysis tools |
| 48 | 7. Coverage Analysis and Closure (2/3) | 0:36 | 7. Coverage Analysis and Closure (2/3). Coverage goals Coverage strategies Coverage improvement Coverage metrics Coverage Patterns |
| 49 | 7. Coverage Analysis and Closure (3/3) | 0:24 | 7. Coverage Analysis and Closure (3/3). Code coverage Assertion coverage Coverage correlation |
| 50 | 8. Advanced Configuration Patterns (1/2) | 0:36 | 8. Advanced Configuration Patterns (1/2). Configuration Strategies Top-down configuration Bottom-up configuration Mixed configuration Configuration best practices |
| 51 | 8. Advanced Configuration Patterns (2/2) | 0:28 | 8. Advanced Configuration Patterns (2/2). Runtime configuration Configuration updates Configuration validation Configuration debugging |
| 52 | 9. Performance Optimization (1/2) | 0:36 | 9. Performance Optimization (1/2). Testbench Performance Performance bottlenecks Optimization strategies Memory optimization Simulation speed |
| 53 | 9. Performance Optimization (2/2) | 0:28 | 9. Performance Optimization (2/2). Efficient sequence design Sequence reuse Sequence caching Sequence performance |
| 54 | 10. Advanced Debugging Techniques (1/2) | 0:36 | 10. Advanced Debugging Techniques (1/2). UVM Debugging UVM debugging tools Phase debugging Component debugging Transaction debugging |
| 55 | 10. Advanced Debugging Techniques (2/2) | 0:28 | 10. Advanced Debugging Techniques (2/2). Coverage gaps Coverage analysis Coverage improvement Coverage tools |
| 56 | Command reference highlights | 0:08 | Next section: Command reference highlights. |
| 57 | Advanced UVM topics | 0:24 | Advanced UVM topics. ./scripts/module5.sh --virtual-sequences --configuration — coordination and config objects ./scripts/module5.sh --coverage --callbacks — coverage sampling and callback injection ./scripts/module5.sh --register-model — RAL map and bus adapter drill Full detail in docs/MODULE5.md command reference. |
| 58 | Integrated regression | 0:24 | Integrated regression. ./scripts/module5.sh --pyuvm-tests — test_advanced_uvm against multi-channel DUT cd module5/tests/pyuvm_tests && make SIM=verilator TEST=test_advanced_uvm ./scripts/module5.sh — all example tracks then tests when doing full module sweep Full detail in docs/MODULE5.md command reference. |
| 59 | Coverage and config debug | 0:24 | Coverage and config debug. Inspect coverage reports/sample counts from example logs when goals are not met Config object + ConfigDB overrides in --configuration — re-run to verify behavior change Callback tests inject delays/errors — use verbosity to see callback invocation order Full detail in docs/MODULE5.md command reference. |
| 60 | Hands-on examples | 0:08 | Next section: Hands-on examples. |
| 61 | Module 5 orchestrator | 0:45 | Module 5 orchestrator. Watch the terminal output and confirm you see the expected pass message. |
| 62 | Exercise scaffold | 0:28 | Exercise scaffold. Review the code on screen and match it to files in the repository. |
| 63 | Demo: Virtual Sequences | 0:45 | Demo: Virtual Sequences. Watch the terminal output and confirm you see the expected pass message. |
| 64 | Demo: Coverage Models | 0:45 | Demo: Coverage Models. Watch the terminal output and confirm you see the expected pass message. |
| 65 | Demo: Configuration Objects | 0:45 | Demo: Configuration Objects. Watch the terminal output and confirm you see the expected pass message. |
| 66 | Demo: UVM Callbacks | 0:45 | Demo: UVM Callbacks. Watch the terminal output and confirm you see the expected pass message. |
| 67 | Demo: Register Model | 0:45 | Demo: Register Model. Watch the terminal output and confirm you see the expected pass message. |
| 68 | Practice & assessment | 0:08 | Next section: Practice & assessment. |
| 69 | What you should know (1/3) | 0:36 | By now you should be able to explain the following. Create and use virtual sequences Implement coverage models Design complex configuration objects Use UVM callbacks effectively Use advanced register model features From MODULE5 Learning Outcomes. |
| 70 | What you should know (2/3) | 0:36 | By now you should be able to explain the following. Analyze and close coverage Optimize testbench performance Debug advanced testbenches Apply advanced patterns Virtual sequencer From MODULE5 Learning Outcomes. |
| 71 | What you should know (3/3) | 0:16 | By now you should be able to explain the following. Multiple sequencer coordination From MODULE5 Learning Outcomes. |
| 72 | Exercises | 0:32 | Exercises. Virtual Sequences Coverage Implementation Configuration Design Callback Implementation Register Model |
| 73 | Assessment checklist | 0:36 | Assessment checklist. Can create virtual sequences Can implement coverage models Can design configuration objects Can use callbacks effectively Can use advanced register model |
| 74 | Summary & next steps | 0:28 | In summary: Master sequences, coverage, configuration, and virtual sequences Next up: Next module in course. Master sequences, coverage, configuration, and virtual sequences Complete module5/CHECKLIST.md Review module5/EXAMPLES.md and run each lab Next: Next module in course |

        ## Section narration (edit for TTS)

        - **How to learn:** Module 4 agent/scoreboard integration is prerequisite — multi-channel env extends the same TLM patterns Then Review `module5/dut/advanced/multi_channel.v` — multiple logical channels needing coordinated stimulus Then Study virtual sequencer concept before `virtual_sequences/` examples — one coordinator, many agents Then Skim RAL terminology: register map, fields, adapter, predictor — used in `register_model/`.
- **Design architecture (Advanced DUT architecture, Advanced UVM environment architecture, Execution pipeline, Register model layer):** Walk through the block diagram, then relate each block to files under module5/examples/.
- **Verification (Coverage-driven verification, Virtual sequences and configuration tests, Step-by-step lab execution, Closure):** Explain what stimulus is applied, what is checked, and what is intentionally out of scope.
- **Syllabus:** Cover 10 topic section(s) — pause on protocol timing and signals.
- **Before exercises:** Ask learners to recall the learning outcomes slide; they should explain each bullet in their own words.
- **Hands-on:** Run module5/EXAMPLES.md labs; narrate expected PASS lines.

        ## Notes

        - Slides from **Before You Start**, **Design Architecture**, **Verification & Testing Methods**, **Topics Covered**, **EXAMPLES.md**, and **Learning Outcomes**.
        - Full detail: `docs/MODULE5.md` and `module5/EXAMPLES.md`.
        - Regenerate: `regenerate_course_outlines.sh <course_root> --module 5`
