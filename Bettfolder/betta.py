<<<<<<< HEAD
=======
from PyProbs import Probability as pr
import multiprocessing
import matplotlib.pyplot as plt
from pprint import pprint


def slump(win_chance):  # Returnar True/False i proportion till winchance
    return pr.Prob(win_chance/100)


def new_balance(win_chance, balance, bet_andel):  # Updaterar balance
    dx = bet_andel/100*balance if slump(win_chance) else -bet_andel/100*balance
    # dx beräknar mängden vinst/förlust
    balance += dx
    return balance


def game_loop(arg):
    print("in")
    win_chance, balance, bet_andel, games = arg
    # print("in")
    for _ in range(games):
        balance = new_balance(win_chance, balance, bet_andel)
        if balance <= 0:
            break
    # print(balance)
    print("out")
    return balance


def sim_average(win_chance, balance, bet_andel, games, simuleringar):

    arguments = ((win_chance, balance, bet_andel, games)
                 for _ in range(simuleringar))

    # pprint(arguments)
    pool = multiprocessing.Pool()
    """
    värden = [(game_loop(win_chance, balance,
              bet_andel, games)) for _ in range(simuleringar)]
    """
    värden = pool.map(game_loop, arguments)

    # värden = list(värden)
    print(värden, "värden")
    average = sum(värden) / len(värden)
    return average


def andels_variation(win_chance, balance, bet_andel, games, simuleringar):
    x_axel_andel = [i for i in range(bet_andel[0], bet_andel[1]) if i % 5]
    print(bet_andel[0], bet_andel[1], "betande")
    #pprint(x_axel_andel)
    A_V = [sim_average(win_chance, balance, i, games,
           simuleringar) for i in range(bet_andel[0], bet_andel[1]) if i % 5]
    highest_balance = max(A_V)
    return A_V, x_axel_andel, highest_balance


def hextriplet(colortuple):
    return '#' + ''.join(f'{i:02X}' for i in colortuple)


# Plotta simuleringar med varierande win_chance
def final_simulation(win_chance, balance, bet_andel, games, simuleringar):
    for i, w in enumerate(range(*win_chance, 5)):
        color = (10, 0, 0)
        # print(i, w)
        color = (int(30*(i+1)), int(255-(50*i)), 0)
        HEX_color = hextriplet(color)
        # print(HEX_color), print(color)
        A_V, x_axel_andel, highest_balance = andels_variation(w, balance,
                                                              bet_andel, games,
                                                              simuleringar)
        plt.yscale("log")
        plt.plot(x_axel_andel, A_V, HEX_color, linewidth=2)


def main():
    # Rörliga parametrar
    win_chance = (50, 71)
    bet_andel = (50, 61)

    # Fixerade parametrar
    balance = 1000
    games = 5
    simuleringar = 5

    final_simulation(win_chance, balance, bet_andel, games, simuleringar)
    plt.show()


if __name__ == '__main__':
    main()
>>>>>>> 629068550cf90459ae5b9edbb594af72077bda8a
