import math

def f(x):
    return (x**3) + 3 * (x**2) - 9 * x - 5 + math.cos(x)

def bisect(a, b, eps):
    steps = 0
    while abs(b - a) > eps:
        c = (a + b) / 2
        if f(c) == 0:
            return c, steps
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
        steps += 1
    return (a + b) / 2, steps


eps = 0.001
x1 = -5
x2 = 5

while x1 <= x2:
    if f(x1) * f(x1+eps) <= 0:
        root, steps = bisect(x1, min(x1+eps, x2), eps)
        print(f"Interval: [{x1:.3f};{min(x1+eps, x2):.3f}]")
        print(f"Value: {root:.3f}")
        print(f"Steps:{steps}")
        print()
    x1 += eps



