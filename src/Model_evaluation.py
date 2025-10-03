import joblib
import pandas as pd 
import numpy as np
import seaborn as sns
import json
import matplotlib.pyplot as plt
from sklearn.metrics import silhouette_score
from sklearn.metrics import davies_bouldin_score



# load the raw data
df=pd.read_csv(r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\data\processed\clustered_Mall_Customers.csv")

# load the saved kmeans model
kmeans=joblib.load(r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\outputs\models\K-Means_model.pkl")

# load the scaler 
scaler=joblib.load(r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\outputs\Scaler")

x=scaler.fit_transform(df)

# evaluate the kmeans model
si_score=silhouette_score(x,df["Cluster"])
de_score=davies_bouldin_score(x,df["Cluster"])
print("silhouette_score:  ",si_score)
print("davies_bouldin_score:  ",de_score)

# save the metrics
metrics={
    "davies_bouldin_score:  ": de_score,
    "silhouette_score:  ": si_score
    }

with open (r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\outputs\metrics.json","w") as f:
    json.dump(metrics,f)