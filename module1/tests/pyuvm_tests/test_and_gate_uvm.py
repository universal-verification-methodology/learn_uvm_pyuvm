"""
Module 1: AND Gate UVM Test
pyuvm testbench for AND gate.

Demonstrates:
- UVM test structure
- UVM phases
- UVM reporting
"""

from pyuvm import *


class AndGateTransaction(uvm_sequence_item):
    """Transaction for AND gate test."""
    
    def __init__(self, name="AndGateTransaction"):
        super().__init__(name)
        self.a = 0
        self.b = 0
        self.expected_y = 0
    
    def __str__(self):
        return f"a={self.a}, b={self.b}, expected_y={self.expected_y}"


class AndGateSequence(uvm_sequence):
    """Sequence to generate AND gate test vectors."""
    
    async def body(self):
        """Generate test vectors."""
        test_vectors = [
            (0, 0, 0),
            (0, 1, 0),
            (1, 0, 0),
            (1, 1, 1),
        ]
        
        for a, b, expected_y in test_vectors:
            txn = AndGateTransaction()
            txn.a = a
            txn.b = b
            txn.expected_y = expected_y
            await self.start_item(txn)
            await self.finish_item(txn)


class AndGateDriver(uvm_driver):
    """Driver to apply inputs to DUT."""
    
    def build_phase(self):
        self.seq_item_port = uvm_seq_item_pull_port("seq_item_port", self)
    
    async def run_phase(self):
        while True:
            txn = await self.seq_item_port.get_next_item()
            # In real implementation, drive DUT signals here
            self.logger.info(f"Driving: {txn}")
            await self.seq_item_port.item_done()


class AndGateMonitor(uvm_monitor):
    """Monitor to observe DUT outputs."""
    
    async def run_phase(self):
        while True:
            # In real implementation, sample DUT outputs here
            await Timer(10, units="ns")
            self.logger.info("Monitoring DUT outputs")


class AndGateAgent(uvm_agent):
    """Agent containing driver and monitor."""
    
    def build_phase(self):
        self.driver = AndGateDriver.create("driver", self)
        self.monitor = AndGateMonitor.create("monitor", self)
        self.seqr = uvm_sequencer("sequencer", self)
    
    def connect_phase(self):
        self.driver.seq_item_port.connect(self.seqr.seq_item_export)


class AndGateEnv(uvm_env):
    """Test environment."""
    
    def build_phase(self):
        self.agent = AndGateAgent.create("agent", self)
    
    def connect_phase(self):
        pass


@uvm_test()
class AndGateTest(uvm_test):
    """Test class for AND gate."""
    
    async def build_phase(self):
        self.env = AndGateEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        seq = AndGateSequence.create("seq")
        await seq.start(self.env.agent.seqr)
        await Timer(100, units="ns")
        self.drop_objection()
    
    def check_phase(self):
        self.logger.info("Checking test results")


if __name__ == "__main__":
    # Note: This is a simplified example
    # In practice, you would use cocotb to run this with a simulator
    print("This is a pyuvm test structure example.")
    print("To run with cocotb, use the Makefile in the test directory.")

