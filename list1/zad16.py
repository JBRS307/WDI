#Rozwiązanie ciągu pozornie skomplikowanego

def findLongestSeries():
    res = 0
    longest = 0
    for start_a in range(2, 10_001):
        a = start_a
        count = 0
        while abs(a-1) > 0.000000001:
            a = (a%2) * (3*a+1) + (1-(a%2)) * (a/2)
            count += 1
        if count > longest:
            longest = count
            res = start_a
    
    return res
#=====================================================
if __name__ == "__main__":
    print(findLongestSeries())