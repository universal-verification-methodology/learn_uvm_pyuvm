// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag);
#endif  // VL_DEBUG

void Vtop___024root___eval_triggers__ico(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_triggers__ico\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VicoTriggered[0U] = ((0xfffffffffffffffeULL 
                                      & vlSelfRef.__VicoTriggered
                                      [0U]) | (IData)((IData)(vlSelfRef.__VicoFirstIteration)));
    vlSelfRef.__VicoFirstIteration = 0U;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop___024root___dump_triggers__ico(vlSelfRef.__VicoTriggered, "ico"s);
    }
#endif
}

bool Vtop___024root___trigger_anySet__ico(const VlUnpacked<QData/*63:0*/, 1> &in) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_anySet__ico\n"); );
    // Locals
    IData/*31:0*/ n;
    // Body
    n = 0U;
    do {
        if (in[n]) {
            return (1U);
        }
        n = ((IData)(1U) + n);
    } while ((1U > n));
    return (0U);
}

void Vtop___024root___ico_sequent__TOP__0(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ico_sequent__TOP__0\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.axi4_lite_slave__DOT__ACLK = vlSelfRef.ACLK;
    vlSelfRef.axi4_lite_slave__DOT__ARESETn = vlSelfRef.ARESETn;
    vlSelfRef.axi4_lite_slave__DOT__AWVALID = vlSelfRef.AWVALID;
    vlSelfRef.AWREADY = vlSelfRef.axi4_lite_slave__DOT__AWREADY;
    vlSelfRef.axi4_lite_slave__DOT__AWADDR = vlSelfRef.AWADDR;
    vlSelfRef.axi4_lite_slave__DOT__AWPROT = vlSelfRef.AWPROT;
    vlSelfRef.axi4_lite_slave__DOT__WVALID = vlSelfRef.WVALID;
    vlSelfRef.WREADY = vlSelfRef.axi4_lite_slave__DOT__WREADY;
    vlSelfRef.axi4_lite_slave__DOT__WDATA = vlSelfRef.WDATA;
    vlSelfRef.axi4_lite_slave__DOT__WSTRB = vlSelfRef.WSTRB;
    vlSelfRef.BVALID = vlSelfRef.axi4_lite_slave__DOT__BVALID;
    vlSelfRef.axi4_lite_slave__DOT__BREADY = vlSelfRef.BREADY;
    vlSelfRef.BRESP = vlSelfRef.axi4_lite_slave__DOT__BRESP;
    vlSelfRef.axi4_lite_slave__DOT__ARVALID = vlSelfRef.ARVALID;
    vlSelfRef.ARREADY = vlSelfRef.axi4_lite_slave__DOT__ARREADY;
    vlSelfRef.axi4_lite_slave__DOT__ARADDR = vlSelfRef.ARADDR;
    vlSelfRef.axi4_lite_slave__DOT__ARPROT = vlSelfRef.ARPROT;
    vlSelfRef.RVALID = vlSelfRef.axi4_lite_slave__DOT__RVALID;
    vlSelfRef.axi4_lite_slave__DOT__RREADY = vlSelfRef.RREADY;
    vlSelfRef.RDATA = vlSelfRef.axi4_lite_slave__DOT__RDATA;
    vlSelfRef.RRESP = vlSelfRef.axi4_lite_slave__DOT__RRESP;
}

