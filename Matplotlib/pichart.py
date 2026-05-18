import matplotlib.pyplot as plt
import numpy as np

categories= ["Freshmen", "Sophomores", "Juniors", "Senoirs"]
value = np.array([300, 250, 190, 110])
colors = ["red", "skyblue", "green", "cyan"]

plt.pie(value, labels=categories,
        autopct = "%1.1f%%" ,# pct - percentage, .1f - one decimal point , %% - show percent sogn 
        colors = colors,
        explode = [0, 0, 0.1, 0], # this show hilighted 
        shadow= True,
        startangle= 90)
plt.title("xyz collage")

plt.show()

