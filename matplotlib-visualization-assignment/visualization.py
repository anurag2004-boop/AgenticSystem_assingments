import numpy as np
import matplotlib.pyplot as plt
# Create a list of 10 epochs
epochs = np.arange(1, 11)
# Generate synthetic training loss values for these epochs
loss_values = np.random.uniform(low=0.1, high=1.0, size=len(epochs))
# Line Plot: Loss vs Epoch
plt.figure(figsize=(10, 5))

plt.plot(epochs, loss_values, marker='o', linestyle='-', color='b')
plt.title('Training Loss vs Epoch')
plt.xlabel('Epoch')
plt.ylabel('Training Loss')
plt.grid()
plt.show()
# Scatter Plot: Epoch vs Loss
plt.figure(figsize=(10, 5))
plt.scatter(epochs, loss_values, color='r')
plt.title('Epoch vs Training Loss')
plt.xlabel('Epoch')
plt.ylabel('Training Loss')
plt.grid()
plt.show()
# Bar Chart comparing accuracy of three models
models = ['Model A', 'Model B', 'Model C']
accuracy = [0.85, 0.90, 0.88]
plt.figure(figsize=(10, 5))
plt.bar(models, accuracy, color=['blue', 'orange', 'green'])
plt.title('Model Accuracy Comparison')
plt.xlabel('Models')
plt.ylabel('Accuracy')
plt.ylim(0, 1)  # Set y-axis limits to 0-1 for better visualization
plt.grid(axis='y')
plt.show()

