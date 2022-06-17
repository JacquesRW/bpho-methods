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

scheme_arg_types = [ctypes.c_double]
mylib.rk4_scheme.argtypes = mylib.euler_scheme.argtypes = scheme_arg_types
mylib.rk4_scheme.restype = ctypes.POINTER(ctypes.c_double * 111)
mylib.euler_scheme.restype = ctypes.POINTER(ctypes.c_double * 1101)


def euler_scheme(U: float) -> np.ndarray:
    n = 1101
    N = 10
    soln = mylib.euler_scheme(U)
    data = np.asarray([soln[0][:n:N], soln[1][:n:N], soln[2][:n:N]])
    return data


def rk4_scheme(U: float) -> np.ndarray:
    soln = mylib.rk4_scheme(U)
    data = np.asarray([soln[0], soln[1], soln[2]])
    return data
