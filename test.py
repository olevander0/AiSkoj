import itertools
from pprint import pprint
parameters = ((1000,), (60, 70, 80), (51, 52, 53), (1000,), ("f1", "f2"))

par =  (("kuk", "BUK"), (60, 70, 80))
a, b = par
S = list(itertools.product(*parameters))
pprint(S)
print(len(S))
#print(list(itertools.product(*parameters)))
