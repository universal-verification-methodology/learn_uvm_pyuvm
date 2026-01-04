"""
Module 8 Example 8.3: UVM Recorders
Demonstrates transaction recording for analysis.
"""

from pyuvm import *
import cocotb
from cocotb.triggers import Timer
# Explicitly import uvm_analysis_imp - it may not be exported by from pyuvm import *
# Try multiple possible import paths
_uvm_analysis_imp = None
try:
    # First try: check if it's in the namespace after from pyuvm import *
    _uvm_analysis_imp = globals()['uvm_analysis_imp']
except KeyError:
    # Second try: import from pyuvm module directly
    import pyuvm
    if hasattr(pyuvm, 'uvm_analysis_imp'):
        _uvm_analysis_imp = pyuvm.uvm_analysis_imp
    else:
        # Third try: try TLM module paths
        for module_name in ['s15_uvm_tlm_1', 's15_uvm_tlm', 's16_uvm_tlm_1', 's16_uvm_tlm']:
            try:
                tlm_module = __import__(f'pyuvm.{module_name}', fromlist=['uvm_analysis_imp'])
                if hasattr(tlm_module, 'uvm_analysis_imp'):
                    _uvm_analysis_imp = tlm_module.uvm_analysis_imp
                    break
            except (ImportError, AttributeError):
                continue

if _uvm_analysis_imp is not None:
    globals()['uvm_analysis_imp'] = _uvm_analysis_imp
import json
import cocotb
from datetime import datetime


class RecorderTransaction(uvm_sequence_item):
    """Transaction for recorder example."""
    
    def __init__(self, name="RecorderTransaction"):
        super().__init__(name)
        self.data = 0
        self.address = 0
        self.timestamp = 0
        self.transaction_id = 0
    
    def __str__(self):
        return f"id={self.transaction_id}, data=0x{self.data:02X}, addr=0x{self.address:04X}, ts={self.timestamp}"
    
    def to_dict(self):
        """Convert transaction to dictionary for recording."""
        return {
            'transaction_id': self.transaction_id,
            'data': hex(self.data),
            'address': hex(self.address),
            'timestamp': self.timestamp
        }


class TextRecorder(uvm_subscriber):
    """
    Text recorder for transactions.

    Records transactions to a text file.
    """

    def __init__(self, name="TextRecorder", parent=None, filename="transactions.txt"):
        super().__init__(name, parent)
        self.filename = filename
        self.recorded_count = 0
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building Text Recorder (file: {self.filename})")
        # Open file for writing
        self.file = open(self.filename, 'w')
        self.file.write(f"Transaction Recording Started: {datetime.now()}\n")
        self.file.write("=" * 60 + "\n")
    
    def write(self, txn):
        """Record transaction."""
        self.recorded_count += 1
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
        self.file.write(f"[{timestamp}] {txn}\n")
        self.logger.debug(f"[{self.get_name()}] Recorded: {txn}")
    
    def report_phase(self):
        """Report phase - close file."""
        self.file.write("=" * 60 + "\n")
        self.file.write(f"Transaction Recording Ended: {datetime.now()}\n")
        self.file.write(f"Total transactions recorded: {self.recorded_count}\n")
        self.file.close()
        self.logger.info(f"[{self.get_name()}] Recorded {self.recorded_count} transactions to {self.filename}")


class JSONRecorder(uvm_subscriber):
    """
    JSON recorder for transactions.

    Records transactions to a JSON file.
    """

    def __init__(self, name="JSONRecorder", parent=None, filename="transactions.json"):
        super().__init__(name, parent)
        self.filename = filename
        self.transactions = []
        self.recorded_count = 0
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building JSON Recorder (file: {self.filename})")
        self.start_time = datetime.now()
    
    def write(self, txn):
        """Record transaction."""
        self.recorded_count += 1
        record = txn.to_dict() if hasattr(txn, 'to_dict') else {'transaction': str(txn)}
        record['record_time'] = datetime.now().isoformat()
        self.transactions.append(record)
        self.logger.debug(f"[{self.get_name()}] Recorded: {txn}")
    
    def report_phase(self):
        """Report phase - write JSON file."""
        end_time = datetime.now()
        recording_data = {
            'start_time': self.start_time.isoformat(),
            'end_time': end_time.isoformat(),
            'total_transactions': self.recorded_count,
            'transactions': self.transactions
        }
        
        with open(self.filename, 'w') as f:
            json.dump(recording_data, f, indent=2)
        
        self.logger.info(f"[{self.get_name()}] Recorded {self.recorded_count} transactions to {self.filename}")