void Vtop___024root___eval_ico(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_ico\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VicoTriggered[0U])) {
        vlSelfRef.axi4_lite_slave__DOT__ACLK = vlSelfRef.ACLK;
        vlSelfRef.axi4_lite_slave__DOT__ARESETn = vlSelfRef.ARESETn;
        vlSelfRef.axi4_lite_slave__DOT__AWVALID = vlSelfRef.AWVALID;
        vlSelfRef.AWREADY = vlSelfRef.axi4_lite_slave__DOT__AWREADY;
        vlSelfRef.axi4_lite_slave__DOT__AWADDR = vlSelfRef.AWADDR;
        vlSelfRef.axi4_lite_slave__DOT__AWPROT = vlSelfRef.AWPROT;
        vlSelfRef.axi4_lite_slave__DOT__WVALID = vlSelfRef.WVALID;
        vlSelfRef.WREADY = vlSelfRef.axi4_lite_slave__DOT__WREADY;
        vlSelfRef.axi4_lite_slave__DOT__WDATA = vlSelfRef.WDATA;
        vlSelfRef.axi4_lite_slave__DOT__WSTRB = vlSelfRef.WSTRB;
        vlSelfRef.BVALID = vlSelfRef.axi4_lite_slave__DOT__BVALID;
        vlSelfRef.axi4_lite_slave__DOT__BREADY = vlSelfRef.BREADY;
        vlSelfRef.BRESP = vlSelfRef.axi4_lite_slave__DOT__BRESP;
        vlSelfRef.axi4_lite_slave__DOT__ARVALID = vlSelfRef.ARVALID;
        vlSelfRef.ARREADY = vlSelfRef.axi4_lite_slave__DOT__ARREADY;
        vlSelfRef.axi4_lite_slave__DOT__ARADDR = vlSelfRef.ARADDR;
        vlSelfRef.axi4_lite_slave__DOT__ARPROT = vlSelfRef.ARPROT;
        vlSelfRef.RVALID = vlSelfRef.axi4_lite_slave__DOT__RVALID;
        vlSelfRef.axi4_lite_slave__DOT__RREADY = vlSelfRef.RREADY;
        vlSelfRef.RDATA = vlSelfRef.axi4_lite_slave__DOT__RDATA;
        vlSelfRef.RRESP = vlSelfRef.axi4_lite_slave__DOT__RRESP;
    }
}

bool Vtop___024root___eval_phase__ico(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__ico\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    CData/*0:0*/ __VicoExecute;
    // Body
    Vtop___024root___eval_triggers__ico(vlSelf);
    __VicoExecute = Vtop___024root___trigger_anySet__ico(vlSelfRef.__VicoTriggered);
    if (__VicoExecute) {
        Vtop___024root___eval_ico(vlSelf);
    }
    return (__VicoExecute);
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__act(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag);
#endif  // VL_DEBUG

void Vtop___024root___eval_triggers__act(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_triggers__act\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VactTriggered[0U] = (QData)((IData)(
                                                    ((((~ (IData)(vlSelfRef.axi4_lite_slave__DOT__ARESETn)) 
                                                       & (IData)(vlSelfRef.__Vtrigprevexpr___TOP__axi4_lite_slave__DOT__ARESETn__0)) 
                                                      << 1U) 
                                                     | ((IData)(vlSelfRef.axi4_lite_slave__DOT__ACLK) 
                                                        & (~ (IData)(vlSelfRef.__Vtrigprevexpr___TOP__axi4_lite_slave__DOT__ACLK__0))))));
    vlSelfRef.__Vtrigprevexpr___TOP__axi4_lite_slave__DOT__ACLK__0 
        = vlSelfRef.axi4_lite_slave__DOT__ACLK;
    vlSelfRef.__Vtrigprevexpr___TOP__axi4_lite_slave__DOT__ARESETn__0 
        = vlSelfRef.axi4_lite_slave__DOT__ARESETn;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop___024root___dump_triggers__act(vlSelfRef.__VactTriggered, "act"s);
    }
#endif
}

bool Vtop___024root___trigger_anySet__act(const VlUnpacked<QData/*63:0*/, 1> &in) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_anySet__act\n"); );
    // Locals
    IData/*31:0*/ n;
    // Body
    n = 0U;
    do {
        if (in[n]) {
            return (1U);
        }
        n = ((IData)(1U) + n);
    } while ((1U > n));
    return (0U);
}

