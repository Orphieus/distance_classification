# distance_classification
MLPR lab submission

![image](https://github.com/user-attachments/assets/53751b0e-d299-4fd5-8596-d38f34dddc5a)



#### 1. What are the common distance metrics used in distance-based classification algorithms? 

  -> Euclidean Distance: Computes straight-line distance and is applied typically in KNN and clustering.
Manhattan Distance: Computes the total absolute difference between points.
Minkowski Distance: Generalization of Euclidean and Manhattan distances.
Cosine Similarity/Distance: Computes the angle between two vectors, used typically in text and recommendation systems.
Hamming Distance: Computed as the number of differing elements in categorical or binary information.
Mahalanobis Distance: Also considers correlations within the data and scales distances by it.



#### 2. What are some real-world applications of distance-based classification algorithms? 

  -> Healthcare: Forecasting diseases from patient symptoms or medical histories.
Recommender Systems: Detecting similar users or products to recommend.
Image Recognition: Detecting objects, faces, or features in pictures.
Fraud Detection: Detecting anomalies in transaction patterns.
Document Classification: Clustering documents or emails by similarity.
Retail: Segmentation of customers and purchase behavior prediction.
Sports Analytics: Comparing player performances or team tactics.

#### 3. Explain various distance metrics. 

  -> Euclidean Distance: Tracks straight-line distance and is optimal for numeric data.
Manhattan Distance: Returns the sum of absolute differences and is optimal for grid-like data.
Minkowski Distance: Generalizes different types of distance depending on a parameter.
Cosine Similarity: Measures vector similarity in high-dimensional spaces.
Hamming Distance: Counts category or binary data differences.
Mahalanobis Distance: Addresses correlations and scales with variance.

#### 4. What is the role of cross validation in model performance? 

  -> Guarantees the model to perform well on new data by dividing it into training and testing sets.
Reduces overfitting risk by measuring performance on various data splits.
Assists in choosing the optimal parameters, e.g., the number of neighbors in KNN.

#### 5. Explain variance and bias in terms of KNN? 

  -> Bias: Indicates the degree to which the model oversimplifies the data. KNN has low bias as it uses actual data points. Very small k values, though, can cause overfitting of the data.
Variance: Shows how much the model's predictions vary with varying training data. Small k values create high variance as the model is sensitive to noise. Large k values decrease variance but may oversimplify the data.
Trade-Off: Choosing the right k balances bias and variance, ensuring better generalization.



![plot1](https://github.com/user-attachments/assets/f3f2e60b-a5eb-4f28-af48-74ed43214751)
![plot2](https://github.com/user-attachments/assets/15b82d56-8e34-4464-be17-1f78294a5258)
![plot3](https://github.com/user-attachments/assets/ec53c26b-356b-419e-a187-a64e54c9611a)
![plot4](https://github.com/user-attachments/assets/2fee5748-37dd-4f52-adbe-b08de5ebee45)
![shashi](https://github.com/user-attachments/assets/56c664c3-6702-40c5-b232-0a2af4d9930d)

