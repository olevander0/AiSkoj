import simulate_games as sg
import collections

game_atribut = (
        "balance",
        "bet_andel",
        "win_chance",
        "bets",
        "func_bal"
        )

game = sg.create_namedtuple(game_atribut)

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
def main():
    sg.main()


if __name__ == '__main__':
    main()
