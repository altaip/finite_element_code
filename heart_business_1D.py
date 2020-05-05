from nelder import *
from o_func_1D import *
from scipy.optimize import minimize
import numpy as np

f=lambda x: objective_function(x)
#xo=np.random.random((7,1))
xo=[.57,5.12,.1,2,1200,1]

ans=minimize(f,xo,method='Nelder-Mead')
print('nelder',ans)