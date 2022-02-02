from PyProbs import Probability as pr
import random


def new_balance(game):
    def slump(win_chance):
        return pr.Prob(win_chance/100)
    new_balance = game.balance
    for _ in range(game.bets):
        dx = 0
        if slump(game.win_chance):
            dx = game.bet_andel/100*new_balance
        else:
            dx = -game.bet_andel/100*new_balance
        new_balance += dx
    return new_balance


def new_balance_double(game):
    def slump(win_chance):
        return pr.Prob(win_chance/100)
    new_balance = game.balance
    dx = game.bet_andel/100*new_balance
    for _ in range(game.bets):
        if slump(game.win_chance):
            new_balance += dx
            dx = game.bet_andel/100*new_balance
        else:
            new_balance -= dx
            dx = dx * 2
        if new_balance <= 0:
            return 0
    return new_balance


def winrate



def win_seq(game):
    def slump(win_chance):
        return pr.Prob(win_chance/100)
    return (slump(game.win_chance) for ):



def test(game):
    bal = 0
    for i in range(game.bets):
        bal += random.randint(1, 9)*10**(i)
    return(bal)


def get_functions():
    functions = {"new_balance": new_balance,
                 "new_balance_double": new_balance_double,
                 "test": test}
    return functions
