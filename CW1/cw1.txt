#Siwocha Lukasz
#Cw. 1
#Python


#NOT
u2_not = 1
u_input = [0,1]
w_not = [-0.2, 0.1]
y = 0
output = 0

print("NOT:")
for u in u_input:
    y = u * w_not[0] + u2_not * w_not[1]
    if y>=0:
        output = 1
    else:
        output = 0
    print("Input: {},  Output: {}".format(u, output))


#AND & NAND
u3_and = 1
u1_and_input = [0,1,0,1]
u2_and_input = [0,0,1,1]
w_and = [0.3, 0.3, -0.5]
y = 0
output = []
output_NAND = []

for u1 in u1_and_input:
    for u2 in u2_and_input:
        y = u1 * w_and[0] + u2 * w_and[1] + u3_and * w_and[2]
        if y>= 0:
            #AND
            output.append("Input: {} {},  Output: 1".format(u1, u2))
            #NAND
            output_NAND.append("Input: {} {},  Output: 0".format(u1, u2))
        else:
            #AND
            output.append("Input: {} {},  Output: 0".format(u1, u2))
            #NAND
            output_NAND.append("Input: {} {},  Output: 1".format(u1, u2))
print("\nAND")
print(*set(output), sep="\n")
print("\nNAND")
print(*set(output_NAND), sep="\n")

#OR
u3_or = 1
u1_or_input = [0,1,0,1]
u2_or_input = [0,0,1,1]
w_or = [0.2, 0.2, -0.1]
y = 0
output_or = []

for u1 in u1_or_input:
    for u2 in u2_or_input:
        y = u1 * w_or[0] + u2 * w_or[1] + u3_or * w_or[2]
        if y>=0:
            output_or.append("Input: {} {},  Output: 1".format(u1, u2))
        else:
            output_or.append("Input: {} {},  Output: 0".format(u1, u2))

print("\nOR")
print(*set(output_or), sep="\n")
