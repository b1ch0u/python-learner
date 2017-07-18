res = 'OK'

test_atoms = [
        ([], []),
        ([1], [1]),
        ([1], [2]),
        ([1, 2, 3], [2, 4, 4]),
        ([1, 2, 3], [1, 0, 1])
]
prop_f = dot

def real_f(l1, l2):
    return sum(x*y for x,y in zip(l1, l2))

for v in test_atoms:
    l1, l2 = v
    prop = prop_f(l1, l2)
    real_res = real_f(l1, l2)
    if prop != real_res:
        res = 'f({}) returned {} instead of {}'.format(v, prop, real_res)
        break

