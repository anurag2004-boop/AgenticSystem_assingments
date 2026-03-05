import numpy as np
# Step 1: Create a NumPy array representing numeric data
data = np.array([10, 20, 30, 40,])  # Example numeric data array
# Step 2: Compute mean and standard deviation
mean = np.mean(data)
std = np.std(data)
# Step 3: Normalize the data
normalized = (data - mean) / std
# Step 4: Reshape the normalized data into a 2D array
reshaped = normalized.reshape(4, 1)  # Reshaping to a 4x1 array
# Step 5: Print the results
print("Original array:", data)
print("Mean:", mean)
print("Standard Deviation:", std)
print("Normalized array:", normalized)
print("Reshaped array:\n", reshaped)
print("Shape of reshaped array:", reshaped.shape)
