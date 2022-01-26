"""
games = ((game(balance=1000, bet_andel=25, win_chance=55, bets=500),
         (game(balance=1000, bet_andel=25, win_chance=55, bets=500),
         (game(balance=1000, bet_andel=25, win_chance=55, bets=500),)

balances = (101, 231, 2141)

def update_bal(args):
    game, bal = args
    return game._replace(balance=bal, bets=0)

(game(balance=101, bet_andel=25, win_chance=55, bets=0)


args = (game(balance=1000, bet_andel=25, win_chance=55, bets=500), 101)

output = [game(balance=101, bet_andel=25, win_chance=55, bets=0]
for args in zip(games, balances):
    args = (101, (game(balance=1000, bet_andel=25, win_chance=55, bets=500))
    output.append(update_bal(args))
"""
lst = ["a", "b", "c"]
tupp = (1, 2, 3)


def mult_3(arg):
    return arg[0], arg[1]*3


merg = []

for arg in zip(lst, tupp):
    merg.append(mult_3(arg))
print(merg)

iterator = zip(lst, tupp)
print(iterator)
m_o = (map(mult_3, iterator))
for i in m_o:
    print(i)
