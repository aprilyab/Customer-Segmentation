# Customer Segmentation Project

## Project Overview

This project performs **customer segmentation** for a mall dataset, focusing on clustering customers based on **annual income** and **spending score**. The goal is to identify distinct customer groups to help businesses improve marketing strategies and customer engagement.

This project demonstrates the **end-to-end workflow of an unsupervised machine learning pipeline**, including data preprocessing, scaling, exploratory data analysis, K-Means clustering, and cluster visualization.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Table of Contents](#table-of-contents)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Requirements](#requirements)
- [Data Cleaning and Preprocessing](#data-cleaning-and-preprocessing)
- [Clustering](#clustering)
- [Visualization](#visualization)
- [Model Evaluation](#model-evaluation)
- [References](#references)
- [Author](#author)

---

## Dataset

* **Recommended Dataset:** Mall Customer Dataset (Kaggle)  
* **File Used:** `Mall_Customers.csv`  
* **Features:** 
  - `Annual Income (k$)` → Customer annual income  
  - `Spending Score (1-100)` → Customer spending score  
* **Target:** No explicit target (unsupervised learning)

---

## Project Structure

```text
Customer-Segmentation/
│
├── data/                     # Original and processed dataset
│   ├── raw/                  # Raw CSV file
│   │   └── Mall_Customers.csv
│   └── processed/            # Scaled and cleaned dataset
│
├── notebooks/                # Jupyter notebooks
│   └── Explanatory_Data_Analysis.ipynb
│
├── outputs/                  # Models, figures, and metrics
│   ├── figures/              # Cluster visualizations
│   ├── models/               # Saved KMeans model
│   └── metrics.json          # Cluster evaluation metrics
│
├── src/                      # Python scripts
│   ├── data_cleaning_and_processing.py
│   ├── clustering.py
│   ├── Visualize_predictions.py
│   └── Model_evaluation.py
│
├── .gitignore                # Git ignore rules
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
Requirements

Install required Python packages using:

pip install -r requirements.txt


Python Libraries:

pandas → Data manipulation

numpy → Numerical computations

scikit-learn → K-Means clustering

matplotlib → Plotting clusters

seaborn → Advanced visualizations

.gitignore example:

__pycache__/
*.py[cod]
.ipynb_checkpoints/
data/processed/
outputs/

Data Cleaning and Preprocessing

Steps performed to prepare data for clustering:

Select relevant columns: Annual Income (k$) and Spending Score (1-100)

Handle missing values: Drop rows with missing data (if any)

Scaling: Standardize features using StandardScaler

Save processed data in data/processed/ for reproducibility

Clustering

Exploratory Data Analysis (EDA): Visualize distribution of income and spending score

Optimal Clusters: Determine the number of clusters using the Elbow Method

K-Means Clustering: Apply K-Means with the selected number of clusters

Assign cluster labels to each customer for segmentation

Visualization

2D Scatter Plots: Customers colored by cluster label

Cluster Centers: Highlighted with X markers

Outputs saved in outputs/figures/

Model Evaluation

Evaluate cluster compactness and separation using WCSS (Within-Cluster Sum of Squares)

Save trained KMeans model in outputs/models/ for future use

Metrics stored in outputs/metrics.json

References

Mall Customer Dataset - Kaggle

Scikit-learn KMeans Documentation

Pandas Documentation

Matplotlib Documentation

Seaborn Documentation

Author

Name: Henok Yoseph
Email: henokapril@gmail.com

GitHub: https://github.com/aprilyab
