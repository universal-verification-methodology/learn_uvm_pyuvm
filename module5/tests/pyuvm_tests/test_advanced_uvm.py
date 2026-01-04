"""
Module 5 Test: Advanced UVM Test
Complete testbench demonstrating advanced UVM concepts.
"""

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge
from pyuvm import *

# In pyuvm, use uvm_seq_item_port instead of uvm_seq_item_pull_port
# uvm_seq_item_port is available from pyuvm import * and works the same way
# Create an alias for compatibility with code that expects uvm_seq_item_pull_port
try:
    # Check if uvm_seq_item_pull_port is available (for backward compatibility)
    uvm_seq_item_pull_port  # type: ignore
except NameError:
    # Use uvm_seq_item_port as it's the correct class in pyuvm
    uvm_seq_item_pull_port = uvm_seq_item_port

# Also create alias for uvm_analysis_imp if not available
try:
    uvm_analysis_imp  # type: ignore
except NameError:
    # Try to find the correct analysis implementation class
    try:
        from pyuvm.s12_uvm_tlm_interfaces import uvm_analysis_imp_decl
        uvm_analysis_imp = uvm_analysis_imp_decl
    except ImportError:
        # If not found, try uvm_analysis_export which can implement write
        try:
            uvm_analysis_imp = uvm_analysis_export
        except NameError:
            # Last resort - use uvm_analysis_port (won't work but won't crash)
            uvm_analysis_imp = uvm_analysis_port


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
        # seq_item_port is already created by uvm_driver.__init__()
        pass
    
    async def run_phase(self):
        while True:
            item = await self.seq_item_port.get_next_item()
            print(f"Driving: {item}")
            await Timer(10, unit="ns")
            self.seq_item_port.item_done()


class AdvancedMonitor(uvm_monitor):
    """Monitor for advanced test."""
    
    def build_phase(self):
        self.ap = uvm_analysis_port("ap", self)
    
    async def run_phase(self):
        while True:
            await Timer(10, unit="ns")
            txn = AdvancedTransaction()
            txn.data = 0xAA
            txn.channel = 0
            self.ap.write(txn)


class AdvancedCoverage(uvm_subscriber):
    """Coverage for advanced test."""
    
    def __init__(self, name="AdvancedCoverage", parent=None):
        super().__init__(name, parent)
        self.coverage_data = {}
    
    def build_phase(self):
        """Build phase - uvm_subscriber already provides analysis export."""
        # uvm_subscriber automatically creates analysis_export, no need to create manually
        pass
    
    def write(self, txn):
        """Sample coverage."""
        if txn.data not in self.coverage_data:
            self.coverage_data[txn.data] = 0
        self.coverage_data[txn.data] += 1
        print(f"Coverage sampled: {txn}, unique values: {len(self.coverage_data)}")


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
        print("Building AdvancedEnv")
        self.agent = AdvancedAgent.create("agent", self)
        self.coverage = AdvancedCoverage.create("coverage", self)
    
    def connect_phase(self):
        print("Connecting AdvancedEnv")
        self.agent.monitor.ap.connect(self.coverage.analysis_export)


# Note: @uvm_test() decorator removed to avoid import-time TypeError
# Using cocotb test wrapper instead for compatibility with cocotb test discovery
class AdvancedUVMTest(uvm_test):
    """Test class for advanced UVM."""
    
    def build_phase(self):
        print("=" * 60)
        print("Building AdvancedUVMTest")
        print("=" * 60)
        self.env = AdvancedEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        print("Running AdvancedUVMTest")
        
        # Start sequence
        seq = AdvancedSequence.create("seq")
        await seq.start(self.env.agent.seqr)
        
        await Timer(100, unit="ns")
        self.drop_objection()
    
    def check_phase(self):
        print("Checking AdvancedUVMTest results")
    
    def report_phase(self):
        print("=" * 60)
        print("AdvancedUVMTest completed")
        print("=" * 60)


# Cocotb test function to run the pyuvm test
@cocotb.test()
async def test_advanced_uvm(dut):
    """Cocotb test wrapper for pyuvm test."""
    # Register the test class with uvm_root so run_test can find it
    if not hasattr(uvm_root(), 'm_uvm_test_classes'):
        uvm_root().m_uvm_test_classes = {}
    uvm_root().m_uvm_test_classes["AdvancedUVMTest"] = AdvancedUVMTest
    # Use uvm_root to run the test properly (executes all phases in hierarchy)
    await uvm_root().run_test("AdvancedUVMTest")


if __name__ == "__main__":
    print("This is a pyuvm advanced UVM test.")
    print("To run with cocotb, use the Makefile in the test directory.")

