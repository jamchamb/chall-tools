def mod_fac(n, mod):
    """Modular factorial"""
    if n < 0:
        raise Exception("mod_fac: must give non-negative n")
    elif n == 0:
        return 1
    
    result = n % mod
    for i in range((n % mod)-1, 0, -1):
        result = mod_mult(result, i, mod)
    return result

def mod_mult(x, y, mod):
    """Modular multiplication"""
    return (x % mod * y % mod) % mod

def mod_div(numerator, denominator, mod):
    """Modular division"""
    return mod_mult(numerator, pow(denominator,mod-2,mod), mod)

def mod_choose(n, k, mod):
    """Modular binomial coefficient"""
    if k > n:
        return 0
    elif k == n:
        return 1
    else:
        return mod_div(mod_fac(n, mod), mod_mult(mod_fac(k, mod), mod_fac(n-k, mod), mod), mod)

def mod_exp(x, y, mod):
    """Modular exponentiation (can upgrade to use repeated squaring)"""
    result = 1
    for i in range(0, y):
        result *= (x % mod)
        result = result % mod
    return result
