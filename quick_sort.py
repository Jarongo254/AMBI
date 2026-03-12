def pivot(T,i,j): # var_l should be returned by something???
    p = T[i]            #Using first element as pivot
    k = i
    l = j + 1
    while True:
        k = k+1
        while k <= j and T[k] < p:
            k = k + 1
        l = l - 1
        while T[l] > p:
            l = l - 1
        if k >= l:
            break

        T[k], T[l] = T[l], T[k]
    T[i], T[l] = T[l], T[i]     # Place pivot in correct position
    return l             # Return partition index

def quick_sort(T, i, j):
    if i < j:
        l = pivot(T, i, j)
        quick_sort(T, i, l - 1)
        quick_sort(T, l + 1, j)
    return T

def main():
    T = list(map(int, input("Enter your array to sort, space separated: ").split()))
    i=0
    j= len(T) - 1
    print("Sorted array:", quick_sort(T,i,j))

if __name__ == "__main__":
    main()

