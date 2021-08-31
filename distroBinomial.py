import matplotlib.pyplot as plt
import math

def binomial(x, n, p):
    fact = math.factorial(n) / (math.factorial(x) * math.factorial(n-x))

    probability = p**x * (1 - p)**(n-x)

    return fact * probability

ex = [6, 10, 20, 40, 80, 160]
p = 0.5

for n in ex:
    Xs = [k/n  for  k in range(n+1)] # genera una lista desde 0 hasta n y se guardan en la lista Xs
    Ys = [binomial(x,n,p) for x in range(n+1)]

    plt.plot(Xs, Ys, label = f"n={n}")

plt.xlabel('Probablilidades')
plt.ylabel('$f"{x}"$')

plt.legend()
plt.show()