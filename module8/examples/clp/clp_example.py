"""
Module 8 Example 8.1: Command Line Processor (CLP)
Demonstrates using UVM Command Line Processor for test configuration.
"""

from pyuvm import *
import sys
import cocotb
from cocotb.triggers import Timer


class CLPTransaction(uvm_sequence_item):
    """Transaction for CLP example."""
    
    def __init__(self, name="CLPTransaction"):
        super().__init__(name)
        self.data = 0
        self.address = 0
    
    def __str__(self):
        return f"data=0x{self.data:02X}, addr=0x{self.address:04X}"


class CLPEnv(uvm_env):
    """Environment demonstrating CLP usage."""
    
    def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Building CLP Environment")
        self.logger.info("=" * 60)
        
        # Get command-line arguments using Python's argparse (CLP equivalent)
        # In pyuvm, we use Python's standard library instead of UVM CLP
        self.test_mode = self.get_clp_arg("+test_mode", "normal")
        self.debug_level = int(self.get_clp_arg("+debug_level", "0"))
        self.num_transactions = int(self.get_clp_arg("+num_transactions", "10"))
        self.seed = int(self.get_clp_arg("+seed", "0"))
        
        self.logger.info(f"CLP Configuration:")
        self.logger.info(f"  test_mode: {self.test_mode}")
        self.logger.info(f"  debug_level: {self.debug_level}")
        self.logger.info(f"  num_transactions: {self.num_transactions}")
        self.logger.info(f"  seed: {self.seed}")
        
        # Create agent for sequence execution
        self.agent = CLPAgent.create("agent", self)
    
    def get_clp_arg(self, arg_name, default_value):
        """
        Get command-line argument value.
        
        In pyuvm/Python, we use sys.argv or argparse.
        This function simulates UVM CLP behavior.
        
        Args:
            arg_name: Argument name (e.g., "+test_mode")
            default_value: Default value if argument not found
        
        Returns:
            Argument value or default
        """
        # Remove '+' prefix if present
        clean_name = arg_name.lstrip('+')
        
        # Check sys.argv for argument
        for i, arg in enumerate(sys.argv):
            if arg.startswith(f"+{clean_name}="):
                return arg.split('=')[1]
            elif arg == f"+{clean_name}":
                # Boolean flag
                if i + 1 < len(sys.argv):
                    return sys.argv[i + 1]
                return "1"
        
        return default_value


class CLPSequence(uvm_sequence):
    """Sequence using CLP configuration."""
    
    def __init__(self, name="CLPSequence", num_transactions=10):
        super().__init__(name)
        self.num_transactions = num_transactions
    
    async def body(self):
        """Generate transactions based on CLP configuration."""
        # Note: Sequences don't have logger, so we skip logging here
        for i in range(self.num_transactions):
            txn = CLPTransaction()
            txn.data = i * 0x10
            txn.address = i * 0x100
            await self.start_item(txn)
            await self.finish_item(txn)


class CLPDriver(uvm_driver):
    """Simple driver for CLP example."""
    
    def build_phase(self):
        self.seq_item_port = uvm_seq_item_pull_port("seq_item_port", self)
    
    async def run_phase(self):
        """Run phase - consume transactions from sequencer."""
        while True:
            txn = await self.seq_item_port.get_next_item()
            self.logger.info(f"[{self.get_name()}] Received transaction: {txn}")
            # Simulate processing
            await Timer(1, unit="ns")
            await self.seq_item_port.item_done()


class CLPAgent(uvm_agent):
    """Agent for CLP example."""
    
    def build_phase(self):
        self.logger.info("Building CLP agent")
        self.driver = CLPDriver.create("driver", self)
        self.seqr = uvm_sequencer("sequencer", self)
    
    def connect_phase(self):
        self.logger.info("Connecting CLP agent")
        self.driver.seq_item_port.connect(self.seqr.seq_item_export)


# Note: @uvm_test() decorator removed to avoid import-time TypeError
# Using cocotb test wrapper instead for compatibility with cocotb test discovery
class CLPTest(uvm_test):
    """
    Test demonstrating Command Line Processor usage.
    
    Usage:
        python clp_example.py +test_mode=stress +debug_level=2 +num_transactions=20 +seed=12345
    """
    
    def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Command Line Processor Example Test")
        self.logger.info("=" * 60)
        self.env = CLPEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running CLP test")
        
        # Use CLP configuration
        test_mode = self.env.test_mode
        self.logger.info(f"Running in {test_mode} mode")
        
        if test_mode == "stress":
            self.logger.info("Stress test mode: Running extended test")
        elif test_mode == "quick":
            self.logger.info("Quick test mode: Running minimal test")
        else:
            self.logger.info("Normal test mode: Running standard test")
        
        # Start sequence with configuration from environment
        num_txns = self.env.num_transactions if hasattr(self.env, 'num_transactions') else 10
        seq = CLPSequence.create("seq")
        seq.num_transactions = num_txns
        await seq.start(self.env.agent.seqr)
        
        await Timer(100, unit="ns")
        self.drop_objection()
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("CLP test completed")
        self.logger.info("=" * 60)
        self.logger.info("CLP Configuration used:")
        self.logger.info(f"  test_mode: {self.env.test_mode}")
        self.logger.info(f"  debug_level: {self.env.debug_level}")
        self.logger.info(f"  num_transactions: {self.env.num_transactions}")
        self.logger.info(f"  seed: {self.env.seed}")


# Cocotb test function to run the pyuvm test
@cocotb.test()
async def test_clp(dut):
    """Cocotb test wrapper for pyuvm test."""
    # Register the test class with uvm_root so run_test can find it
    if not hasattr(uvm_root(), 'm_uvm_test_classes'):
        uvm_root().m_uvm_test_classes = {}
    uvm_root().m_uvm_test_classes["CLPTest"] = CLPTest
    # Use uvm_root to run the test properly (executes all phases in hierarchy)
    await uvm_root().run_test("CLPTest")


if __name__ == "__main__":
    print("Command Line Processor Example")
    print("=" * 60)
    print("This example demonstrates UVM CLP usage in pyuvm.")
    print("In pyuvm, we use Python's sys.argv or argparse instead of UVM CLP.")
    print("")
    print("Usage:")
    print("  python clp_example.py +test_mode=stress +debug_level=2 +num_transactions=20")
    print("")
    print("Command-line arguments:")
    print("  +test_mode=<mode>        Test mode (normal, stress, quick)")
    print("  +debug_level=<level>     Debug level (0-3)")
    print("  +num_transactions=<num>  Number of transactions")
    print("  +seed=<seed>             Random seed")
    print("")

