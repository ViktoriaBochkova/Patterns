import math


def decorator(fn):
    def first(a, b, c):
        print("Run method: " + str(fn.__name__) + " with arguments : " + str(a) + "," + str(b) + "," + str(c))
        fn(a, b, c)
        print("Stop method: " + str(fn.__name__))

    return first


@decorator
def Discriminant(a: float, b: float, c: float):
    disc = b ** 2 - 4 * a * c
    print("Дискриминант D = %.2f" % disc)
    if disc > 0:
        x1 = (-b + math.sqrt(disc)) / (2 * a)
        x2 = (-b - math.sqrt(disc)) / (2 * a)
        print("x1 = %.2f \nx2 = %.2f" % (x1, x2))
    elif disc == 0:
        x = -b / (2 * a)
        print("x = %.2f" % x)
    else:
        print("Корней нет")


Discriminant(1.5, 5, 4)
