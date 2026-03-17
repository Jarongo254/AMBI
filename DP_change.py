'''
function change(N)
    array d[1...n]            // coin denominations
    array C[1...n, 0...N]     // DP matrix

    for i <- 1 to n do
        C[i,0] <- 0           // amount 0 needs 0 coins

    for i <- 1 to n do
        for j <- 1 to N do

            if i = 1 and j < d[1] then
                C[i,j] <- +∞

            else if i = 1 then
                C[i,j] <- 1 + C[1, j - d[1]]

            else if j < d[i] then
                C[i,j] <- C[i-1,j]

            else
                C[i,j] <- min( C[i-1,j],
                               1 + C[i, j - d[i]] )

    return C

function backtrack(N)
    array d[1...n]  // Coin denominations
    C = change(N)
    i <- n
    j <- N
    while j > 0 do
        if i > 1 and C[i,j] = C[i-1,j] then
            i <- i - 1    // No coin of denom i needed
        else
            print d[i] // coin i used
            j <- j - d[i]
'''
def change(N):
    D = [100, 25, 10, 5, 1]   # coin denominations
    n = len(D)

    # DP matrix: n rows, N+1 columns
    C = [[0]*(N+1) for _ in range(n)]

    # First column = 0
    for i in range(n):
        C[i][0] = 0

    for i in range(n):
        for j in range(1, N+1):

            if i == 0 and j < D[0]:
                C[i][j] = float('inf')

            elif i == 0:
                C[i][j] = 1 + C[0][j - D[0]]

            elif j < D[i]:
                C[i][j] = C[i-1][j]

            else:
                C[i][j] = min(C[i-1][j],
                              1 + C[i][j - D[i]])

    return C, C[n-1][N]

def backtrack(N):
    D = [100, 25, 10, 5, 1]
    C, _ = change(N)

    i = len(D) - 1
    j = N

    while j > 0:
        if i > 0 and C[i][j] == C[i-1][j]:
            i = i - 1
        else:
            print(f"coin of denomination {D[i]} used")
            j = j - D[i]

def main():
    N = int(input("Enter amount of change to pay"))
    C,v = change(N)
    print("Optimal number of coins: ", v)
    backtrack(N)

if __name__=="__main__":
    main()
