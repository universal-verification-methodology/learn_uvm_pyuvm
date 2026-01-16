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
    vlSelfRef.simple_dma__DOT__clk = vlSelfRef.clk;
    vlSelfRef.simple_dma__DOT__rst_n = vlSelfRef.rst_n;
    vlSelfRef.simple_dma__DOT__dma_start = vlSelfRef.dma_start;
    vlSelfRef.dma_done = vlSelfRef.simple_dma__DOT__dma_done;
    vlSelfRef.simple_dma__DOT__dma_src_addr = vlSelfRef.dma_src_addr;
    vlSelfRef.simple_dma__DOT__dma_dst_addr = vlSelfRef.dma_dst_addr;
    vlSelfRef.simple_dma__DOT__dma_length = vlSelfRef.dma_length;
    vlSelfRef.simple_dma__DOT__dma_channel = vlSelfRef.dma_channel;
}

void Vtop___024root___eval_ico(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_ico\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VicoTriggered[0U])) {
        vlSelfRef.simple_dma__DOT__clk = vlSelfRef.clk;
        vlSelfRef.simple_dma__DOT__rst_n = vlSelfRef.rst_n;
        vlSelfRef.simple_dma__DOT__dma_start = vlSelfRef.dma_start;
        vlSelfRef.dma_done = vlSelfRef.simple_dma__DOT__dma_done;
        vlSelfRef.simple_dma__DOT__dma_src_addr = vlSelfRef.dma_src_addr;
        vlSelfRef.simple_dma__DOT__dma_dst_addr = vlSelfRef.dma_dst_addr;
        vlSelfRef.simple_dma__DOT__dma_length = vlSelfRef.dma_length;
        vlSelfRef.simple_dma__DOT__dma_channel = vlSelfRef.dma_channel;
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
                                                    ((((~ (IData)(vlSelfRef.simple_dma__DOT__rst_n)) 
                                                       & (IData)(vlSelfRef.__Vtrigprevexpr___TOP__simple_dma__DOT__rst_n__0)) 
                                                      << 1U) 
                                                     | ((IData)(vlSelfRef.simple_dma__DOT__clk) 
                                                        & (~ (IData)(vlSelfRef.__Vtrigprevexpr___TOP__simple_dma__DOT__clk__0))))));
    vlSelfRef.__Vtrigprevexpr___TOP__simple_dma__DOT__clk__0 
        = vlSelfRef.simple_dma__DOT__clk;
    vlSelfRef.__Vtrigprevexpr___TOP__simple_dma__DOT__rst_n__0 
        = vlSelfRef.simple_dma__DOT__rst_n;
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
    SData/*15:0*/ __Vdly__simple_dma__DOT__length_reg;
    __Vdly__simple_dma__DOT__length_reg = 0;
    SData/*15:0*/ __Vdly__simple_dma__DOT__count;
    __Vdly__simple_dma__DOT__count = 0;
    // Body
    __Vdly__simple_dma__DOT__length_reg = vlSelfRef.simple_dma__DOT__length_reg;
    __Vdly__simple_dma__DOT__count = vlSelfRef.simple_dma__DOT__count;
    if (vlSelfRef.simple_dma__DOT__rst_n) {
        if (((IData)(vlSelfRef.simple_dma__DOT__dma_start) 
             & (~ (IData)(vlSelfRef.simple_dma__DOT__dma_done)))) {
            vlSelfRef.simple_dma__DOT__src_addr_reg 
                = vlSelfRef.simple_dma__DOT__dma_src_addr;
            vlSelfRef.simple_dma__DOT__dst_addr_reg 
                = vlSelfRef.simple_dma__DOT__dma_dst_addr;
            __Vdly__simple_dma__DOT__length_reg = vlSelfRef.simple_dma__DOT__dma_length;
            vlSelfRef.simple_dma__DOT__channel_reg 
                = vlSelfRef.simple_dma__DOT__dma_channel;
            __Vdly__simple_dma__DOT__count = 0U;
        } else if (vlSelfRef.simple_dma__DOT__dma_done) {
            vlSelfRef.simple_dma__DOT__dma_done = 0U;
        } else if (((IData)(vlSelfRef.simple_dma__DOT__count) 
                    < (IData)(vlSelfRef.simple_dma__DOT__length_reg))) {
            __Vdly__simple_dma__DOT__count = (0x0000ffffU 
                                              & ((IData)(1U) 
                                                 + (IData)(vlSelfRef.simple_dma__DOT__count)));
        } else {
            vlSelfRef.simple_dma__DOT__dma_done = 1U;
        }
    } else {
        vlSelfRef.simple_dma__DOT__dma_done = 0U;
        vlSelfRef.simple_dma__DOT__src_addr_reg = 0U;
        vlSelfRef.simple_dma__DOT__dst_addr_reg = 0U;
        __Vdly__simple_dma__DOT__length_reg = 0U;
        vlSelfRef.simple_dma__DOT__channel_reg = 0U;
        __Vdly__simple_dma__DOT__count = 0U;
    }
    vlSelfRef.simple_dma__DOT__length_reg = __Vdly__simple_dma__DOT__length_reg;
    vlSelfRef.simple_dma__DOT__count = __Vdly__simple_dma__DOT__count;
    vlSelfRef.dma_done = vlSelfRef.simple_dma__DOT__dma_done;
}

