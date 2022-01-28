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


<<<<<<< HEAD
=======
def set_game(game, parameter):
    p1, p2, p3, p4, p5 = (*parameter, )
    new_game = game._replace(balance=p1, bet_andel=p2,
                             win_chance=p3, bets=p4, func_bal=p5)
    return new_game


def game_variants(game, parameters):
    permuted_parameters = tuple(itertools.product(*parameters))
    return tuple((set_game(game, para) for para in permuted_parameters))

>>>>>>> f41b537a6de087dc20e692ecee73955efcbf9455

def copy_game(game, antal):
    return tuple((game for _ in range(antal)))


@timer_func
def copy_game_variants(variants, antal):
    return tuple(copy_game(variant, antal) for variant in variants)


@timer_func
def merge_games(all_games):
    merged_games = all_games[0]
    if len(all_games) == 1:
        return merged_games
    for games in all_games[1:]:
        merged_games += games
    return merged_games


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
    game_empty = game(balance=None,
                      bet_andel=None,
                      win_chance=None,
                      bets=None,
                      func_bal=None)
    parameters = ((1000, ), (10, 15, 20, 25),
                  (50, 55, 60), (100, ), (new_balance, new_balance_double))
    para2 = ((1000, ), (10, ),
             (50, 55), (100, ), (new_balance, new_balance_double))
    variants = game_variants(game_empty, parameters)
    copied_variants = copy_game_variants(variants, 100)
    mergy = merge_games(copied_variants)
    print(len(mergy))
    # pprint(mergy)

    """
    game_single1 = game(balance=1000,
                        bet_andel=5,
                        win_chance=51,
                        bets=1000,
                        func_bal=new_balance)
<<<<<<< HEAD

=======
    """
    # f = game_single1.func_bal
    # print(f)
    # print(f(game_single1))
    """
>>>>>>> f41b537a6de087dc20e692ecee73955efcbf9455
    game_single2 = game(balance=1000,
                        bet_andel=5,
                        win_chance=51,
                        bets=1000,
                        func_bal=new_balance_double)
    """
    # print(game_single1)

    # games_single = (game_single1, game_single2)

    # games = copy_game(games_single1, 10000)

<<<<<<< HEAD
    games = copy_game(game_single1, 1000)
    games2 = copy_game(game_single2, 1000)
=======
    # games = copy_game(game_single1, 2)
    # games2 = copy_game(game_single2, 2)
>>>>>>> f41b537a6de087dc20e692ecee73955efcbf9455
    # pprint(games)
    # mergy = merge_games((games, games2))
    # pprint(mergy)
    # games = create_games(games_single, 10)
    # pprint(games)
    new_games = create_new_balances(mergy, new_balances(mergy))
    # pprint(new_games)

    def round_bal(games):
        return tuple(map(lambda game: round(game.balance), new_games))

    new_games_rounded = create_new_balances(new_games, round_bal(new_games))
    # pprint(new_games_rounded)

    # bals = tuple(map((lambda game: game.balance), new_games_rounded))
    # pprint(bal)

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
