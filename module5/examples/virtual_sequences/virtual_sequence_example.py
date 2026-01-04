"""
Module 5 Example 5.1: Virtual Sequences
Demonstrates virtual sequencer and virtual sequence coordination.
"""

from pyuvm import *
import cocotb


class VirtualTransaction(uvm_sequence_item):
    """Transaction for virtual sequence example."""
    
    def __init__(self, name="VirtualTransaction"):
        super().__init__(name)
        self.data = 0
        self.channel = 0
    
    def __str__(self):
        return f"data=0x{self.data:02X}, channel={self.channel}"


class ChannelSequence(uvm_sequence):
    """Sequence for a single channel."""
    
    def __init__(self, name="ChannelSequence", channel=0, num_items=5):
        super().__init__(name)
        self.channel = channel
        self.num_items = num_items
    
    async def body(self):
        """Generate transactions for this channel."""
        self.logger.info(f"[{self.get_name()}] Starting channel {self.channel} sequence")
        
        for i in range(self.num_items):
            txn = VirtualTransaction()
            txn.data = i * 0x10
            txn.channel = self.channel
            
            await self.start_item(txn)
            await self.finish_item(txn)
            
            self.logger.info(f"[{self.get_name()}] Generated transaction {i} for channel {self.channel}: {txn}")


class VirtualSequence(uvm_sequence):
    """
    Virtual sequence coordinating multiple sequencers.
    
    Shows:
    - Virtual sequence structure
    - Multiple sequencer coordination
    - Parallel sequence execution
    - Sequence synchronization
    """
    
    def __init__(self, name="VirtualSequence"):
        super().__init__(name)
        # Virtual sequencer references (set by test)
        self.master_seqr = None
        self.slave_seqr = None
    
    async def body(self):
        """Body method - coordinate multiple sequences."""
        self.logger.info("=" * 60)
        self.logger.info(f"[{self.get_name()}] Starting virtual sequence")
        self.logger.info("=" * 60)
        
        # Start sequences on different sequencers in parallel
        if self.master_seqr and self.slave_seqr:
            self.logger.info("[VirtualSequence] Starting parallel sequences")
            
            # Start master sequence
            master_seq = ChannelSequence.create("master_seq", channel=0, num_items=3)
            master_task = cocotb.start_soon(master_seq.start(self.master_seqr))
            
            # Start slave sequence
            slave_seq = ChannelSequence.create("slave_seq", channel=1, num_items=3)
            slave_task = cocotb.start_soon(slave_seq.start(self.slave_seqr))
            
            # Wait for both to complete
            await master_task
            await slave_task
            
            self.logger.info("[VirtualSequence] Parallel sequences completed")
        
        # Sequential execution example
        self.logger.info("=" * 60)
        self.logger.info("[VirtualSequence] Starting sequential sequences")
        
        if self.master_seqr:
            seq1 = ChannelSequence.create("seq1", channel=0, num_items=2)
            await seq1.start(self.master_seqr)
        
        if self.slave_seqr:
            seq2 = ChannelSequence.create("seq2", channel=1, num_items=2)
            await seq2.start(self.slave_seqr)
        
        self.logger.info("[VirtualSequence] Sequential sequences completed")
        self.logger.info("=" * 60)


class VirtualSequencer(uvm_sequencer):
    """
    Virtual sequencer containing references to multiple sequencers.
    
    Shows:
    - Virtual sequencer structure
    - Multiple sequencer references
    - Virtual sequencer implementation
    """
    
    def build_phase(self):
        """Build phase - virtual sequencer doesn't create sub-sequencers."""
        self.logger.info(f"[{self.get_name()}] Building virtual sequencer")
        # References to actual sequencers (set in connect_phase)
        self.master_seqr = None
        self.slave_seqr = None
    
    def connect_phase(self):
        """Connect phase - get references to actual sequencers."""
        self.logger.info(f"[{self.get_name()}] Connecting virtual sequencer")
        # In real implementation, get sequencer references from environment
        # self.master_seqr = self.env.master_agent.seqr
        # self.slave_seqr = self.env.slave_agent.seqr


class MasterAgent(uvm_agent):
    """Master agent."""
    
    def build_phase(self):
        self.logger.info("Building MasterAgent")
        self.seqr = uvm_sequencer("sequencer", self)
    
    def connect_phase(self):
        self.logger.info("Connecting MasterAgent")


class SlaveAgent(uvm_agent):
    """Slave agent."""
    
    def build_phase(self):
        self.logger.info("Building SlaveAgent")
        self.seqr = uvm_sequencer("sequencer", self)
    
    def connect_phase(self):
        self.logger.info("Connecting SlaveAgent")


class VirtualEnv(uvm_env):
    """Environment with multiple agents and virtual sequencer."""
    
    def build_phase(self):
        self.logger.info("Building VirtualEnv")
        self.master_agent = MasterAgent.create("master_agent", self)
        self.slave_agent = SlaveAgent.create("slave_agent", self)
        self.virtual_seqr = VirtualSequencer.create("virtual_seqr", self)
    
    def connect_phase(self):
        self.logger.info("Connecting VirtualEnv")
        # Connect virtual sequencer to actual sequencers
        self.virtual_seqr.master_seqr = self.master_agent.seqr
        self.virtual_seqr.slave_seqr = self.slave_agent.seqr


@uvm_test()
class VirtualSequenceTest(uvm_test):
    """Test demonstrating virtual sequences."""
    
    async def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Virtual Sequence Example Test")
        self.logger.info("=" * 60)
        self.env = VirtualEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running virtual sequence test")
        
        # Create and start virtual sequence
        virtual_seq = VirtualSequence.create("virtual_seq")
        virtual_seq.master_seqr = self.env.virtual_seqr.master_seqr
        virtual_seq.slave_seqr = self.env.virtual_seqr.slave_seqr
        
        await virtual_seq.start(self.env.virtual_seqr)
        
        await Timer(10, units="ns")
        self.drop_objection()
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Virtual sequence test completed")
        self.logger.info("=" * 60)


if __name__ == "__main__":
    print("This is a pyuvm virtual sequence example.")
    print("To run with cocotb, use the Makefile in the test directory.")

