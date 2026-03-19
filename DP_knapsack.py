def knapsack(w,v,W):
    n = len(w)
    if n == 0 or W <= 0:
        return [[0] * (W + 1)] if W >= 0 else [[0]]

    V = [[0]*(W+1) for _ in range(n)] # DP matrix
    for i in range(0, n):
        for j in range(0, W+1):
            if i == 0 or j == 0:
                V[i][j] = 0
            elif w[i] <= j:   # the item fits
                V[i][j] = max(V[i-1][j],  # Don't take current item
                              v[i] + V[i-1][j-w[i]])  # Take current item
            else:
                V[i][j] = V[i-1][j]
    return V

def backtrack(w,v,W):
    V = knapsack(w,v,W)
    if not w or W <= 0:
        print("No items can be taken")
        return

    i = len(w) - 1
    j = W

    while i >= 0 and j > 0:
        if i > 0 and V[i][j] == V[i-1][j]:
            i = i - 1
        else:
            print(f"Item {w[i]} taken")
            j = j - w[i]
            i = i - 1

def main():
    w = [2, 3, 4, 5]
    v = [3, 4, 5, 6]
    W = 5

    V = knapsack(w, v, W)
    result = V[len(w)-1][W] if w else 0
    print(f"Max value: {result}")
    backtrack(w, v, W)

if __name__=="__main__":
    main()
