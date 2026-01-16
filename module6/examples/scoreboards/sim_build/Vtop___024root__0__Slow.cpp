// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"

VL_ATTR_COLD void Vtop___024root___eval_static(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_static\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__Vtrigprevexpr___TOP__axi4_lite_slave__DOT__ACLK__0 
        = vlSelfRef.axi4_lite_slave__DOT__ACLK;
    vlSelfRef.__Vtrigprevexpr___TOP__axi4_lite_slave__DOT__ARESETn__0 
        = vlSelfRef.axi4_lite_slave__DOT__ARESETn;
}

VL_ATTR_COLD void Vtop___024root___eval_initial(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_initial\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

VL_ATTR_COLD void Vtop___024root___eval_final(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_final\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
}

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__stl(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag);
#endif  // VL_DEBUG
VL_ATTR_COLD bool Vtop___024root___eval_phase__stl(Vtop___024root* vlSelf);

VL_ATTR_COLD void Vtop___024root___eval_settle(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_settle\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    IData/*31:0*/ __VstlIterCount;
    // Body
    __VstlIterCount = 0U;
    vlSelfRef.__VstlFirstIteration = 1U;
    do {
        if (VL_UNLIKELY(((0x00000064U < __VstlIterCount)))) {
#ifdef VL_DEBUG
            Vtop___024root___dump_triggers__stl(vlSelfRef.__VstlTriggered, "stl"s);
#endif
            VL_FATAL_MT("../../dut/protocols/axi4_lite_slave.v", 40, "", "Settle region did not converge after 100 tries");
        }
        __VstlIterCount = ((IData)(1U) + __VstlIterCount);
    } while (Vtop___024root___eval_phase__stl(vlSelf));
}

VL_ATTR_COLD void Vtop___024root___eval_triggers__stl(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_triggers__stl\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    vlSelfRef.__VstlTriggered[0U] = ((0xfffffffffffffffeULL 
                                      & vlSelfRef.__VstlTriggered
                                      [0U]) | (IData)((IData)(vlSelfRef.__VstlFirstIteration)));
    vlSelfRef.__VstlFirstIteration = 0U;
#ifdef VL_DEBUG
    if (VL_UNLIKELY(vlSymsp->_vm_contextp__->debug())) {
        Vtop___024root___dump_triggers__stl(vlSelfRef.__VstlTriggered, "stl"s);
    }
#endif
}

VL_ATTR_COLD bool Vtop___024root___trigger_anySet__stl(const VlUnpacked<QData/*63:0*/, 1> &in);

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__stl(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__stl\n"); );
    // Body
    if ((1U & (~ (IData)(Vtop___024root___trigger_anySet__stl(triggers))))) {
        VL_DBG_MSGS("         No '" + tag + "' region triggers active\n");
    }
    if ((1U & (IData)(triggers[0U]))) {
        VL_DBG_MSGS("         '" + tag + "' region trigger index 0 is active: Internal 'stl' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD bool Vtop___024root___trigger_anySet__stl(const VlUnpacked<QData/*63:0*/, 1> &in) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___trigger_anySet__stl\n"); );
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

VL_ATTR_COLD void Vtop___024root___eval_stl(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_stl\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    if ((1ULL & vlSelfRef.__VstlTriggered[0U])) {
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

VL_ATTR_COLD bool Vtop___024root___eval_phase__stl(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___eval_phase__stl\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Locals
    CData/*0:0*/ __VstlExecute;
    // Body
    Vtop___024root___eval_triggers__stl(vlSelf);
    __VstlExecute = Vtop___024root___trigger_anySet__stl(vlSelfRef.__VstlTriggered);
    if (__VstlExecute) {
        Vtop___024root___eval_stl(vlSelf);
    }
    return (__VstlExecute);
}

bool Vtop___024root___trigger_anySet__ico(const VlUnpacked<QData/*63:0*/, 1> &in);

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__ico(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__ico\n"); );
    // Body
    if ((1U & (~ (IData)(Vtop___024root___trigger_anySet__ico(triggers))))) {
        VL_DBG_MSGS("         No '" + tag + "' region triggers active\n");
    }
    if ((1U & (IData)(triggers[0U]))) {
        VL_DBG_MSGS("         '" + tag + "' region trigger index 0 is active: Internal 'ico' trigger - first iteration\n");
    }
}
#endif  // VL_DEBUG

bool Vtop___024root___trigger_anySet__act(const VlUnpacked<QData/*63:0*/, 1> &in);

#ifdef VL_DEBUG
VL_ATTR_COLD void Vtop___024root___dump_triggers__act(const VlUnpacked<QData/*63:0*/, 1> &triggers, const std::string &tag) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___dump_triggers__act\n"); );
    // Body
    if ((1U & (~ (IData)(Vtop___024root___trigger_anySet__act(triggers))))) {
        VL_DBG_MSGS("         No '" + tag + "' region triggers active\n");
    }
    if ((1U & (IData)(triggers[0U]))) {
        VL_DBG_MSGS("         '" + tag + "' region trigger index 0 is active: @(posedge axi4_lite_slave.ACLK)\n");
    }
    if ((1U & (IData)((triggers[0U] >> 1U)))) {
        VL_DBG_MSGS("         '" + tag + "' region trigger index 1 is active: @(negedge axi4_lite_slave.ARESETn)\n");
    }
}
#endif  // VL_DEBUG

VL_ATTR_COLD void Vtop___024root___ctor_var_reset(Vtop___024root* vlSelf) {
    VL_DEBUG_IF(VL_DBG_MSGF("+    Vtop___024root___ctor_var_reset\n"); );
    Vtop__Syms* const __restrict vlSymsp VL_ATTR_UNUSED = vlSelf->vlSymsp;
    auto& vlSelfRef = std::ref(*vlSelf).get();
    // Body
    const uint64_t __VscopeHash = VL_MURMUR64_HASH(vlSelf->vlNamep);
    vlSelf->ACLK = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 3034660589080906099ull);
    vlSelf->ARESETn = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 11625642876178449192ull);
    vlSelf->AWVALID = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 11750918698781911943ull);
    vlSelf->AWREADY = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 17297234574184235162ull);
    vlSelf->AWADDR = VL_SCOPED_RAND_RESET_I(32, __VscopeHash, 3704207311081907456ull);
    vlSelf->AWPROT = VL_SCOPED_RAND_RESET_I(3, __VscopeHash, 7076923066334087385ull);
    vlSelf->WVALID = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 9495255681580949789ull);
    vlSelf->WREADY = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 17076114656213402080ull);
    vlSelf->WDATA = VL_SCOPED_RAND_RESET_I(32, __VscopeHash, 13545846466767745629ull);
    vlSelf->WSTRB = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 17384056636743468383ull);
    vlSelf->BVALID = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 8367422369656964262ull);
    vlSelf->BREADY = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 18149121645282540317ull);
    vlSelf->BRESP = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 12793087776628502554ull);
    vlSelf->ARVALID = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 1896485211029909696ull);
    vlSelf->ARREADY = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 11936612248788037190ull);
    vlSelf->ARADDR = VL_SCOPED_RAND_RESET_I(32, __VscopeHash, 17761954141230437835ull);
    vlSelf->ARPROT = VL_SCOPED_RAND_RESET_I(3, __VscopeHash, 4622094218666349735ull);
    vlSelf->RVALID = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 5829902753712117520ull);
    vlSelf->RREADY = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 2085817933989443683ull);
    vlSelf->RDATA = VL_SCOPED_RAND_RESET_I(32, __VscopeHash, 4866321451055619796ull);
    vlSelf->RRESP = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 17082317525515500324ull);
    vlSelf->axi4_lite_slave__DOT__ACLK = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 3064556554388272116ull);
    vlSelf->axi4_lite_slave__DOT__ARESETn = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 9288383414069408872ull);
    vlSelf->axi4_lite_slave__DOT__AWVALID = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 6258793095501765650ull);
    vlSelf->axi4_lite_slave__DOT__AWREADY = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 16281233134493343396ull);
    vlSelf->axi4_lite_slave__DOT__AWADDR = VL_SCOPED_RAND_RESET_I(32, __VscopeHash, 8972882985743065186ull);
    vlSelf->axi4_lite_slave__DOT__AWPROT = VL_SCOPED_RAND_RESET_I(3, __VscopeHash, 9869756506787959736ull);
    vlSelf->axi4_lite_slave__DOT__WVALID = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 18168352935381733502ull);
    vlSelf->axi4_lite_slave__DOT__WREADY = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 3016007778758478713ull);
    vlSelf->axi4_lite_slave__DOT__WDATA = VL_SCOPED_RAND_RESET_I(32, __VscopeHash, 10529316179120149992ull);
    vlSelf->axi4_lite_slave__DOT__WSTRB = VL_SCOPED_RAND_RESET_I(4, __VscopeHash, 8808500256834480651ull);
    vlSelf->axi4_lite_slave__DOT__BVALID = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 9284935256251554695ull);
    vlSelf->axi4_lite_slave__DOT__BREADY = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 5054486302197025292ull);
    vlSelf->axi4_lite_slave__DOT__BRESP = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 9087902711421585238ull);
    vlSelf->axi4_lite_slave__DOT__ARVALID = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 14306260012427034008ull);
    vlSelf->axi4_lite_slave__DOT__ARREADY = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 12983612923460393443ull);
    vlSelf->axi4_lite_slave__DOT__ARADDR = VL_SCOPED_RAND_RESET_I(32, __VscopeHash, 5376445607231156176ull);
    vlSelf->axi4_lite_slave__DOT__ARPROT = VL_SCOPED_RAND_RESET_I(3, __VscopeHash, 18043364310262677454ull);
    vlSelf->axi4_lite_slave__DOT__RVALID = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 12995728839675915735ull);
    vlSelf->axi4_lite_slave__DOT__RREADY = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 9024601422434617660ull);
    vlSelf->axi4_lite_slave__DOT__RDATA = VL_SCOPED_RAND_RESET_I(32, __VscopeHash, 14931538133589772657ull);
    vlSelf->axi4_lite_slave__DOT__RRESP = VL_SCOPED_RAND_RESET_I(2, __VscopeHash, 8891484909249726633ull);
    for (int __Vi0 = 0; __Vi0 < 1024; ++__Vi0) {
        vlSelf->axi4_lite_slave__DOT__memory[__Vi0] = VL_SCOPED_RAND_RESET_I(32, __VscopeHash, 13574519678020883956ull);
    }
    vlSelf->axi4_lite_slave__DOT__write_state = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 13974991232865775285ull);
    vlSelf->axi4_lite_slave__DOT__read_state = VL_SCOPED_RAND_RESET_I(1, __VscopeHash, 14633322551774103212ull);
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__VstlTriggered[__Vi0] = 0;
    }
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__VicoTriggered[__Vi0] = 0;
    }
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__VactTriggered[__Vi0] = 0;
    }
    vlSelf->__Vtrigprevexpr___TOP__axi4_lite_slave__DOT__ACLK__0 = 0;
    vlSelf->__Vtrigprevexpr___TOP__axi4_lite_slave__DOT__ARESETn__0 = 0;
    for (int __Vi0 = 0; __Vi0 < 1; ++__Vi0) {
        vlSelf->__VnbaTriggered[__Vi0] = 0;
    }
}
