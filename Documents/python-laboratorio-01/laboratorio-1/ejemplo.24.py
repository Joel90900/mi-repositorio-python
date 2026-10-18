import matplotlib.pyplot as plt
import random

x = [random.randint(0, 100) for _ in range(30)]
y = [random.randint(0, 100) for _ in range(30)]

plt.scatter(x, y, c="red")
plt.title("Puntos")
plt.show()