import numpy as np
data = np.array([1, 2, 3, 4, 5])
mean = np.mean(data)
normalized = ( data - mean) / np.std(data)
print("Normalized Data:", normalized)
standardized = (data - mean) / np.std(data)
print("Standardized Data:", standardized)   
