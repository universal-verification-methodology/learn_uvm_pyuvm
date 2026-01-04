# Makefile for Module 3 pyuvm tests
# Usage: make SIM=verilator test_simple_uvm

# Default simulator
SIM ?= verilator

# Python files
PYTHON_FILES = test_simple_uvm.py

# Verilog files
VERILOG_FILES = ../../dut/simple_blocks/adder.v

# Test to run
TEST ?= test_simple_uvm

# Cocotb variables
MODULE = $(TEST)
TOPLEVEL = adder
COCOTB_REDUCED_LOG_FMT = 1

# Include cocotb makefile
include $(shell cocotb-config --makefiles)/Makefile.sim

.PHONY: clean
clean:
	rm -rf __pycache__
	rm -rf sim_build
	rm -rf results.xml
	rm -rf *.vcd
	rm -rf *.log

