import matplotlib.pyplot as plt
from pprint import pprint

def hextriplet(colortuple):
    return '#' + ''.join(f'{i:02X}' for i in colortuple)


def optic():
    OP = {}
    for wc in range(50, 101):
        OP[wc] = (1, 0)
    return OP


def andringsfaktor(bet_andel, OP):
    # winning_wc = []

    for wc in range(50, 101):

        x = 1
        win = 1 + bet_andel/100
        loss = 1 - bet_andel/100
        # print(w)
        for i in range(100):
            if i<wc:
                x*= win
            else:
                x*= loss
        if x > 1:
            # winning_wc.append((wc, x))
            if x > OP[wc][0]:
                OP[wc] = (x, bet_andel)


# winning_wc = andringsfaktor(12)
#print(winning_wc)

def get_OP():
    OP = optic()
    for bet in range(1, 101):
        andringsfaktor(bet, OP)
    return OP


pprint(get_OP())
OP = get_OP()



x_axel = []
y_axel = []
col_axel = []
for key, (faktor, betandel) in OP.items():
    x_axel.append(key)
    y_axel.append(faktor)
    col_axel.append(betandel)

color = (0, 255, 0)
color2 = (255, 0, 0)
hex = hextriplet(color)
hex2 = hextriplet(color2)
plt.yscale("log")
plt.plot(col_axel, y_axel, hex, linewidth=2)
plt.plot(x_axel, y_axel, hex2, linewidth=2)
plt.show()


"""
def get_WC_ensure_win():
    list = []
    list2 = []
    for bet in range(1, 100):
        wc, x = andringsfaktor(bet)
        list.append((wc, bet))
        list2.append((x, bet))
    return list, list2





FACK_THIS_SHIT, pack_this_shit = get_WC_ensure_win()

y_axel, x_axel = zip(*FACK_THIS_SHIT)
y_axel2, x_axel2 = zip(*pack_this_shit)


print(x_axel, y_axel)

print(FACK_THIS_SHIT)



color = (255, 0, 0)
color2 = (0, 255, 0)
hex = hextriplet(color)
hex2 = hextriplet(color2)
#plt.figure(200)
plt.plot(x_axel, y_axel, hex, linewidth=2)
#plt.show()
#plt.figure(300)
plt.plot(x_axel2, y_axel2, hex2, linewidth=2)
plt.show()
"""
