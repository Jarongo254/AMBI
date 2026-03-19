def change(n):
    C = {100, 25, 10, 5, 1}
    S = []  # Initialize empty solution set
    s = 0   # sum of items in S
    while s != n:
        feasible = {x for x in C if x + s <= n}
        if not feasible:
            return "No solution found"

        x = max(feasible)
        S.append(x)
        s += x
    return S

def main():
    #C = list(map(int, input("Enter denominations, space separated: ").split()))
    n = int(input("Amount to pay back: "))
    print(change(n))

if __name__ == "__main__":
    main()
