import numpy as np

arithmetic = np.arange(0,16,2)
print(arithmetic)
print("ndim: ",arithmetic.ndim," shape:", arithmetic.shape)

#resize to 2*4 2-dim array
arithmetic.resize(2,4)
print()
print(arithmetic)
print("ndim: ",arithmetic.ndim," shape:", arithmetic.shape)

#resize to 2*2*2 3-dim array
array = arithmetic.resize(2,2,2)
print()
print(arithmetic)
print("ndim: ",arithmetic.ndim," shape:", arithmetic.shape)