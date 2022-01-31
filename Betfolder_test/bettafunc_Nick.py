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
        "bet_tactic"
        ]


game = collections.namedtuple("game", game_atribut)


def set_game_parameters(game, parameter):
    p1, p2, p3, p4, p5 = (*parameter, )
    new_game = game._replace(balance=p1, bet_andel=p2,
                             win_chance=p3, bets=p4, bet_tactic=p5)
    return new_game


def game_variants(game, parameters):
    permuted_parameters = tuple(itertools.product(*parameters))
    return tuple((set_game_parameters(game, para) for para in permuted_parameters))


def copy_game(game, antal):
    return tuple((game for _ in range(antal)))


def copy_game_variants(variants, antal):
    return tuple(copy_game(variant, antal) for variant in variants)

# Betting metod - DEFAULT # Returnerar balance för ett game efter alla bets
def default_betting(game):
    def slump(win_chance):
        return pr.Prob(win_chance/100)
    curret_balance = game.balance
    final_balance = None
    for _ in range(game.bets):
        dx = 0
        if slump(game.win_chance):
            dx = game.bet_andel/100*curret_balance
        else:
            dx = -game.bet_andel/100*curret_balance
        curret_balance += dx
    final_balance = curret_balance
    return final_balance

# betting metoder
"""
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
"""

def func(game):
    return game.bet_tactic(game)


def merge_games(all_games): # Lägger alla games i en gemensam tuple
    merged_games = ()
    for games in all_games:
        merged_games += games
    return merged_games


@timer_func
def multi_final_blanace_for_all_games(games):  # ger en tuple med samtliga updaterade balances
    pool = multiprocessing.Pool()
    balances = pool.map(func, games)
    return tuple(balances)


@timer_func # samma som function ovan utan multiprocessing
def final_blanace_for_all_games(games):
    balances = map(func, games)
    return tuple(balances)


def update_balance(games, balances):
    def update_bal(args):
        game, bal = args
        return game._replace(balance=bal, bets=0)
    newgames = map(update_bal, zip(games, balances))
    return tuple(newgames)



def main():
    game_empty = game(balance=None,
                      bet_andel=None,
                      win_chance=None,
                      bets=None,
                      bet_tactic=None)
    parameters = ((1000, ), (10, 15, 20, 25),
                  (50, 55, 60), (1000, ), (default_betting, ))

    variants = game_variants(game_empty, parameters)
    copied_variants = copy_game_variants(variants, 100)
    merged_games = merge_games(copied_variants) # alla games i en tuple
    # final_bal_all_games = final_blanace_for_all_games(merged_games)
    final_bal__all_games_multi = multi_final_blanace_for_all_games(merged_games)
    # stats = update_balance(merged_games, final_bal_all_games)
    stats_multi = update_balance(merged_games, final_bal__all_games_multi)

    # pprint(stats_multi)



    def round_bal(games):
        return tuple(map(lambda game: round(game.balance), games))

    stats_rounded_multi = update_balance(stats_multi, round_bal(stats_multi))
    pprint(stats_rounded_multi)

if __name__ == '__main__':
    main()
