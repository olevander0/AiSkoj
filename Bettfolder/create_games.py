from collections import namedtuple
import itertools
from pprint import pprint


def create_namedtuple(game_args):
    return namedtuple("game", game_args)


def set_game(game, parameters):
    return game._make(parameters)


def game_variants(game, parameters):
    permuted_parameters = tuple(itertools.product(*parameters))
    return tuple((set_game(game, para) for para in permuted_parameters))


def copy_game(game, antal):
    return tuple((game for _ in range(antal)))


def copy_game_variants(variants, antal):
    return tuple(copy_game(variant, antal) for variant in variants)


def merge_games(all_games):
    merged_games = all_games[0]
    if len(all_games) == 1:
        return merged_games
    for games in all_games[1:]:
        merged_games += games
    return merged_games


def create_all_games(game_atribut, parameters, antal):
    game = create_namedtuple(game_atribut)
    copied_games = copy_game_variants(game_variants(game, parameters), antal)
    return merge_games(copied_games)


def main():

    game_atribut = (
            "balance",
            "bet_andel",
            "win_chance",
            "bets",
            "func_bal"
            )
    parameters = ((1000, ), (10, 15, 20, 25),
                  (50, 55, 60), (True, ),
                  ("new_balance", "new_balance_double"))

    merged_games = create_all_games(game_atribut, parameters, 3)
    pprint(merged_games)


if __name__ == '__main__':
    main()
