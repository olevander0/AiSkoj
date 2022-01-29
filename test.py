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
