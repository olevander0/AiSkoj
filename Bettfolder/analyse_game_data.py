from create_games import create_all_games
from simulate_games import perform_simulations
from pprint import pprint


def main():
    game_atribut = (
            "balance",
            "bet_andel",
            "win_chance",
            "bets",
            "func_bal"
            )
    parameters = ((1000, ), (10, 25),
                  (70, 80, 90), (10, ),
                  ("new_balance", "new_balance_double"))

    games = create_all_games(game_atribut, parameters, 2)
    pprint(games)
    print()
    tested_games = perform_simulations(games)
    pprint(tested_games)


"""
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
"""


if __name__ == '__main__':
    main()
