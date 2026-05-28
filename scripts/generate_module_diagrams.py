#!/usr/bin/env python3
"""Write per-module rtl/verification/testing Mermaid diagrams for slide media."""

from __future__ import annotations

from pathlib import Path

# module -> (rtl_architecture.mmd, verification_architecture.mmd, testing_methods.mmd)
DIAGRAMS: dict[int, tuple[str, str, str]] = {
    0: (
        """flowchart TB
  subgraph host["Host environment"]
    PY[Python 3.10+ venv]
    GIT[Git / submodules]
    GCC[GCC or Clang + Make]
  end
  subgraph sim["Simulation"]
    VER[Verilator]
    COC[cocotb]
    UVM[pyuvm]
  end
  PY --> COC
  PY --> UVM
  GCC --> VER
  VER --> COC
  COC --> UVM
""",
        """flowchart LR
  DOC[docs/MODULE0.md] --> SCR[scripts/module0.sh]
  SCR --> INS[install_verilator / cocotb / pyuvm]
  INS --> CHK[--check smoke]
  CHK --> M1[Module 1 labs]
""",
        """flowchart TD
  A[Run module0.sh] --> B{Tool present?}
  B -->|no| C[Fix install layer]
  B -->|yes| D[--check pass]
  D --> E[Ready for RTL testbenches]
  C --> A
""",
    ),
    1: (
        """flowchart TB
  subgraph dut["module1/dut"]
    AND[simple_gates/and_gate]
    CTR[counters/counter]
  end
  CLK[clk / rst_n] --> AND
  CLK --> CTR
  AND --> OUT1[result]
  CTR --> OUT2[count]
""",
        """flowchart LR
  subgraph py["Python layer"]
    EX[examples: transactions]
    CT[cocotb_tests]
    PT[pyuvm_tests]
  end
  EX --> CT
  EX --> PT
  CT --> DUT[(RTL DUT)]
  PT --> DUT
""",
        """flowchart TD
  S[Stimulus: directed vectors] --> DUT[(DUT)]
  DUT --> M[Monitor / read signals]
  M --> C{Match expected?}
  C -->|yes| P[PASS]
  C -->|no| F[FAIL + log]
""",
    ),
    2: (
        """flowchart TB
  subgraph regs["Registers"]
    SR[simple_register]
    SH[shift_register]
  end
  subgraph other["Reference DUTs"]
    FIFO[simple_fifo]
    FSM[simple_fsm]
  end
  CLK[clk] --> SR
  CLK --> SH
""",
        """flowchart LR
  TB[cocotb @test coroutines] --> DRV[drive dut ports]
  DRV --> DUT[(register / shift DUT)]
  DUT --> MON[sample on triggers]
  MON --> CHK[assert + log]
""",
        """flowchart TD
  R[Reset test first] --> W[Directed writes]
  W --> E[Edge / boundary values]
  E --> REG[cocotb regression]
  REG --> OK{All pass?}
""",
    ),
    3: (
        """flowchart LR
  A[operands a,b] --> ADD[adder.v]
  ADD --> SUM[sum]
  CLK[clk / rst] --> ADD
""",
        """flowchart TB
  T[uvm_test] --> E[uvm_env]
  E --> AG[uvm_agent]
  AG --> SEQ[sequencer / sequences]
  AG --> DRV[driver]
  AG --> MON[monitor]
  DRV --> DUT[(adder)]
  MON --> DUT
""",
        """flowchart TD
  B[build_phase] --> C[connect_phase]
  C --> R[run_phase + objections]
  R --> X[extract / report]
  X --> P{UVM TEST PASSED?}
""",
    ),
    4: (
        """flowchart LR
  subgraph ifc["simple_interface.v"]
    V[valid/ready]
    AD[addr / data]
    RES[result]
  end
  CLK[clk] --> ifc
""",
        """flowchart TB
  SEQ[sequence] --> SQR[sequencer]
  SQR --> DRV[driver]
  DRV --> DUT[(interface DUT)]
  DUT --> MON[monitor]
  MON --> AP[analysis port]
  AP --> SB[scoreboard]
""",
        """flowchart TD
  ITEM[sequence_item] --> DRV[drive beat]
  DRV --> DUT[(DUT)]
  DUT --> MON[monitor item]
  MON --> SB{scoreboard compare}
  SB -->|match| PASS
  SB -->|mismatch| FAIL
""",
    ),
    5: (
        """flowchart TB
  subgraph mc["multi_channel.v"]
    CH0[channel 0]
    CH1[channel 1]
    CH2[channel N]
  end
  CFG[config / registers] --> mc
""",
        """flowchart TB
  VS[virtual sequencer] --> A0[agent 0]
  VS --> A1[agent 1]
  A0 --> DUT[(multi_channel)]
  A1 --> DUT
  MON[monitors] --> COV[coverage]
  MON --> CB[callbacks]
  REG[register model] --> DUT
""",
        """flowchart TD
  VS[virtual sequence] --> COV[sample coverage]
  COV --> G{Goals met?}
  G -->|yes| DONE[sign-off]
  G -->|no| MORE[add tests]
  MORE --> VS
""",
    ),
    6: (
        """flowchart TB
  subgraph axi["axi4_lite_slave"]
    AW[AW channel]
    W[W channel]
    B[B channel]
    AR[AR channel]
    R[R channel]
  end
  MEM[(memory interface)]
  axi --> MEM
""",
        """flowchart TB
  ENV[uvm_env] --> MA[master agent]
  ENV --> SA[slave / memory agent]
  ENV --> PC[protocol checker]
  MA --> DUT[(AXI slave)]
  SA --> DUT
  MON[monitors] --> SB[scoreboard]
  PC --> DUT
""",
        """flowchart TD
  CHK[protocol checker rules] --> TR[AXI transactions]
  TR --> DUT[(DUT)]
  DUT --> SB[system scoreboard]
  SB --> P{Consistent?}
""",
    ),
    7: (
        """flowchart TB
  subgraph soc["module7 IP blocks"]
    DMA[simple_dma]
    UART[uart]
  end
  BUS[internal control] --> DMA
  BUS --> UART
""",
        """flowchart LR
  VIP[verification IP agents] --> ENV[uvm_env]
  ENV --> DMA[(DMA DUT)]
  ENV --> UART[(UART DUT)]
  ENV --> SB[system scoreboard]
""",
        """flowchart TD
  SM[smoke regressions] --> NG[nightly full EXAMPLES]
  NG --> REL[release + coverage]
  REL --> SHIP[sign-off]
""",
    ),
    8: (
        """flowchart TB
  CLP[CLP plusargs] --> CFG[test config]
  CFG --> ENV[existing uvm_env]
  subgraph util["UVM utilities"]
    CMP[comparators]
    REC[recorders]
    POOL[pools / queues]
  end
  ENV --> util
""",
        """flowchart LR
  MON[monitor] --> AP[analysis port]
  AP --> CMP[comparator]
  AP --> REC[recorder]
  AP --> SB[scoreboard]
""",
        """flowchart TD
  RUN[run test] --> CMP[compare stream]
  CMP --> REC[record transactions]
  REC --> RPT[report + CLP filters]
""",
    ),
}


def main() -> None:
    course_root = Path(__file__).resolve().parents[1]
    for mod, (rtl, verif, test) in DIAGRAMS.items():
        diag_dir = course_root / "media" / f"module{mod}" / "assets" / "diagrams"
        diag_dir.mkdir(parents=True, exist_ok=True)
        (diag_dir / "rtl_architecture.mmd").write_text(rtl.strip() + "\n", encoding="utf-8")
        (diag_dir / "verification_architecture.mmd").write_text(
            verif.strip() + "\n",
            encoding="utf-8",
        )
        (diag_dir / "testing_methods.mmd").write_text(test.strip() + "\n", encoding="utf-8")
        print(f"OK: module{mod} diagrams")


if __name__ == "__main__":
    main()
