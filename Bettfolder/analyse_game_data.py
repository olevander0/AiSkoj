from create_games import create_all_games
from simulate_games import perform_simulations
from typing import NamedTuple
# from pprint import pprint
import statistics


class GameStats(NamedTuple):
    average: int
    median: int
    max: int
    min: int


def set_game_stats(game, parameter):
    return game._make(parameter)


def grouper(n, iterable):
    return tuple(iterable[i:i + n] for i in range(0, len(iterable), n))


def get_bal_all_games(games):
    def get_bal_gameclones(clones):
        return tuple(clone.balance for clone in clones)
    return tuple(get_bal_gameclones(clones) for clones in games)


def set_average_for_gamevariant(games, averages):
    def change_bal(game_instance, bal):
        return game_instance._replace(balance=bal)
    AV = (change_bal(clones[0], bal) for clones, bal in zip(games, averages))
    return tuple(AV)


def stats_for_games(all_balances):
    def get_stats_for_clones(balances):
        def get_average(balances):
            return statistics.mean(balances)

        def get_median(balances):
            return statistics.median(balances)

        def get_max(balances):
            return max(balances)

        def get_min(balances):
            return min(balances)
        game_stats = GameStats(get_average(balances), get_median(balances),
                               get_max(balances), get_min(balances))
        return game_stats

    return tuple(get_stats_for_clones(balances) for balances in all_balances)


def main():
    copies = 1000
    game_atribut = (
            "balance",
            "bet_andel",
            "win_chance",
            "bets",
            "func_bal"
            )

    parameters = ((1000, ), (15, 17, 19, 21, 23, 25),
                  (51, 52, 53, 54, 55), (100, ),
                  ("new_balance", ))

    games = create_all_games(game_atribut, parameters, copies)
    grouped_games = grouper(copies, games)
    # pprint(games)
    # print()
    tested_games = perform_simulations(games)
    grouped = grouper(copies, tested_games)

    # pprint(tested_games)
    # print("hej")
    # pprint(grouped)
    all_balances = get_bal_all_games(grouped)
    stats = stats_for_games(all_balances)
    for (game_start, game_stats) in zip(grouped_games, stats):
        print(game_start[0])
        print(game_stats)
        print()


if __name__ == '__main__':
    main()
