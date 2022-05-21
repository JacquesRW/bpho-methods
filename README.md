# bpho-methods
A collection of methods for the BPhO 2022 Computational Challenge.

### Model:
This solves the following set of ODEs in a variety of ways:


$$
\begin{align}
\frac{dT}{dh} & = -L(P,T) \\
\frac{dP}{dh} & = -\frac{M_d g}{R T_K} \left ( P - U \left ( 1-\frac{M_V}{M_d} \right ) E_S(T) \right ) 
\end{align} 
$$

Given

$$
\begin{align}
 L(P,T) & = g \frac{1+\frac{\Delta H_s \frac{M_V}{M_d}  r(P,T)}{R_s T_K}}{c_{pd}+\frac{\Delta H_s^2 \frac{M_V}{M_d}  r(P,T)}{R_{sw} T_K^2}} \\
r(P,T) & = \frac{UE_S(T)}{P-UE_S(T)} \\
E_S(T) & = 6.1121e^{ \left (18.678 - \frac{T}{234.5} \right ) \left (\frac{T}{T+257.14} \right ) }
\end{align}
$$

where $T_K = T  + 273.15$ - i.e the Kelvin conversion - and for some parameter $U \in [0,1]$, given the initial conditions $h_0 = 0$ km, $P_0=1013.25$ mbar and $T_0 = 15^\circ$ C, with step size $\Delta h=0.01$, up to $h_1 = 11$ km.
### Contains:
- euler's method: recommended (read: mandated) by BPhO
- neural network: gives 'wobbly' results, needs further work (if worth it) and c++ implementation (maybe fortran instead for matmul)
- rk4 method: approx 40% faster than euler

### Other:
- 'py_ref.py' contains roughly equivalent python code to the c++ code used for euler and rk4
