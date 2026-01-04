"""
Module 2 Test: Shift Register
Testbench for shift_register module.
"""

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import Timer, RisingEdge


async def reset_dut(dut, duration_ns=50):
    """Reset the DUT."""
    dut.rst_n.value = 0
    dut.shift.value = 0
    dut.data_in.value = 0
    await Timer(duration_ns, units="ns")
    dut.rst_n.value = 1
    await Timer(10, units="ns")


@cocotb.test()
async def test_shift_register_reset(dut):
    """Test shift register reset."""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    await reset_dut(dut)
    
    assert dut.q.value.integer == 0, "Shift register should be reset"
    assert dut.data_out.value.integer == 0, "Data out should be reset"


@cocotb.test()
async def test_shift_register_operation(dut):
    """Test shift register shift operation."""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    await reset_dut(dut)
    dut.shift.value = 1
    
    # Shift in data
    test_data = [1, 0, 1, 1, 0, 1, 0, 0]
    
    for bit in test_data:
        dut.data_in.value = bit
        await RisingEdge(dut.clk)
        await Timer(1, units="ns")
    
    # Check final value
    expected = 0b10110100
    assert dut.q.value.integer == expected, \
        f"Expected 0b{expected:08b}, got 0b{dut.q.value.integer:08b}"


@cocotb.test()
async def test_shift_register_serial_out(dut):
    """Test shift register serial output."""
    clock = Clock(dut.clk, 10, units="ns")
    cocotb.start_soon(clock.start())
    
    await reset_dut(dut)
    
    # Load data
    dut.shift.value = 1
    for i in range(8):
        dut.data_in.value = (i % 2)
        await RisingEdge(dut.clk)
        await Timer(1, units="ns")
    
    # Shift out
    expected_bits = []
    for i in range(8):
        await RisingEdge(dut.clk)
        await Timer(1, units="ns")
        expected_bits.append(dut.data_out.value.integer)
    
    print(f"Serial output: {expected_bits}")