class TransactionDatabase(uvm_subscriber):
    """
    Transaction database for storing and querying transactions.

    In-memory database for transaction analysis.
    """

    def __init__(self, name="TransactionDatabase", parent=None):
        super().__init__(name, parent)
        self.database = []
        self.recorded_count = 0
    
    def build_phase(self):
        self.logger.info(f"[{self.get_name()}] Building Transaction Database")
    
    def write(self, txn):
        """Store transaction in database."""
        self.recorded_count += 1
        record = {
            'id': self.recorded_count,
            'transaction': txn.to_dict() if hasattr(txn, 'to_dict') else {'data': str(txn)},
            'timestamp': datetime.now().isoformat()
        }
        self.database.append(record)
        self.logger.debug(f"[{self.get_name()}] Stored: {txn}")
    
    def query(self, filter_func=None):
        """Query database with optional filter."""
        if filter_func:
            return [r for r in self.database if filter_func(r)]
        return self.database
    
    def report_phase(self):
        """Report phase - show database statistics."""
        self.logger.info(f"[{self.get_name()}] Database contains {len(self.database)} transactions")
        if len(self.database) > 0:
            self.logger.info(f"  First transaction: {self.database[0]['transaction']}")
            self.logger.info(f"  Last transaction: {self.database[-1]['transaction']}")


class RecorderEnv(uvm_env):
    """Environment demonstrating recorder usage."""
    
    def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Building Recorder Environment")
        self.logger.info("=" * 60)
        
        # Create multiple recorders
        self.text_recorder = TextRecorder.create("text_recorder", self)
        self.text_recorder.filename = "transactions.txt"
        self.json_recorder = JSONRecorder.create("json_recorder", self)
        self.json_recorder.filename = "transactions.json"
        self.database = TransactionDatabase.create("database", self)
        
        self.ap = uvm_analysis_port("ap", self)
    
    def connect_phase(self):
        self.logger.info("Connecting Recorder Environment")
        # Connect to all recorders
        self.ap.connect(self.text_recorder.analysis_export)
        self.ap.connect(self.json_recorder.analysis_export)
        self.ap.connect(self.database.analysis_export)


# Note: @uvm_test() decorator removed to avoid import-time TypeError
# Using cocotb test wrapper instead for compatibility with cocotb test discovery
class RecorderTest(uvm_test):
    """Test demonstrating recorder usage."""
    
    def build_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Recorder Example Test")
        self.logger.info("=" * 60)
        self.env = RecorderEnv.create("env", self)
    
    async def run_phase(self):
        self.raise_objection()
        self.logger.info("Running recorder test")
        
        # Generate and record transactions
        for i in range(10):
            txn = RecorderTransaction()
            txn.transaction_id = i
            txn.data = i * 0x10
            txn.address = i * 0x100
            txn.timestamp = i * 10
            
            self.env.ap.write(txn)
            await Timer(10, unit="ns")
        
        await Timer(50, unit="ns")
        self.drop_objection()
    
    def report_phase(self):
        self.logger.info("=" * 60)
        self.logger.info("Recorder test completed")
        self.logger.info("=" * 60)
        self.logger.info("Check generated files:")
        self.logger.info("  - transactions.txt (text format)")
        self.logger.info("  - transactions.json (JSON format)")


# Cocotb test function to run the pyuvm test
@cocotb.test()
async def test_recorder(dut):
    """Cocotb test wrapper for pyuvm test."""
    # Register the test class with uvm_root so run_test can find it
    if not hasattr(uvm_root(), 'm_uvm_test_classes'):
        uvm_root().m_uvm_test_classes = {}
    uvm_root().m_uvm_test_classes["RecorderTest"] = RecorderTest
    # Use uvm_root to run the test properly (executes all phases in hierarchy)
    await uvm_root().run_test("RecorderTest")


if __name__ == "__main__":
    print("This is a pyuvm recorder example.")
    print("To run with cocotb, use the Makefile in the test directory.")

