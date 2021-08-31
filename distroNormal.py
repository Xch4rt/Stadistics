from numpy import random
import matplotlib.pyplot as plt
'''
x = random.randint(0,5,20)
print(x)

plt.hist(x,5)
plt.show()
'''
x = random.normal(5,1,10000) #normal recibe media, desviacion estandar y valores a generar 
print(x)
#mientras mas valores, mas semejante sera a la campana de gauss
plt.hist(x,100)
plt.show()
