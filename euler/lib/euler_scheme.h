#pragma once

#if defined(_MSC_VER)
    #define IMPORT __declspec(dllimport)
#elif defined(__GNUC__)
    #define IMPORT
#endif

extern "C" IMPORT double** euler_scheme(double dh, double h0, double h1, double P0, double T0, double U);