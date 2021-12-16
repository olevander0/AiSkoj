from PyProbs import Probability as pr
WC = 51
ba = 1/10


def slump():
    return pr.Prob(WC/100)


def new_balance(balance):
    if slump():
        balance += ba*balance
    else:
        balance -= ba*balance
    return balance


def simulering(balance, games):
    for _ in range(games):
        balance = new_balance(balance)
        if balance == 0:
            break
    return balance


värden = [(simulering(1000, 100)) for _ in range(50)]

print(värden)
