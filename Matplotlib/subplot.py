import matplotlib.pyplot as plt
import numpy as np

# Subplot - A subplot is a plot that is embedded within another plot.

fig, axs = plt.subplots(2, 2, figsize=(10, 8))
x1 = np.array([1, 2, 3, 4, 5])
y1 = np.array([2, 3, 5, 7, 11])
scores = np.array([85, 90, 78, 92, 88, 95, 80, 82, 91, 89])
x2 = np.array([1, 2, 3, 4, 5])
y2 = np.array([1, 4, 6, 8, 10])

# Scatter plot
axs[0, 0].scatter(x1, y1, color='skyblue', alpha=0.9, s=100)
axs[0, 0].set_title("Class A")
axs[0, 0].set_xlabel("Hours Studied")
axs[0, 0].set_ylabel("Marks (In %)")

# Histogram
axs[0, 1].hist(scores, bins=10, color='skyblue', alpha=0.7, edgecolor='black')
axs[0, 1].set_title("Distribution of Test Scores")
axs[0, 1].set_xlabel("Scores")
axs[0, 1].set_ylabel("Number of Students")

# Box plot
axs[1, 0].boxplot([x1, x2], labels=["Class A", "Class B"])
axs[1, 0].set_title("Box Plot of Study Hours")
axs[1, 0].set_ylabel("Hours Studied")

# Line plot
axs[1, 1].plot(x1, y1, marker='o', color='skyblue', label='Class A')
axs[1, 1].plot(x2, y2, marker='o', color='red', label='Class B')
axs[1, 1].set_title("Line Plot of Test Scores")
axs[1, 1].set_xlabel("Hours Studied")
axs[1, 1].set_ylabel("Marks (In %)")
axs[1, 1].legend()

plt.tight_layout()
plt.show()