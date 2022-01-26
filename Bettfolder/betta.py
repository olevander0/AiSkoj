

from PyProbs import Probability as pr
import matplotlib.pyplot as plt


def slump(win_chance):
    return pr.Prob(win_chance/100)


def new_balance(win_chance, balance, bet_andel):
    dx = bet_andel/100*balance if slump(win_chance) else -bet_andel/100*balance
    balance += dx
    return balance


def game_loop(win_chance, balance, bet_andel, games):
    for _ in range(games):
        balance = new_balance(win_chance, balance, bet_andel)
        if balance <= 0:
            break
    return balance


def sim_average(win_chance, balance, bet_andel, games, simuleringar):
    värden = [(game_loop(win_chance, balance,
              bet_andel, games)) for _ in range(simuleringar)]
    average = sum(värden) / len(värden)
    return average


def andels_variation(win_chance, balance, bet_andel, games, simuleringar):
    x_axel_andel = [i for i in range(bet_andel[0], bet_andel[1])]
    print(x_axel_andel)
    A_V = [sim_average(win_chance, balance, i, games,
           simuleringar) for i in range(bet_andel[0], bet_andel[1])]
    highest_balance = max(A_V)
    return A_V, x_axel_andel, highest_balance


def hextriplet(colortuple):
    return '#' + ''.join(f'{i:02X}' for i in colortuple)


# Plotta simuleringar med varierande win_chance
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


# Rörliga parametrar
win_chance = (50, 71)
bet_andel = (0, 101)

# Fixerade parametrar
balance = 1000
games = 10
simuleringar = 50
s = sim_average(51, 1000, 5, 100, 100)
print(s)
# final_simulation(win_chance, balance, bet_andel, games, simuleringar)
# plt.show()
