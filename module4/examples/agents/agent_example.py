"""
Module 4 Example 4.4: Complete Agent Implementation
Demonstrates complete agent with driver, monitor, sequencer, and sequences.
"""

from pyuvm import *
import cocotb
from cocotb.triggers import Timer, RisingEdge


class AgentTransaction(uvm_sequence_item):
    """Transaction for complete agent example."""
    
    def __init__(self, name="AgentTransaction"):
        super().__init__(name)
        self.data = 0
        self.address = 0
    
    def __str__(self):
        return f"data=0x{self.data:02X}, addr=0x{self.address:04X}"


class AgentSequence(uvm_sequence):
    """Sequence for agent."""
    
    async def body(self):
        """Generate transactions."""
        for i in range(5):
            txn = AgentTransaction()
            txn.data = i * 0x10
            txn.address = i * 0x100
            await self.start_item(txn)
            await self.finish_item(txn)


class AgentDriver(uvm_driver):
    """Driver for agent."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building driver")
        self.seq_item_port = uvm_seq_item_pull_port("seq_item_port", self)
    
    def connect_phase(self):
        self.logger.info(f"[{self.get_name()}] Connecting driver")
    
    async def run_phase(self):
        """Run phase - drive transactions."""
        self.logger.info(f"[{self.get_name()}] Starting driver")
        
        while True:
            item = await self.seq_item_port.get_next_item()
            self.logger.info(f"[{self.get_name()}] Driving: {item}")
            
            # Drive to DUT (simulated)
            # In real code: cocotb.dut.data.value = item.data
            # In real code: cocotb.dut.address.value = item.address
            await Timer(10, units="ns")
            
            await self.seq_item_port.item_done()


class AgentMonitor(uvm_monitor):
    """Monitor for agent."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building monitor")
        self.ap = uvm_analysis_port("ap", self)
    
    async def run_phase(self):
        """Run phase - monitor DUT."""
        self.logger.info(f"[{self.get_name()}] Starting monitor")
        
        while True:
            # Sample DUT (simulated)
            await Timer(10, units="ns")
            
            # Create transaction from sampled signals
            txn = AgentTransaction()
            txn.data = 0xAA  # Simulated
            txn.address = 0x1000  # Simulated
            
            self.logger.info(f"[{self.get_name()}] Sampled: {txn}")
            self.ap.write(txn)


class CompleteAgent(uvm_agent):
    """
    Complete agent with all components.
    
    Shows:
    - Agent structure
    - Component instantiation
    - Component connections
    - Active/passive configuration
    """
    
    def build_phase(self):
        """Build phase - create components."""
        self.logger.info("=" * 60)
        self.logger.info(f"[{self.get_name()}] Building complete agent")
        
        # Get agent configuration
        self.active = True
        config = None
        if ConfigDB().get(None, "", f"{self.get_full_name()}.active", config):
            self.active = config
        
        self.logger.info(f"[{self.get_name()}] Agent mode: {'ACTIVE' if self.active else 'PASSIVE'}")
        
        # Always create monitor
        self.monitor = AgentMonitor.create("monitor", self)
        
        # Create driver and sequencer only if active
        if self.active:
            self.driver = AgentDriver.create("driver", self)
            self.seqr = uvm_sequencer("sequencer", self)
            self.logger.info(f"[{self.get_name()}] Created driver and sequencer")
        else:
            self.logger.info(f"[{self.get_name()}] Passive agent - no driver/sequencer")
    
    def connect_phase(self):
        """Connect phase - connect components."""
        self.logger.info(f"[{self.get_name()}] Connecting agent")
        
        if self.active:
            # Connect driver to sequencer
            self.driver.seq_item_port.connect(self.seqr.seq_item_export)
            self.logger.info(f"[{self.get_name()}] Connected driver to sequencer")
        
        # Monitor analysis port is connected externally in environment
        self.logger.info(f"[{self.get_name()}] Agent connections complete")


class AgentScoreboard(uvm_scoreboard):
    """Scoreboard for agent."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building scoreboard")
        self.ap = uvm_analysis_export("ap", self)
        self.imp = uvm_analysis_imp("imp", self)
        self.ap.connect(self.imp)
        self.received = []
    
    def write(self, txn):
        """Receive transactions from monitor."""
        self.logger.info(f"[{self.get_name()}] Scoreboard received: {txn}")
        self.received.append(txn)
    
    def check_phase(self):
        """Check phase."""
        self.logger.info(f"[{self.get_name()}] Scoreboard check: received {len(self.received)} transactions")


class AgentEnv(uvm_env):
    """Environment with complete agent."""
    
    def build_phase(self):
        self.logger.info("Building AgentEnv")
        self.agent = CompleteAgent.create("agent", self)
        self.scoreboard = AgentScoreboard.create("scoreboard", self)
    
    def connect_phase(self):
        self.logger.info("Connecting AgentEnv")
        # Connect monitor analysis port to scoreboard
        self.agent.monitor.ap.connect(self.scoreboard.ap)


@uvm_test()
class CompleteAgentTest(uvm_test):
    """Test demonstrating complete agent."""
    
    async def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Complete Agent Example Test")
        self.logger.info("=" * 60)
        self.env = AgentEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running complete agent test")
        
        # Start sequence if agent is active
        if self.env.agent.active:
            self.logger.info("Starting sequence on active agent")
            seq = AgentSequence.create("seq")
            await seq.start(self.env.agent.seqr)
        
        await Timer(100, units="ns")
        self.drop_objection()
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Complete agent test completed")
        self.logger.info("=" * 60)


@uvm_test()
class PassiveAgentTest(uvm_test):
    """Test demonstrating passive agent."""
    
    async def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Passive Agent Example Test")
        self.logger.info("=" * 60)
        
        # Configure agent as passive
        ConfigDB().set(None, "", "env.agent.active", False)
        
        self.env = AgentEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running passive agent test")
        await Timer(100, units="ns")
        self.drop_objection()
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Passive agent test completed")
        self.logger.info("=" * 60)


if __name__ == "__main__":
    print("This is a pyuvm complete agent example.")
    print("To run with cocotb, use the Makefile in the test directory.")

