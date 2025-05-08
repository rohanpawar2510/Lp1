def firstFit(blockSize, m, processSize, n):  
    allocation = [-1] * n
    for i in range(n):
        
        for j in range(m):
            if blockSize[j] >= processSize[i]:
                allocation[i]=j
                blockSize[j]-= processSize[i]
                break
                
                  
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
    firstFit(blockSize, m, processSize, n)

