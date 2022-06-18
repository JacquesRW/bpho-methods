from methods import *
from typing import Callable, Dict
from time import perf_counter as tm


def speed_test(method: Callable, tests: int) -> float:
    '''
    Returns average execution time of 'method' in microseconds.
    '''
    start = tm()
    for i in range(tests + 1):
        method(i / tests)
    duration = tm() - start
    avg_time = duration / (tests + 1) * 1_000_000
    return avg_time


def test_all(methods: list[Callable], tests: int) -> Dict[str, float]:
    '''
    Creates dictionary of all methods and their average execution time in microseconds.
    Mostly defunct now as only the 2 rk4 methods are worth using.
    '''
    avg_times = {}
    for method in methods:
        avg_times[method.__name__] = speed_test(method, tests)
    return avg_times


if __name__ == "__main__":
    methods = [cpp_rk4_scheme, py_rk4_scheme]
    avg_times = test_all(methods, 1000)
    for i in avg_times:
        print(f'{i} took {avg_times[i]:.4} microseconds on average.')
