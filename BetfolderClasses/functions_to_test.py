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


def win_seq(antal, wc):
    def slump(wc):
        return pr.Prob(wc/100)
    return tuple(slump(wc) for _ in range(antal))


def test(game):
    bal = 0
    for i in range(game.bets):
        bal += random.randint(1, 9)*10**(i)
    return(bal)


def get_change_factor(game):
    win = 1 + game.bet_andel/100
    loss = 1 - game.bet_andel/100
    # print(w)
    for i in range(100):
        if i < game.win_chance:
            x *= win
        else:
            x *= loss
    return x


def get_functions():
    functions = {"new_balance": new_balance,
                 "new_balance_double": new_balance_double,
                 "test": test,
                 "get_change_factor": get_change_factor}
    return functions


def main():
    seq = win_seq(100, 50)
    print(seq)


if __name__ == '__main__':
    main()
