import time
from insert_sort import insert

def pivot(T,i,j): # var_l should be returned by something???
    p = T[i]            #Using first element as pivot
    print("Initial pivot is:", p)
    time.sleep(2)
    k = i
    print("Pointer k initiated at",k)
    time.sleep(2)
    print("Element here is",T[k])
    time.sleep(2)
    l = j + 1
    print("Pointer l initiated at",l)
    time.sleep(2)
    print("Currently no element here (beyond array)")
    time.sleep(2)
    while True:
        k = k+1
        print("pointer k moved to",k)
        time.sleep(2)
        print("Element here is",T[k])
        time.sleep(2)
        while k <= j and T[k] < p:
            k = k + 1
            print("pointer k moved to",k)
            time.sleep(2)
            if k <= j:
                print("Element here is",T[k])
            if k == j:
                print("pointer k now at the last index")
            if k > j:
                print("k has moved beyond last element")
            time.sleep(2)
        l = l - 1
        print("pointer l moved to",l)
        time.sleep(2)
        print("Element here is",T[l])
        time.sleep(2)
        while T[l] > p:
            print(f"T[l] is {T[l]} and p is {p}")
            l = l - 1
            print("pointer l moved to",l)
            time.sleep(2)
        if k >= l:
            print(f"k is now {k} and l is now {l}. Crossover")
            break

        T[k], T[l] = T[l], T[k]
        print(f"{T[k]} and {T[l]} swapped")
        time.sleep(2)
        print(f"Array is now {T}")
        time.sleep(2)
    T[i], T[l] = T[l], T[i]     # Place pivot in correct position
    print(f"{T[i]} and {T[l]} swapped")
    time.sleep(2)
    print(f"Array is now {T}")
    time.sleep(2)
    return l             # Return partition index

def quick_sort(T, i, j, depth=0):
    indent = "  " * depth

    if j - i + 1 <= 4:
        print("Array is sufficiently small. Using insertion sort now")
        insert(T)

    else:
        print(f"{indent}QuickSort called on indices [{i}:{j}] → {T[i:j+1]}")
        time.sleep(2)
        l = pivot(T, i, j)

        print(f"{indent}Pivot placed at index {l}, value {T[l]}")
        print(f"{indent}Left partition: {T[i:l]}")
        print(f"{indent}Right partition: {T[l+1:j+1]}")
        time.sleep(2)

        quick_sort(T, i, l - 1, depth+1)
        quick_sort(T, l + 1, j, depth+1)

    #else:
    #    print(f"{indent}Subarray of size ≤1 → already sorted")
    #    time.sleep(2)

    return T

def main():
    #T = list(map(int, input("Enter your array to sort, space separated: ").split()))
    T = [5, 2, 8, 1, 7, 10, 3]
    i=0
    j= len(T) - 1
    print("Sorted array:", quick_sort(T,i,j))

if __name__ == "__main__":
    main()

