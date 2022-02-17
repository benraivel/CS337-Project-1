import process as p
import scheduler as s
import pandas as pd
import random

from scipy.stats import dlaplace, boltzmann, planck


def kernel(scheduler, verbose = True):
    '''
    uses scheduler function to schedule processes and record statistics
    '''
    CPU = []
    ready = []
    time = 0
    
    processes = [p.Process(0, 3, 0, 4),
                 p.Process(1, 6, 1, 7),
                 p.Process(2, 2, 2, 2),
                 p.Process(3, 12, 3, 6)]

    s.add_ready(processes, ready, time)

    while len(ready) > 0:
        time = scheduler(processes, ready, CPU, time, verbose)

    for process in CPU:
        PID = process[process]

    df = pd.DataFrame(CPU)
    df.to_csv('results.csv', index=False)
    
        


def generate_processes(n_process = 100, arrival_freq = 1):
    # generate n random arrival times, evenly distributed
    arrival_times = []
    for i in range(n_process):
        arrival_times.append(random.randint(0,n_process*arrival_freq))
    arrival_times.sort()
    
    # generate n random burst times following planck distribution
    burst_times = planck.rvs(0.4, size = n_process) + 1

    # construct list of processes
    processes = []
    for i in range(n_process):
        processes.append(process.Process(i, burst_times[i], arrival_times[i], random.randint(0,5)))

    return processes

#kernel(s.FCFS_scheduler)


print()
kernel(s.FCFS_scheduler)

kernel(s.SJF_scheduler)

kernel(s.priority_scheduler)