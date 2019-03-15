#Siwocha Lukasz
#Cw. 3
#Python


def init_vector(value, size):
    vector = [value] * size
    return vector


def generate_z0(type):
    z0 = init_vector(-1.0, 25)

    if type == "normal":
        z0[6] = 1.0
        z0[7] = 1.0
        z0[8] = 1.0
        z0[11] = 1.0
        z0[13] = 1.0
        z0[16] = 1.0
        z0[17] = 1.0
        z0[18] = 1.0
    elif type == "disturbed":
        z0[1] = 1.0
        z0[2] = 1.0
        z0[3] = 1.0
        z0[6] = 1.0
        z0[8] = 1.0
        z0[11] = 1.0
        z0[13] = 1.0
        z0[16] = 1.0
        z0[17] = 1.0
        z0[18] = 1.0

    return z0


def generate_z1(type):
    z1 = init_vector(-1.0, 25)

    if type == "normal":
        z1[6] = 1.0
        z1[7] = 1.0
        z1[12] = 1.0
        z1[17] = 1.0
    elif type == "disturbed":
        z1[2] = 1.0
        z1[7] = 1.0
        z1[12] = 1.0
        z1[17] = 1.0
        z1[22] = 1.0

    return z1


def calculate_Wmatrix(z0, z1):
    W = [[0 for x in range(25)] for y in range(25)]

    for i in range(25):
        for j in range(25):
            W[i][j] = 1.0 / 25.0 * (z0[i] * z0[j] + z1[i] * z1[j])
    return W


def calculate_sgn(vec):
    for i in range(25):
        if vec[i] >= 0.0:
            vec[i] = 1.0
        else:
            vec[i] = -1.0
    return vec


def calculate_F(W, u):
    y = init_vector(0.0, 25)
    y_value = 0.0

    for i in range(25):
        for j in range(25):
            y_value += W[i][j] * u[j]
        y[i] = y_value
        y_value = 0.0
    y = calculate_sgn(y)
    return y


def print_results(vec):
    for i in range(25):
        if vec[i] == -1.0:
            print("-", end="")
        else:
            print("*", end="")
        if i % 5 == 4:
            print()
    print("\n")

z0 = generate_z0("normal")
z0_ = generate_z0("disturbed")
z1 = generate_z1("normal")
z1_ = generate_z1("disturbed")

W = calculate_Wmatrix(z0, z1)
y = [0.0] * 25

#Z0
print("z0")
y = calculate_F(W, z0)
print_results(y)

#Z0 disturbed
print("z0 disturbed")
y = calculate_F(W, z0_)
print_results(y)

#Z1
print("z1")
y = calculate_F(W, z1)
print_results(y)

#Z1 disturbed
print("z1 disturbed")
y = calculate_F(W, z1_)
print_results(y)