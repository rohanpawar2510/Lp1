def nextFit(blockSize, m, processSize, n):  
    allocation = [-1] * n
    j=0
    t = m-1
    for i in range(n):
        while j<m:
        
        
            if blockSize[j] >= processSize[i]:
                allocation[i]=j
                blockSize[j]-= processSize[i]
                t=(j-1)%m
                break
            if t==j:
                t=(j-1)%m
                break
            j=(j+1)%m
                
                  
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
    nextFit(blockSize, m, processSize, n)

