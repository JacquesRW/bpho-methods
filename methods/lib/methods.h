#pragma once
#include <array>
// compilation to .dll on windows is weird 
// linux works fine of course
#if defined(_MSC_VER)
    #define EXPORT __declspec(dllexport)
    #define IMPORT __declspec(dllimport)
#elif defined(__GNUC__)
    #define EXPORT
    #define IMPORT
#endif

const double dh = 0.1;
const double P0 = 1013.25;
const double T0 = 15;
const int rk4_n = 111;
const int euler_n = 1101;

extern "C" IMPORT std::array<std::array<double,euler_n>,3> euler_scheme(double U);
extern "C" IMPORT std::array<std::array<double,rk4_n>,3> rk4_scheme(double U);