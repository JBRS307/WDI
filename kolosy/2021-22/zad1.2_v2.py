from random import randrange


def to_system_4(arr):
    leng = len(arr)
    res = [[] for _ in range(leng)]

    res_i = 0
    for n in arr:
        digs = [False]*4
        while n != 0:
            digs[n%4] = True #Nie trzeba bawić się w sprawdzanie indeksów
            n //= 4
        res[res_i] = digs
        res_i += 1
    
    return res
#-----------------------------------------------------

def change_mask(mask):
    i = 1
    while mask[-i]:
        i+=1
    
    mask[-i] = True
    for j in range(-i+1, 0):
        mask[j] = False
    
    return mask
#-----------------------------------------------------

def check_arr(arr):
    arr = to_system_4(arr)
    # print(arr)
    mask = [False, False, False, True] #Jest 15 różnych podzbiorów (wyłączamy zbiór pusty)

    max_seq = 0
    for _ in range(14): #Tyle musi być zmian między maskami
        seq = 0
        for num in arr:
            if num == mask:
                seq += 1
        
        max_seq = max(max_seq, seq)
        mask = change_mask(mask)
    
    # print(mask)

    return max_seq
#=====================================================

if __name__ == "__main__":
    n, k = map(int, input("Rozmiar, zakres: ").strip().split())

    arr = [randrange(1, k+1) for _ in range(n)]

    print(arr)

    print(check_arr(arr))
