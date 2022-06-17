#pragma once
#include <vector>
// compilation to .dll on windows is weird 
// linux works fine of course
#if defined(_MSC_VER)
    #define EXPORT __declspec(dllexport)
    #define IMPORT __declspec(dllimport)
#elif defined(__GNUC__)
    #define EXPORT
    #define IMPORT
#endif

extern "C" IMPORT std::vector<std::vector<double>> euler_scheme(double dh, double h, double P0, double T0, double U);
extern "C" IMPORT std::vector<std::vector<double>> rk4_scheme(double dh, double h, double P0, double T0, double U);