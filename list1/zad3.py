def commonSubSeq(sumToFind):
    currSum = 0
    smallest = secondSmallest = 1
    secondLargest, largest = 0, 1

    while smallest <= sumToFind:
        secondLargest, largest = largest, secondLargest + largest
        currSum += largest
        if currSum == sumToFind:
            return True
        while currSum > sumToFind:
            currSum -= smallest
            smallest, secondSmallest = secondSmallest, secondSmallest + smallest
            if currSum == sumToFind:
                return True
    
    return False
#=====================================================
if __name__ == "__main__":
    n = int(input())
    print(commonSubSeq(n))