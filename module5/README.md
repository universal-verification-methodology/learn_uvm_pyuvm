# Module 5: Advanced UVM Concepts

This directory contains all examples, exercises, and test cases for Module 5.

## Directory Structure

```
module5/
├── examples/              # pyuvm examples for each topic
│   ├── virtual_sequences/ # Virtual sequence examples
│   ├── coverage/          # Coverage model examples
│   ├── configuration/     # Configuration object examples
│   ├── callbacks/        # Callback examples
│   └── register_model/   # Register model examples
├── dut/                   # Verilog Design Under Test modules
│   └── advanced/          # Advanced modules for testing
├── tests/                 # Testbenches
│   └── pyuvm_tests/      # pyuvm testbenches
└── exercises/            # Exercise solutions
```

## Running Examples

Use the `module5.sh` script to run examples:

```bash
# Run all examples
./scripts/module5.sh

# Run specific examples
./scripts/module5.sh --virtual-sequences
./scripts/module5.sh --coverage
./scripts/module5.sh --configuration
./scripts/module5.sh --callbacks
./scripts/module5.sh --register-model
./scripts/module5.sh --pyuvm-tests
```

## Topics Covered

1. **Advanced Sequences** - Virtual sequences, sequence libraries, arbitration
2. **UVM Coverage Models** - Functional coverage, coverage implementation
3. **Complex Configuration** - Configuration objects, hierarchy, resource database
4. **UVM Callbacks** - Callback implementation, pre/post callbacks
5. **Register Model** - Advanced register model features
6. **Virtual Sequences** - Coordinating multiple sequencers
7. **Coverage Analysis** - Coverage collection and closure
8. **Advanced Configuration** - Configuration patterns and strategies
9. **Performance Optimization** - Testbench optimization
10. **Advanced Debugging** - Debugging techniques

