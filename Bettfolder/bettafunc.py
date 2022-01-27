import collections
from PyProbs import Probability as pr
import multiprocessing
import itertools
# import math as m
# import matplotlib.pyplot as plt
from pprint import pprint
import statistics
from time import time


def timer_func(func):
    # This function shows the execution time of
    # the function object passed
    def wrap_func(*args, **kwargs):
        t1 = time()
        result = func(*args, **kwargs)
        t2 = time()
        print(f'Function {func.__name__!r} executed in {(t2-t1):.4f}s')
        return result
    return wrap_func


game_atribut = [
        "balance",
        "bet_andel",
        "win_chance",
        "bets",
        "func_bal"
        ]


game = collections.namedtuple("game", game_atribut)


def copy_game(game, antal):
    return tuple((game for _ in range(antal)))


def copy_games(games, antal):
    listed_games = []
    for game in games:
        for _ in range(antal):
            listed_games.append(game)
    return tuple(listed_games)


def merge_games(all_games):
    merged_games = (*all_games[0],)

    # pprint(merged_games)
    if len(all_games) == 1:
        return merged_games
    for games in all_games[1:]:
        merged_games = merged_games + (*games,)
    return merged_games

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


def func(game):
    return game.func_bal(game)


@timer_func
def new_balances(games):  # ger en tuple med samtliga updaterade balances
    pool = multiprocessing.Pool()
    balances = pool.map(func, games)
    return tuple(balances)


@timer_func
def new_balances2(games):  # samma som function ovan utan multiprocessing
    balances = map(func, games)
    return tuple(balances)


def new_balances_all(all_games):
    for games in all_games:
        pass


def main():

    game_single1 = game(balance=1000,
                        bet_andel=5,
                        win_chance=51,
                        bets=1000,
                        func_bal=new_balance)
    game_single2 = game(balance=1000,
                        bet_andel=5,
                        win_chance=51,
                        bets=10,
                        func_bal=new_balance_double)
    # print(game_single1)

    # games_single = (game_single1, game_single2)

    # games = copy_game(games_single1, 10000)

    games = copy_game(game_single1, 10)
    games2 = copy_game(game_single2, 10)
    # pprint(games)
    mergy = merge_games((games, games2))
    pprint(mergy)
    # games = create_games(games_single, 10)
    # pprint(games)
    new_games = create_new_balances(mergy, new_balances(mergy))
    # new_games2 = create_new_balances(games, new_balances2(games))
    # pprint(new_games)

    def round_bal(games):
        return tuple(map(lambda game: round(game.balance), new_games))

    new_games_rounded = create_new_balances(new_games, round_bal(new_games))
    pprint(new_games_rounded)

    # bals = tuple(map((lambda game: game.balance), new_games_rounded))
    #pprint(bal)
    """
    def filter_help(game):
        return game.bet_andel == 25
    games1 = tuple(filter(filter_help, new_games_rounded))
    pprint(games1)
    """

    # print(bals)
    """
    above_s = len(tuple(filter(lambda x: x > game_single1.balance, bals)))
    print("above start =", above_s, "av", len(bals), "games")
    print("median =", statistics.median(bals))
    print("average =", statistics.mean(bals))
    print("max =", max(bals))
    print("min =", min(bals))
    """

if __name__ == '__main__':
    main()
