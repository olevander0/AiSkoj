from collections import namedtuple
import itertools
from pprint import pprint


class GameVariants:

    def create_namedtuple(self, game_args):
        return namedtuple("game", game_args)

    def set_game(self, parameters):
        return self.namedtuple._make(parameters)

    def create_variants(self, parameters):
        permuted_parameters = tuple(itertools.product(*parameters))
        return tuple((self.set_game(para)
                     for para in permuted_parameters))
    """
    def copy_game(self, game, antal):
        return tuple((game for _ in range(antal)))

    def copy_game_variants(self, variants, antal):
        return tuple(self.copy_game(variant, antal) for variant in variants)

    def merge_games(self, all_games):
        return tuple(itertools.chain(*all_games))
    """

    def __init__(self, game_atribut, parameters):
        self.namedtuple = self.create_namedtuple(game_atribut)
        self.variants = self.create_variants(parameters)
        # self.analyzed_variants = tuple()

    def replace_variant(self, game_variant, substitute_by_index):
        paras = [substitute_by_index[i] if i in substitute_by_index else value
                 for i, value in enumerate(game_variant)]
        return self.namedtuple._make(paras)


def main():
    game_atribut = (
            "multiplier",
            "bet_andel",
            "win_chance",
            "bets"
            )
    parameters = ((1, ), (10, 15, 20, 25),
                  (50, 55, 60), (100, ))

    g = GameVariants(game_atribut, parameters)

    pprint(g.variants)
    newvar = g.replace_variant(g.variants[0], {0: "dfs"})
    print(newvar)


if __name__ == '__main__':
    main()
