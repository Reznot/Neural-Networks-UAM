#Siwocha Lukasz
#Cw. 8
#Python

from math import e
from math import log
import random
import time as exectime

tZero = 5.0
temperature = 3.0
time = 5.0


def calculate_theta(vec):
    sum = 0.0
    for i in range(25):
        sum += vec[i]
    return sum


def calculate_vectorC(vec):
    out = [[] * 25] * 25
    tmp = []
    for i in range(25):
        tmp.clear()
        for j in range(25):
            if i != j:
                tmp.append((vec[i] - 0.5) * (vec[j] - 0.5))
            else:
                tmp.append(0.0)
        out[i] = tmp[:]
    return out


def calculateFuit(u):
    local = [u, temperature]
    return 1.0 / (1.0 + pow(e, -1.0 * (local[0] / local[1])))


def generateRandomVector():
    vec = [
        round(random.random() * 10), round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10), round(random.random() * 10),
        round(random.random() * 10), round(random.random() * 10),
    ]
    temp = []
    for i in range(25):
        if (vec[i] % 2 == 0):
            temp.append(1.0)
        else:
            temp.append(0.0)

    return temp


def generate_next_vector(prev, vecC):
    vec = []
    uit = 0.0
    for i in range(25):
        uit = 0.0
        for j in range(25):
            uit += 2 * vecC[i][j] * prev[j]
        uit -= calculate_theta(vecC[i])
        if uit > 0:
            vec.append(1.0)
        elif uit == 0:
            vec.append(prev[i])
        else:
            vec.append(0.0)
    return vec


def generateNextTemperature(time):
    return tZero / (1.0 + log(time))


def print_vector(vector):
    line = "|"
    for i in range(25):
        if (vector[i] <= 0.0):
            line = line + "   |"
        else:
            line = line + " * |"

        if (i % 5 == 4):
            print(line)
            line = "|"


Xs = [
    0.0, 0.0, 0.0, 0.0, 0.0,
    0.0, 1.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0, 0.0,
    0.0, 0.0, 1.0, 0.0, 0.0
]

vecC = calculate_vectorC(Xs)
vecX = generateRandomVector()
print_vector(vecX)

while (True):
    vecX = generate_next_vector(vecX, vecC)
    time += 1.0
    exectime.sleep(1)
    print("T: " + str(time) + " - temperature: " + str(temperature))
    print_vector(vecX)