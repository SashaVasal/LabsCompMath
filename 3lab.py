import math


# поменять в соответствии с вариантом
def func(x: float):
    return x**2 + math.log(x + 5)

a = 0.5
b = 1.0

x_d = {
    1: 0.73,
    2: 0.52,
    3: 0.97,
    4: 0.73
}
# end


def difference(f_0, f_1):
    return f_0 - f_1


def main():
    count = 10
    h = (b - a) / count
    x = []
    f = [[]]

    for i in range(count + 1):
        x.append(a + h * i)
        f[0].append(func(x[i]))

    print(*f[0])
    for i in range(count):
        f.append([])
        for j in range(count - i):
            f[i+1].append(difference(f[i][j+1], f[i][j]))
        print(*f[i+1])

    t = (x_d[2] - x[0]) / h
    L_2 = float()  # Первая Ньютона
    for i in range(count + 1):
        t_product = 1.
        for j in range(i):
            t_product *= (t - j)
        L_2 += f[i][0] * t_product / math.factorial(i)
    print("L_2 = %a" % L_2)

    t = (x_d[3] - x[-1]) / h
    L_3 = float()  # Вторая Ньютона
    for i in range(count + 1):
        t_product = 1.
        for j in range(i):
            t_product *= (t + j)
        L_3 += f[i][-1] * t_product / math.factorial(i)
    print("L_3 = %a" % L_3)


if __name__ == '__main__':
    main()