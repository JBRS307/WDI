# Test czy liczba jest iloczynem dwóch kolejnych wyrazów ciągu
def fibAndTest(test):
    if test == 1:
        return True
    n1 = 1
    n2 = 1
    while n1+n2 <= test:
        if n2*(n1+n2) == test:
            return True
        n1, n2 = n2, n1+n2
    return False
#==================================================
if __name__ == "__main__":
    tester = int(input().strip())
    print(fibAndTest(tester))
    