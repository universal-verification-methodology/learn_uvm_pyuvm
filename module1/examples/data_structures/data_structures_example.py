"""
Module 1: Data Structures for Verification
Demonstrates Python data structures useful for verification.
"""

from collections import deque, defaultdict, Counter, namedtuple
from typing import List, Dict, Any
import random


# Named tuple for transactions
Transaction = namedtuple('Transaction', ['id', 'address', 'data', 'timestamp'])


class TransactionQueue:
    """
    Transaction queue using deque.
    
    Demonstrates deque for FIFO/LIFO operations.
    """
    
    def __init__(self, maxsize: int = 100) -> None:
        """Initialize transaction queue."""
        self.queue: deque = deque(maxlen=maxsize)
        self._id_counter = 0
    
    def push(self, address: int, data: int) -> None:
        """Push transaction to queue."""
        self._id_counter += 1
        txn = Transaction(
            id=self._id_counter,
            address=address,
            data=data,
            timestamp=0
        )
        self.queue.append(txn)
    
    def pop(self) -> Transaction:
        """Pop transaction from queue (FIFO)."""
        return self.queue.popleft()
    
    def is_empty(self) -> bool:
        """Check if queue is empty."""
        return len(self.queue) == 0
    
    def size(self) -> int:
        """Get queue size."""
        return len(self.queue)


class Scoreboard:
    """
    Scoreboard for verification results.
    
    Demonstrates defaultdict and Counter.
    """
    
    def __init__(self) -> None:
        """Initialize scoreboard."""
        self.expected: Dict[int, int] = defaultdict(int)
        self.actual: Dict[int, int] = defaultdict(int)
        self.mismatches: List[tuple] = []
        self.match_count = Counter()
    
    def add_expected(self, address: int, data: int) -> None:
        """Add expected transaction."""
        self.expected[address] = data
    
    def add_actual(self, address: int, data: int) -> bool:
        """Add actual transaction and check."""
        self.actual[address] = data
        
        if address in self.expected:
            if self.expected[address] == data:
                self.match_count['matches'] += 1
                return True
            else:
                self.match_count['mismatches'] += 1
                self.mismatches.append((address, self.expected[address], data))
                return False
        else:
            self.match_count['unexpected'] += 1
            return False
    
    def get_statistics(self) -> Dict[str, Any]:
        """Get scoreboard statistics."""
        return {
            'matches': self.match_count['matches'],
            'mismatches': self.match_count['mismatches'],
            'unexpected': self.match_count['unexpected'],
            'mismatch_list': self.mismatches
        }


class CoverageCollector:
    """
    Coverage data collector.
    
    Demonstrates set and dictionary for coverage.
    """
    
    def __init__(self) -> None:
        """Initialize coverage collector."""
        self.covered_bins: Dict[str, set] = {}
        self.hit_counts: Dict[str, Counter] = {}
    
    def add_coverage(self, bin_name: str, value: Any) -> None:
        """Add coverage point."""
        if bin_name not in self.covered_bins:
            self.covered_bins[bin_name] = set()
            self.hit_counts[bin_name] = Counter()
        
        self.covered_bins[bin_name].add(value)
        self.hit_counts[bin_name][value] += 1
    
    def get_coverage(self, bin_name: str) -> float:
        """Get coverage percentage for a bin."""
        if bin_name not in self.covered_bins:
            return 0.0
        
        # Assume we know the total possible values
        # In practice, this would come from coverage model
        return len(self.covered_bins[bin_name]) / 10.0 * 100.0  # Example: 10 possible values
    
    def get_all_coverage(self) -> Dict[str, float]:
        """Get coverage for all bins."""
        return {bin_name: self.get_coverage(bin_name) 
                for bin_name in self.covered_bins.keys()}


def main() -> None:
    """Run data structures examples."""
    print("=" * 60)
    print("Module 1: Data Structures for Verification")
    print("=" * 60)
    print()
    
    # Example 1: Transaction Queue
    print("1. Transaction Queue (deque):")
    txn_queue = TransactionQueue(maxsize=10)
    for i in range(5):
        txn_queue.push(address=0x1000 + i, data=i * 2)
    print(f"   Queue size: {txn_queue.size()}")
    while not txn_queue.is_empty():
        txn = txn_queue.pop()
        print(f"   Popped: id={txn.id}, addr=0x{txn.address:X}, data=0x{txn.data:X}")
    print()
    
    # Example 2: Scoreboard
    print("2. Scoreboard (defaultdict, Counter):")
    scoreboard = Scoreboard()
    
    # Add expected transactions
    for i in range(5):
        scoreboard.add_expected(address=0x1000 + i, data=i * 2)
    
    # Add actual transactions (some match, some don't)
    for i in range(7):
        data = i * 2 if i < 5 else i * 3  # Mismatch for i >= 5
        scoreboard.add_actual(address=0x1000 + i, data=data)
    
    stats = scoreboard.get_statistics()
    print(f"   Matches: {stats['matches']}")
    print(f"   Mismatches: {stats['mismatches']}")
    print(f"   Unexpected: {stats['unexpected']}")
    if stats['mismatch_list']:
        print(f"   Mismatch details: {stats['mismatch_list']}")
    print()
    
    # Example 3: Coverage Collector
    print("3. Coverage Collector (set, Counter):")
    coverage = CoverageCollector()
    
    # Add coverage points
    for _ in range(20):
        bin_name = random.choice(['address', 'data', 'opcode'])
        value = random.randint(0, 9)
        coverage.add_coverage(bin_name, value)
    
    all_coverage = coverage.get_all_coverage()
    for bin_name, cov_percent in all_coverage.items():
        print(f"   {bin_name}: {cov_percent:.1f}% coverage")
        hit_counts = coverage.hit_counts[bin_name]
        print(f"      Unique values: {len(coverage.covered_bins[bin_name])}")
        print(f"      Total hits: {sum(hit_counts.values())}")
    print()
    
    # Example 4: List comprehensions
    print("4. List Comprehensions:")
    addresses = [0x1000 + i for i in range(10)]
    data_values = [i * 2 for i in range(10)]
    transactions = [Transaction(id=i, address=addr, data=data, timestamp=0)
                    for i, (addr, data) in enumerate(zip(addresses, data_values))]
    print(f"   Created {len(transactions)} transactions")
    print(f"   First transaction: {transactions[0]}")
    print()
    
    # Example 5: Dictionary comprehensions
    print("5. Dictionary Comprehensions:")
    address_to_data = {addr: data for addr, data in zip(addresses, data_values)}
    print(f"   Created address map with {len(address_to_data)} entries")
    print(f"   Sample: {dict(list(address_to_data.items())[:3])}")
    print()
    
    print("=" * 60)
    print("Example completed successfully!")
    print("=" * 60)


if __name__ == "__main__":
    main()

