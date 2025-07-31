import matplotlib.pyplot as plt
import numpy as np
overs = np.arange(1, 11)
score = [4, 8, 2, 6, 8, 10, 13, 1, 5, 3]
plt.bar(overs, score, color='green')
plt.title("Score summary")
plt.xlabel("OVERS")
plt.ylabel("RUNS TAKEN")
plt.xticks(overs)
plt.grid(axis='x', linestyle="-", alpha=0.9)
plt.show()