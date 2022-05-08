import ctypes
import numpy as np

mylib = ctypes.windll.LoadLibrary('euler/resources/dll/euler_scheme.dll')
mylib.eulerSchemeTropo.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))
mylib.eulerSchemeTropo.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]


def euler_scheme(dh: float, h0: float, h1: float, P0: float, T0: float, U: float, dN: float) -> np.ndarray:
    n = int((h1 - h0) / dh) + 1
    N = int(dN / dh)
    soln = mylib.eulerSchemeTropo(dh, h0, h1, P0, T0, U)
    data = np.asarray([soln[0][:n:N], soln[1][:n:N], soln[2][:n:N]])
    return data
