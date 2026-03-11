def insert(T): # Input is an array T of length n
    for i in range(1,len(T)): # At each each i the comparison is with i-1, so the starting point is at position 2 - 1st element is also assumed as already sorted - this line gives O(n-1)
        x = T[i]
        j = i-1
        while j >= 0 and x < T[j]: # if the element at i is smaller than previous, move it backwards
            T[j+1] = T[j]
            j = j -1
        T[j+1] = x

    return T

def main():
    T = list(map(int, input("Enter your array to sort, space separated: ").split()))
    print("Sorted array:", insert(T))

if __name__ == "__main__":
    main()

