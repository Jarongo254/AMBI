
"""
A la russe algorithm for multiplication of two large integers
"""

def russe(m,n):
    result = 0 # Initailaize result with 0
    while n > 0: # Repeat until n = 1 (n > 0)
        if n%2 != 0: # checks if n is odd after each division step
            result = result + m

        n = n // 2 # floor division of n by 2
        m = m * 2 # cumulatively multiplying m by 2
    return result

def main():
    m = int(input("Enter first number: "))
    n = int(input("Enter second number: "))
    print(russe(m,n))

if __name__ == "__main__":
    main()
