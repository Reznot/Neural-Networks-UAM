import math
import numpy as np


def check_epsilon(s_new, s_old, w_new, w_old, eps):
    ret = False
    for i in range(2):
        for j in range(3):
            if max(abs(s_new[i] - s_old[i]), abs(w_new[i][j] - w_old[i][j])) < eps:
                ret = True
    return ret


def f(u, beta):
    return 1 / (1 + math.pow(math.e, (-beta * u)))


def f_prim(u, beta):
    val = f(u, beta)
    return beta * val * (1 - val)


def de_s(s, x, y, z, i, beta):
    sum = 0.0
    for p in range(4):
        sum += (
                (y[p] - z[p]) *
                f_prim(
                    s[0] * x[p][0] +
                    s[1] * x[p][1] +
                    s[2] * x[p][2],
                    beta
                ) * x[p][i]
        )
    return sum


def de_w(s, x, y, z, i, j, beta, u, w):
    sum = 0.0
    for p in range(4):
        sum += (
                (y[p] - z[p]) *
                f_prim(
                    s[0] * x[p][0] +
                    s[1] * x[p][1] +
                    s[2] * x[p][2],
                    beta
                ) * s[i] *
                f_prim(
                    w[i][0] * u[p][0] +
                    w[i][1] * u[p][1] +
                    w[i][2] * u[p][2],
                    beta
                ) * u[p][j]
        )
    return sum


def get_s_new(s_old, c, de_s):
    s_new = []
    for i in range(3):
        s_new.append(s_old[i] - c * de_s[i])
    return s_new


def get_w_new(w_old, c, de_w):
    w_new = [[], []]
    for i in range(2):
        for j in range(3):
            w_new[i].append(w_old[i][j] - c * de_w[i][j])
    return w_new


def iterate(U, W, S_old, c, beta):
    S = S_old
    Z = [0, 1, 1, 0]

    x = [[], [], [], []]
    y = []

    DE_s = []
    DE_w = [[], [], []]

    for p in range(4):
        x[p].append(f(
            W[0][0] * U[p][0] +
            W[0][1] * U[p][1] +
            W[0][2] * U[p][2],
            beta
        ))
        x[p].append(f(
            W[1][0] * U[p][0] +
            W[1][1] * U[p][1] +
            W[1][2] * U[p][2],
            beta
        ))
        x[p].append(1)

        y.append(
            f(
                S[0] * x[p][0] +
                S[1] * x[p][1] +
                S[2] * x[p][2],
                beta
            )
        )

    for i in range(3):
        DE_s.append(
            de_s(S, x, y, Z, i, beta)
        )

    for i in range(2):
        for j in range(3):
            DE_w[i].append(
                de_w(S, x, y, Z, i, j, beta, U, W)
            )

    s_new = get_s_new(S, c, DE_s)
    w_new = get_w_new(W, c, DE_w)

    return s_new, w_new, y


def main(c, eps, beta):
    U = [
        [0, 0, 1],
        [1, 0, 1],
        [0, 1, 1],
        [1, 1, 1]
    ]
    W = [
        [0, 1, 2],
        [0, 1, 2]
    ]
    S = [0, 1, 2]
    Beta = beta
    Eps = eps
    c = c
    s_new, w_new, y = iterate(U, W, S, c, Beta)
    while (not check_epsilon(s_new, S, w_new, W, Eps)):
        S = s_new
        W = w_new
        s_new, w_new, y = iterate(U, W, S, c, Beta)

    print(f"____________________________\nC: {c}, Epsilon: {eps}, Beta: {beta}\n")
    print("============\nW:")
    for w in w_new:
        print(*w)
    print("============\nS:")
    for s in s_new:
        print(s)
    print("============\nY")
    print(*y)


if __name__ == "__main__":
    eps = 0.0001
    for c in np.arange(0.1, 1.1, 0.1):
        for beta in np.arange(1.0, 4.0, 1.0):
            main(c, eps, beta)