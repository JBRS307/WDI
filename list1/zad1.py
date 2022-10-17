# Fibonacci, mniejsze od 1_000_000
def fib(n1, n2):
    if (n1+n2) < 1_000_000:
        print(n1+n2, end=" ")
        fib(n2, n1+n2)
    else:
        print()
        return
#===================================================
if __name__ == "__main__":
    print("1 1", end=" ")
    fib(1, 1)