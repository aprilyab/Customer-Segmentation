
si_score=silhouette_score(x,df["Cluster"])
de_score=davies_bouldin_score(x,df["Cluster"])
print("silhouette_score:  ",si_score)
print("davies_bouldin_score:  ",de_score)

# save the metrics
metrics={