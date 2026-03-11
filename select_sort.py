def select(T):
    for i in range(0, len(T)-1):
        minj = i
        minx = T[i]
        for j in range(i+1, len(T)):
            if T[j] < minx:
                minj = j
                minx = T[j]

        T[minj] = T[i]
        T[i] = minx

    return T


def main():
    T = list(map(int, input("Enter your array to sort, space separated: ").split()))
    print("Sorted array:", select(T))

if __name__ == "__main__":
    main()
