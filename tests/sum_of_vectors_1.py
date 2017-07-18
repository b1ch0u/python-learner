res = 'OK'

test_atoms = [
        [(1, 0)],
        [(1, -1), (2, -2)],
        [(1, 3), (0, 4), (8, 10), (9, 0)]
]
prop_f = vect_sum

from functools import reduce
def real_f(l):
    return reduce(lambda x,y: (x[0] + y[0], x[1] + y[1]), l)

for v in test_atoms:
    prop = prop_f(v)
    real_res = real_f(v)
    if prop != real_res:
        res = 'f({}) returned {} instead of {}'.format(v, prop, real_res)
        break

