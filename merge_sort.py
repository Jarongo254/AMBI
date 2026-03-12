import math
from insert_sort import insert


def merge(U, V, T):
    i=0
    j=0
    m = len(U)
    n = len(V)
    U.append(float('inf'))
    V.append(float('inf'))
    for k in range(0, m+n):
        if U[i] < V[j]:
            T[k] = U[i]
            i += 1
        else:
            T[k] = V[j]
            j += 1
    return T

def merge_sort(T):
    n = len(T)
    if n < 5:
        return insert(T)

    else:
        U = T[0:n//2+1]
        V = T[n//2 + 1:n]
        merge_sort(U)
        merge_sort(V)
        merge(U, V, T)
    return T


def main():
    T = list(map(int, input("Enter your array to sort, space separated: ").split()))
    print("Sorted array:", merge_sort(T))

if __name__ == "__main__":
    main()
