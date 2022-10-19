#Rozwiązanie x**x = 2020 (x**x - 2020 = 0) metodą bisekcji

def f(x):
    return x**x - 2020
#-----------------------------------------------------
def solve(eps = 0.0000001):
    a, b = 0, 100

    while abs(a-b) > eps:
        x = (a+b)/2
        if f(x) == 0:
            return x
        if f(a)*f(x) < 0:
            b = x
        elif f(b)*f(x) < 0:
            a = x
    
    return (a+b)/2
#=====================================================
if __name__ == "__main__":
    print(solve())