def Knapsack(w, v, W):
    n = len(w)
    ratios = []
    x = [0] * n
    for i in range(n):
        ratios[i] = v[i]/w[i]

    total_weight = 0 # knapsack is initially empty

    while total_weight < W:
        i = max(range(n), key=lambda k: ratios[k]) # greedy selection (highest v[i]/w[i])
        if ratios[i] == -1:   # already used
            break
        if total_weight + w[i] <= W:  # adding whole object i is feasible
            x[i] = 1 # take the whole item
            total_weight += w[i]
        else:
            x[i] = (W - total_weight) / w[i] # take a fraction
            total_weight = W  # knapsack is now full

        ratios[i] = -1

    return x  # return set of fractions

def main():
    w = [10, 20, 30]
    v = [60, 100, 120]
    W = 50
    print(Knapsack(w, v, W))

if __name__=="__main__":
    main()
