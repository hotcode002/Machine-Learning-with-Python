import numpy as np
import matplotlib.pyplot as plt

i = np.random.randn(1000) * 10

i = np.sort(i)

print(i)

plt.boxplot(i)
plt.show()

plt.hist(i, bins=50)
plt.show()
