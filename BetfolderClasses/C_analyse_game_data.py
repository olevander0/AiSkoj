from A_create_games import CreateGames
from B_simulate_games import perform_simulations
from typing import NamedTuple
from pprint import pprint
import statistics


class GameStats(NamedTuple):
    average: int
    median: int
    max: int
    min: int


def set_game_stats(game, parameter):
    return game._make(parameter)


def get_bal_all_games(games, copies):
    def get_bal_gameclones(clones):
        return tuple(clone.balance for clone in clones)
    return tuple(get_bal_gameclones(games[i:i + copies])
                 for i in range(0, len(games), copies))


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


def match_game_with_stats(variants, stats):
    return tuple((v, s) for v, s in zip(variants, stats))


def stats_for_games_procent(variants, stats):
    def get_percentage_diff(start_bal, new_bal):
        if new_bal == 0:
            return -100
        percentage = ((new_bal/start_bal) * 100) - 100
        return round(percentage)

    def set_percentage_diff(start_bal, game_stats):
        percentages = (get_percentage_diff(start_bal, new_bal)
                       for new_bal in game_stats)
        return GameStats._make(percentages)
    g_percentages = (set_percentage_diff(variant.balance, game_stats)
                     for variant, game_stats in zip(variants, stats))
    return tuple(g_percentages)


def gen_data():
    copies = 500
    game_atribut = (
            "balance",
            "bet_andel",
            "win_chance",
            "bets",
            "func_bal"
            )
    bet_andelar = tuple(i for i in range(10, 30))
    win_chances = (51, 52, 53, 55, 54)
    bets = 150
    parameters = ((1000, ), (bet_andelar),
                  (win_chances), (bets, ),
                  ("new_balance", ))

    g = CreateGames(game_atribut, parameters, copies)
    tested_games = perform_simulations(g.all_games_merged)
    all_balances = get_bal_all_games(tested_games, copies)
    stats = stats_for_games(all_balances)
    pstats = stats_for_games_procent(g.variants, stats)
    return (match_game_with_stats(g.variants, pstats))


def main():
    copies = 500
    game_atribut = (
            "balance",
            "bet_andel",
            "win_chance",
            "bets",
            "func_bal"
            )
    bet_andelar = tuple(i for i in range(10, 30))
    win_chances = (60, )
    parameters = ((1000, ), (bet_andelar),
                  (win_chances), (400, ),
                  ("new_balance", ))

    g = CreateGames(game_atribut, parameters, copies)
    tested_games = perform_simulations(g.all_games_merged)
    # pprint(tested_games)
    # print("hej")
    # pprint(grouped)
    all_balances = get_bal_all_games(tested_games, copies)
    stats = stats_for_games(all_balances)
    pprint(stats)
    print()
    pstats = stats_for_games_procent(g.variants, stats)

    pprint(match_game_with_stats(g.variants, pstats))



    """
    for (game_start, game_stats, pstats) in zip(grouped_games, stats, pstats):
        print(game_start[0])
        print(game_stats)
        print(pstats)
        print()
    """


if __name__ == '__main__':
    main()
