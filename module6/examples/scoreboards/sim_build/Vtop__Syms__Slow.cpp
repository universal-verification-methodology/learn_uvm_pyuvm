// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Symbol table implementation internals

#include "Vtop__pch.h"

Vtop__Syms::Vtop__Syms(VerilatedContext* contextp, const char* namep, Vtop* modelp)
    : VerilatedSyms{contextp}
    // Setup internal state of the Syms class
    , __Vm_modelp{modelp}
    // Setup top module instance
    , TOP{this, namep}
{
    // Check resources
    Verilated::stackCheck(274);
    // Setup sub module instances
    // Configure time unit / time precision
    _vm_contextp__->timeunit(-9);
    _vm_contextp__->timeprecision(-12);
    // Setup each module's pointers to their submodules
    // Setup each module's pointer back to symbol table (for public functions)
    TOP.__Vconfigure(true);
    // Setup scopes
    __Vscopep_TOP = new VerilatedScope{this, "TOP", "TOP", "<null>", 0, VerilatedScope::SCOPE_OTHER};
    __Vscopep_axi4_lite_slave = new VerilatedScope{this, "axi4_lite_slave", "axi4_lite_slave", "axi4_lite_slave", -9, VerilatedScope::SCOPE_MODULE};
    // Set up scope hierarchy
    __Vhier.add(0, __Vscopep_axi4_lite_slave);
    // Setup export functions - final: 0
    // Setup export functions - final: 1
    // Setup public variables
    __Vscopep_TOP->varInsert("ACLK", &(TOP.ACLK), false, VLVT_UINT8, VLVD_IN|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("ARADDR", &(TOP.ARADDR), false, VLVT_UINT32, VLVD_IN|VLVF_PUB_RW, 0, 1 ,31,0);
    __Vscopep_TOP->varInsert("ARESETn", &(TOP.ARESETn), false, VLVT_UINT8, VLVD_IN|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("ARPROT", &(TOP.ARPROT), false, VLVT_UINT8, VLVD_IN|VLVF_PUB_RW, 0, 1 ,2,0);
    __Vscopep_TOP->varInsert("ARREADY", &(TOP.ARREADY), false, VLVT_UINT8, VLVD_OUT|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("ARVALID", &(TOP.ARVALID), false, VLVT_UINT8, VLVD_IN|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("AWADDR", &(TOP.AWADDR), false, VLVT_UINT32, VLVD_IN|VLVF_PUB_RW, 0, 1 ,31,0);
    __Vscopep_TOP->varInsert("AWPROT", &(TOP.AWPROT), false, VLVT_UINT8, VLVD_IN|VLVF_PUB_RW, 0, 1 ,2,0);
    __Vscopep_TOP->varInsert("AWREADY", &(TOP.AWREADY), false, VLVT_UINT8, VLVD_OUT|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("AWVALID", &(TOP.AWVALID), false, VLVT_UINT8, VLVD_IN|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("BREADY", &(TOP.BREADY), false, VLVT_UINT8, VLVD_IN|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("BRESP", &(TOP.BRESP), false, VLVT_UINT8, VLVD_OUT|VLVF_PUB_RW, 0, 1 ,1,0);
    __Vscopep_TOP->varInsert("BVALID", &(TOP.BVALID), false, VLVT_UINT8, VLVD_OUT|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("RDATA", &(TOP.RDATA), false, VLVT_UINT32, VLVD_OUT|VLVF_PUB_RW, 0, 1 ,31,0);
    __Vscopep_TOP->varInsert("RREADY", &(TOP.RREADY), false, VLVT_UINT8, VLVD_IN|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("RRESP", &(TOP.RRESP), false, VLVT_UINT8, VLVD_OUT|VLVF_PUB_RW, 0, 1 ,1,0);
    __Vscopep_TOP->varInsert("RVALID", &(TOP.RVALID), false, VLVT_UINT8, VLVD_OUT|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("WDATA", &(TOP.WDATA), false, VLVT_UINT32, VLVD_IN|VLVF_PUB_RW, 0, 1 ,31,0);
    __Vscopep_TOP->varInsert("WREADY", &(TOP.WREADY), false, VLVT_UINT8, VLVD_OUT|VLVF_PUB_RW, 0, 0);
    __Vscopep_TOP->varInsert("WSTRB", &(TOP.WSTRB), false, VLVT_UINT8, VLVD_IN|VLVF_PUB_RW, 0, 1 ,3,0);
    __Vscopep_TOP->varInsert("WVALID", &(TOP.WVALID), false, VLVT_UINT8, VLVD_IN|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("ACLK", &(TOP.axi4_lite_slave__DOT__ACLK), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("ARADDR", &(TOP.axi4_lite_slave__DOT__ARADDR), false, VLVT_UINT32, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,31,0);
    __Vscopep_axi4_lite_slave->varInsert("ARESETn", &(TOP.axi4_lite_slave__DOT__ARESETn), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("ARPROT", &(TOP.axi4_lite_slave__DOT__ARPROT), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,2,0);
    __Vscopep_axi4_lite_slave->varInsert("ARREADY", &(TOP.axi4_lite_slave__DOT__ARREADY), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("ARVALID", &(TOP.axi4_lite_slave__DOT__ARVALID), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("AWADDR", &(TOP.axi4_lite_slave__DOT__AWADDR), false, VLVT_UINT32, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,31,0);
    __Vscopep_axi4_lite_slave->varInsert("AWPROT", &(TOP.axi4_lite_slave__DOT__AWPROT), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,2,0);
    __Vscopep_axi4_lite_slave->varInsert("AWREADY", &(TOP.axi4_lite_slave__DOT__AWREADY), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("AWVALID", &(TOP.axi4_lite_slave__DOT__AWVALID), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("BREADY", &(TOP.axi4_lite_slave__DOT__BREADY), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("BRESP", &(TOP.axi4_lite_slave__DOT__BRESP), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,1,0);
    __Vscopep_axi4_lite_slave->varInsert("BVALID", &(TOP.axi4_lite_slave__DOT__BVALID), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("RDATA", &(TOP.axi4_lite_slave__DOT__RDATA), false, VLVT_UINT32, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,31,0);
    __Vscopep_axi4_lite_slave->varInsert("READ_DATA", const_cast<void*>(static_cast<const void*>(&(TOP.axi4_lite_slave__DOT__READ_DATA))), true, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,0,0);
    __Vscopep_axi4_lite_slave->varInsert("READ_IDLE", const_cast<void*>(static_cast<const void*>(&(TOP.axi4_lite_slave__DOT__READ_IDLE))), true, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,0,0);
    __Vscopep_axi4_lite_slave->varInsert("RREADY", &(TOP.axi4_lite_slave__DOT__RREADY), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("RRESP", &(TOP.axi4_lite_slave__DOT__RRESP), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,1,0);
    __Vscopep_axi4_lite_slave->varInsert("RVALID", &(TOP.axi4_lite_slave__DOT__RVALID), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("WDATA", &(TOP.axi4_lite_slave__DOT__WDATA), false, VLVT_UINT32, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,31,0);
    __Vscopep_axi4_lite_slave->varInsert("WREADY", &(TOP.axi4_lite_slave__DOT__WREADY), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("WRITE_DATA", const_cast<void*>(static_cast<const void*>(&(TOP.axi4_lite_slave__DOT__WRITE_DATA))), true, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,0,0);
    __Vscopep_axi4_lite_slave->varInsert("WRITE_IDLE", const_cast<void*>(static_cast<const void*>(&(TOP.axi4_lite_slave__DOT__WRITE_IDLE))), true, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,0,0);
    __Vscopep_axi4_lite_slave->varInsert("WSTRB", &(TOP.axi4_lite_slave__DOT__WSTRB), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 1 ,3,0);
    __Vscopep_axi4_lite_slave->varInsert("WVALID", &(TOP.axi4_lite_slave__DOT__WVALID), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("memory", &(TOP.axi4_lite_slave__DOT__memory), false, VLVT_UINT32, VLVD_NODIR|VLVF_PUB_RW, 1, 1 ,0,1023 ,31,0);
    __Vscopep_axi4_lite_slave->varInsert("read_state", &(TOP.axi4_lite_slave__DOT__read_state), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
    __Vscopep_axi4_lite_slave->varInsert("write_state", &(TOP.axi4_lite_slave__DOT__write_state), false, VLVT_UINT8, VLVD_NODIR|VLVF_PUB_RW, 0, 0);
}

Vtop__Syms::~Vtop__Syms() {
    // Tear down scope hierarchy
    __Vhier.remove(0, __Vscopep_axi4_lite_slave);
    // Clear keys from hierarchy map after values have been removed
    __Vhier.clear();
    // Tear down scopes
    VL_DO_CLEAR(delete __Vscopep_TOP, __Vscopep_TOP = nullptr);
    VL_DO_CLEAR(delete __Vscopep_axi4_lite_slave, __Vscopep_axi4_lite_slave = nullptr);
    // Tear down sub module instances
}
