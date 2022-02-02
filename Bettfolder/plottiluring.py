import pyplot as plt

def get_data_dict(all_stats):
    data = {}
    for Game, GameStats in all_stats:
        if Game.win_chance not in data.keys():
            data[Game.win_chance] = [[Game.bet_andel], [GameStats.average]]
        else:
            data[Game.win_chance][0].append(Game.bet_andel)
            data[Game.win_chance][1].append(GameStats.average)
    return data


def
    for i, key in enumerate(plt_data):





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
