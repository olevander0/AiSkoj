from pathos.multiprocessing import ProcessingPool
from functions_to_test import get_functions
from create_games import GameVariants


def create_new_balances(games, balances):
    def update_bal(args):
        game_instance, bal = args
        return game_instance._replace(balance=bal, bets=0)
    newgames = map(update_bal, zip(games, balances))
    return tuple(newgames)


def func(game_instance):
    return get_functions()[game_instance.func_bal](game_instance)


def perform_simulations(games):  # ger en tuple med samtliga updaterade balances
    simulted_games = ProcessingPool().map(func, games)
    return tuple(simulted_games)


def main():
    game_atribut = (
            "multiplier",
            "bet_andel",
            "win_chance",
            "bets"
            )
    parameters = ((1, ), (10, 15, 20, 25, 30, 35, 40),
                  (50, 55, 60), (100, ))

    games = GameVariants(game_atribut, parameters)
    from pprint import pprint
    pprint(games.variants)
    simulated_games = perform_simulations(games.variants)
    pprint(simulated_games)


if __name__ == '__main__':
    main()
