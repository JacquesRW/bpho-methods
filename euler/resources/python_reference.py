import math
import numpy as np

def _calc_Es(T: float) -> float:
    return 6.1121 * math.exp((18.678 - T / 234.5) * (T / (T + 257.14)))

def _calc_L(P: float, Es: float, U: float, TK: float) -> float:
    r = U * Es / (P - U * Es)
    return 9.7734 * (1.0 + 5420.3 * r / TK) / (1.0 + 8400955.5 * r / (TK * TK))

def _calc_dP(P: float, U: float, Es: float, TK: float) -> float:
    return -34.171 * (P - 0.37776 * U * Es) / TK

def py_single_sim(dh: float, h0: float, h1: float, P0: float, T0: float ,U: float, dN: float) -> list[np.ndarray]:
    n = int((h1-h0)/dh)+1
    N = int(dN/dh)
    P = np.zeros(n)
    T = np.zeros(n)
    L = np.zeros(n)
    P[0] = P0
    T[0] = T0
    L[0] = _calc_L(P0,_calc_Es(T0),U, T0 + 273.15)
    for i in range(1,n):
        t = T[i - 1] - L[i - 1] * dh
        TK = t + 273.15
        Es = _calc_Es(t)
        T[i] = t 
        P[i] = P[i - 1] + dh * _calc_dP(P[i-1],U,Es,TK) 
        L[i] = _calc_L(P[i],Es,U,TK) 
    data = np.asarray([P[:n:N],T[:n:N],L[:n:N]])
    return data