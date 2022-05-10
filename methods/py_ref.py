import math
import numpy as np


def _calc_Es(T: float) -> float:
    return 6.1121 * math.exp((18.678 - T / 234.5) * (T / (T + 257.14)))


def _calc_L(P: float, UEs: float, TK: float) -> float:
    r = UEs / (P - UEs)
    return 9.7734 * (TK + 5420.3 * r) / (TK * TK + 8400955.5 * r) * TK


def _calc_dP(P: float, UEs: float, TK: float) -> float:
    return -34.171 * (P - 0.37776 * UEs) / TK


def euler_scheme(dh: float, h0: float, h1: float, P0: float, T0: float, U: float, dN: float) -> np.ndarray:
    n = int((h1 - h0) / dh) + 1
    N = int(dN / dh)
    P = [0] * n
    T = [0] * n
    L = [0] * n
    P[0] = P0
    T[0] = T0
    L[0] = _calc_L(P0, U * _calc_Es(T0), T0 + 273.15)
    for i in range(1, n):
        t = T[i - 1] - L[i - 1] * dh
        TK = t + 273.15
        UEs = U * _calc_Es(t)
        T[i] = t
        P[i] = P[i - 1] + dh * _calc_dP(P[i - 1], UEs, TK)
        L[i] = _calc_L(P[i], UEs, TK)
    data = np.asarray([P[:n:N], T[:n:N], L[:n:N]])
    return data


def rk4_scheme(dh: float, h0: float, h1: float, P0: float, T0: float, U: float, dN: float) -> np.ndarray:
    n = int((h1 - h0) / dh) + 1
    N = int(dN / dh)
    P = [0] * n
    T = [0] * n
    L = [0] * n
    P[0] = P0
    T[0] = T0
    L[0] = _calc_L(P0, U * _calc_Es(T0), T0 + 273.15)
    for i in range(1, n):
        # rk coefficients
        p1 = P[i - 1]
        t1 = T[i - 1]
        UEs1 = U * _calc_Es(t1)
        tk1 = t1 + 273.15
        k1 = _calc_L(p1, UEs1, tk1)
        K1 = _calc_dP(p1, UEs1, tk1)

        t2 = t1 - dh * k1 / 2
        p2 = p1 + dh * K1 / 2
        UEs2 = U * _calc_Es(t2)
        tk2 = t1 + 273.15
        k2 = _calc_L(p2, UEs2, tk2)
        K2 = _calc_dP(p2, UEs2, tk2)

        t3 = t1 - dh * k2 / 2
        p3 = p1 + dh * K2 / 2
        UEs3 = U * _calc_Es(t3)
        tk3 = t3 + 273.15
        k3 = _calc_L(p3, UEs3, tk3)
        K3 = _calc_dP(p3, UEs3, tk3)

        t4 = t1 - dh * k3
        p4 = p1 + dh * K3
        UEs4 = U * _calc_Es(t4)
        tk4 = t4 + 273.15
        k4 = _calc_L(p4, UEs4, tk4)
        K4 = _calc_dP(p4, UEs4, tk4)

        # rk4 updates
        T[i] = t1 - (k1 + 2 * k2 + 2 * k3 + k4) * dh / 6
        P[i] = p1 + (K1 + 2 * K2 + 2 * K3 + K4) * dh / 6
        L[i] = k1

    data = np.asarray([P[:n:N], T[:n:N], L[:n:N]])
    return data
