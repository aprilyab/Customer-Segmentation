import pandas as pd 
import numpy as np

# load the raw data
df=pd.read_csv(r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\data\raw\Mall_Customers.csv")

# identify the numbeer of null rows
print(df.isnull().sum())

# remove rows with null value
df=df.dropna()

num_cols=df.select_dtypes(include=["float64","int64"])
cat_cols=df.select_dtypes(include=["object","category"])

# Keep only relevant columns (feature + target)
df = df[['Annual Income (k$)', 'Spending Score (1-100)']]

# Drop rows with missing values in 'studytime' or 'G3'
df = df.dropna(subset=['Spending Score (1-100)', 'Annual Income (k$)'])


# check th outlier in the target variable 'Exam_Score'
print(f"min value of the 'Spending Score' {df['Spending Score (1-100)'].min()} ")
print(f"max value of the 'Spending Score' {df['Spending Score (1-100)'].max()} ")

df=df[(df['Spending Score (1-100)']>=0)  &  (df['Spending Score (1-100)']<=100) ]
print(df["Annual Income (k$)"].max())
print(df["Annual Income (k$)"].min())


df.to_csv(r"C:\Users\user\Desktop\Elavvo ML Internship\Customer-Segmentation\data\processed\cleaned_Mall_Customers.csv")