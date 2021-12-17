from PyProbs import Probability as pr
WC = 52


def slump():
    return pr.Prob(WC/100)


def new_balance(balance, bet_andel):
    if slump():
        balance += bet_andel*balance
    else:
        balance -= bet_andel*balance
    return balance


def simulering(balance, bet_andel, games):
    for _ in range(games):
        balance = new_balance(balance, bet_andel)
        if balance <= 0:
            break
    return balance


def sim_average(balance, bet_andel, games):
    värden = [(simulering(balance, bet_andel, games)) for _ in range(100)]
    average = sum(värden) / len(värden)
    return average


def andels_variation(balance, games):
    A_V = [(sim_average(balance, i/100, games), i) for i in range(10, 101)]
    return A_V


print(andels_variation(1000, 500))