void Vtop___024root___eval_nba(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_nba\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    SData/*15:0*/ __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__length_reg;
    __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__length_reg = 0;
    SData/*15:0*/ __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__count;
    __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__count = 0;
    // Body
    if ((3ULL & vlSelfRef.__VnbaTriggered[0U])) {
        __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__length_reg 
            = vlSelfRef.simple_dma__DOT__length_reg;
        __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__count 
            = vlSelfRef.simple_dma__DOT__count;
        if (vlSelfRef.simple_dma__DOT__rst_n) {
            if (((IData)(vlSelfRef.simple_dma__DOT__dma_start) 
                 & (~ (IData)(vlSelfRef.simple_dma__DOT__dma_done)))) {
                vlSelfRef.simple_dma__DOT__src_addr_reg 
                    = vlSelfRef.simple_dma__DOT__dma_src_addr;
                vlSelfRef.simple_dma__DOT__dst_addr_reg 
                    = vlSelfRef.simple_dma__DOT__dma_dst_addr;
                __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__length_reg 
                    = vlSelfRef.simple_dma__DOT__dma_length;
                vlSelfRef.simple_dma__DOT__channel_reg 
                    = vlSelfRef.simple_dma__DOT__dma_channel;
                __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__count = 0U;
            } else if (vlSelfRef.simple_dma__DOT__dma_done) {
                vlSelfRef.simple_dma__DOT__dma_done = 0U;
            } else if (((IData)(vlSelfRef.simple_dma__DOT__count) 
                        < (IData)(vlSelfRef.simple_dma__DOT__length_reg))) {
                __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__count 
                    = (0x0000ffffU & ((IData)(1U) + (IData)(vlSelfRef.simple_dma__DOT__count)));
            } else {
                vlSelfRef.simple_dma__DOT__dma_done = 1U;
            }
        } else {
            vlSelfRef.simple_dma__DOT__dma_done = 0U;
            vlSelfRef.simple_dma__DOT__src_addr_reg = 0U;
            vlSelfRef.simple_dma__DOT__dst_addr_reg = 0U;
            __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__length_reg = 0U;
            vlSelfRef.simple_dma__DOT__channel_reg = 0U;
            __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__count = 0U;
        }
        vlSelfRef.simple_dma__DOT__length_reg = __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__length_reg;
        vlSelfRef.simple_dma__DOT__count = __Vinline__nba_sequent__TOP__0___Vdly__simple_dma__DOT__count;
        vlSelfRef.dma_done = vlSelfRef.simple_dma__DOT__dma_done;
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
            VL_FATAL_MT("../../dut/dma/simple_dma.v", 17, "", "Input combinational region did not converge after 100 tries");
        }
        __VicoIterCount = ((IData)(1U) + __VicoIterCount);
    } while (Vtop___024root___eval_phase__ico(vlSelf));
    __VnbaIterCount = 0U;
    do {
        if (VL_UNLIKELY(((0x00000064U < __VnbaIterCount)))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__act(vlSelfRef.__VnbaTriggered, "nba"s);
#endif
            VL_FATAL_MT("../../dut/dma/simple_dma.v", 17, "", "NBA region did not converge after 100 tries");
        }
        __VnbaIterCount = ((IData)(1U) + __VnbaIterCount);
        vlSelfRef.__VactIterCount = 0U;
        do {
            if (VL_UNLIKELY(((0x00000064U < vlSelfRef.__VactIterCount)))) {
#ifdef VL_DEBUG
                Vtop___024root___dump_triggers__act(vlSelfRef.__VactTriggered, "act"s);
#endif
                VL_FATAL_MT("../../dut/dma/simple_dma.v", 17, "", "Active region did not converge after 100 tries");
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
    if (VL_UNLIKELY(((vlSelfRef.clk & 0xfeU)))) {
        Verilated::overWidthError("clk");
    }
    if (VL_UNLIKELY(((vlSelfRef.rst_n & 0xfeU)))) {
        Verilated::overWidthError("rst_n");
    }
    if (VL_UNLIKELY(((vlSelfRef.dma_start & 0xfeU)))) {
        Verilated::overWidthError("dma_start");
    }
    if (VL_UNLIKELY(((vlSelfRef.dma_channel & 0xf8U)))) {
        Verilated::overWidthError("dma_channel");
    }
}
#endif  // VL_DEBUG
