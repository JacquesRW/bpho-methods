#define IMPORT_API __declspec(dllimport)

extern "C" IMPORT_API double** euler_scheme(double dh, double h0, double h1, double P0, double T0, double U);