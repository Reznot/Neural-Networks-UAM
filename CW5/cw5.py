#Siwocha Lukasz
#Cw. 5
#Python

import math

flag = True
beta = 1.0
c = 1
eps = 0.000001
z = [0.0, 1.0, 1.0, 0.0]
s = [0, 1, 2]

u = []
w = []

x1 = [0.0] * 4
x2 = [0.0] * 4
x3 = [0.0] * 4

x = []
y = []

si = [0.0] * 3
s_new = [0.0] * 3
wij = [[0.0 for i in range(3)] for j in range(2)]
w_new = [[0.0 for i in range(3)] for j in range(2)]


def getF(u):
    global beta
    return 1.0 / (1.0 + math.exp(-1.0) * beta * u)


def detF(u):
    return beta * (1 - getF(u))


def calcX1(w, u):
    global x1
    for i in range(4):
        x1[i] = getF(w[0][0] * u[i][0] + w[0][1] * u[i][1] + w[0][2] * u[i][2])
    return x1


def calcX2(w, u):
    global x2
    for i in range(4):
        x2[i] = getF(w[1][0] * u[i][0] + w[1][1] * u[i][1] + w[1][2] * u[i][2])
    return x2


def getX(x1, x2, x3):
    global x
    x = [x1, x2, x3]
    return x


def calcY(s, x):
    y = [0.0] * 4
    for i in range(4):
        y[i] = (getF(s[0] * x[0][i] + s[1] * x[1][i] + s[2] * x[2][i]))
    return y


def calcSi(y, z, s, x):
    global si
    for i in range(3):
        for j in range(4):
            si[i] = (y[j] - z[j]) * detF(s[0] * x[0][j] + s[1] * x[1][j] + s[2] * x[2][j]) * x[i][j]
    return si


def calcWij(y, z, s, w, u, x):
    u1 = [0.0] * 4
    u2 = [0.0] * 4
    global wij
    for i in range(4):
        u1[i] = (s[0] * x[0][i] + s[1] * x[1][i] + s[2] * x[2][i])
    for i in range(2):
        for j in range(4):
            u2[j] += w[i][0] * u[j][0] + w[i][1] * u[j][1] + w[i][2] * u[j][2]
    for i in range(2):
        for j in range(3):
            for k in range(4):
                wij[i][j] += (y[k] - z[k]) * detF(u1[k]) * s[i] * detF(u2[k]) * u[k][j]
    return wij


def max(w_new, w, s_new, s):
    max1 = 0.0
    max2 = 0.0
    for i in range(3):
        if abs(s_new[i] - s[i]) > max1:
            max1 = abs(s_new[i] - s[i])
    for i in range(2):
        for j in range(3):
            if abs(w_new[i][j] - w[i][j]) > max2:
                max2 = abs(w_new[i][j] - w[i][j])
    if (max1 < eps) and (max2 < eps):
        return False
    else:
        return True


def train():
    global wij, w_new, x1, x2, x3, x, y, si, s_new, s, z, w, u, c, flag
    counter = 0
    while flag:
        x1 = calcX1(w, u)
        x2 = calcX2(w, u)
        x3 = [1.0, 1.0, 1.0, 1.0]
        x = getX(x1, x2, x3)
        y = calcY(s, x)
        si = calcSi(y, z, s, x)
        wij = calcWij(y, z, s, w, u, x)

        s_new[0] = s[0] - c * si[0]
        s_new[1] = s[1] - c * si[1]
        s_new[2] = s[2] - c * si[2]
        w_new[0][0] = w[0][0] - c * wij[0][0]
        w_new[0][1] = w[0][1] - c * wij[0][1]
        w_new[0][2] = w[0][2] - c * wij[0][2]
        w_new[1][0] = w[1][0] - c * wij[1][0]
        w_new[1][1] = w[1][1] - c * wij[1][1]
        w_new[1][2] = w[1][2] - c * wij[1][2]

        flag = max(w_new, w, s_new, s)
        s = s_new[:]
        w = w_new[:]
        counter = counter + 1

    print(f'iteracja: {counter}')
    print('wagi: ')
    for i in range(2):
        for j in range(3):
            # print('w' + str(i + 1) + str(j + 1) + ':' + w_new[i][j] + '\t')
            print(f"W{i+1}{j+1} : {w_new[i][j]:.0f}\t")
        print("\n")
    for i in range(3):
        # print('s' + str(i + 1) + ':' + s_new[i] + '\t')
        print(f"S{i+1} : {s_new[i]:.6f}\t")
    print()
    print("y:")
    print(f"0 XOR 0 : {y[0]}")
    print(f"1 XOR 0 : {y[1]}")
    print(f"0 XOR 1 {y[2]}")
    print(f"1 XOR 1 {y[3]}")


u.append([0, 0, 1])
u.append([1, 0, 1])
u.append([0, 1, 1])
u.append([1, 1, 1])

for i in range(3):
    w.append([0, 1, 2])
    w.append([0, 1, 2])

train()