void Vtop___024root___nba_sequent__TOP__0(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___nba_sequent__TOP__0\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    CData/*0:0*/ __Vdly__axi4_lite_slave__DOT__write_state;
    __Vdly__axi4_lite_slave__DOT__write_state = 0;
    CData/*0:0*/ __Vdly__axi4_lite_slave__DOT__WREADY;
    __Vdly__axi4_lite_slave__DOT__WREADY = 0;
    CData/*0:0*/ __Vdly__axi4_lite_slave__DOT__BVALID;
    __Vdly__axi4_lite_slave__DOT__BVALID = 0;
    CData/*0:0*/ __Vdly__axi4_lite_slave__DOT__read_state;
    __Vdly__axi4_lite_slave__DOT__read_state = 0;
    CData/*0:0*/ __Vdly__axi4_lite_slave__DOT__RVALID;
    __Vdly__axi4_lite_slave__DOT__RVALID = 0;
    IData/*31:0*/ __VdlyVal__axi4_lite_slave__DOT__memory__v0;
    __VdlyVal__axi4_lite_slave__DOT__memory__v0 = 0;
    SData/*9:0*/ __VdlyDim0__axi4_lite_slave__DOT__memory__v0;
    __VdlyDim0__axi4_lite_slave__DOT__memory__v0 = 0;
    CData/*0:0*/ __VdlySet__axi4_lite_slave__DOT__memory__v0;
    __VdlySet__axi4_lite_slave__DOT__memory__v0 = 0;
    // Body
    __Vdly__axi4_lite_slave__DOT__RVALID = vlSelfRef.axi4_lite_slave__DOT__RVALID;
    __VdlySet__axi4_lite_slave__DOT__memory__v0 = 0U;
    __Vdly__axi4_lite_slave__DOT__WREADY = vlSelfRef.axi4_lite_slave__DOT__WREADY;
    __Vdly__axi4_lite_slave__DOT__BVALID = vlSelfRef.axi4_lite_slave__DOT__BVALID;
    __Vdly__axi4_lite_slave__DOT__read_state = vlSelfRef.axi4_lite_slave__DOT__read_state;
    __Vdly__axi4_lite_slave__DOT__write_state = vlSelfRef.axi4_lite_slave__DOT__write_state;
    if (vlSelfRef.axi4_lite_slave__DOT__ARESETn) {
        if (((IData)(vlSelfRef.axi4_lite_slave__DOT__ARVALID) 
             & (~ (IData)(vlSelfRef.axi4_lite_slave__DOT__ARREADY)))) {
            vlSelfRef.axi4_lite_slave__DOT__ARREADY = 1U;
            __Vdly__axi4_lite_slave__DOT__read_state = 1U;
        } else {
            vlSelfRef.axi4_lite_slave__DOT__ARREADY = 0U;
        }
        if (((IData)(vlSelfRef.axi4_lite_slave__DOT__AWVALID) 
             & (~ (IData)(vlSelfRef.axi4_lite_slave__DOT__AWREADY)))) {
            vlSelfRef.axi4_lite_slave__DOT__AWREADY = 1U;
            __Vdly__axi4_lite_slave__DOT__write_state = 1U;
        } else {
            vlSelfRef.axi4_lite_slave__DOT__AWREADY = 0U;
        }
        if (((IData)(vlSelfRef.axi4_lite_slave__DOT__read_state) 
             & (~ (IData)(vlSelfRef.axi4_lite_slave__DOT__RVALID)))) {
            __Vdly__axi4_lite_slave__DOT__RVALID = 1U;
            vlSelfRef.axi4_lite_slave__DOT__RDATA = 
                vlSelfRef.axi4_lite_slave__DOT__memory
                [(0x000003ffU & (vlSelfRef.axi4_lite_slave__DOT__ARADDR 
                                 >> 2U))];
            vlSelfRef.axi4_lite_slave__DOT__RRESP = 0U;
        } else if (((IData)(vlSelfRef.axi4_lite_slave__DOT__RREADY) 
                    & (IData)(vlSelfRef.axi4_lite_slave__DOT__RVALID))) {
            __Vdly__axi4_lite_slave__DOT__RVALID = 0U;
            __Vdly__axi4_lite_slave__DOT__read_state = 0U;
        }
        if ((((IData)(vlSelfRef.axi4_lite_slave__DOT__write_state) 
              & (IData)(vlSelfRef.axi4_lite_slave__DOT__WVALID)) 
             & (~ (IData)(vlSelfRef.axi4_lite_slave__DOT__WREADY)))) {
            __Vdly__axi4_lite_slave__DOT__WREADY = 1U;
            __VdlyVal__axi4_lite_slave__DOT__memory__v0 
                = vlSelfRef.axi4_lite_slave__DOT__WDATA;
            __VdlyDim0__axi4_lite_slave__DOT__memory__v0 
                = (0x000003ffU & (vlSelfRef.axi4_lite_slave__DOT__AWADDR 
                                  >> 2U));
            __VdlySet__axi4_lite_slave__DOT__memory__v0 = 1U;
        } else {
            __Vdly__axi4_lite_slave__DOT__WREADY = 0U;
        }
        if (((IData)(vlSelfRef.axi4_lite_slave__DOT__WREADY) 
             & (IData)(vlSelfRef.axi4_lite_slave__DOT__WVALID))) {
            __Vdly__axi4_lite_slave__DOT__BVALID = 1U;
            vlSelfRef.axi4_lite_slave__DOT__BRESP = 0U;
        } else if (((IData)(vlSelfRef.axi4_lite_slave__DOT__BREADY) 
                    & (IData)(vlSelfRef.axi4_lite_slave__DOT__BVALID))) {
            __Vdly__axi4_lite_slave__DOT__BVALID = 0U;
            __Vdly__axi4_lite_slave__DOT__write_state = 0U;
        }
    } else {
        vlSelfRef.axi4_lite_slave__DOT__ARREADY = 0U;
        __Vdly__axi4_lite_slave__DOT__read_state = 0U;
        vlSelfRef.axi4_lite_slave__DOT__AWREADY = 0U;
        __Vdly__axi4_lite_slave__DOT__write_state = 0U;
        __Vdly__axi4_lite_slave__DOT__RVALID = 0U;
        vlSelfRef.axi4_lite_slave__DOT__RDATA = 0U;
        vlSelfRef.axi4_lite_slave__DOT__RRESP = 0U;
        __Vdly__axi4_lite_slave__DOT__WREADY = 0U;
        __Vdly__axi4_lite_slave__DOT__BVALID = 0U;
        vlSelfRef.axi4_lite_slave__DOT__BRESP = 0U;
    }
    vlSelfRef.axi4_lite_slave__DOT__read_state = __Vdly__axi4_lite_slave__DOT__read_state;
    vlSelfRef.axi4_lite_slave__DOT__RVALID = __Vdly__axi4_lite_slave__DOT__RVALID;
    vlSelfRef.axi4_lite_slave__DOT__write_state = __Vdly__axi4_lite_slave__DOT__write_state;
    if (__VdlySet__axi4_lite_slave__DOT__memory__v0) {
        vlSelfRef.axi4_lite_slave__DOT__memory[__VdlyDim0__axi4_lite_slave__DOT__memory__v0] 
            = __VdlyVal__axi4_lite_slave__DOT__memory__v0;
    }
    vlSelfRef.axi4_lite_slave__DOT__WREADY = __Vdly__axi4_lite_slave__DOT__WREADY;
    vlSelfRef.axi4_lite_slave__DOT__BVALID = __Vdly__axi4_lite_slave__DOT__BVALID;
    vlSelfRef.ARREADY = vlSelfRef.axi4_lite_slave__DOT__ARREADY;
    vlSelfRef.AWREADY = vlSelfRef.axi4_lite_slave__DOT__AWREADY;
    vlSelfRef.RVALID = vlSelfRef.axi4_lite_slave__DOT__RVALID;
    vlSelfRef.RDATA = vlSelfRef.axi4_lite_slave__DOT__RDATA;
    vlSelfRef.RRESP = vlSelfRef.axi4_lite_slave__DOT__RRESP;
    vlSelfRef.WREADY = vlSelfRef.axi4_lite_slave__DOT__WREADY;
    vlSelfRef.BVALID = vlSelfRef.axi4_lite_slave__DOT__BVALID;
    vlSelfRef.BRESP = vlSelfRef.axi4_lite_slave__DOT__BRESP;
}

