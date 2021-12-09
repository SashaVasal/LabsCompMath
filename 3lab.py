import math


# поменять в соответствии с вариантом
def func(x: float):
    return x ** 2 + math.log(x + 5)


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
    print(*x)

    print(*f[0])
    for i in range(count):
        f.append([])
        for j in range(count - i):
            f[i + 1].append(difference(f[i][j + 1], f[i][j]))
        print(*f[i + 1])

    # Первая Ньютона
    t = (x_d[2] - x[0]) / h
    N_1 = 0.
    for i in range(count + 1):
        t_product = 1.
        for j in range(i):
            t_product *= (t - j)
        N_1 += f[i][0] * t_product / math.factorial(i)
    print("N_1 = %a" % N_1)

    # Вторая Ньютона
    t = (x_d[3] - x[-1]) / h
    N_2 = 0.
    for i in range(count + 1):
        t_product = 1.
        for j in range(i):
            t_product *= (t + j)
        N_2 += f[i][-1] * t_product / math.factorial(i)
    print("N_2 = %a" % N_2)

    # Поиск ближайшего к x****
    diff = x_d[4] - x[0]
    pos = 0
    for i in range(len(x)):
        if abs(x_d[4] - x[i]) <= diff:
            pos = i
            diff = abs(x_d[4] - x[i])
    # Вторая Гаусса для интерполирования вперед
    t = (x_d[4] - x[pos])
    G_2 = 0.
    for i in range(count + 1):
        t_product = 1.
        for j in range(i):
            t_product *= (t + j) if j % 2 == 0 else (t - j)
        tmp = 1 if i % 2 == 0 else 0
        pos = pos - i + tmp
        G_2 += f[i][pos] * t_product / math.factorial(i)
    print("G_2 = %a" % G_2)


if __name__ == '__main__':
    main()
