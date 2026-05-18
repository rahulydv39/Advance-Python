import matplotlib.pyplot as plt
import numpy as np


# Grid( )- helps make plot easier to read by adding refference lines.

x = [1, 2, 3, 4, 5]
y = [5, 10, 15, 20, 25]

plt.grid(axis="y", # axis = x means line will show to x only 
        linewidth = 2,
        color= "lightgray",
        linestyle="dashed"
        ) 


plt.plot(x,y)
plt.show()