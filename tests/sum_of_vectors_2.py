res = 'OK'

test_atoms = [
        [(1, 0)],
        [(1, 0, 9)],
        [(1, -1), (2, -2)],
        [(1, 3, 6, 7), (0, 4, 4, -2), (8, 10, 9, 1), (9, 0, 7, -1)]
]
prop_f = vect_sum

from functools import reduce
def real_f(l):
    def vect_add(x, y):
        return [xi + yi for xi,yi in zip(x, y)]
    return reduce(vect_add, l)

for v in test_atoms:
    prop = prop_f(v)
    real_res = real_f(v)
    if prop != real_res:
        res = 'f({}) returned {} instead of {}'.format(v, prop, real_res)
        break

