"""
Module 4 Test: Complete Agent Test
Complete UVM testbench with driver, monitor, sequencer, and scoreboard.
"""

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge
from pyuvm import *


class InterfaceTransaction(uvm_sequence_item):
    """Transaction for interface test."""
    
    def __init__(self, name="InterfaceTransaction"):
        super().__init__(name)
        self.data = 0
        self.address = 0
        self.expected_result = 0
    
    def __str__(self):
        return (f"data=0x{self.data:02X}, addr=0x{self.address:04X}, "
                f"expected=0x{self.expected_result:02X}")


class InterfaceSequence(uvm_sequence):
    """Sequence generating test vectors."""
    
    async def body(self):
        """Generate test vectors."""
        test_vectors = [
            (0x00, 0x1000, 0x01),
            (0x01, 0x1001, 0x02),
            (0xFF, 0x1FFF, 0x00),  # Overflow
            (0x7F, 0x2000, 0x80),
            (0x0A, 0x3000, 0x0B),
        ]
        
        for data, addr, expected in test_vectors:
            txn = InterfaceTransaction()
            txn.data = data
            txn.address = addr
            txn.expected_result = expected
            await self.start_item(txn)
            await self.finish_item(txn)


class InterfaceDriver(uvm_driver):
    """Driver for interface."""
    
    def build_phase(self):
        self.seq_item_port = uvm_seq_item_pull_port("seq_item_port", self)
    
    async def run_phase(self):
        while True:
            item = await self.seq_item_port.get_next_item()
            # In real implementation, drive DUT signals
            # cocotb.dut.data.value = item.data
            # cocotb.dut.address.value = item.address
            # cocotb.dut.valid.value = 1
            self.logger.info(f"Driving: {item}")
            await Timer(10, units="ns")
            # cocotb.dut.valid.value = 0
            await self.seq_item_port.item_done()


class InterfaceMonitor(uvm_monitor):
    """Monitor for interface."""
    
    def build_phase(self):
        self.ap = uvm_analysis_port("ap", self)
    
    async def run_phase(self):
        while True:
            # In real implementation, sample DUT outputs
            # await RisingEdge(cocotb.dut.ready)
            # result = cocotb.dut.result.value.integer
            await Timer(10, units="ns")
            # Create transaction from sampled values
            txn = InterfaceTransaction()
            # txn.data = cocotb.dut.data.value.integer
            # txn.result = result
            self.ap.write(txn)


class InterfaceScoreboard(uvm_scoreboard):
    """Scoreboard for interface."""
    
    def build_phase(self):
        self.ap = uvm_analysis_export("ap", self)
        self.imp = uvm_analysis_imp("imp", self)
        self.ap.connect(self.imp)
        self.expected = []
        self.actual = []
        self.mismatches = []
    
    def write(self, txn):
        """Receive transactions."""
        self.actual.append(txn)
        if len(self.expected) > 0:
            exp = self.expected.pop(0)
            if txn.expected_result != exp.expected_result:
                self.mismatches.append((exp, txn))
                self.logger.error(f"Mismatch: expected=0x{exp.expected_result:02X}, "
                                f"actual=0x{txn.expected_result:02X}")
    
    def add_expected(self, txn):
        """Add expected transaction."""
        self.expected.append(txn)
    
    def check_phase(self):
        """Check phase."""
        self.logger.info(f"Scoreboard: expected={len(self.expected)}, "
                        f"actual={len(self.actual)}, mismatches={len(self.mismatches)}")


class InterfaceAgent(uvm_agent):
    """Agent for interface."""
    
    def build_phase(self):
        self.driver = InterfaceDriver.create("driver", self)
        self.monitor = InterfaceMonitor.create("monitor", self)
        self.seqr = uvm_sequencer("sequencer", self)
    
    def connect_phase(self):
        self.driver.seq_item_port.connect(self.seqr.seq_item_export)


class InterfaceEnv(uvm_env):
    """Environment for interface test."""
    
    def build_phase(self):
        self.logger.info("Building InterfaceEnv")
        self.agent = InterfaceAgent.create("agent", self)
        self.scoreboard = InterfaceScoreboard.create("scoreboard", self)
    
    def connect_phase(self):
        self.logger.info("Connecting InterfaceEnv")
        self.agent.monitor.ap.connect(self.scoreboard.ap)


@uvm_test()
class CompleteAgentTest(uvm_test):
    """Test class for complete agent."""
    
    async def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Building CompleteAgentTest")
        self.logger.info("=" * 60)
        self.env = InterfaceEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running CompleteAgentTest")
        
        # Start sequence
        seq = InterfaceSequence.create("seq")
        await seq.start(self.env.agent.seqr)
        
        await Timer(100, units="ns")
        self.drop_objection()
    
    def check_phase(self):
        self.logger.info("Checking CompleteAgentTest results")
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("CompleteAgentTest completed")
        self.logger.info("=" * 60)


if __name__ == "__main__":
    print("This is a pyuvm complete agent test.")
    print("To run with cocotb, use the Makefile in the test directory.")

