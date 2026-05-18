import matplotlib.pyplot as plt
import numpy as np 

# Histogram = A visual representation of the distribution of quantitative data.
#             They group values into bins (intervals)
#             and counts how many fail in each range.

scores = np.random.normal(loc=80, scale=10, size=100) # loc - mean, scale - standard deviation, size - number of data points
scores = np.clip(scores, 0, 100) # to ensure scores are between 0 and 100

plt.hist(scores, bins=10, color='skyblue', alpha=0.7, edgecolor='black')
plt.title("Distribution of Test Scores")
plt.xlabel("Scores")
plt.ylabel("Number of Students")
plt.show()