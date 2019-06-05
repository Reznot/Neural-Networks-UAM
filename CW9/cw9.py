import random
import math

cities = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
L = 3
M = 100
T0 = 1.0


def dist(a, b):
    if ((a == 1 & b == 10) | (a == 10 & b == 1)):
        d = 1
    else:
        d = abs(a - b)
    return (d)


def changeT(T, T0, t):
    T = T0 / (1 + math.log(t + 1))
    return (T)


def swap_S(S):
    rs = random.sample(range(0, 10), 2)
    zm_pom = S[rs[0]]
    S[rs[0]] = S[rs[1]]
    S[rs[1]] = zm_pom
    return (S)


def cost(S):
    e = 0
    for i in range(0, 9):
        e = e + dist(S[i], S[i + 1])
    e = e + dist(S[9], S[0])
    return (e)


def simmulated_annealing():
    S = random.sample(range(1, 11), 10)
    E_old = cost(S)
    T = T0
    ar = 0
    while (ar <= L):
        t = 0
        ar = 0
        while (t < M):
            S_old = S[:]
            E_old = cost(S_old)
            S_new = swap_S(S_old)
            E_new = cost(S_new)
            deltaE = E_old - E_new
            if ((deltaE < 0) | (random.uniform(0, 1) < math.exp(-deltaE / T))):
                S = S_new
                ar = ar + 1
            t = t + 1
        T = changeT(T, T0, t)
    print("Zadanie 1")
    print("S:", *S)
    print("Koszt:", cost(S))


simmulated_annealing()


def dist2(a, b):
    if ((a == 1 & b == 2) | (a == 9 & b == 10)):
        d = 1
    elif (a < b):
        d = a * a * a + b * b * b - a * a * b - a * b * b + 4 * a * a - 4 * b * b + 4 * a - 4 * b + 1
    elif (a > b):
        d = dist(a, b)
    elif (a == b):
        d = 0
    return (d)


def cost2(S):
    e = 0
    for i in range(0, 9):
        e = e + dist2(S[i], S[i + 1])
    e = e + dist2(S[9], S[0])
    return (e)


def simmulated_annealing2():
    S = random.sample(range(1, 11), 10)
    E_old = cost2(S)
    T = T0
    ar = 0
    while (ar <= L):
        t = 0
        ar = 0
        while (t < M):
            S_old = S[:]
            E_old = cost2(S_old)
            S_new = swap_S(S_old)
            E_new = cost2(S_new)
            deltaE = E_old - E_new
            if ((deltaE < 0) | (random.uniform(0, 1) < math.exp(-deltaE / T))):
                S = S_new
                ar = ar + 1
            t = t + 1
        T = changeT(T, T0, t)
    print("\nZadanie 2")
    print("S:", *S)
    print("Koszt:", cost2(S))


simmulated_annealing2()