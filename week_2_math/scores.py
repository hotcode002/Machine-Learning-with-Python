import matplotlib.pyplot as plt
import numpy as np

# Read the scores file
scores = np.genfromtxt("./data/gre_scores_3_sets.csv",delimiter=",")

f, (ax1, ax2,ax3) = plt.subplots(1, 3, sharey=True)
ax1.set_xlim(200,400)
ax1.axvline(x=305, ymin=0, ymax = 800, linewidth=2, color='r')
ax1.axvline(x=300, ymin=0, ymax = 800, linewidth=2, color='g')
ax1.hist(scores[:,0],bins=300)
ax2.set_xlim(200,400)
ax2.axvline(x=315, ymin=0, ymax = 800, linewidth=2, color='r')
ax2.axvline(x=300, ymin=0, ymax = 800, linewidth=2, color='g')
ax2.hist(scores[:,1],bins=300)
ax3.set_xlim(200,400)
ax3.axvline(x=330, ymin=0, ymax = 800, linewidth=2, color='r')
ax3.axvline(x=300, ymin=0, ymax = 800, linewidth=2, color='g')
ax3.hist(scores[:,2],bins=300)
plt.show()
