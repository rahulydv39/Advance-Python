import matplotlib.pyplot as plt
import numpy as np

# numpy array list is faster than python list 
X = np.array([2023, 2027, 2030])
Y1 = np.array([10, 25, 17])
Y2 = np.array([15, 8, 18])

line_style = dict( marker = "o",  
                   linestyle = "--", 
                   linewidth = 2, 
                   markersize = 10, 
                   markerfacecolor="blue")

plt.title("Class Size", fontsize = 15,
                        family = "Arial",
                        fontweight = "bold",
                        color="#ff0000")


plt.xlabel("Year", fontsize = 15,
                   family = "Arial",
                   fontweight = "bold",
                   color="#1af033")

plt.ylabel("Students", fontsize = 15,
                   family = "Arial",
                   fontweight = "bold",
                   color="#1af033")

# force it to show the exact year only

plt.tick_params(axis="both",
                 colors="#2dbefc")

plt.plot(X,Y1, color = "#1c5bfc", **line_style)


plt.plot(X,Y2)


plt.show()