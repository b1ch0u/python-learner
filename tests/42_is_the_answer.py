res = 'OK'

test_atoms = list(range(-10, 10))
prop_f = f

def real_f(v):
    return 42

for v in test_atoms:
    prop = prop_f(v)
    real_res = real_f(v)
    if prop != real_res:
        res = 'f({}) returned {} instead of {}'.format(v, prop, real_res)
        break
