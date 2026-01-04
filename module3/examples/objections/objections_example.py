"""
Module 3 Example: Objection Mechanism
Demonstrates UVM objection mechanism for test control.
"""

from pyuvm import *


class ObjectionComponent(uvm_component):
    """
    Component demonstrating objection usage.
    """
    
    async def run_phase(self):
        """Run phase with objections."""
        self.raise_objection()
        self.logger.info(f"[{self.get_name()}] Raised objection")
        
        # Simulate work
        await Timer(50, units="ns")
        self.logger.info(f"[{self.get_name()}] Work completed")
        
        self.drop_objection()
        self.logger.info(f"[{self.get_name()}] Dropped objection")


class MultipleObjectionsComponent(uvm_component):
    """
    Component with multiple objections.
    """
    
    async def run_phase(self):
        """Run phase with multiple objections."""
        # Raise multiple objections
        self.raise_objection()
        self.raise_objection()
        self.logger.info(f"[{self.get_name()}] Raised 2 objections")
        
        await Timer(30, units="ns")
        
        # Drop one objection
        self.drop_objection()
        self.logger.info(f"[{self.get_name()}] Dropped 1 objection, 1 remaining")
        
        await Timer(20, units="ns")
        
        # Drop remaining objection
        self.drop_objection()
        self.logger.info(f"[{self.get_name()}] Dropped all objections")


class ObjectionEnv(uvm_env):
    """Environment with objection components."""
    
    def build_phase(self):
        self.logger.info("Building ObjectionEnv")
        self.comp1 = ObjectionComponent.create("comp1", self)
        self.comp2 = ObjectionComponent.create("comp2", self)
        self.comp3 = MultipleObjectionsComponent.create("comp3", self)
    
    async def run_phase(self):
        """Environment can also raise objections."""
        self.raise_objection()
        self.logger.info("[ObjectionEnv] Raised objection")
        await Timer(100, units="ns")
        self.drop_objection()
        self.logger.info("[ObjectionEnv] Dropped objection")


@uvm_test()
class ObjectionTest(uvm_test):
    """
    Test demonstrating objection mechanism.
    """
    
    async def build_phase(self):
        """Build phase."""
        self.logger.info("=" * 60)
        self.logger.info("Objection Mechanism Example")
        self.logger.info("=" * 60)
        self.env = ObjectionEnv.create("env", self)
    
    async def run_phase(self):
        """Run phase - main test with objections."""
        # Test raises objection to keep simulation running
        self.raise_objection()
        self.logger.info("[Test] Raised objection - simulation will run")
        
        # Components will raise/drop their own objections
        # Simulation continues until all objections are dropped
        await Timer(200, units="ns")
        
        self.logger.info("[Test] Dropping objection - simulation will end")
        self.drop_objection()
    
    def report_phase(self):
        """Report phase."""
        self.logger.info("=" * 60)
        self.logger.info("Objection test completed")
        self.logger.info("=" * 60)


@uvm_test()
class ObjectionTimingTest(uvm_test):
    """
    Test demonstrating objection timing.
    """
    
    async def build_phase(self):
        """Build phase."""
        self.logger.info("=" * 60)
        self.logger.info("Objection Timing Example")
        self.logger.info("=" * 60)
        self.env = ObjectionEnv.create("env", self)
    
    async def run_phase(self):
        """Run phase - demonstrate objection timing."""
        self.raise_objection()
        
        self.logger.info("Test started - objection raised")
        
        # Wait for components to complete
        await Timer(150, units="ns")
        
        self.logger.info("All components should have dropped objections")
        self.logger.info("Dropping test objection - simulation will end")
        self.drop_objection()


if __name__ == "__main__":
    print("This is a pyuvm objection example.")
    print("To run with cocotb, use the Makefile in the test directory.")

