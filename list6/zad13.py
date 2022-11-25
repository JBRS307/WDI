def rec_split(num, first = 1, n = 1):
    diff = num - first*n
    for _ in range(n):
        print(first, end=", ")
    if diff != 0:
        print(f"{diff},")
    else:
        print(',')
    
    if (n+1)*first < num:
        rec_split(num, first, n+1)
    elif first+1 <= num//2:
        rec_split(num, first+1, 1)

if __name__ == "__main__":
    n = int(input())
    rec_split(n)