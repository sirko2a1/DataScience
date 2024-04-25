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

ex6_1 = np.random.randint(1,11,size=(7))
ex6_2 = np.random.randint(1,11,size=(7))
ex6 = np.dot(ex6_1, ex6_2)

ex7_1 = np.random.randint(1, 11, size=(2, 2))
ex7_2 = np.random.randint(1, 11, size=(2, 3))
ex7 = np.dot(ex7_1, ex7_2)

ex8_1 = np.random.randint(1, 11, size=(3, 3))
ex8 = np.linalg.inv(ex8_1)
ex9_1 = np.random.randint(0, 2, size=(4, 4))
ex9 = ex9_1.T

ex10_1 = np.random.randint(1,11, size=(3, 4))
ex10_2 = np.random.randint(1,11, size=(4))
ex10 = np.dot(ex10_1, ex10_2)

print('ex1 = ', ex1)
print('ex2 = ', ex2)
print('ex3 = ', ex3)
print('ex4 = ', ex4)
#print(a)
#print(b)
print('ex5 + = ', ex5_1)
print('ex5 - =  ', ex5_2)
print('ex5 * = ', ex5_3)
print('ex6 = ', ex6)
print('ex7 = ', ex7)
print('ex8 = ', ex8)
print('ex9 = ', ex9)
print('ex10 = ', ex10)