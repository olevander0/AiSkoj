from PyProbs import Probability as pr
ba = 25/100
WC = 55
pr.Prob(WC/100)



def slump():
    return pr.Prob(WC/100)



def new_balance(balance):
    if slump():
        balance += ba*balance
    else:
        balance -= ba*balance
    return balance


def simmulering(balance, games):
    for _ in range(games):
        balance = new_balance(balance)
        if balance == 0:
            break
    return balance

def tjena(balance, games):
    for _ in range(50):
        print (simmulering(balance, games))


tjena(100, 100)
