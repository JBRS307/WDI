def check(n):
    if n%2 == 0:
        return True
    a = 7
    while a <= n//2:
        if n%a == 0:
            return True
        a = 9*a+4
    return False
#=================================================
if __name__ == "__main__":
    n = int(input())
    print(check(n))