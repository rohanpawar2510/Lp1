def fcfs(processes, burst_time):
    n = len(processes)
    waiting_time = [0] * n
    turnaround_time = [0] * n

    # Calculate waiting time
    for i in range(1, n):
        waiting_time[i] = waiting_time[i - 1] + burst_time[i - 1]

    # Calculate turnaround time
    for i in range(n):
        turnaround_time[i] = waiting_time[i] + burst_time[i]

    # Display results
    print("Process  BT  WT  TAT")
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"P{processes[i]}      {burst_time[i]}    {waiting_time[i]}    {turnaround_time[i]}")
    print(f"Average waiting time = {total_wt / n}")
    print(f"Average turn around time = {total_tat / n}")

# Example usage
processes = [1, 2, 3]
burst_time = [5, 9, 6]
fcfs(processes, burst_time)
