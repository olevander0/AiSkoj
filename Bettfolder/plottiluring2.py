import matplotlib.pyplot as plt
from analyse_game_data import gen_data
from pprint import pprint

import matplotlib.patches as mpatches


def hextriplet(colortuple):
    return '#' + ''.join(f'{i:02X}' for i in colortuple)


def get_graphs(all_stats):
    data = {}

    def add_axes_to_color(color_list, x_axel, y_axel):
        color_list.append((x_axel, y_axel))
    for (game, GameStats) in all_stats:
        if game.win_chance not in data:
            data[game.win_chance] = []
        add_axes_to_color(data[game.win_chance],
                          game.bet_andel, GameStats.average)
    return data


def plot_data(data):
    color_names = []
    for i, (w_c, tupled_axes) in enumerate(data.items()):
        color = (10, 0, 0)
        color = (int(30*(i+1)), int(255-(50*i)), 0)
        x_axel, y_axel = zip(*tupled_axes)
        hex = hextriplet(color)
        f = f"{w_c}% winchance"
        color_names.append(mpatches.Patch(color=hex, label=f))
        plt.ylim((-100, 10000))
        plt.plot(x_axel, y_axel, hex, linewidth=2)
    plt.legend(handles=color_names)
    plt.show()


def main():
    game_data = gen_data()
    pprint(game_data)

    data = get_graphs(game_data)
    pprint(data)

    plot_data(data)


if __name__ == "__main__":
    main()
