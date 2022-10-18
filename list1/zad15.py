from math import sqrt

def findPI():
    product = sqrt(0.5)
    nextt = product
    for _ in range(1000):
        nextt = sqrt(0.5+0.5*(nextt))
        product *= nextt
    return 2/product
#=====================================================
if __name__ == "__main__":
    print(findPI())