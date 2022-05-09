#include "methods.h"
#include <iostream>
#include <cmath>

double calc_Es(double T) {
    return 6.1121 * exp((18.678 - T / 234.5) * (T / (T + 257.14)));
}
double calc_L(double P, double UEs, double TK) {
    double r = UEs / (P - UEs);
    return 9.7734 * (TK + 5420.3 * r) / (TK * TK + 8400955.5 * r) * TK;
}
double calc_dP(double P, double UEs, double TK) {
    return -34.171 * (P - 0.37776 * UEs) / TK;
}

double** euler_scheme(double dh, double h0, double h1, double P0, double T0, double U) {
    int n = (h1 - h0) / dh + 1;
    double* P = new double[n];
    double* T = new double[n];
    double* L = new double[n];
    double t, UEs, TK;
    P[0] = P0;
    T[0] = T0;
    double UEs0 = U * calc_Es(T0);
    double TK0 = T0 + 273.15;
    L[0] = calc_L(P0, UEs0, TK0);
    for (int i = 1; i < n; i++) {
        t = T[i - 1] - L[i - 1] * dh;
        UEs = U * calc_Es(t);
        TK = t + 273.15;
        T[i] = t;
        P[i] = P[i - 1] + dh * calc_dP(P[i-1],UEs,TK);
        L[i] = calc_L(P[i],UEs,TK);  
    }
    double** soln = new double* [3];
    soln[0] = P;
    soln[1] = T;
    soln[2] = L;
    return soln;
}
double** rk4_scheme(double dh, double h0, double h1, double P0, double T0, double U) {
    int n = (h1 - h0) / dh + 1;
    double* P = new double[n];
    double* T = new double[n];
    double* L = new double[n];

    double t1,t2,t3,t4;
    double p1,p2,p3,p4;
    double UEs1,UEs2,UEs3,UEs4;
    double tk1,tk2,tk3,tk4;
    double k1,k2,k3,k4;
    double K1,K2,K3,K4;

    P[0] = P0;
    T[0] = T0;
    double UEs0 = U * calc_Es(T0);
    double TK0 = T0 + 273.15;
    L[0] = calc_L(P0, UEs0, TK0);

    for (int i = 1; i < n; i++) {
        p1 = P[i - 1];
        t1 = T[i - 1];
        UEs1 = U * calc_Es(t1);
        tk1 = t1 + 273.15;
        k1 = calc_L(p1, UEs1, tk1);
        K1 = calc_dP(p1, UEs1, tk1);

        t2 = t1 - dh * k1 / 2;
        p2 = p1 + dh * K1 / 2;
        UEs2 = U * calc_Es(t2);
        tk2 = t1 + 273.15;
        k2 = calc_L(p2, UEs2, tk2);
        K2 = calc_dP(p2, UEs2, tk2);

        t3 = t1 - dh * k2 / 2;
        p3 = p1 + dh * K2 / 2;
        UEs3 = U * calc_Es(t3);
        tk3 = t3 + 273.15;
        k3 = calc_L(p3, UEs3, tk3);
        K3 = calc_dP(p3, UEs3, tk3);

        t4 = t1 - dh * k3;
        p4 = p1 + dh * K3;
        UEs4 = U * calc_Es(t4);
        tk4 = t4 + 273.15;
        k4 = calc_L(p4, UEs4, tk4);
        K4 = calc_dP(p4, UEs4, tk4);

        T[i] = t1 - (k1 + 2 * k2 + 2 * k3 + k4) * dh / 6;
        P[i] = p1 + (K1 + 2 * K2 + 2 * K3 + K4) * dh / 6;
        L[i] = k1;  
    }
    double** soln = new double* [3];
    soln[0] = P;
    soln[1] = T;
    soln[2] = L;
    return soln;
}