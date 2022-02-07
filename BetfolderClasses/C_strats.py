from B_simulate_games import get_stats
import random as r
from PyProbs import Probability as pr
from pprint import pprint


def random_win_chance(data2, bet_depth):
    random_wc_list = []
    # lowest_wc, higest_wc = list(data2.keys())[0], list(data2.keys())[-1]
    # game = data2[lowest_wc]
    lowest_wc, higest_wc = 50, 55
    # game = data2[50]
    #for i in range(game.bets):
    for i in range(bet_depth):
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
    bet_andel = fixed_andel / 100
    win = 1 + bet_andel
    loss = 1 - bet_andel
    for bool in bool_list:
        if bool:
            change_factor *= win
        else:
            change_factor *= loss
    return change_factor


def multiple_of_fixed(bool_list, bet_range, simulations):
    fixed_bet_dict = {}
    for i in range(simulations):
        for fixed_bet in range(bet_range):
            if fixed_bet not in fixed_bet_dict:
                fixed_bet_dict[fixed_bet] = [fixed(fixed_bet, bool_list)]
            else:
                fixed_bet_dict[fixed_bet].append(fixed(fixed_bet, bool_list))
    return fixed_bet_dict


def get_average_multiple_fixed(fixed_bet_dict):
    for key, values in fixed_bet_dict.items():
        fixed_bet_dict[key] = sum(values)/len(values)
    return fixed_bet_dict

# Ger ett dict där nyckeln motsvarar antalet bets man gör.
# Värdet man får är ett nytt dict där nyckeln svarar för betandelen och värdet
# man får i detta innre dictionary är average multiplier för 10 games (Simulations = 10)
def get_average_multiple_bet_depth(bet_depth, data2, bet_range, simulations):
    average_bet_depth = {}
    for bd in range(bet_depth):
        random_wc_list = random_win_chance(data2, bd)
        bool_list = get_boolean_list(random_wc_list)
        fixed_bet_dict = multiple_of_fixed(bool_list, bet_range, simulations)
        average_bet_depth[bd] = get_average_multiple_fixed(fixed_bet_dict)
    return average_bet_depth


def highest_fixed(bool_list):
    highest = (1, 0)
    for bet_andel in range(0, 101):
        change_factor = fixed(bet_andel, bool_list)
        if change_factor > highest[0]:
            highest = (change_factor, bet_andel)
    return highest





def main():
    data, data2 = get_stats()

    bet_depth = 3
    random_wc = random_win_chance(data2, bet_depth)
    print(random_wc)

    bool_list = get_boolean_list(random_wc)
    print(bool_list)

    result = default(data2, random_wc, bool_list)
    print(result)

    bet_range = 101
    simulations = 10
    multiple_fixed = multiple_of_fixed(bool_list, bet_range, simulations)
    print(multiple_fixed)

    average = get_average_multiple_fixed(multiple_fixed)
    print(average)

    average_bet_depth = get_average_multiple_bet_depth(bet_depth, data2,
                                                       bet_range, simulations)
    pprint(average_bet_depth)

    #result2 = highest_fixed(bool_list)
    #print(result2)


if __name__ == "__main__":
    main()
