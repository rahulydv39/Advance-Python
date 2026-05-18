import matplotlib.pyplot as plt
import numpy as np

# bar chart - compares catogaries of data by representing each catogry with a bar

catogories = ["Bread", "fruit", "vegitables", "protien", "dairy", "sweet"]
values = np.array([4, 3, 5, 3, 2, 1])

plt.bar(catogories, values, color="skyblue")
# for horizontal bar chart
"""plt.barh(catogories, values, color="skyblue")"""


plt.title("Daily Consuption")
plt.xlabel("Food")
plt.ylabel("Quantity")

plt.show()
