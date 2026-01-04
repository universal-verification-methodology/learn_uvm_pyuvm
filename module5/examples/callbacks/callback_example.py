"""
Module 5 Example 5.4: UVM Callbacks
Demonstrates callback implementation and usage.
"""

from pyuvm import *


class DriverTransaction(uvm_sequence_item):
    """Transaction for callback example."""
    
    def __init__(self, name="DriverTransaction"):
        super().__init__(name)
        self.data = 0
    
    def __str__(self):
        return f"data=0x{self.data:02X}"


class DriverCallback(uvm_callback):
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
        self.seq_item_port = uvm_seq_item_pull_port("seq_item_port", self)
    
    async def run_phase(self):
        """Run phase with callback execution."""
        self.logger.info(f"[{self.get_name()}] Starting driver")
        
        while True:
            item = await self.seq_item_port.get_next_item()
            
            # Execute pre-drive callbacks
            self.logger.info(f"[{self.get_name()}] Executing pre-drive callbacks")
            for callback in self.get_callbacks(DriverCallback):
                item = callback.pre_drive(self, item)
            
            # Drive transaction
            self.logger.info(f"[{self.get_name()}] Driving: {item}")
            await Timer(10, units="ns")
            
            # Execute post-drive callbacks
            self.logger.info(f"[{self.get_name()}] Executing post-drive callbacks")
            for callback in self.get_callbacks(DriverCallback):
                callback.post_drive(self, item)
            
            await self.seq_item_port.item_done()


class MonitorCallback(uvm_callback):
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
        """Run phase with callback execution."""
        self.logger.info(f"[{self.get_name()}] Starting monitor")
        
        while True:
            # Sample DUT (simulated)
            await Timer(10, units="ns")
            
            txn = DriverTransaction()
            txn.data = 0xAA
            
            # Execute pre-sample callbacks
            for callback in self.get_callbacks(MonitorCallback):
                txn = callback.pre_sample(self, txn)
            
            # Sample transaction
            self.logger.info(f"[{self.get_name()}] Sampled: {txn}")
            
            # Execute post-sample callbacks
            for callback in self.get_callbacks(MonitorCallback):
                callback.post_sample(self, txn)
            
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
        """End of elaboration - register callbacks."""
        self.logger.info("Registering callbacks")
        
        # Register driver callbacks
        driver_callback = DriverCallback.create("driver_callback")
        self.driver.add_callback(driver_callback)
        self.logger.info("Registered driver callback")
        
        # Register monitor callbacks
        monitor_callback = MonitorCallback.create("monitor_callback")
        self.monitor.add_callback(monitor_callback)
        self.logger.info("Registered monitor callback")


class CallbackEnv(uvm_env):
    """Environment with callbacks."""
    
    def build_phase(self):
        self.logger.info("Building CallbackEnv")
        self.agent = CallbackAgent.create("agent", self)
    
    def connect_phase(self):
        self.logger.info("Connecting CallbackEnv")


@uvm_test()
class CallbackTest(uvm_test):
    """Test demonstrating callbacks."""
    
    async def build_phase(self):
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


if __name__ == "__main__":
    print("This is a pyuvm callback example.")
    print("To run with cocotb, use the Makefile in the test directory.")