void Vtop___024root___eval_nba(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_nba\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((3ULL & vlSelfRef.__VnbaTriggered[0U])) {
        Vtop___024root___nba_sequent__TOP__0(vlSelf);
    }
}

void Vtop___024root___trigger_orInto__act(VlUnpacked<QData/*63:0*/, 1> &out, const VlUnpacked<QData/*63:0*/, 1> &in) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_orInto__act\n"); );
    // Locals
    IData/*31:0*/ n;
    // Body
    n = 0U;
    do {
        out[n] = (out[n] | in[n]);
        n = ((IData)(1U) + n);
    } while ((1U > n));
}

bool Vtop___024root___eval_phase__act(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__act\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    Vtop___024root___eval_triggers__act(vlSelf);
    Vtop___024root___trigger_orInto__act(vlSelfRef.__VnbaTriggered, vlSelfRef.__VactTriggered);
    return (0U);
}

void Vtop___024root___trigger_clear__act(VlUnpacked<QData/*63:0*/, 1> &out) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_clear__act\n"); );
    // Locals
    IData/*31:0*/ n;
    // Body
    n = 0U;
    do {
        out[n] = 0ULL;
        n = ((IData)(1U) + n);
    } while ((1U > n));
}

bool Vtop___024root___eval_phase__nba(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__nba\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    CData/*0:0*/ __VnbaExecute;
    // Body
    __VnbaExecute = Vtop___024root___trigger_anySet__act(vlSelfRef.__VnbaTriggered);
    if (__VnbaExecute) {
        Vtop___024root___eval_nba(vlSelf);
        Vtop___024root___trigger_clear__act(vlSelfRef.__VnbaTriggered);
    }
    return (__VnbaExecute);
}

