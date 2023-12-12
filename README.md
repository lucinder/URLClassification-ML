# URL Classification with ML
Research project - evaluating the most effective metrics for predicting malicious URLs using ML.
### What dataset is used?
We randomly sampled 60,000 benign and 40,000 malicious urls from [this kaggle dataset](https://www.kaggle.com/datasets/sid321axn/malicious-urls-dataset/).

### What metrics are used?
**Classification bins:**
- Benign (0) or malicious (1)
  
**Features:**
- URL Length
- URL file extension (.html, .php, .pdf for example)
- Hostname
- Top-Level Domain
- Does the URL use a commmon shortener (bit.ly, ow.ly, etc.)?
- Domain features:
  * Domain token count
  * Domain token average length
  * Domain token max length
  * Domain token length standard deviation
- Path features:
  * Path token count
  * Path token average length
  * Path token max length
  * Path token length standard deviation

Note: we were going to use content features, but the amount of 404s and connection problems using this dataset have made it infeasible. Many URLs in this dataset are now depreciated, but still useful for research purposes.

## Results
Table 1 shows the performance metrics of different ML models on the dataset with an 80-20 training-testing split.

***Table 1: Model Performance Metrics***

| Model         | Accuracy | Precision | Recall | F1 Score | ROC-AUC | Confusion Matrix |
|--------------|:-----:|:-----:|:-----:|:-----:|:-----:| :--- |
| Random Forest |  |  |  |  |  | |
| K-Nearest Neighbors |  |  |  |  |  | |
| Logistic Regression |  |  |  |  |  | |
| Stochastic Gradient Descent |  |  |  |  |  | |
| Support Vector Classification |  |  |  |  |  | |
| Gaussian Naive Bayes | 63.12 | 66.26 | 15.75 | 25.45 | 42.64 | ![Untitled](https://github.com/lucinder/URLClassification-ML/assets/81818595/d5c9277b-b02d-450d-a45e-fc322e07d059) |
| K-Means Clustering | 68.97 | 69.49 | 39.87 | 50.67 | 64.11 | ![Untitled-1](https://github.com/lucinder/URLClassification-ML/assets/81818595/8a284ad7-3c3a-4656-a280-93a3c969ad31) |
| Mini-Batch K-Means Clustering | 54.14 | 40.30 | 30.64 | 34.81 | 49.79 | ![Untitled](https://github.com/lucinder/URLClassification-ML/assets/81818595/9d1be276-9289-46a1-9af1-00d0065ce52e) |
| Spectral Clustering | 59.92 | 18.92 | 0.09 | 0.17 | 49.92 | ![Untitled](https://github.com/lucinder/URLClassification-ML/assets/81818595/efcbcd8f-26ea-4526-85a5-268f7ade9d26) |
| Gaussian Mixture Model | 59.05 | 43.95 | 8.96 | 14.88  | 50.0 | ![Untitled-1](https://github.com/lucinder/URLClassification-ML/assets/81818595/70d1718f-1d35-4ae2-ac27-9f2276754753) |
| DBSCAN | 60.10 | 100.0 | 0.16 | 0.32 | 49.92 | ![Untitled](https://github.com/lucinder/URLClassification-ML/assets/81818595/048c20a3-9c38-473b-9157-6641cde06300) |
