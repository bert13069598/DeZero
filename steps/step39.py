import numpy as np

if '__file__' in globals():
    import os, sys

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dezero import Variable
from dezero import functions as F

x = Variable(np.array([1, 2, 3, 4, 5, 6]))
y = F.sum(x)
# y.backward()
print(y)
print(x.grad)

x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
y = F.sum(x, axis=1, keepdims=True)
# y.backward()
print(y)
print(x.grad)

x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
y = x.sum(axis=1, keepdims=True)
# y.backward()
print(y)
print(x.grad)
