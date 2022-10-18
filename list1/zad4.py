def intRoot(n):
    i = 1
    summ = 1
    count = 0
    while summ < n:
        count += 1
        i += 2
        summ += i
    
    if summ == n:
        return count+1

    return count
#=====================================================
if __name__ == "__main__":
    n = int(input())
    print(intRoot(n))