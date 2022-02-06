from B_simulate_games import get_stats
import random as r
from PyProbs import Probability as pr
from pprint import pprint


def random_win_chance(data2):
    random_wc_list = []
    lowest_wc, higest_wc = list(data2.keys())[0], list(data2.keys())[-1]
    game = data2[lowest_wc]
    for i in range(game.bets):
        random_wc_list.append(r.randint(lowest_wc, higest_wc))
    return random_wc_list





def get_boolean_list(random_wc_list):
    def slump(wc):
        return pr.Prob(wc/100)
    return [slump(wc) for wc in random_wc_list]


def default(data2, random_wc, bool_list):
    change_factor = 1
    for bool, wc in zip(bool_list, random_wc):
        win = 1 + data2[wc].bet_andel/100
        loss = 1 - data2[wc].bet_andel/100
        if bool:
            change_factor *= win
        else:
            change_factor *= loss
    return change_factor


def fixed_bet_andel(bool_list, bet_andel):
    change_factor = 1
    win = 1 + bet_andel/100
    loss = 1 - bet_andel/100
    for bool in bool_list:
        if bool:
            change_factor *= win
        else:
            change_factor *= loss
    return change_factor


def different_fixed_bet(bool_list, bet_range):
    fixed_bet_list = []
    for bet in range(bet_range):
        fixed_bet_list.append((fixed_bet_andel(bool_list, bet), bet))
    return fixed_bet_list


def main():
    data, data2 = get_stats()
    random_wc = random_win_chance(data2)
    print(random_wc)

    bool_list = get_boolean_list(random_wc)
    print(bool_list)

    result = default(data2, random_wc, bool_list)
    print(result)

    result_fixed = different_fixed_bet(bool_list, 100)
    pprint(result_fixed)


if __name__ == "__main__":
    main()
