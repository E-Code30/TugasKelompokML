import numpy as np
from sklearn.cluster import KMeans

# Menyiapkan dataset
dataset = np.array([[0.6, 0.7], [0.8, 0.9], [0.4, 0.5], [0.2, 0.3], [0.1, 0.2]])

# Melakukan pengolompokkan k-means
kmeans = KMeans(n_clusters=2, random_state=0).fit(dataset)

# Mencetak hasil pengolompokkan
print("Hasil pengolompokkan:")
for i in range(len(dataset)):
    if kmeans.labels_[i] == 0:
        print(f"Data {i+1} adalah buah")
    else:
        print(f"Data {i+1} adalah sayur")
