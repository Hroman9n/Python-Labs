import numpy as np
import random
 
# задание 1
a = np.arange(1, 16).reshape(3, 5).transpose()
 
print(a)
 
print()
 
# задание 2
a = np.arange(25).reshape(5, 5)
 
b = np.array([1, 5, 10, 15, 20])
 
print(a)
 
c = a/b
 
c = c.transpose()
 
print(c)
 
print()
 
# задание 3
a = np.array([random.random() for i in range(30)]).reshape(10, 3)
 
print(a)
 
b = abs(a - 0.5).argsort()
 
c = b[:, 0]
 
for i in range(len(c)):
    print(a[i, c[i]])