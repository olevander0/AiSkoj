# pprint(mergy)

"""
game_single1 = game(balance=1000,
                    bet_andel=5,
                    win_chance=51,
                    bets=1000,
                    func_bal=new_balance)



"""
# f = game_single1.func_bal
# print(f)
# print(f(game_single1))
"""

game_single2 = game(balance=1000,
                    bet_andel=5,
                    win_chance=51,
                    bets=1000,
                    func_bal=new_balance_double)
"""
# print(game_single1)

# games_single = (game_single1, game_single2)

# games = copy_game(games_single1, 10000)


# games = copy_game(game_single1, 1000)
# games2 = copy_game(game_single2, 1000)

# games = copy_game(game_single1, 2)
# games2 = copy_game(game_single2, 2)

# pprint(games)
# mergy = merge_games((games, games2))
# pprint(mergy)
# games = create_games(games_single, 10)
# pprint(games)
# pprint(new_games_rounded)

# bals = tuple(map((lambda game: game.balance), new_games_rounded))
# pprint(bal)

"""
def filter_help(game):
    return game.bet_andel == 25
games1 = tuple(filter(filter_help, new_games_rounded))
pprint(games1)
"""

# print(bals)
"""
above_s = len(tuple(filter(lambda x: x > game_single1.balance, bals)))
print("above start =", above_s, "av", len(bals), "games")
print("median =", statistics.median(bals))
print("average =", statistics.mean(bals))
print("max =", max(bals))
print("min =", min(bals))
"""

def create_namedtuple(game_args):
    return collections.namedtuple("game", game_args)


game_atribut = (
        "balance",
        "bet_andel",
        "win_chance",
        "bets",
        "func_bal"
        )

game = create_namedtuple(game_atribut)


def set_game(game, parameter):
    return game._make(parameter)


def game_variants(game, parameters):
    permuted_parameters = tuple(itertools.product(*parameters))
    return tuple((set_game(game, para) for para in permuted_parameters))


def copy_game(game, antal):
    return tuple((game for _ in range(antal)))


@timer_func
def copy_game_variants(variants, antal):
    return tuple(copy_game(variant, antal) for variant in variants)


@timer_func
def merge_games(all_games):
    merged_games = all_games[0]
    if len(all_games) == 1:
        return merged_games
    for games in all_games[1:]:
        merged_games += games
    return merged_games
