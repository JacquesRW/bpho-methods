import math
import numpy as np
# equivalent (but slower) implementation of euler_scheme.dll


def _calc_Es(T: float) -> float:
    return 6.1121 * math.exp((18.678 - T / 234.5) * (T / (T + 257.14)))


def _calc_L(P: float, Es: float, U: float, TK: float) -> float:
    r = U * Es / (P - U * Es)
    return 9.7734 * (1.0 + 5420.3 * r / TK) / (1.0 + 8400955.5 * r / (TK * TK))


def _calc_dP(P: float, Es: float, U: float, TK: float) -> float:
    return -34.171 * (P - 0.37776 * U * Es) / TK


def rk4_scheme(dh: float, h0: float, h1: float, P0: float, T0: float, U: float, dN: float) -> np.ndarray:
    n = int((h1 - h0) / dh) + 1
    N = int(dN / dh)
    P = [0] * n
    T = [0] * n
    L = [0] * n
    P[0] = P0
    T[0] = T0
    L[0] = _calc_L(P0, _calc_Es(T0), U, T0 + 273.15)
    for i in range(1, n):
        p = P[i - 1]
        t1 = T[i - 1]
        tk = t1 + 273.15
        k1 = L[i - 1]
        k2 = _calc_L(p + dh * k1 / 2, _calc_Es(t1 + dh * k1 / 2), U, tk + dh * k1 / 2)
        k3 = _calc_L(p + dh * k2 / 2, _calc_Es(t1 + dh * k2 / 2), U, tk + dh * k2 / 2)
        k4 = _calc_L(p + dh * k3, _calc_Es(t1 + dh * k3), U, tk + dh * k3)
        t = t1 - (k1 + 2 * k2 + 2 * k3 + k4) * dh / 6
        T[i] = t
        K1 = _calc_dP(p, U, _calc_Es(t1), tk)
        K2 = _calc_dP(p + dh * K1 / 2, _calc_Es(t1 + dh * K1 / 2), U, tk + dh * K1 / 2)
        K3 = _calc_dP(p + dh * K2 / 2, _calc_Es(t1 + dh * K2 / 2), U, tk + dh * K2 / 2)
        K4 = _calc_dP(p + dh * K3, _calc_Es(t1 + dh * K3), U, tk + dh * K3)
        P[i] = p + (K1 + 2 * K2 + 2 * K3 + K4) * dh / 6
        L[i] = _calc_L(P[i], _calc_Es(t), U, t + 273.15)
    data = np.asarray([P[:n:N], T[:n:N], L[:n:N]])
    return data
