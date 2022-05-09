#include <cmath>

double** euler_scheme(double dh, double h0, double h1, double P0, double T0, double U) {
    int n = (h1 - h0) / dh + 1;
    double* P = new double[n];
    double* T = new double[n];
    double* L = new double[n];
    P[0] = P0;
    T[0] = T0;
    double Es0 = 6.1121 * exp((18.678 - T0 / 234.5) * (T0 / (T0 + 257.14)));
    double TK0 = T0 + 273.15;
    double r0 = U * Es0 / (P0 - U * Es0);
    L[0] = 9.7734 * (1.0 + 5420.3 * r0 / TK0) / (1.0 + 8400955.5 * r0 / (TK0 * TK0));
    for (int i = 1; i < n; i++) {
        double t = T[i - 1] - L[i - 1] * dh;
        double Es = 6.1121 * exp((18.678 - t / 234.5) * (t / (t + 257.14)));
        double TK = t + 273.15;
        T[i] = t;
        P[i] = P[i - 1] - dh * 34.171 * (P[i - 1] - 0.37776 * U * Es) / TK;
        double r = U * Es / (P[i] - U * Es);
        L[i] = 9.7734 * (1.0 + 5420.3 * r / TK) / (1.0 + 8400955.5 * r / (TK * TK));  
    }
    double** soln = new double* [3];
    soln[0] = P;
    soln[1] = T;
    soln[2] = L;
    return soln;
}