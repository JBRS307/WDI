def change_mask(mask):
    i = 1
    while mask[-i]:
        i+=1
    
    mask[-i] = True
    for j in range(-i+1, 0):
        mask[j] = False
    
    return mask

if __name__ == "__main__":
    mask = [False, False, False, True]

    for _ in range(14):
        mask = change_mask(mask)
        print(mask)