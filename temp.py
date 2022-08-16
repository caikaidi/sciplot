import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0, 10, 100)
y = np.sin(x)

def f(a, *args):
    print(a)
    print(args)
    print(args[0])
    print(args[4])

f(1, 2,3)