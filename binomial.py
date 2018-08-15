# binomial theorem
# (x+y)^n = sigma(k=0..n) (n choose k) x^k * y*n-k

from math import factorial as fact

def binom_string(values, n):
    """Formatting the binomial string to be printed."""
    msg = "(x+y)^" + str(n) + " = "
    for i in range(n+1):
        c, x, y = values['c'][i], values['x'][i], values['y'][i]
        if c == 0: continue
        if c > 1: msg += str(c)
        if x == 1: msg += 'x'
        if x > 1: msg += 'x^' + str(x)
        if y == 1: msg += 'y'
        if y > 1: msg += 'y^' + str(y)
        msg += ' + '
    return msg[:-3]

def binomial(n):
    """Prints the expansion of (x+y)^n"""
    values = {'x':[], 'y':[], 'c':[]}
    choose = lambda n, k: int(fact(n) / (fact(k)*fact(n-k)))
    for k in range(n+1):  # sigma goes from 0 to n inclusive, range is exclusive
        values['x'] = values['x'] + [k]
        values['y'] = values['y'] + [n-k]
        values['c'] = values['c'] + [choose(n, k)]
    print(binom_string(values, n))
    
    
binomial(3)  # (x+y)^3 = y^3 + 3xy^2 + 3x^2y + x^3
binomial(5)  # (x+y)^5 = y^5 + 5xy^4 + 10x^2y^3 + 10x^3y^2 + 5x^4y + x^5


        
