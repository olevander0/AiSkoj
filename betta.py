from PyProbs import Probability as pr
<<<<<<< HEAD
WC = 52
=======
import matplotlib.pyplot as plt
>>>>>>> cf1c496237fd96a9b684b834ea01f8f9c1565ce6


def slump(WC):
    return pr.Prob(WC/100)


<<<<<<< HEAD
def new_balance(balance, bet_andel):
    if slump():
        balance += bet_andel*balance
    else:
        balance -= bet_andel*balance
    return balance


def simulering(balance, bet_andel, games):
    for _ in range(games):
        balance = new_balance(balance, bet_andel)
=======
def new_balance(WC, balance, bet_andel):
    if slump(WC):
        balance += bet_andel/100*balance
    else:
        balance -= bet_andel/100*balance
    return balance


def game_loop(WC, balance, bet_andel, games):
    for _ in range(games):
        balance = new_balance(WC, balance, bet_andel)
>>>>>>> cf1c496237fd96a9b684b834ea01f8f9c1565ce6
        if balance <= 0:
            break
    return balance


<<<<<<< HEAD
def sim_average(balance, bet_andel, games):
    värden = [(simulering(balance, bet_andel, games)) for _ in range(100)]
=======
def sim_average(WC, balance, bet_andel, games, simuleringar):
    värden = [(game_loop(WC, balance, bet_andel, games)) for _ in range(simuleringar)]
>>>>>>> cf1c496237fd96a9b684b834ea01f8f9c1565ce6
    average = sum(värden) / len(värden)
    return average


<<<<<<< HEAD
def andels_variation(balance, games):
    A_V = [(sim_average(balance, i/100, games), i) for i in range(10, 101)]
    return A_V


print(andels_variation(1000, 500))
=======
def andels_variation(WC, balance, bet_andel, games, simuleringar):
    x_axel_andel = [i for i in range(bet_andel[0], bet_andel[1]) if i%5]
    A_V = [sim_average(WC, balance, i, games, simuleringar) for i in range(bet_andel[0], bet_andel[1]) if i%5]
    highest_balance = max(A_V)
    return A_V, x_axel_andel, highest_balance


def hextriplet(colortuple):
    return '#' + ''.join(f'{i:02X}' for i in colortuple)


# Plotta simuleringar med varierande WC
def final_simulation(WC, balance, bet_andel, games, simuleringar):
    for i, w in enumerate(range(*WC, 10)):
        color = (10, 0, 0)
        print(i, w)
        color = (int(30*(i+1)), int(255-(50*i)), 0)
        HEX_color = hextriplet(color)
        print(HEX_color), print(color)
        A_V, x_axel_andel, highest_balance = andels_variation(w, balance, bet_andel, games, simuleringar)
        plt.yscale("log")
        plt.plot(x_axel_andel, A_V, HEX_color, linewidth = 2)


#Rörliga parametrar
WC = (30, 81)
bet_andel = (0, 101)

# Fixerade parametrar
balance = 1000
games = 50
simuleringar = 500

final_simulation(WC, balance, bet_andel, games, simuleringar)
plt.show()
>>>>>>> cf1c496237fd96a9b684b834ea01f8f9c1565ce6
