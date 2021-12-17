from PyProbs import Probability as pr

import matplotlib.pyplot as plt


def hextriplet(colortuple):
    return '#' + ''.join(f'{i:02X}' for i in colortuple)


WC = (40, 71)


x_axel = [i for i in range(10)]
y_axel = [i for i in range(10)]

for i, w in enumerate(range(*WC, 10)):
    color = (40, 0, 0)
    print(i, w)
    color = (int(40*(i+1)), 0, 0)
    HEX_color = hextriplet(color)
    plt.plot(x_axel, y_axel, HEX_color)
    plt.axis([x_axel[0], x_axel[-1], y_axel[0], y_axel[-1]])
    print(HEX_color), print(color)







plt.show()
