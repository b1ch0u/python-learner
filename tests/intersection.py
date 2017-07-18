res = 'OK'

test_atoms = [
        ([], []),
        ([], [1]),
        ([1], []),
        ([1], [1]),
        ([1], [2]),
        ([1, 2, 3], [2, 4]),
        ([1, 2, 3], [4, 5])
]
prop_f = inter

def real_f(l1, l2):
    return [e for e in l1 if e in l2]

for v in test_atoms:
    l1, l2 = v
    prop = prop_f(l1, l2)
    real_res = real_f(l1, l2)
    if prop != real_res:
        res = 'f({}) returned {} instead of {}'.format(v, prop, real_res)
        break
