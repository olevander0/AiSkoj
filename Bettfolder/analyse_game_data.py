from create_games import create_all_games
from simulate_games import perform_simulations
from collections import namedtuple
from pprint import pprint
import statistics

def set_game_stats(game, parameter):
    return game._make(parameter)


def grouper(n, iterable):
    return tuple(iterable[i:i + n] for i in range(0, len(iterable), n))


def get_bal_all_games(games):
    def get_bal_gameclones(clones):
        return tuple(clone.balance for clone in clones)
    return tuple(get_bal_gameclones(clones) for clones in games)


def get_average(all_balances):
    return tuple(statistics.mean(balances) for balances in all_balances)


def set_average_for_gamevariant(games, averages):
    def change_bal(game_instance, bal):
        return game_instance._replace(balance=bal)
    AV = (change_bal(clones[0], bal) for clones, bal in zip(games, averages))
    return tuple(AV)

"""
def median

def max
"""

def stats_for_game(game_stats, all_balances):
    for balances in all_balances:



def main():
    copies = 10
    game_atribut = (
            "balance",
            "bet_andel",
            "win_chance",
            "bets",
            "func_bal"
            )
    game_stats_atribut = (
            "average",
            "max",
            "min",
            "median",
            )
    game_stats = namedtuple("game_stats", game_stats_atribut)
    parameters = ((1000, ), (10, ),
                  (70, 80), (10, ),
                  ("test", ))

    games = create_all_games(game_atribut, parameters, copies)
    pprint(games)
    print()
    tested_games = perform_simulations(games)
    grouped = grouper(copies, tested_games)

    pprint(tested_games)
    print("hej")
    pprint(grouped)
    all_balances = get_bal_all_games(grouped)
    average = get_average(all_balances)

    pprint(all_balances)
    print()
    pprint(average)
    G_AV = set_average_for_gamevariant(grouped, average)
    pprint(G_AV)


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
