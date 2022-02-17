import matplotlib.pyplot as plt
from pprint import pprint
from B_simulate_games import get_stats
import matplotlib.patches as mpatches


def hextriplet(colortuple):
    return '#' + ''.join(f'{i:02X}' for i in colortuple)


def unpack_axes(games):
    bet_andelar, multipliers = [], []
    for game in games:
        bet_andelar.append(game.bet_andel)
        multipliers.append(game.multiplier)
    return bet_andelar, multipliers


def plot_data(data):
    # color_names = []
    for i, (w_c, tupled_axes) in enumerate(data.items()):
        x_axel, y_axel = unpack_axes(tupled_axes)
        color = (10, 0, 0)
        color = (int(255/((i+1)*2)), int(i*2), i*3)
        hex = hextriplet(color)
    #    f = f"{w_c}% winchance"
        # color_names.append(mpatches.Patch(color=hex, label=f))
        plt.yscale("log")
        plt.plot(x_axel, y_axel, hex, linewidth=2)
    # plt.legend(handles=color_names)
    plt.show()


def plot_data2(data):
    x_axel, y_axel = [], []
    for w_c, maxvals in data.items():
        x_axel.append(w_c)
        y_axel.append(maxvals[1])
    color = (10, 0, 0)
    hex = hextriplet(color)
    # plt.yscale("log")
    plt.plot(x_axel, y_axel, hex, linewidth=2)
    plt.show()


def main():
    data, data2 = get_stats()
    pprint(data)
    plot_data(data)
    plot_data2(data2)


if __name__ == "__main__":
    main()
