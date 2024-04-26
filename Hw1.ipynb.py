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

ex6_1 = np.random.randint(7)
ex6_2 = np.random.randint(7)
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

ex11_1 = np.random.randint(0, 2, size=(2, 3))
ex11_2 = np.random.randint(0, 2, size=(3))
ex11 = np.dot(ex11_1, ex11_2)

ex12_1 = np.random.randint(1, 11, size=(2, 2))
ex12_2 = np.random.randint(1, 11, size=(2, 2))
ex12 = ex12_1*ex12_2

ex13_1 = np.random.randint(1, 11, size=(2, 2))
ex13_2 = np.random.randint(1, 11, size=(2, 2))
ex13 = np.dot(ex13_1, ex13_2)

ex14_1 = np.random.randint(1, 101, size=(5, 5))
ex14 = np.sum(ex14_1)

ex15_1 = np.random.randint(1, 11, size=(4, 4))
ex15_2 = np.random.randint(1, 11, size=(4, 4))
ex15 = ex15_1 - ex15_2

ex16_1 = np.random.randint(0, 2, size=(3, 3))
ex16_2 = np.sum(ex16_1, axis=1)
ex16 = ex16_2.reshape(-1, 1)

ex17 = np.random.randint(1, 100, size=(3, 4))
ex17_sqr = np.square(ex17)

ex18 = np.random.randint(1, 51, size=(4))
ex18_root = np.sqrt(ex18)

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
print('ex11 = ', ex11)
print('ex12 = ', ex12)
print('ex13 = ', ex13)
print('ex14 = ', ex14)
print('ex15 = ', ex15)
print('ex16 = ', ex16)
print('ex17 = ', ex17_sqr)
print('ex18 = ', ex18_root)