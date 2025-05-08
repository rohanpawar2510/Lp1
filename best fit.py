def bestfit(blocksize, m, processsize, n):
    allocation = [-1] * n

    for i in range(n):
        bestidx = -1
        for j in range(m):
            if blocksize[j] >= processsize[i]:  # Changed '>' to '>=' to allow exact fit
                if bestidx == -1 or blocksize[bestidx] > blocksize[j]:
                    bestidx = j

        if bestidx != -1:
            allocation[i] = bestidx
            blocksize[bestidx] -= processsize[i]

    print("\nBest Fit Allocation:")
    print("Process No\tProcess Size\tBlock No")
    for i in range(n):
         
        print(f"{i + 1}\t\t{processsize[i]}\t\t", end="")
        if allocation[i] != -1:
            print(f"{allocation[i] + 1}")
        else:
            print("Not Allocated")



if __name__ == "__main__":
    blocksize = list(map(int, input("Enter memory block sizes (comma-separated): ").split(',')))
    m = len(blocksize)
    
    processsize = list(map(int, input("Enter process sizes (comma-separated): ").split(',')))
    n = len(processsize)

    bestfit(blocksize, m, processsize, n)
