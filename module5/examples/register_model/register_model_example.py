"""
Module 5 Example 5.5: Advanced Register Model
Demonstrates register model usage (basic example).
Note: Full register model support may vary in pyuvm.
"""

from pyuvm import *
import cocotb
from cocotb.triggers import Timer

# Note: pyuvm uses uvm_seq_item_port instead of uvm_seq_item_pull_port


class RegisterTransaction(uvm_sequence_item):
    """Transaction for register model example."""
    
    def __init__(self, name="RegisterTransaction"):
        super().__init__(name)
        self.address = 0
        self.data = 0
        self.is_write = True
    
    def __str__(self):
        op = "WRITE" if self.is_write else "READ"
        return f"{op}: addr=0x{self.address:04X}, data=0x{self.data:02X}"


class RegisterModel(uvm_object):
    """
    Simple register model implementation.
    
    Shows:
    - Register model structure
    - Register operations
    - Register access patterns
    Note: This is a simplified example. Full UVM register model
    support may require additional pyuvm features.
    """
    
    def __init__(self, name="RegisterModel"):
        super().__init__(name)
        # Simple register storage (address -> value)
        self.registers = {}
        # Register definitions
        self.reg_defs = {
            0x0000: "CONTROL",
            0x0004: "STATUS",
            0x0008: "DATA",
            0x000C: "CONFIG",
        }
    
    def write(self, address, data):
        """Write register."""
        print(f"[{self.get_name()}] Writing register 0x{address:04X} ({self.reg_defs.get(address, 'UNKNOWN')}): 0x{data:02X}")
        self.registers[address] = data
        return True

    def read(self, address):
        """Read register."""
        value = self.registers.get(address, 0)
        print(f"[{self.get_name()}] Reading register 0x{address:04X} ({self.reg_defs.get(address, 'UNKNOWN')}): 0x{value:02X}")
        return value

    def peek(self, address):
        """Peek register (backdoor read)."""
        value = self.registers.get(address, 0)
        print(f"[{self.get_name()}] Peeking register 0x{address:04X}: 0x{value:02X}")
        return value
    
    def poke(self, address, data):
        """Poke register (backdoor write)."""
        print(f"[{self.get_name()}] Poking register 0x{address:04X}: 0x{data:02X}")
        self.registers[address] = data
        return True
    
    def update(self):
        """Update registers (write desired values to hardware)."""
        print(f"[{self.get_name()}] Updating registers")
        for addr, value in self.registers.items():
            print(f"  Register 0x{addr:04X}: 0x{value:02X}")
        return True


class RegisterSequence(uvm_sequence):
    """Sequence for register access."""
    
    async def body(self):
        """Body method - perform register operations."""
        print(f"[{self.get_name()}] Starting register sequence")
        
        # Get register model from sequencer (in real implementation)
        # reg_model = self.sequencer.reg_model
        
        # Simulate register operations
        operations = [
            (0x0000, 0x01, True),   # Write CONTROL
            (0x0004, 0x00, False),  # Read STATUS
            (0x0008, 0xAB, True),   # Write DATA
            (0x000C, 0x00, False),  # Read CONFIG
        ]
        
        for addr, data, is_write in operations:
            txn = RegisterTransaction()
            txn.address = addr
            txn.data = data
            txn.is_write = is_write
            
            await self.start_item(txn)
            await self.finish_item(txn)
            
            print(f"[{self.get_name()}] Register operation: {txn}")


class RegisterDriver(uvm_driver):
    """Driver for register access."""
    
    def build_phase(self):
        print(f"[{self.get_name()}] Building register driver")
        # seq_item_port is already created by uvm_driver.__init__()
        # In real implementation, would have register model reference
        self.reg_model = None
    
    async def run_phase(self):
        """Run phase - execute register operations."""
        print(f"[{self.get_name()}] Starting register driver")
        
        while True:
            item = await self.seq_item_port.get_next_item()
            
            # Execute register operation
            if item.is_write:
                print(f"[{self.get_name()}] Writing register: {item}")
                # In real: self.reg_model.write(item.address, item.data)
            else:
                print(f"[{self.get_name()}] Reading register: {item}")
                # In real: data = self.reg_model.read(item.address)
            
            await Timer(10, units="ns")
            self.seq_item_port.item_done()


class RegisterAgent(uvm_agent):
    """Agent for register access."""
    
    def build_phase(self):
        print("Building RegisterAgent")
        self.driver = RegisterDriver.create("driver", self)
        self.seqr = uvm_sequencer("sequencer", self)
        # Create register model
        self.reg_model = RegisterModel("reg_model")
        self.driver.reg_model = self.reg_model
    
    def connect_phase(self):
        print("Connecting RegisterAgent")
        self.driver.seq_item_port.connect(self.seqr.seq_item_export)


class RegisterEnv(uvm_env):
    """Environment with register model."""
    
    def build_phase(self):
        print("Building RegisterEnv")
        self.agent = RegisterAgent.create("agent", self)
    
    def connect_phase(self):
        print("Connecting RegisterEnv")


# Note: @uvm_test() decorator removed to avoid import-time TypeError
# Using cocotb test wrapper instead for compatibility with cocotb test discovery
class RegisterModelTest(uvm_test):
    """Test demonstrating register model."""
    
    def build_phase(self):
        print("=" * 60)
        print("Register Model Example Test")
        print("=" * 60)
        self.env = RegisterEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        print("Running register model test")
        
        # Demonstrate register operations
        print("=" * 60)
        print("Register Operations:")
        
        # Frontdoor operations
        self.env.agent.reg_model.write(0x0000, 0x01)
        value = self.env.agent.reg_model.read(0x0000)
        print(f"Read back value: 0x{value:02X}")
        
        # Backdoor operations
        self.env.agent.reg_model.poke(0x0004, 0x80)
        value = self.env.agent.reg_model.peek(0x0004)
        print(f"Peeked value: 0x{value:02X}")
        
        # Start register sequence
        seq = RegisterSequence.create("seq")
        await seq.start(self.env.agent.seqr)
        
        await Timer(10, units="ns")
        self.drop_objection()
    
    def report_phase(self):
        print("=" * 60)
        print("Register model test completed")
        print("=" * 60)


# Cocotb test function to run the pyuvm test
@cocotb.test()
async def test_register_model(dut):
    """Cocotb test wrapper for pyuvm test."""
    # Register the test class with uvm_root so run_test can find it
    if not hasattr(uvm_root(), 'm_uvm_test_classes'):
        uvm_root().m_uvm_test_classes = {}
    uvm_root().m_uvm_test_classes["RegisterModelTest"] = RegisterModelTest
    # Use uvm_root to run the test properly (executes all phases in hierarchy)
    await uvm_root().run_test("RegisterModelTest")


if __name__ == "__main__":
    print("This is a pyuvm register model example.")
    print("Note: This is a simplified example. Full UVM register model")
    print("support may require additional pyuvm features.")
    print("To run with cocotb, use the Makefile in the test directory.")

