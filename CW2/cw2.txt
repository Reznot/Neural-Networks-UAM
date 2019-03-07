#Siwocha Lukasz
#Cw. 2
#Python


def create_UMatrix():


    U1 = [0.0] * 26
    U2 = [0.0] * 26
    U3 = [0.0] * 26
    U4 = [0.0] * 26
    U5 = [0.0] * 26

    U1[6] = 1.0
    U1[7] = 1.0
    U1[12] = 1.0
    U1[17] = 1.0
    U1[22] = 1.0
    U1[25] = 1.0

    U2[2] = 1.0
    U2[3] = 1.0
    U2[8] = 1.0
    U2[13] = 1.0
    U2[25] = 1.0

    U3[5] = 1.0
    U3[6] = 1.0
    U3[11] = 1.0
    U3[16] = 1.0
    U3[21] = 1.0
    U3[25] = 1.0

    U4[6] = 1.0
    U4[7] = 1.0
    U4[8] = 1.0
    U4[11] = 1.0
    U4[13] = 1.0
    U4[16] = 1.0
    U4[17] = 1.0
    U4[18] = 1.0
    U4[25] = 1.0

    U5[10] = 1.0
    U5[11] = 1.0
    U5[12] = 1.0
    U5[15] = 1.0
    U5[17] = 1.0
    U5[20] = 1.0
    U5[21] = 1.0
    U5[22] = 1.0
    U5[25] = 1.0

    u = [U1, U2, U3, U4, U5]
    return u


def set_Z(t):
    if 1 + ((t - 1) % 5) <= 3:
        return 1.0
    else:
        return 0.0


def get_Y(w, u):
    y = 0.0
    for i in range(26):
        y += u[i] * w[i]

    if y >= 0:
        return 1.0
    else:
        return 0.0

def Perceptron(c):
    counter = 0
    t = 1


    #vector w with 1.0 values
    w = [1.0] * 26

    u = create_UMatrix()

    while counter != 5:
        z = set_Z(t)
        y = get_Y(w, u[(t-1) % 5])

        for i in range(26):
            w[i] = w[i] + c * (z-y) * u[(t - 1) % 5][i]

        t += 1
        if y == z:
            counter += 1
        else:
            counter = 0

    print(f"c = {c}     t = {t}  wektor wag = {w}")


Perceptron(1)
Perceptron(0.1)
Perceptron(0.01)