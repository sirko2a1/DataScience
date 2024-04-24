import numpy as np

ex1 = np.arange(1, 11)

ex2 = np.zeros((3, 3))

ex3 = np.random.randint(1, 11, size=(5, 5))

ex4 = np.random.randint(0, 2, size=(4, 4))

a = np.random.randint(1, 11, size=(5))
b = np.random.randint(1, 11, size=(5))
ex5_1 = a+b
ex5_2 = a-b
ex5_3 = a*b


print(ex1)
print(ex2)
print(ex3)
print(ex4)
print(a)
print(b)
print(ex5_1)
print(ex5_2)
print(ex5_3)