from B_simulate_games import get_stats
import random as r
from PyProbs import Probability as pr


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
        bet_andel = data2[wc].bet_andel / 100
        win = 1 + bet_andel
        loss = 1 - bet_andel
        if bool:
            change_factor *= win
        else:
            change_factor *= loss
    return change_factor


def fixed(fixed_andel, bool_list):
    change_factor = 1
    for bool in bool_list:
        bet_andel = fixed_andel / 100
        win = 1 + bet_andel
        loss = 1 - bet_andel
        if bool:
            change_factor *= win
        else:
            change_factor *= loss
    return change_factor


def highest_fixed(bool_list):
    highest = (1, 0)
    for bet_andel in range(0, 101):
        change_factor = fixed(bet_andel, bool_list)
        if change_factor > highest[0]:
            highest = (change_factor, bet_andel)
    return highest


def main():
    data, data2 = get_stats()
    # from pprint import pprint
    random_wc = random_win_chance(data2)
    print(random_wc)

    bool_list = get_boolean_list(random_wc)
    print(bool_list)

    result = default(data2, random_wc, bool_list)
    print(result)

    result2 = highest_fixed(bool_list)
    print(result2)


if __name__ == "__main__":
    main()
