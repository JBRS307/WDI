from math import isqrt, log10

def is_prime(n):
    if n <= 3:
        return n > 1
    if not n%2 or not n%3:
        return False
    
    for i in range(5, isqrt(n)+1, 6):
        if not n%i or not n%(i+2):
            return False
    
    return True
#-----------------------------------------------------

def rotate(n):
    leng = int(log10(n)) #Długość pomniejszona o 1, przyda się później

    last = n%10
    n //= 10
    return last * (10**leng) + n
#-----------------------------------------------------

def mult_digs_in_sys(n, system):
    res = 1
    while n != 0:
        res *= n%system
        n //= system
    
    return res
#-----------------------------------------------------

def check(n):
    min_system = float('inf')
    for system in range(3, 17): #Nie trzeba sprawdzać systemu binarnego, iloczyn będzie 1 albo 0, żaden nie jest pierwszy
        rotation = n
        n_checked = False
        while rotation != n or not n_checked:
            if is_prime(mult_digs_in_sys(rotation, system)):
                min_system = min(min_system, system)
                break
            rotation = rotate(rotation)
            n_checked = True
    
    return None if min_system == float('inf') else min_system
#=====================================================
if __name__ == "__main__":
    n = int(input())

    # print(rotate(n))
    # print(mult_digs_in_sys(n, 4))

    print(check(n))
