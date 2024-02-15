import math

import numpy as np

if '__file__' in globals():
    import os, sys

    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from dezero import Variable, sin
from dezero.utils import plot_dot_graph

x = Variable(np.array(np.pi / 4))
y = sin(x)
y.backward()

print(y.data)
print(x.grad)


def taylor_sin(x, threshold=0.0001):
    y = 0
    for i in range(10000):
        c = (-1) ** i / math.factorial(2 * i + 1)
        t = c * x ** (2 * i + 1)
        y = y + t
        if abs(t.data) < threshold:
            break
    return y


x.cleargrad()
y = taylor_sin(x)
y.backward()

print(y.data)
print(x.grad)
plot_dot_graph(y, verbose=False, to_file='taylor_sin.png')
