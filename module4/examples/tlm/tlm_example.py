"""
Module 4 Example: TLM (Transaction-Level Modeling)
Demonstrates TLM interfaces, ports, exports, and implementations.
"""

from pyuvm import *


class TLMTransaction(uvm_sequence_item):
    """Transaction for TLM examples."""
    
    def __init__(self, name="TLMTransaction"):
        super().__init__(name)
        self.data = 0
    
    def __str__(self):
        return f"data=0x{self.data:02X}"


# TLM Put Interface Example
class PutProducer(uvm_component):
    """Component using put port to send transactions."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building PutProducer")
        self.put_port = uvm_put_port("put_port", self)
    
    async def run_phase(self):
        """Run phase - produce transactions."""
        self.raise_objection()
        self.logger.info(f"[{self.get_name()}] Starting producer")
        
        for i in range(5):
            txn = TLMTransaction()
            txn.data = i * 0x10
            self.logger.info(f"[{self.get_name()}] Producing: {txn}")
            await self.put_port.put(txn)
            self.logger.info(f"[{self.get_name()}] Put transaction: {txn}")
        
        self.drop_objection()


class PutConsumer(uvm_component):
    """Component using put export to receive transactions."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building PutConsumer")
        self.put_export = uvm_put_export("put_export", self)
        self.put_imp = uvm_put_imp("put_imp", self)
        self.put_export.connect(self.put_imp)
    
    async def put(self, txn):
        """Put implementation method."""
        self.logger.info(f"[{self.get_name()}] Received via put: {txn}")
        await Timer(5, units="ns")


# TLM Get Interface Example
class GetProducer(uvm_component):
    """Component using get export to provide transactions."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building GetProducer")
        self.get_export = uvm_get_export("get_export", self)
        self.get_imp = uvm_get_imp("get_imp", self)
        self.get_export.connect(self.get_imp)
        self.transactions = []
        for i in range(5):
            txn = TLMTransaction()
            txn.data = i * 0x20
            self.transactions.append(txn)
        self.index = 0
    
    async def get(self):
        """Get implementation method."""
        if self.index < len(self.transactions):
            txn = self.transactions[self.index]
            self.index += 1
            self.logger.info(f"[{self.get_name()}] Providing via get: {txn}")
            await Timer(5, units="ns")
            return txn
        return None


class GetConsumer(uvm_component):
    """Component using get port to receive transactions."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building GetConsumer")
        self.get_port = uvm_get_port("get_port", self)
    
    async def run_phase(self):
        """Run phase - consume transactions."""
        self.raise_objection()
        self.logger.info(f"[{self.get_name()}] Starting consumer")
        
        for i in range(5):
            txn = await self.get_port.get()
            if txn:
                self.logger.info(f"[{self.get_name()}] Got transaction: {txn}")
        
        self.drop_objection()


# TLM Transport Interface Example
class TransportComponent(uvm_component):
    """Component using transport interface."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building TransportComponent")
        self.transport_port = uvm_transport_port("transport_port", self)
        self.transport_export = uvm_transport_export("transport_export", self)
        self.transport_imp = uvm_transport_imp("transport_imp", self)
        self.transport_export.connect(self.transport_imp)
    
    async def transport(self, req):
        """Transport implementation - request/response."""
        self.logger.info(f"[{self.get_name()}] Received request: {req}")
        # Create response
        resp = TLMTransaction()
        resp.data = req.data + 1
        await Timer(10, units="ns")
        self.logger.info(f"[{self.get_name()}] Sending response: {resp}")
        return resp


# TLM FIFO Example
class FIFOProducer(uvm_component):
    """Component producing to TLM FIFO."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building FIFOProducer")
        self.put_port = uvm_put_port("put_port", self)
    
    async def run_phase(self):
        self.raise_objection()
        for i in range(5):
            txn = TLMTransaction()
            txn.data = i * 0x30
            self.logger.info(f"[{self.get_name()}] Producing to FIFO: {txn}")
            await self.put_port.put(txn)
        self.drop_objection()


class FIFOConsumer(uvm_component):
    """Component consuming from TLM FIFO."""
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building FIFOConsumer")
        self.get_port = uvm_get_port("get_port", self)
    
    async def run_phase(self):
        self.raise_objection()
        for i in range(5):
            txn = await self.get_port.get()
            if txn:
                self.logger.info(f"[{self.get_name()}] Consuming from FIFO: {txn}")
        self.drop_objection()


class TLMEnv(uvm_env):
    """Environment demonstrating TLM connections."""
    
    def build_phase(self):
        self.logger.info("Building TLMEnv")
        # Put interface components
        self.put_producer = PutProducer.create("put_producer", self)
        self.put_consumer = PutConsumer.create("put_consumer", self)
        
        # Get interface components
        self.get_producer = GetProducer.create("get_producer", self)
        self.get_consumer = GetConsumer.create("get_consumer", self)
        
        # Transport interface components
        self.transport_comp = TransportComponent.create("transport_comp", self)
        
        # FIFO components
        self.fifo = uvm_tlm_fifo("fifo", self)
        self.fifo_producer = FIFOProducer.create("fifo_producer", self)
        self.fifo_consumer = FIFOConsumer.create("fifo_consumer", self)
    
    def connect_phase(self):
        self.logger.info("Connecting TLMEnv")
        # Connect put interface
        self.put_producer.put_port.connect(self.put_consumer.put_export)
        
        # Connect get interface
        self.get_consumer.get_port.connect(self.get_producer.get_export)
        
        # Connect FIFO
        self.fifo_producer.put_port.connect(self.fifo.put_export)
        self.fifo_consumer.get_port.connect(self.fifo.get_export)


@uvm_test()
class TLMTest(uvm_test):
    """Test demonstrating TLM usage."""
    
    async def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("TLM Example Test")
        self.logger.info("=" * 60)
        self.env = TLMEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running TLM test")
        
        # Demonstrate transport
        self.logger.info("=" * 60)
        self.logger.info("Transport Interface Example:")
        req = TLMTransaction()
        req.data = 0xAA
        resp = await self.env.transport_comp.transport_port.transport(req)
        self.logger.info(f"Request: {req}, Response: {resp}")
        
        await Timer(100, units="ns")
        self.drop_objection()
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("TLM test completed")
        self.logger.info("=" * 60)


if __name__ == "__main__":
    print("This is a pyuvm TLM example.")
    print("To run with cocotb, use the Makefile in the test directory.")

