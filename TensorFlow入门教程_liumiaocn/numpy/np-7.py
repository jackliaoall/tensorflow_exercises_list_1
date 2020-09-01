import numpy as np

arr = np.array([1,2,3,4])
print("sample standard deviation: np.std()", np.std(arr, ddof=1))