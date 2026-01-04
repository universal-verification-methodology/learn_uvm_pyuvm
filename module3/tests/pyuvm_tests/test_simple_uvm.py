"""
Module 3 Test Case 3.1: Simple UVM Test
Complete UVM testbench for simple adder.
"""

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge
from pyuvm import *


class AdderTransaction(uvm_sequence_item):
    """Transaction for adder test."""
    
    def __init__(self, name="AdderTransaction"):
        super().__init__(name)
        self.a = 0
        self.b = 0
        self.expected_sum = 0
        self.expected_carry = 0
    
    def __str__(self):
        return (f"a=0x{self.a:02X}, b=0x{self.b:02X}, "
                f"expected_sum=0x{self.expected_sum:02X}, "
                f"expected_carry={self.expected_carry}")


class AdderSequence(uvm_sequence):
    """Sequence generating adder test vectors."""
    
    async def body(self):
        """Generate test vectors."""
        test_vectors = [
            (0x00, 0x00, 0x00, 0),
            (0x01, 0x01, 0x02, 0),
            (0xFF, 0x01, 0x00, 1),  # Overflow
            (0x80, 0x80, 0x00, 1),  # Overflow
            (0x0A, 0x05, 0x0F, 0),
        ]
        
        for a, b, expected_sum, expected_carry in test_vectors:
            txn = AdderTransaction()
            txn.a = a
            txn.b = b
            txn.expected_sum = expected_sum
            txn.expected_carry = expected_carry
            await self.start_item(txn)
            await self.finish_item(txn)


class AdderDriver(uvm_driver):
    """Driver for adder DUT."""
    
    def build_phase(self):
        self.seq_item_port = uvm_seq_item_pull_port("seq_item_port", self)
    
    async def run_phase(self):
        while True:
            txn = await self.seq_item_port.get_next_item()
            # In real implementation, drive DUT signals
            # cocotb.dut.a.value = txn.a
            # cocotb.dut.b.value = txn.b
            self.logger.info(f"Driving: {txn}")
            await Timer(10, units="ns")
            await self.seq_item_port.item_done()


class AdderMonitor(uvm_monitor):
    """Monitor for adder DUT."""
    
    def build_phase(self):
        self.ap = uvm_analysis_port("ap", self)
    
    async def run_phase(self):
        while True:
            # In real implementation, sample DUT outputs
            # sum = cocotb.dut.sum.value.integer
            # carry = cocotb.dut.carry.value.integer
            await Timer(10, units="ns")
            self.logger.debug("Monitoring DUT")


class AdderScoreboard(uvm_scoreboard):
    """Scoreboard for adder verification."""
    
    def build_phase(self):
        self.ap = uvm_analysis_export("ap", self)
        self.expected = []
        self.actual = []
    
    def write(self, txn):
        """Receive transactions from monitor."""
        self.actual.append(txn)
        self.logger.info(f"Scoreboard received: {txn}")
    
    def check_phase(self):
        """Check phase - verify results."""
        self.logger.info("=" * 60)
        self.logger.info("Scoreboard Check")
        self.logger.info(f"Total transactions: {len(self.actual)}")
        if len(self.expected) == len(self.actual):
            self.logger.info("✓ Transaction count matches")
        else:
            self.logger.error(f"✗ Transaction count mismatch: "
                            f"expected={len(self.expected)}, actual={len(self.actual)}")


class AdderAgent(uvm_agent):
    """Agent for adder."""
    
    def build_phase(self):
        self.driver = AdderDriver.create("driver", self)
        self.monitor = AdderMonitor.create("monitor", self)
        self.seqr = uvm_sequencer("sequencer", self)
    
    def connect_phase(self):
        self.driver.seq_item_port.connect(self.seqr.seq_item_export)
        self.monitor.ap.connect(self.env.scoreboard.ap)


class AdderEnv(uvm_env):
    """Environment for adder test."""
    
    def build_phase(self):
        self.logger.info("Building AdderEnv")
        self.agent = AdderAgent.create("agent", self)
        self.scoreboard = AdderScoreboard.create("scoreboard", self)
    
    def connect_phase(self):
        self.logger.info("Connecting AdderEnv")
        self.agent.monitor.ap.connect(self.scoreboard.ap)


@uvm_test()
class AdderTest(uvm_test):
    """Test class for adder."""
    
    async def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Building AdderTest")
        self.logger.info("=" * 60)
        self.env = AdderEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running AdderTest")
        
        # Start sequence
        seq = AdderSequence.create("seq")
        await seq.start(self.env.agent.seqr)
        
        await Timer(100, units="ns")
        self.drop_objection()
    
    def check_phase(self):
        self.logger.info("Checking AdderTest results")
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("AdderTest completed")
        self.logger.info("=" * 60)


if __name__ == "__main__":
    # Note: This is a structural example
    # In practice, you would use cocotb to run this with a simulator
    print("This is a pyuvm test structure example.")
    print("To run with cocotb, use the Makefile in the test directory.")

