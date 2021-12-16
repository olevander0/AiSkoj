from PyProbs import Probability as pr
<<<<<<< HEAD
ba = 25/100
WC = 55
pr.Prob(WC/100)

=======
WC = 51
ba = 1/10
>>>>>>> 4e9e6fe299869be646094227eda86a4ac4659f9b


def slump():
    return pr.Prob(WC/100)


<<<<<<< HEAD

=======
>>>>>>> 4e9e6fe299869be646094227eda86a4ac4659f9b
def new_balance(balance):
    if slump():
        balance += ba*balance
    else:
        balance -= ba*balance
    return balance


<<<<<<< HEAD
def simmulering(balance, games):
=======
def simulering(balance, games):
>>>>>>> 4e9e6fe299869be646094227eda86a4ac4659f9b
    for _ in range(games):
        balance = new_balance(balance)
        if balance == 0:
            break
    return balance

<<<<<<< HEAD
def tjena(balance, games):
    for _ in range(50):
        print (simmulering(balance, games))


tjena(100, 100)
=======

värden = [(simulering(1000, 100)) for _ in range(50)]

print(värden)
>>>>>>> 4e9e6fe299869be646094227eda86a4ac4659f9b
