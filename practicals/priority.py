n = int(input("Enter the number of processes: "))
p = [0] * 10
pp = [0] * 10
bt = [0] * 10
w = [0] * 10
t = [0] * 10

print("Enter the burst time and priority for each process:")
for i in range(n):
    print(f"Process[{i + 1}]")
    bt[i] = int(input("Burst Time: "))
    pp[i] = int(input("Priority: "))
    p[i] = i + 1

for i in range(n - 1):
    for j in range(i + 1, n):
        if pp[i] < pp[j]:
            pp[i], pp[j] = pp[j], pp[i]
            bt[i], bt[j] = bt[j], bt[i]
            p[i], p[j] = p[j], p[i]

w[0] = 0
awt = 0
t[0] = bt[0]
atat = t[0]

for i in range(1, n):
    w[i] = t[i - 1]
    awt += w[i]
    t[i] = w[i] + bt[i]
    atat += t[i]

print("Process \t Burst time \t Wait time \t TAT \t Priority ")
for i in range(n):
    print(f"{p[i]}\t\t{bt[i]}\t\t{w[i]}\t\t{t[i]}\t\t{pp[i]}")

awt /= n
atat /= n

print(f"Average Wait time: {awt}")
print(f"Average TAT: {atat}")
