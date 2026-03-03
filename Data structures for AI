import numpy as np 
np.random.seed(42)  
data  = np.random.randint(0, 100,(100,2))

#mea and std devision 
mean = np.mean(data, axis=0)
std = np.std(data, axis=0)
#normalization
normalized_data = (data - mean) / std

#split (80% train, 20% test)
split_index = int(0.8 * len(normalized_data))
train_data = normalized_data[:split_index]
test_data = normalized_data[split_index:]


#print shapes
print("\norignal shape :", data.shape)
print("normalized shape :", normalized_data.shape)

print ("\ntrain shape :", train_data.shape)
print("test shape :", test_data.shape)

print("\nmean of train data :", np.mean(train_data, axis=0))
print("std of train data :", np.std(train_data, axis=0))

print("\nNote: changing train also changed normalised (slicing give views):")
