from os import system


def hanoi(stack_a, stack_b, stack_c, n):
    # if n == 0:
    #     return

    if n == 1:
        stack_b.append(stack_a.pop())
    else:
        hanoi(stack_a, stack_c, stack_b, n-1)
        stack_b.append(stack_a.pop())
        hanoi(stack_c, stack_b, stack_a, n-1)
    

#=====================================================

if __name__ == "__main__":
    system("clear")
    stack_a = [i for i in range(5, -1, -1)]
    stack_b = []
    stack_c = []

    hanoi(stack_a, stack_b, stack_c, len(stack_a))
    print(stack_a)
    print(stack_b)
    print(stack_c)