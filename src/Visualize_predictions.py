import pandas as pd 
import numpy as np
import seaborn as sns
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# load the raw data
df=pd.read_csv(r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\data\processed\clustered_Mall_Customers.csv")


# create an object
scaler=StandardScaler()
x=scaler.fit_transform(df)

# Visualize clusters using 2D plots
sns.scatterplot(x="Annual Income (k$)",y="Spending Score (1-100)",data=df,hue="Cluster",palette="viridis")
plt.title("Custemer Segmentation")
plt.xlabel("Annual Income (k$)")
plt.ylabel("Spending Score (1-100)")
plt.savefig(r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\outputs\figures\clusters_plot.png")
plt.show()