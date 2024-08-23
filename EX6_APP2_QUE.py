# Function to find the waiting time for all processes
def find_waiting_time(processes, n, bt, wt):
    # Waiting time for the first process is 0
    wt[0] = 0
    # Calculating waiting time
    for i in range(1, n):
        wt[i] = bt[i - 1] + wt[i - 1]

# Function to calculate turn around time
def find_turn_around_time(processes, n, bt, wt, tat):
    # Calculating turn around time by adding bt[i] + wt[i]
    for i in range(n):
        tat[i] = bt[i] + wt[i]

# Function to calculate average time
def find_avg_time(processes, n, bt):
    wt = [0] * n
    tat = [0] * n
    total_wt = 0
    total_tat = 0
    
    # Function to find waiting time of all processes
    find_waiting_time(processes, n, bt, wt)
    
    # Function to find turn around time for all processes
    find_turn_around_time(processes, n, bt, wt, tat)
    
    # Display processes along with all details
    print("Process ID\tBurst Time\tWaiting Time\tTurn Around Time")
    
    # Calculate total waiting time and total turn around time
    for i in range(n):
        total_wt += wt[i]
        total_tat += tat[i]
        print(f"{processes[i]}\t\t{bt[i]}\t\t{wt[i]}\t\t{tat[i]}")
    
    print(f"Average waiting time = {total_wt / n}")
    print(f"Average turn around time = {total_tat / n}")

# Driver code
if __name__ == "__main__":
    # Process IDs
    processes = [1, 2, 3]
    n = len(processes)
    # Burst time of all processes
    bt = [10, 5, 8]
    
    find_avg_time(processes, n, bt)
