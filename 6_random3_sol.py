import matplotlib.pyplot as plt
import random
fre = []
prob = []
n = 0
total_try = 3000
for j in range(1, total_try+1):
    i = random.randint(1, 6)
    k = random.randint(1, 6)
    if (i == 3 and k == 3):
        n += 1

    fre.append(n/j)
    prob.append(1/36)

plt.plot(range(1, total_try+1), fre, 'b', range(1, total_try+1), prob, 'r')
plt.legend(['Relative Frequency', 'Probability'])
plt.show()
