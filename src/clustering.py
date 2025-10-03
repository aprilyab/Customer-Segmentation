import pandas as pd 
import numpy as np
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
import joblib

# load the raw data
df=pd.read_csv(r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\data\processed\cleaned_Mall_Customers.csv")


# create an object
scaler=StandardScaler()
x=scaler.fit_transform(df)

# use Elbow method to determine optimal number of clusters
wcss=[]
for k in range(1,11):
    kmeans=KMeans(n_clusters=k,random_state=42)
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)

# make plot
plt.plot(range(1,11),wcss,marker="o")
plt.title("Elbow Method for optimized K")
plt.xlabel("numbr of clusters")
plt.ylabel("wcss")


# create object
k_means=KMeans(init="k-means++",n_init=12,n_clusters=4)
df["Cluster"]=k_means.fit_predict(x)
print(df)

# save the kmeans model 
joblib.dump(k_means,r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\outputs\models\K-Means_model.pkl")
joblib.dump(scaler,r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\outputs\Scaler")

df.to_csv(r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\data\processed\clustered_Mall_Customers.csv")




