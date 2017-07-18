res = 'OK'

test_atoms = list(range(20))
prop_f = fib

def real_f(n):
    if n < 2:
        return n
    return real_f(n - 1) + real_f(n - 2)

for v in test_atoms:
    prop = prop_f(v)
    real_res = real_f(v)
    if prop != real_res:
        res = 'f({}) returned {} instead of {}'.format(v, prop, real_res)
        break
