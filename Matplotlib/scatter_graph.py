import matplotlib.pyplot as plt
import numpy as np 

# sactter grapgh = shows the relationship betwen two variables 
#                  helps to identify a correlation ( +,-, none )
#                  Example: Study hours vs. Test scores

x1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
y1 = np.array([23, 55, 60, 72, 75, 80, 87, 90, 93, 95, 97])

x2 = np.array([0, 1, 2, 2, 3, 4, 5, 5, 6, 7, 9])
y2 = np.array([13, 45, 50, 52, 65, 70, 77, 80, 85, 93, 99])

plt.scatter(x1,y1, color= "skyblue",
                 alpha=0.9,
                 s = 100, # for dot size
                 label = "Class A")

plt.scatter(x2,y2, color= "red",
                 alpha=0.9,
                 s = 100, # for dot size
                 label = "Class B")


plt.title("Test Score")
plt.xlabel("Hours Studied")
plt.ylabel("Marks (In %)")
plt.legend()
plt.show()