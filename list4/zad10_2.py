from random import randrange


if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [[randrange(-k, k+1) for _ in range(n)] for _ in range(n)]

    rows = False in [0 in row for row in arr]
    cols = False in [0 in [arr[i][j] for i in range(n)] for j in range(n)]

    print(not(rows and cols))
