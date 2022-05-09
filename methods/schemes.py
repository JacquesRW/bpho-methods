import ctypes
import numpy as np

try:  # just running the file
    print("Trying default .dll loading.")
    mylib = ctypes.windll.LoadLibrary('methods/lib/methods.dll')
    print("Default .dll loading used.")
except FileNotFoundError:  # from workspace root (VSCode Debug)
    print("Trying alternate .dll loading.")
    mylib = ctypes.windll.LoadLibrary('lib/methods.dll')
    print("Alternate .dll loading used.")
except AttributeError:  # for use from linux cl
    print("Trying .so loading.")
    try:
        mylib = ctypes.cdll.LoadLibrary('methods/lib/euler_scheme.so')
    except FileNotFoundError:
        mylib = ctypes.cdll.LoadLibrary('lib/euler_scheme.so')

mylib.euler_scheme.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))
mylib.euler_scheme.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]
mylib.rk4_scheme.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))
mylib.rk4_scheme.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]


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
