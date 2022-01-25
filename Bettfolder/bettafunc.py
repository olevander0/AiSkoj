import collections
from PyProbs import Probability as pr
import multiprocessing
# import matplotlib.pyplot as plt
from pprint import pprint

game = collections.namedtuple("game", [
        "balance",
        "bet_andel",
        "win_chance",
        "bets"])


def create_game_inputs(arg, antal):
    output = (arg for _ in range(antal))
    return tuple(output)


def create_games(arguments):
    newgames = (game(balance=arg[0],
                bet_andel=arg[1],
                win_chance=arg[2],
                bets=arg[3]) for arg in arguments)
    return tuple(newgames)


def create_new_balances(games, balances):
    newgames = (game(balance=balances[i],
                bet_andel=games[i].bet_andel,
                win_chance=games[i].win_chance,
                bets=0) for i in range(len(games)))
    return tuple(newgames)


def slump(win_chance):
    return pr.Prob(win_chance/100)


def new_balance(game):
    new_balance = game.balance
    print(game.bets)
    for _ in range(game.bets):
        dx = 0
        if slump(game.win_chance):
            dx = game.bet_andel/100*new_balance
        else:
            dx = -game.bet_andel/100*new_balance
        # dx beräknar mängden vinst/förlust
        new_balance += dx
    return new_balance


def new_balances(games):  # ger en tuple med samtliga updaterade balances
    pool = multiprocessing.Pool()
    updated_game = pool.map(new_balance, games)
    # updated_game = map(new_balance, games)
    return tuple(updated_game)


def main():
    arguments = create_game_inputs((1000, 10, 51, 1000), 10)

    games = create_games(arguments)
    games2 = (game(balance=1, bet_andel="hej", win_chance=2, bets=3),
              game(balance=1000, bet_andel="hej", win_chance=2, bets=3))

    print(games2[1].balance)

    pprint(games)
    new_games = create_new_balances(games, new_balances(games))
    pprint(new_games)


if __name__ == '__main__':
    main()
