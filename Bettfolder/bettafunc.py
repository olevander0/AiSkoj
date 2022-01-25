import collections
from PyProbs import Probability as pr
import multiprocessing
# import matplotlib.pyplot as plt
from pprint import pprint
game = collections.namedtuple("game", [
        "balance",
        "bet_andel",
        "win_chance",
        "bets"])


def create_game_inputs(balance, bet_andel, win_chance, bets, antal):
    balances = tuple((balance for _ in range(antal)))
    bet_andelar = tuple((bet_andel for _ in range(antal)))
    win_chances = tuple((win_chance for _ in range(antal)))
    betsleft = tuple((bets for _ in range(antal)))
    return balances, bet_andelar, win_chances, betsleft


def create_games(balances, bet_andelar, win_chances, betsleft):
    newgames = (game(balance=balances[i],
                bet_andel=bet_andelar[i],
                win_chance=win_chances[i],
                bets=betsleft[i]) for i in range(len(balances)))
    return tuple(newgames)


def create_new_balances(games, balances):
    newgames = (game(balance=balances[i],
                bet_andel=games[i].bet_andel,
                win_chance=games[i].win_chance,
                bets=0) for i in range(len(games)))
    return tuple(newgames)


def slump(win_chance):
    return pr.Prob(win_chance/100)


def new_balance(game):
    new_balance = game.balance
    print(game.bets)
    for _ in range(game.bets):
        dx = 0
        if slump(game.win_chance):
            dx = game.bet_andel/100*new_balance
        else:
            dx = -game.bet_andel/100*new_balance
        # dx beräknar mängden vinst/förlust
        new_balance += dx
    return new_balance


def new_balances(games):  # ger en tuple med samtliga updaterade balances
    pool = multiprocessing.Pool()
    updated_game = pool.map(new_balance, games)
    # updated_game = map(new_balance, games)
    return tuple(updated_game)


def main():
    balances, bet_andelar, win_chances, betsleft = create_game_inputs(1000, 10,
                                                                      51, 1000,
                                                                      10)

    games = create_games(balances, bet_andelar, win_chances, betsleft)

    pprint(games)
    new_games = create_new_balances(games, new_balances(games))
    pprint(new_games)


if __name__ == '__main__':
    main()
