# bpho-methods
A collection of methods for the BPhO 2022 Computational Challenge.
- euler's method: recommended (read: mandated) by BPhO
- neural network: gives 'wobbly' results, needs further work (if worth it) and c++ implementation (maybe fortran instead for matmul)
- rk4 method: sacrifice in accuracy not justifiable for the speed increase, doesn't work effectively because of how intertwined P,T and L are, so h=0.01 is almost needed anyway (and then it is slower)