#Siwocha Lukasz
#Cw. 7
#Python

import time
import random

def calculate_theta(vec):
    sum = 0.0
    for i in range(25):
        sum += vec[i]
    return sum

def calculate_theta2(vec, vec2):
    sum = 0.0
    for i in range(25):
        sum += vec[i]
        sum += vec2[i]
    return sum;

def calculate_vectorC(vec):
    out = [[]*25] * 25
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

def generate_random_vector():
    vec = []
    random.seed(time.time())
    for i in range(25):
        if random.randint(0, 1000) % 2 == 0:
            vec.append(1.0)
        else:
            vec.append(0.0)
    return vec

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

def generate_next_vector2(prev, vecC, vecD):
    vec = []
    uit = 0.0
    for i in range(25):
        uit = 0.0
        for j in range(25):
            uit += 2 * (vecC[i][j] + vecD[i][j]) * prev[j]
        uit -= calculate_theta(vecC[i])

        if uit > 0:
            vec.append(1.0)
        elif uit == 0:
            vec.append(prev[i])
        else:
            vec.append(0.0)
    return vec

def print_vector(vec):
    for i in range(25):
        if vec[i] == 0.0:
            print("-", end='')
        else:
            print("*", end="")
        if i % 5 == 4:
            print()
    print("\n\n")

vecXs = [0.0] * 25
vecXs[6] = 1.0
vecXs[7] = 1.0
vecXs[12] = 1.0
vecXs[17] = 1.0
vecXs[22] = 1.0

vecC = [[0 for x in range(25)] for y in range(25)]
vecC = calculate_vectorC(vecXs)

vecXr = [0.0] * 25
vecXr[1] = 1.0
vecXr[2] = 1.0
vecXr[3] = 1.0
vecXr[6] = 1.0
vecXr[8] = 1.0
vecXr[11] = 1.0
vecXr[13] = 1.0
vecXr[16] = 1.0
vecXr[18] = 1.0
vecXr[21] = 1.0
vecXr[22] = 1.0
vecXr[23] = 1.0

vecD = [[0 for x in range(25)] for y in range(25)]
vecD = calculate_vectorC(vecXr)

vecX = generate_random_vector()
print_vector(vecX)

while True:
        time.sleep(1)
        vecX = generate_next_vector2(vecX, vecC, vecD)
        print_vector(vecX)

