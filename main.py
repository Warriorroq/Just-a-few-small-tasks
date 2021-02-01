def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def sub(a, b):
    return a - b

def div(a, b):
    return a / b

def eq(a, b):
    return a == b

def lt(a, b):
    return a < b

def nds(a, b):
    if(a == 0 or b == 0):
        return a + b

    if(a > b):
        return nds(a % b, b)
    else:
        return nds(a, b % a)

def create(a, b):
    return div(a, b)

def prt(a):
    print(a)

def inp():
    c = input()
    try:
        return float(c)
    except ValueError:
        return inp()