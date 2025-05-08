def bestFit(blockSize, m, processSize, n):  
    allocation = [-1] * n
    for i in range(n):
        bestIdx = -1
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                if bestIdx == -1 or blockSize[bestIdx] > blockSize[j]:
                    bestIdx = j
        if bestIdx != -1:
            allocation[i] = bestIdx
            blockSize[bestIdx] -= processSize[i]
    print("Process No.\tProcess Size\tBlock no.")
    for i in range(n):
        print(f"{i + 1}\t\t{processSize[i]}\t\t", end="")
        if allocation[i] != -1:
            print(f"{allocation[i] + 1}")
        else:
            print("Not Allocated")

if __name__ == '__main__':
    blockSize = list(map(int, input("Enter memory block sizes (comma-separated): ").split(',')))
    m = len(blockSize)
    processSize = list(map(int, input("Enter process sizes (comma-separated): ").split(',')))
    n = len(processSize)
    bestFit(blockSize, m, processSize, n)
