import ctypes
import numpy as np

try:  # just running the file
    mylib = ctypes.windll.LoadLibrary('methods/lib/methods.dll')
except FileNotFoundError:  # from workspace root (VSCode Debug)
    mylib = ctypes.windll.LoadLibrary('lib/methods.dll')
except AttributeError:  # for use from linux cl
    try:
        mylib = ctypes.cdll.LoadLibrary('methods/lib/methods.so')
    except FileNotFoundError:
        mylib = ctypes.cdll.LoadLibrary('lib/methods.so')

scheme_arg_types = [ctypes.c_double] * 6
scheme_return_type = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))

mylib.rk4_scheme.argtypes = mylib.euler_scheme.argtypes = scheme_arg_types
mylib.rk4_scheme.restype = mylib.euler_scheme.restype = scheme_return_type


def euler_scheme(dh: float, h0: float, h1: float, P0: float, T0: float, U: float, dN: float) -> np.ndarray:
    n = int((h1 - h0) / dh) + 1
    N = int(dN / dh)
    soln = mylib.euler_scheme(dh, h0, h1, P0, T0, U)
    data = np.asarray([soln[0][:n:N], soln[1][:n:N], soln[2][:n:N]])
    return data


def rk4_scheme(dh: float, h0: float, h1: float, P0: float, T0: float, U: float, dN: float) -> np.ndarray:
    n = int((h1 - h0) / dh) + 1
    N = int(dN / dh)
    soln = mylib.rk4_scheme(dh, h0, h1, P0, T0, U)
    data = np.asarray([soln[0][:n:N], soln[1][:n:N], soln[2][:n:N]])
    return data