void Vtop___024root___eval(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    IData/*31:0*/ __VicoIterCount;
    IData/*31:0*/ __VnbaIterCount;
    // Body
    __VicoIterCount = 0U;
    vlSelfRef.__VicoFirstIteration = 1U;
    do {
        if (VL_UNLIKELY(((0x00000064U < __VicoIterCount)))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__ico(vlSelfRef.__VicoTriggered, "ico"s);
#endif
            VL_FATAL_MT("../../dut/protocols/axi4_lite_slave.v", 40, "", "Input combinational region did not converge after 100 tries");
        }
        __VicoIterCount = ((IData)(1U) + __VicoIterCount);
    } while (Vtop___024root___eval_phase__ico(vlSelf));
    __VnbaIterCount = 0U;
    do {
        if (VL_UNLIKELY(((0x00000064U < __VnbaIterCount)))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__act(vlSelfRef.__VnbaTriggered, "nba"s);
#endif
            VL_FATAL_MT("../../dut/protocols/axi4_lite_slave.v", 40, "", "NBA region did not converge after 100 tries");
        }
        __VnbaIterCount = ((IData)(1U) + __VnbaIterCount);
        vlSelfRef.__VactIterCount = 0U;
        do {
            if (VL_UNLIKELY(((0x00000064U < vlSelfRef.__VactIterCount)))) {
#ifdef VL_DEBUG
                Vtop___024root___dump_triggers__act(vlSelfRef.__VactTriggered, "act"s);
#endif
                VL_FATAL_MT("../../dut/protocols/axi4_lite_slave.v", 40, "", "Active region did not converge after 100 tries");
            }
            vlSelfRef.__VactIterCount = ((IData)(1U) 
                                         + vlSelfRef.__VactIterCount);
        } while (Vtop___024root___eval_phase__act(vlSelf));
    } while (Vtop___024root___eval_phase__nba(vlSelf));
}

#ifdef VL_DEBUG
void Vtop___024root___eval_debug_assertions(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_debug_assertions\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if (VL_UNLIKELY(((vlSelfRef.ACLK & 0xfeU)))) {
        Verilated::overWidthError("ACLK");
    }
    if (VL_UNLIKELY(((vlSelfRef.ARESETn & 0xfeU)))) {
        Verilated::overWidthError("ARESETn");
    }
    if (VL_UNLIKELY(((vlSelfRef.AWVALID & 0xfeU)))) {
        Verilated::overWidthError("AWVALID");
    }
    if (VL_UNLIKELY(((vlSelfRef.AWPROT & 0xf8U)))) {
        Verilated::overWidthError("AWPROT");
    }
    if (VL_UNLIKELY(((vlSelfRef.WVALID & 0xfeU)))) {
        Verilated::overWidthError("WVALID");
    }
    if (VL_UNLIKELY(((vlSelfRef.WSTRB & 0xf0U)))) {
        Verilated::overWidthError("WSTRB");
    }
    if (VL_UNLIKELY(((vlSelfRef.BREADY & 0xfeU)))) {
        Verilated::overWidthError("BREADY");
    }
    if (VL_UNLIKELY(((vlSelfRef.ARVALID & 0xfeU)))) {
        Verilated::overWidthError("ARVALID");
    }
    if (VL_UNLIKELY(((vlSelfRef.ARPROT & 0xf8U)))) {
        Verilated::overWidthError("ARPROT");
    }
    if (VL_UNLIKELY(((vlSelfRef.RREADY & 0xfeU)))) {
        Verilated::overWidthError("RREADY");
    }
}
#endif  // VL_DEBUG
