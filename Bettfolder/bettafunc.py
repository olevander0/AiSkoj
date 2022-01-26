import collections
from PyProbs import Probability as pr
import multiprocessing
import itertools
# import math as m
# import matplotlib.pyplot as plt
from pprint import pprint
import statistics

game_atribut = [
        "balance",
        "bet_andel",
        "win_chance",
        "bets"]


game = collections.namedtuple("game", game_atribut)


def copy_game(game, antal):
    return tuple((game for _ in range(antal)))


def copy_games(games, antal):
    listed_games = []
    for game in games:
        for _ in range(antal):
            listed_games.append(game)
    return tuple(listed_games)


"""
def create_game_inputs(arg, antal):
    output = (arg for _ in range(antal))
    return tuple(output)


def create_games(arguments):
    newgames = map(lambda arg: (game(*arg)), arguments)
    return tuple(newgames)
"""


def create_new_balances(games, balances):
    def update_bal(args):
        game, bal = args
        return game._replace(balance=bal, bets=0)
    newgames = map(update_bal, zip(games, balances))
    return tuple(newgames)


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


def new_balances(games):  # ger en tuple med samtliga updaterade balances
    pool = multiprocessing.Pool()
    balances = pool.map(new_balance, games)
    # updated_game = map(new_balance, games)
    return tuple(balances)


def new_balances_all(all_games):
    for games in all_games:
        pass


def main():
    game_single1 = game(balance=1000,
                        bet_andel=25,
                        win_chance=55,
                        bets=500)

    game_single2 = game(balance=1000,
                        bet_andel=30,
                        win_chance=55,
                        bets=500)

    # games_single = (game_single1, game_single2)

    # games = copy_game(games_single1, 10000)

    games = copy_games(games_single, 5)
    pprint(games)
    print()
    # games = create_games(games_single, 10)
    # pprint(games)
    new_games = create_new_balances(games, new_balances(games))

    pprint(new_games)
    print()

    def round_bal(games):
        return tuple(map(lambda game: round(game.balance), new_games))

    new_games_rounded = create_new_balances(new_games, round_bal(new_games))
    pprint(new_games_rounded)
    print("sfsf")

    def filter_help(game):
        return game.bet_andel == 25
    games1 = tuple(filter(filter_help, new_games_rounded))
    pprint(games1)
    """
    print(bals)
    above_s = len(tuple(filter(lambda x: x > game_single1.balance, bals)))
    print("above start =", above_s, "av", len(bals), "games")
    print("median =", statistics.median(bals))
    print("average =", statistics.mean(bals))
    print("max =", max(bals))
    print("min =", min(bals))

    """


if __name__ == '__main__':
    main()
