def check_mass(arr, mass, i=0, mass_sum = 1):
    if mass_sum == mass:
        return True
    if mass_sum - 1 == mass:
        return True
    
    if i+1 < len(arr):
        possible = check_mass(arr, mass, i+1, mass_sum + arr[i+1])
        if possible:
            return True
        
        possible = check_mass(arr, mass, i+1, mass_sum)
        if possible:
            return True
        
    return False


#=====================================================

if __name__ == "__main__":
    arr = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    mass = int(input())

    print(check_mass(arr, mass))