# bpho-methods
A collection of methods for the BPhO 2022 Computational Challenge.

### Contains:
- euler's method: recommended (read: mandated) by BPhO
- neural network: gives 'wobbly' results, needs further work (if worth it) and c++ implementation (maybe fortran instead for matmul)
- rk4 method: extremely pog improvement, needs to be implemented in c++ and probably renders the other techniques moot

### Info:
- each method contains a main.py that can be run to execute the code, and will create a dynamic matplotlib figure, with a slider for U values
- each of euler and rk4 have a 'py_ref.py' which contains roughly equivalent python code to the c++ code used in their respective DLLs