from math import log10


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

def check_digits(n):
    digs = [0]*10
    while n > 0:
        digs[n%10] += 1
        n //= 10
    
    if max(digs) > 1:
        return False
    return True
#-----------------------------------------------------

def num_leng(n):
    return int(log10(n))+1
#-----------------------------------------------------

def cut_num(n):
    max_num = 0
    leng = num_leng(n)
    for beg in range(leng):
        for end in range(leng-beg):
            num = n
            num %= 10**(leng-beg)
            num //= (10**end)
            if is_prime(num) and check_digits(num):
                max_num = max(num, max_num)
    
    return max_num
#=====================================================

if __name__ == "__main__":
    n = int(input())

    # print(num_leng(n))

    print(cut_num(n))