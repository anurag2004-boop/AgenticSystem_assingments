import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

np.random.seed(42)

data = {
    'systolic_bp':   np.concatenate([np.random.normal(118, 10, 150),
                                     np.random.normal(142, 12, 150),
                                     np.random.normal(168, 8,  100)]),
    'cholesterol':   np.concatenate([np.random.normal(178, 18, 150),
                                     np.random.normal(222, 22, 150),
                                     np.random.normal(262, 18, 100)]),
    'bmi':           np.concatenate([np.random.normal(21.5, 2, 150),
                                     np.random.normal(27.0, 3, 150),
                                     np.random.normal(33.5, 3, 100)]),
    'glucose_level': np.concatenate([np.random.normal(88,  10, 150),
                                     np.random.normal(112, 14, 150),
                                     np.random.normal(148, 18, 100)]),
    'age':           np.concatenate([np.random.normal(34, 7,  150),
                                     np.random.normal(51, 6,  150),
                                     np.random.normal(63, 5,  100)])
}

df = pd.DataFrame(data)
print(df.head())

# Apply StandardScaler
scaler = StandardScaler()
df_scaled = scaler.fit_transform(df)
print(df_scaled[:10])


import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
inertia = []
K_range = range(1, 11)
for k in K_range:
    kmeans = KMeans(n_clusters=k, init='k-means++', random_state=42)
    kmeans.fit(df_scaled)
    inertia.append(kmeans.inertia_)
plt.figure(figsize=(8, 5))
plt.plot(K_range, inertia, marker='o')
plt.title('Elbow Method for Optimal K')
plt.xlabel('Number of Clusters (K)')
plt.ylabel('Inertia')
plt.xticks(K_range)
plt.grid()
plt.show()  

