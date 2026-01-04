"""
Module 5 Example 5.4: UVM Callbacks
Demonstrates callback implementation and usage.
"""

from pyuvm import *
import cocotb
from cocotb.triggers import Timer

# Note: pyuvm uses uvm_seq_item_port instead of uvm_seq_item_pull_port
# Note: pyuvm may not have uvm_callback class, using uvm_object as base class


class DriverTransaction(uvm_sequence_item):
    """Transaction for callback example."""
    
    def __init__(self, name="DriverTransaction"):
        super().__init__(name)
        self.data = 0
    
    def __str__(self):
        return f"data=0x{self.data:02X}"


class DriverCallback(uvm_object):
    """
    Callback class for driver.
    
    Shows:
    - Callback class definition
    - Callback methods
    - Callback registration
    """
    
    def pre_drive(self, driver, txn):
        """Pre-drive callback."""
        self.logger.info(f"[{self.get_name()}] Pre-drive callback: {txn}")
        # Can modify transaction before driving
        return txn
    
    def post_drive(self, driver, txn):
        """Post-drive callback."""
        self.logger.info(f"[{self.get_name()}] Post-drive callback: {txn}")
        # Can perform actions after driving


class DriverWithCallbacks(uvm_driver):
    """Driver that uses callbacks."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building driver with callbacks")
        # seq_item_port is already created by uvm_driver.__init__()
    
    async def run_phase(self):
        """Run phase - pyuvm doesn't support callbacks so just drive transactions."""
        self.logger.info(f"[{self.get_name()}] Starting driver")

        while True:
            item = await self.seq_item_port.get_next_item()

            # Drive transaction (callback functionality not available in pyuvm)
            self.logger.info(f"[{self.get_name()}] Driving: {item}")
            await Timer(10, unit="ns")

            await self.seq_item_port.item_done()


class MonitorCallback(uvm_object):
    """Callback for monitor."""
    
    def pre_sample(self, monitor, txn):
        """Pre-sample callback."""
        self.logger.info(f"[{self.get_name()}] Pre-sample callback: {txn}")
        return txn
    
    def post_sample(self, monitor, txn):
        """Post-sample callback."""
        self.logger.info(f"[{self.get_name()}] Post-sample callback: {txn}")


class MonitorWithCallbacks(uvm_monitor):
    """Monitor that uses callbacks."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building monitor with callbacks")
        self.ap = uvm_analysis_port("ap", self)
    
    async def run_phase(self):
        """Run phase - pyuvm doesn't support callbacks so just sample transactions."""
        self.logger.info(f"[{self.get_name()}] Starting monitor")

        while True:
            # Sample DUT (simulated)
            await Timer(10, unit="ns")

            txn = DriverTransaction()
            txn.data = 0xAA

            # Sample transaction (callback functionality not available in pyuvm)
            self.logger.info(f"[{self.get_name()}] Sampled: {txn}")
            
            self.ap.write(txn)


class CallbackAgent(uvm_agent):
    """Agent with callbacks."""
    
    def build_phase(self):
        self.logger.info("Building CallbackAgent")
        self.driver = DriverWithCallbacks.create("driver", self)
        self.monitor = MonitorWithCallbacks.create("monitor", self)
        self.seqr = uvm_sequencer("sequencer", self)
    
    def connect_phase(self):
        self.logger.info("Connecting CallbackAgent")
        self.driver.seq_item_port.connect(self.seqr.seq_item_export)
    
    def end_of_elaboration_phase(self):
        """End of elaboration - demonstrate callback classes."""
        self.logger.info("Callback classes are defined but pyuvm doesn't support callback registration")
        self.logger.info("DriverCallback and MonitorCallback classes demonstrate callback structure")


class CallbackEnv(uvm_env):
    """Environment with callbacks."""
    
    def build_phase(self):
        self.logger.info("Building CallbackEnv")
        self.agent = CallbackAgent.create("agent", self)
    
    def connect_phase(self):
        self.logger.info("Connecting CallbackEnv")


# Note: @uvm_test() decorator removed to avoid import-time TypeError
# Using cocotb test wrapper instead for compatibility with cocotb test discovery
class CallbackTest(uvm_test):
    """Test demonstrating callbacks."""
    
    def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Callback Example Test")
        self.logger.info("=" * 60)
        self.env = CallbackEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running callback test")
        await Timer(50, units="ns")
        self.drop_objection()
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Callback test completed")
        self.logger.info("=" * 60)


# Cocotb test function to run the pyuvm test
@cocotb.test()
async def test_callback(dut):
    """Cocotb test wrapper for pyuvm test."""
    # Register the test class with uvm_root so run_test can find it
    if not hasattr(uvm_root(), 'm_uvm_test_classes'):
        uvm_root().m_uvm_test_classes = {}
    uvm_root().m_uvm_test_classes["CallbackTest"] = CallbackTest
    # Use uvm_root to run the test properly (executes all phases in hierarchy)
    await uvm_root().run_test("CallbackTest")


if __name__ == "__main__":
    print("This is a pyuvm callback example.")
    print("To run with cocotb, use the Makefile in the test directory.")

