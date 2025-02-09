import matplotlib.pyplot as plt
from circle import circle

def visualize(r_input, radius, celldm):
    plt.figure()
    plt.axis('equal')
    plt.xlim(0, 1)
    plt.ylim(0, 1)
    for pos in r_input:
        circle(pos[0], pos[1], radius/2)
        if pos[0] - radius/2 < 0:
            circle(pos[0] + celldm, pos[1], radius/2)
        if pos[0] + radius/2 > 1:
            circle(pos[0] - celldm, pos[1], radius/2)
        if pos[1] - radius/2 < 0:
            circle(pos[0], pos[1] + celldm, radius/2)
        if pos[1] + radius/2 > 1:
            circle(pos[0], pos[1] - celldm, radius/2)
        if pos[0] - radius/2 < 0 and pos[1] - radius/2 < 0:
            circle(pos[0] + celldm, pos[1] + celldm, radius/2)
        if pos[0] + radius/2 > 1 and pos[1] + radius/2 > 1:
            circle(pos[0] - celldm, pos[1] - celldm, radius/2)
