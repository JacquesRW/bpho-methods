#include <iostream>
#include <cmath>
#include <array>

const double dh = 0.1;
const double P0 = 1013.25;
const double T0 = 15;
const int rk4_n = 111;

double calc_Es(double T) { return 6.1121 * exp((18.678 - T / 234.5) * (T / (T + 257.14))); }

double calc_L(double P, double UEs, double TK) {
    double r = UEs / (P - UEs);
    return 9.7734 * (TK + 5420.3 * r) / (TK * TK + 8400955.5 * r) * TK;
}

double calc_dP(double P, double UEs, double TK) { return -34.171 * (P - 0.37776 * UEs) / TK; }

std::array<double, rk4_n>* rk4_scheme(double U) {
    // heap allocations
    std::array<double, rk4_n>* soln = new std::array<double, rk4_n>[3];
    // stack allocations
    std::array<double, rk4_n> P, T, L;
    double t1, t2, t3, t4; // temperature
    double p1, p2, p3, p4; // pressure
    double UEs1, UEs2, UEs3, UEs4; // relative humidity
    double tk1, tk2, tk3, tk4; // temperature in kelvin
    double kt1, kt2, kt3, kt4; // temperature component of vector
    double kp1, kp2, kp3, kp4; // pressure component of vector
    // iniital conditions
    P[0] = P0;
    T[0] = T0;
    L[0] = calc_L(1013.25, U * calc_Es(T0), T0 + 273.15);
    // solving
    for (int i = 1; i < rk4_n; i++) {
        // first approximation
        p1 = P[i - 1];
        t1 = T[i - 1];
        UEs1 = U * calc_Es(t1);
        tk1 = t1 + 273.15;
        kt1 = calc_L(p1, UEs1, tk1);
        kp1 = calc_dP(p1, UEs1, tk1);
        // second approximation
        t2 = t1 - dh * kt1 / 2;
        p2 = p1 + dh * kp1 / 2;
        UEs2 = U * calc_Es(t2);
        tk2 = t2 + 273.15;
        kt2 = calc_L(p2, UEs2, tk2);
        kp2 = calc_dP(p2, UEs2, tk2);
        // third approximation
        t3 = t1 - dh * kt2 / 2;
        p3 = p1 + dh * kp2 / 2;
        UEs3 = U * calc_Es(t3);
        tk3 = t3 + 273.15;
        kt3 = calc_L(p3, UEs3, tk3);
        kp3 = calc_dP(p3, UEs3, tk3);
        // fourth approximation
        t4 = t1 - dh * kt3;
        p4 = p1 + dh * kp3;
        UEs4 = U * calc_Es(t4);
        tk4 = t4 + 273.15;
        kt4 = calc_L(p4, UEs4, tk4);
        kp4 = calc_dP(p4, UEs4, tk4);
        // weighted final approximation
        T[i] = t1 - (kt1 + 2 * kt2 + 2 * kt3 + kt4) * dh / 6;
        P[i] = p1 + (kp1 + 2 * kp2 + 2 * kp3 + kp4) * dh / 6;
        L[i] = kt1;
    }
    soln[0] = P;
    soln[1] = T;
    soln[2] = L;
    return soln;
}
int main () {
    std::array<double, rk4_n>* soln = rk4_scheme(0.25);
    for (int i = 0; i < 3; i++) {
        for (int j = 0; j < 111; j+=5) {
            std::cout << soln[i][j] << " ";
        }
        std::cout << "\n";
    }
    return 0;
}