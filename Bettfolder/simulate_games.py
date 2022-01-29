import collections
from PyProbs import Probability as pr
import multiprocessing
import itertools
# import math as m
# import matplotlib.pyplot as plt
from pprint import pprint
import statistics
from timer_function import timer_func


def create_namedtuple(game_args):
    return collections.namedtuple("game", game_args)


game_atribut = (
        "balance",
        "bet_andel",
        "win_chance",
        "bets",
        "func_bal"
        )

game = create_namedtuple(game_atribut)


def set_game(game, parameter):
    return game._make(parameter)


def game_variants(game, parameters):
    permuted_parameters = tuple(itertools.product(*parameters))
    return tuple((set_game(game, para) for para in permuted_parameters))


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

    new_games = create_new_balances(mergy, new_balances(mergy))

    def round_bal(games):
        return tuple(map(lambda game: round(game.balance), new_games))

    new_games_rounded = create_new_balances(new_games, round_bal(new_games))


if __name__ == '__main__':
    main()
