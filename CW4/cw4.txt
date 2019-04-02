#Siwocha Lukasz
#Cw. 4
#Python

def getF(xt):
    F = 2 * pow(xt[0], 2) + 2 * pow(xt[1], 2) + pow(xt[2], 2) - 2 * xt[0] * xt[1] * xt[2] - 2 * xt[1] + 3
    return F


def getG(xt):
    G = 3 * pow(xt[0], 4) + 4 * pow(xt[0], 3) - 12 * pow(xt[0], 2) + 12 * pow(xt[1], 2) - 24 * xt[1]
    return G


def max(xt_new, xt_prev, f_name):
    eps = 0.00000001
    max_val = 0.0
    if f_name == 'f':
        for i in range(3):
            if abs(xt_new[i] - xt_prev[i]) > max_val:
                max_val = abs(xt_new[i] - xt_prev[i])

    if f_name == 'g':
        for i in range(2):
            if abs(xt_new[i] - xt_prev[i]) > max_val:
                max_val = abs(xt_new[i] - xt_prev[i])

    if max_val < eps:
        return False
    else:
        return True


def gradient(xt_prev, f_name):
    c = 0.01
    flag = True
    if f_name == 'f':
        xt_new = []
        while flag:
            xt_new.append(xt_prev[0] - c * (4.0 * xt_prev[0] - 2.0 * xt_prev[1] - 2.0))
            xt_new.append(xt_prev[1] - c * (-2.0 * xt_prev[0] + 4.0 * xt_prev[1] - 2.0 * xt_prev[2]))
            xt_new.append(xt_prev[2] - c * (-2.0 * xt_prev[1] + 2.0 * xt_prev[2]))
            flag = max(xt_new, xt_prev, 'f')
            xt_prev = xt_new
        print(f'\nf:{xt_new}')
        print(f'x = {xt_new[0]:.3f}')
        print(f'y = {xt_new[1]:.3f}')
        print(f'z = {xt_new[2]:.3f}')
        print(f'f(x,y,z)= {getF(xt_new):.3f}')

    if f_name == 'g':
        xt_new = []
        while flag:
            xt_new.append(xt_prev[0] - c * (12 * pow(xt_prev[0], 3) + 12 * pow(xt_prev[0], 2) - 24 * xt_prev[0]))
            xt_new.append(xt_prev[1] - c * ((24 * xt_prev[1]) - 24))
            flag = max(xt_new, xt_prev, 'g')
            xt_prev = xt_new
        print('\ng:')
        print(f'x = {xt_new[0]:.3f}')
        print(f'y = {xt_new[1]:.3f}')
        print(f'f(x,y,z)= {getG(xt_new):.3f}')


xt = [1, 0, 1]
gradient(xt, 'f')
xt = [4, 4]
gradient(xt, 'g')