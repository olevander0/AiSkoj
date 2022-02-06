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
        win = 1 + data2[wc][1]/100
        loss = 1 - data2[wc][1]/100
        if bool:
            change_factor *= win
        else:
            change_factor *= loss
    return change_factor


"""
def fixed_bet_andel(data2, random_wc):
    for wc in random_wc:
        win = 1 + bet_andel/100
        loss = 1 - bet_andel/100
        def slump(wc):
            return pr.Prob(wc/100)
        if slump(wc):
            change_factor *= win
        else:
            change_factor *= loss
    return change_factor
"""


def main():
    data, data2 = get_stats()
    random_wc = random_win_chance(data2)
    print(random_wc)

    bool_list = get_boolean_list(random_wc)
    print(bool_list)

    result = default(data2, random_wc, bool_list)
    print(result)


if __name__ == "__main__":
    main()
