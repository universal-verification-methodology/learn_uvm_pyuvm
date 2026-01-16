// Verilated -*- C++ -*-
// DESCRIPTION: Verilator output: Design implementation internals
// See Vtop.h for the primary calling header

#include "Vtop__pch.h"

// Parameter definitions for Vtop___024root
constexpr CData/*0:0*/ Vtop___024root::axi4_lite_slave__DOT__WRITE_IDLE;
constexpr CData/*0:0*/ Vtop___024root::axi4_lite_slave__DOT__WRITE_DATA;
constexpr CData/*0:0*/ Vtop___024root::axi4_lite_slave__DOT__READ_IDLE;
constexpr CData/*0:0*/ Vtop___024root::axi4_lite_slave__DOT__READ_DATA;


void Vtop___024root___ctor_var_reset(Vtop___024root* vlSelf);

Vtop___024root::Vtop___024root(Vtop__Syms* symsp, const char* namep)
 {
    vlSymsp = symsp;
    vlNamep = strdup(namep);
    // Reset structure values
    Vtop___024root___ctor_var_reset(this);
}

void Vtop___024root::__Vconfigure(bool first) {
    (void)first;  // Prevent unused variable warning
}

Vtop___024root::~Vtop___024root() {
    VL_DO_DANGLING(std::free(const_cast<char*>(vlNamep)), vlNamep);
}
