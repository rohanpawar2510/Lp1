def round_robin(processes, burst_time, quantum):
    n = len(processes)
    rem_bt = burst_time[:]
    t = 0  # current time
    waiting_time = [0] * n

    while True:
        done = True
        for i in range(n):
            if rem_bt[i] > 0:
                done = False
                if rem_bt[i] > quantum:
                    t += quantum
                    rem_bt[i] -= quantum
                else:
                    t += rem_bt[i]
                    waiting_time[i] = t - burst_time[i]
                    rem_bt[i] = 0
        if done:
            break

    turnaround_time = [waiting_time[i] + burst_time[i] for i in range(n)]

    print("Process  BT  WT  TAT")
    for i in range(n):
        print(f"P{processes[i]}      {burst_time[i]}    {waiting_time[i]}    {turnaround_time[i]}")

# Example usage
processes = [1, 2, 3]
burst_time = [24, 3, 3]
quantum = 4
round_robin(processes, burst_time, quantum)
