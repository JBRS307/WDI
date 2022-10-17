# Pierwiastek metodą Newtona
def sqrt(n, eps):
    a = 1
    b = n
    while abs(a-b) >= eps:
        a = (a+b)/2
        b = n/a
    return a
#==============================================
if __name__ == "__main__":
    n = int(input().strip())
    eps = float(input().strip())
    root = sqrt(n, eps)
    count = 0
    while eps < 1:
        eps *= 10
        count += 1
    print(round(root, count))
    # print(root)