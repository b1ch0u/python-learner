res = 'OK'

test_atoms = [
        [],
        [42],
        [0, 42],
        [-42, 21, 64],
        list(range(10))
]
prop_f = average

def real_f(l):
    if not l:
        return 0
    return sum(l) / len(l)

for v in test_atoms:
    prop = prop_f(v)
    real_res = real_f(v)
    if prop != real_res:
        res = 'f({}) returned {} instead of {}'.format(v, prop, real_res)
        break
