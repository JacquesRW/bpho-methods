import ctypes
import numpy as np

mylib = ctypes.windll.LoadLibrary('euler/resources/dll/atmosCalc.dll')
mylib.isWorking()

def cpp_single_sim(dh: float, h0: float, h1: float, P0: float, T0: float , U: float, dN: float) -> np.ndarray:
    n = int((h1-h0)/dh) + 1
    N = int(dN/dh)
    soln = mylib.eulerSchemeTropo(dh,h0,h1,P0,T0,U)
    data = np.asarray([soln[0][:n:N],soln[1][:n:N],soln[2][:n:N]])
    #data = np.asarray([i[:n:N] for i in soln])
    return data

def csv_tropo_data(dh: float, h0: float, h1: float, P0: float, T0: float ,Uset: list[float], dN: float) -> None:
    # not used
    # outputs .csv with data from a list of U values
    columns = len(Uset)
    U = np.array(Uset, dtype=np.float64)
    mylib.testTropo(dh,h0,h1,P0,T0,U,columns,dN)
    print("Created CSV file with Troposphere data.")

mylib.isWorking.restype = ctypes.c_int
mylib.testTropo.restype = ctypes.c_int
mylib.testTropo.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, np.ctypeslib.ndpointer(ctypes.c_double) ,ctypes.c_int, ctypes.c_double]
mylib.eulerSchemeTropo.restype = ctypes.POINTER(ctypes.POINTER(ctypes.c_double))
mylib.eulerSchemeTropo.argtypes = [ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double, ctypes.c_double]