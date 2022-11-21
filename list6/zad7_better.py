def check_mass(arr, mass, i):
    if mass == 0:
        return True
    if i >= len(arr) or mass < 0:
        return False
    
    return check_mass(arr, mass-arr[i], i+1) or check_mass(arr, mass, i+1)
#=====================================================

if __name__ == "__main__":
    arr = [1, 2, 5, 10, 20, 50, 100, 200, 500, 1000]
    mass = int(input())

    print(check_mass(arr, mass, 0))