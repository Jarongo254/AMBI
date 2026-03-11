def hsort(T):
    n = len(T) - 1
    make_heap(T)

    for i in range(n, 1, -1):
        T[1],T[i] = T[i],T[1]
        sift_down(T, 1, i-1)
    return T

def percolate_up(T, i):
    k = i
    while True:
        j = k
        if j > 1 and T[j//2] < T[k]:
            k = j//2
        temp = T[j]
        T[j] = T[k]
        T[k] = temp

        if j == k:
            break
    return T

def sift_down(T, i, n):
    #n = len(T) - 1 # -1 because python works with 0 based indexing but heap uses 1 based indexing
    k = i
    while True:
        j = k
        if 2*j <= n and T[2*j] > T[k]:
            k = 2*j
        if 2*j + 1 <= n and T[(2*j)+1] > T[k]:
            k = 2*j + 1

        T[j], T[k] = T[k], T[j] # swapping
        if j == k:
            break
    return T

def make_heap(T):
    n = len(T) - 1
    for i in range(n//2, 0, -1):
        sift_down(T, i, n)
    return T

def main():
    T = [None] + list(map(int, input("Enter your array to sort, space separated: ").split()))
    print("Sorted array:", hsort(T)[1:])

if __name__=="__main__":
    main()
