import matplotlib.pyplot as plt

fig, axis = plt.subplots(2, 3)

axis[0, 0].plot([1, 2, 3], [1, 2, 3], 'ro')
axis[0, 1].plot([1, 2, 3], [1, 2, 3], 'bo')
axis[0, 2].plot([1, 2, 3], [1, 2, 3], 'go')

axis[1, 0].plot([1, 2, 3], [3, 2, 1], 'ro')
axis[1, 1].plot([1, 2, 3], [3, 2, 1], 'bo')
axis[1, 2].plot([1, 2, 3], [3, 2, 1], 'go')

plt.show()