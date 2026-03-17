"""
function makechange(n)
    C = {100, 25, 10, 5, 1} // Set of candidates (available coins for selection)
    S <- ∅  // initialized empty solution set
    s <- sum of items in S
    while s != n
        x <- largest item in C such that x + s <= n // selection function (largest item); feasibility function (x + s <= n can lead to a soln)
        if no such item
            return no solution found
        S <- S ∪ {a coin of value x}
        s <- s + x
    return S // Solution function
"""

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
