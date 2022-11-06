from random import randrange


def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n%2 == 0 or n%3 == 0 or n <= 1:
        return False

    i = 5
    while i*i <= n:
        if n%i == 0:
            return False
        i += 2

        if n%i == 0:
            return False
        i += 4
    
    return True
#-----------------------------------------------------

def gen_primes(arr, leng):
    primes = []

    for i in range(leng):
        if is_prime(arr[i]):
            primes.append((i, arr[i]))
    
    return primes
#-----------------------------------------------------

def gen_nums(arr, leng):
    primes = gen_primes(arr, leng)
    nums = []

    prod = 1
    for i in range(len(primes)):
        prod *= primes[i][1]
        nums.append((primes[i][0], prod))

    return nums
#-----------------------------------------------------

def find_biggest(arr, leng):
    nums = gen_nums(arr, leng)

    max_num = 0
    for i in range(len(nums)):
        for j in range(nums[i][0]+1, leng):
            if arr[j] == nums[i][1]:
                max_num = max(max_num, arr[j])
                break
    
    return None if max_num == 0 else max_num
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [randrange(1, k+1) for _ in range(n)]
    # arr = [1, 2, 3, 5, 7, 210]

    print(find_biggest(arr, n))
    # print(find_biggest(arr, 6))