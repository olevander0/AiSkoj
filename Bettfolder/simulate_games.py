from pathos.multiprocessing import ProcessingPool
from functions_to_test import get_functions
from create_games import create_all_games


def create_new_balances(games, balances):
    def update_bal(args):
        game_instance, bal = args
        return game_instance._replace(balance=bal, bets=0)
    newgames = map(update_bal, zip(games, balances))
    return tuple(newgames)


def func(game_instance):
    return get_functions()[game_instance.func_bal](game_instance)


def new_balances(games):  # ger en tuple med samtliga updaterade balances
    balances = ProcessingPool().map(func, games)
    return tuple(balances)


def new_balances2(games):  # samma som function ovan utan multiprocessing
    balances = map(func, games)
    return tuple(balances)


def perform_simulations(games):
    return create_new_balances(games, new_balances(games))


def perform_simulations2(games):
    return create_new_balances(games, new_balances2(games))


def main():
    game_atribut = (
            "balance",
            "bet_andel",
            "win_chance",
            "bets",
            "func_bal"
            )
    parameters = ((1000, ), (10, 15, 20, 25, 30, 35, 40),
                  (50, 55, 60), (100, ), ("new_balance", "new_balance_double"))

    games = create_all_games(game_atribut, parameters, 2)
    up_games = perform_simulations(games)
    from pprint import pprint
    pprint(up_games)


if __name__ == '__main__':
    main()
