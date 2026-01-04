"""
Module 4 Example 4.3: UVM Sequencer and Sequences
Demonstrates sequencer usage and sequence implementation.
"""

from pyuvm import *
import random


class DataTransaction(uvm_sequence_item):
    """Transaction for sequencer example."""
    
    def __init__(self, name="DataTransaction"):
        super().__init__(name)
        self.data = 0
        self.address = 0
    
    def __str__(self):
        return f"data=0x{self.data:02X}, addr=0x{self.address:04X}"


class SimpleSequence(uvm_sequence):
    """
    Simple sequence demonstrating basic sequence implementation.
    
    Shows:
    - Sequence class structure
    - body() method implementation
    - Transaction creation
    - Sequence execution
    """
    
    async def body(self):
        """Body method - sequence execution."""
        self.logger.info(f"[{self.get_name()}] Starting sequence body")
        
        # Create and send transactions
        for i in range(5):
            txn = DataTransaction()
            txn.data = i * 0x10
            txn.address = i * 0x100
            
            self.logger.info(f"[{self.get_name()}] Creating transaction {i}: {txn}")
            
            # Start item (request from sequencer)
            await self.start_item(txn)
            self.logger.info(f"[{self.get_name()}] Started item: {txn}")
            
            # Finish item (send to driver)
            await self.finish_item(txn)
            self.logger.info(f"[{self.get_name()}] Finished item: {txn}")
        
        self.logger.info(f"[{self.get_name()}] Sequence body completed")


class RandomSequence(uvm_sequence):
    """
    Sequence demonstrating random transaction generation.
    
    Shows:
    - Random transaction creation
    - Constrained random generation
    - Sequence reuse
    """
    
    def __init__(self, name="RandomSequence", num_items=10):
        super().__init__(name)
        self.num_items = num_items
    
    async def body(self):
        """Body method with random transactions."""
        self.logger.info(f"[{self.get_name()}] Starting random sequence ({self.num_items} items)")
        
        for i in range(self.num_items):
            txn = DataTransaction()
            # Random data generation
            txn.data = random.randint(0, 255)
            txn.address = random.randint(0, 0xFFFF)
            
            await self.start_item(txn)
            await self.finish_item(txn)
            
            self.logger.info(f"[{self.get_name()}] Generated random transaction {i}: {txn}")


class LayeredSequence(uvm_sequence):
    """
    Sequence demonstrating sequence layering.
    
    Shows:
    - Calling other sequences
    - Sequence composition
    - Hierarchical sequences
    """
    
    async def body(self):
        """Body method with sequence layering."""
        self.logger.info(f"[{self.get_name()}] Starting layered sequence")
        
        # Start simple sequence
        simple_seq = SimpleSequence.create("simple_seq")
        await simple_seq.start(self.sequencer)
        self.logger.info(f"[{self.get_name()}] Completed simple sequence")
        
        # Start random sequence
        random_seq = RandomSequence.create("random_seq", num_items=3)
        await random_seq.start(self.sequencer)
        self.logger.info(f"[{self.get_name()}] Completed random sequence")


class SequencerAgent(uvm_agent):
    """Agent with sequencer."""
    
    def build_phase(self):
        self.logger.info("Building SequencerAgent")
        self.seqr = uvm_sequencer("sequencer", self)
    
    def connect_phase(self):
        self.logger.info("Connecting SequencerAgent")


@uvm_test()
class SequencerTest(uvm_test):
    """Test demonstrating sequencer and sequence usage."""
    
    async def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Sequencer Example Test")
        self.logger.info("=" * 60)
        self.env = SequencerAgent.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running sequencer test")
        
        # Start simple sequence
        self.logger.info("=" * 60)
        self.logger.info("Starting SimpleSequence")
        seq1 = SimpleSequence.create("seq1")
        await seq1.start(self.env.seqr)
        
        # Start random sequence
        self.logger.info("=" * 60)
        self.logger.info("Starting RandomSequence")
        seq2 = RandomSequence.create("seq2", num_items=5)
        await seq2.start(self.env.seqr)
        
        # Start layered sequence
        self.logger.info("=" * 60)
        self.logger.info("Starting LayeredSequence")
        seq3 = LayeredSequence.create("seq3")
        await seq3.start(self.env.seqr)
        
        await Timer(10, units="ns")
        self.drop_objection()
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Sequencer test completed")
        self.logger.info("=" * 60)


if __name__ == "__main__":
    print("This is a pyuvm sequencer example.")
    print("To run with cocotb, use the Makefile in the test directory.")

