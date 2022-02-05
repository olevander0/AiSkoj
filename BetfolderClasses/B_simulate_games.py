from pathos.multiprocessing import ProcessingPool
# from functions_to_test import get_functions
from A_create_games import GameVariants
import itertools


def get_change_factor(game_variant):
    change_factor = game_variant.multiplier
    win = 1 + game_variant.bet_andel/100
    loss = 1 - game_variant.bet_andel/100
    for i in range(game_variant.bets):
        if i < game_variant.win_chance:
            change_factor *= win
        else:
            change_factor *= loss
    return change_factor


def perform_simulations(game_variants):  # ger en tuple med samtliga updaterade balances
    def update_variant(game_variant):
        change_factor = get_change_factor(game_variant)
        change = {0: change_factor}
        new_game = game_variants.replace_variant(game_variant, change)
        return new_game
    result = ProcessingPool().map(update_variant, game_variants.variants)
    return tuple(result)


def sort_by_win_chance(simulated_games):
    def sort_winchance(one_simulated_game):
        return one_simulated_game.win_chance
    filtered = itertools.groupby(simulated_games, sort_winchance)
    return filtered


def main():
    game_atribut = (
            "multiplier",
            "bet_andel",
            "win_chance",
            "bets"
            )
    bet_andelar = [i for i in range(1, 101)]
    win_chances = [i for i in range(50, 101)]
    parameters = ((1, ), bet_andelar,
                  win_chances, (100, ))

    game_variants = GameVariants(game_atribut, parameters)
    from pprint import pprint
    simulated_games = perform_simulations(game_variants)
    #pprint(simulated_games)
    print()
    grouped = sort_by_win_chance(simulated_games)
    print(grouped)
    for key, group in grouped:
        keygroup = {key: list(group)}
        print(keygroup)


if __name__ == '__main__':
    main()
