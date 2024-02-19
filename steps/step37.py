import numpy as np

if '__file__' in globals():
    import os, sys

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import dezero.functions as F
from dezero import Variable

x = Variable(np.array(1.0))
y = F.sin(x)
print(y)

var = np.pi / 4
x = Variable(np.array([[var, var * 2, var * 4], [var, var * -2, var * -4]]))
print(x)

x = Variable(np.array([[1, 2, 3], [4, 5, 6]]))
c = Variable(np.array([[10, 20, 30], [40, 50, 60]]))
print(x + c)


