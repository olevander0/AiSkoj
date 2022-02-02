from collections import namedtuple
import itertools
from pprint import pprint


class CreateGames:
    def create_namedtuple(self, game_args):
        return namedtuple("game", game_args)

    def set_game(self, game, parameters):
        return game._make(parameters)

    def game_variants(self, game, parameters):
        permuted_parameters = tuple(itertools.product(*parameters))
        return tuple((self.set_game(game, para)
                     for para in permuted_parameters))

    def copy_game(self, game, antal):
        return tuple((game for _ in range(antal)))

    def copy_game_variants(self, variants, antal):
        return tuple(self.copy_game(variant, antal) for variant in variants)

    def merge_games(self, all_games):
        return tuple(itertools.chain(*all_games))

    def __init__(self, game_atribut, parameters, antal):
        self.namedtuple = self.create_namedtuple(game_atribut)
        self.variants = self.game_variants(self.namedtuple, parameters)
        self.all_games = self.copy_game_variants(self.variants, antal)
        self.all_games_merged = self.merge_games(self.all_games)
        self.key_to_tree = 0
        self.tree = {}

    def add_tree(self, value):
        self.tree[self.key_to_tree] = value
        self.key_to_tree += 1


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

    g = CreateGames(game_atribut, parameters, 3)
    pprint(g.variants)
    print()
    pprint(g.all_games)
    print()
    pprint(g.all_games_merged)


if __name__ == '__main__':
    main()
