"""
Module 5 Test: Advanced UVM Test
Complete testbench demonstrating advanced UVM concepts.
"""

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge
from pyuvm import *


class AdvancedTransaction(uvm_sequence_item):
    """Transaction for advanced UVM test."""
    
    def __init__(self, name="AdvancedTransaction"):
        super().__init__(name)
        self.data = 0
        self.channel = 0
    
    def __str__(self):
        return f"data=0x{self.data:02X}, channel={self.channel}"


class AdvancedSequence(uvm_sequence):
    """Sequence for advanced test."""
    
    async def body(self):
        """Generate transactions."""
        for i in range(5):
            txn = AdvancedTransaction()
            txn.data = i * 0x10
            txn.channel = 0
            await self.start_item(txn)
            await self.finish_item(txn)


class AdvancedDriver(uvm_driver):
    """Driver for advanced test."""
    
    def build_phase(self):
        self.seq_item_port = uvm_seq_item_pull_port("seq_item_port", self)
    
    async def run_phase(self):
        while True:
            item = await self.seq_item_port.get_next_item()
            self.logger.info(f"Driving: {item}")
            await Timer(10, units="ns")
            await self.seq_item_port.item_done()


class AdvancedMonitor(uvm_monitor):
    """Monitor for advanced test."""
    
    def build_phase(self):
        self.ap = uvm_analysis_port("ap", self)
    
    async def run_phase(self):
        while True:
            await Timer(10, units="ns")
            txn = AdvancedTransaction()
            txn.data = 0xAA
            txn.channel = 0
            self.ap.write(txn)


class AdvancedCoverage(uvm_subscriber):
    """Coverage for advanced test."""
    
    def __init__(self, name="AdvancedCoverage"):
        super().__init__(name)
        self.ap = uvm_analysis_export("ap", self)
        self.imp = uvm_analysis_imp("imp", self)
        self.ap.connect(self.imp)
        self.coverage_data = {}
    
    def write(self, txn):
        """Sample coverage."""
        if txn.data not in self.coverage_data:
            self.coverage_data[txn.data] = 0
        self.coverage_data[txn.data] += 1
        self.logger.info(f"Coverage sampled: {txn}, unique values: {len(self.coverage_data)}")


class AdvancedAgent(uvm_agent):
    """Agent for advanced test."""
    
    def build_phase(self):
        self.driver = AdvancedDriver.create("driver", self)
        self.monitor = AdvancedMonitor.create("monitor", self)
        self.seqr = uvm_sequencer("sequencer", self)
    
    def connect_phase(self):
        self.driver.seq_item_port.connect(self.seqr.seq_item_export)


class AdvancedEnv(uvm_env):
    """Environment for advanced test."""
    
    def build_phase(self):
        self.logger.info("Building AdvancedEnv")
        self.agent = AdvancedAgent.create("agent", self)
        self.coverage = AdvancedCoverage.create("coverage", self)
    
    def connect_phase(self):
        self.logger.info("Connecting AdvancedEnv")
        self.agent.monitor.ap.connect(self.coverage.ap)


@uvm_test()
class AdvancedUVMTest(uvm_test):
    """Test class for advanced UVM."""
    
    async def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Building AdvancedUVMTest")
        self.logger.info("=" * 60)
        self.env = AdvancedEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running AdvancedUVMTest")
        
        # Start sequence
        seq = AdvancedSequence.create("seq")
        await seq.start(self.env.agent.seqr)
        
        await Timer(100, units="ns")
        self.drop_objection()
    
    def check_phase(self):
        self.logger.info("Checking AdvancedUVMTest results")
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("AdvancedUVMTest completed")
        self.logger.info("=" * 60)


if __name__ == "__main__":
    print("This is a pyuvm advanced UVM test.")
    print("To run with cocotb, use the Makefile in the test directory.")

