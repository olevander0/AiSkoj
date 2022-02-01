import pyplot as plt

def hextriplet(colortuple):
    return '#' + ''.join(f'{i:02X}' for i in colortuple)

def final_simulation(win_chance, balance, bet_andel, games, simuleringar):
    for i, w in enumerate(range(*win_chance, 5)):
        color = (10, 0, 0)
        color = (int(30*(i+1)), int(255-(50*i)), 0)
        HEX_color = hextriplet(color)
        print(HEX_color), print(color)
        A_V, x_axel_andel, highest_balance = andels_variation(w, balance,
                                                              bet_andel, games,
                                                              simuleringar)
        plt.yscale("log")
        plt.plot(x_axel_andel, A_V, HEX_color, linewidth=2)
        plt.plot(x , y, Färg, BREDD)



def get_x_axel(all_stats):
    data = {}


    for (game, GameStats) in all_stats:

        


(50, 55, 60)

dic = {}

for par in parameter():
    Dic(par:
