def increment_triangle(n):
    print("\n"+"Increment Triangle")
    for i in range(n):
        for j in range(i+1):
            print('*', end=" ")
        print()


def decrement_triangle(n):
    print("\n"+"Decrement Triangle")
    for i in range(n):
        for j in range(n, i, -1):
            print("*", end=" ")
        print()


def in_dec_trianlge(n):
    print("\n"+"Increment Decrement Triangle")
    for i in range(n):
        for j in range(i+1):
            print("*", end=" ")
        print()
    for i in range(n):
        for j in range(n-1, i, -1):
            print("*", end=" ")
        print()


def rev_increment_triangle(n):
    print("\nReverse Increment Triangle")
    for i in range(n):
        for j in range(n):
            if(j >= i):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def rev_decrement_triangle(n):
    print("\nReverse Decrement Triangle")
    for i in range(n):
        for j in range(n):
            if(j >= n-i-1):
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()


def diamond_pattern(n):
    print("\nDiamond Pattern")
    for i in range(n):
        for j in range(i, n):
            print(" ", end=" ")
        for j in range(i):
            print("*", end=" ")
        for j in range(i+1):
            print("*", end=" ")
        print()
    for i in range(1, n):
        for j in range(i+1):
            print(" ", end=" ")
        for j in range(i, n):
            print("*", end=" ")
        for j in range(i+1, n):
            print("*", end=" ")
        print()


if __name__ == "__main__":
    n = int(input())
    # increment_triangle(n)
    # decrement_triangle(n)
    # in_dec_trianlge(n)
    # rev_increment_triangle(n)
    # rev_decrement_triangle(n)
    diamond_pattern(n)
