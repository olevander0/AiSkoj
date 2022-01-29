import collections
import itertools
# import math as m
# import matplotlib.pyplot as plt
from pprint import pprint
import statistics
from timer_function import timer_func


game_atribut = (
        "balance",
        "bet_andel",
        "win_chance",
        "bets",
        "func_bal"
        )


def create_namedtuple(game_args):
    return collections.namedtuple("game", game_args)


game = create_namedtuple(game_atribut)


game = game(balance=None,
            bet_andel=None,
            win_chance=None,
            bets=None,
            func_bal=None)


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
