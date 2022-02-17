from turtle import st
import process as p
import scheduler as s
import pandas as pd
import random

from scipy.stats import dlaplace, boltzmann, planck


def kernel(scheduler, processes = None, verbose = True):
    '''
    uses scheduler function to schedule processes and record statistics
    '''
    # initialize CPU, ready queue, time
    CPU = []
    ready = []
    time = 0
    if processes == None:
        processes = [p.Process(0, 3, 0, 4),
                 p.Process(1, 6, 1, 7),
                 p.Process(2, 2, 2, 2),
                 p.Process(3, 12, 3, 6)]
    s.add_ready(processes, ready, time)

    while len(ready) > 0:
        time = scheduler(processes, ready, CPU, time, verbose)

    wait_times = []
    turnaround_times = []
    for finished_process in CPU:
        PID = finished_process['process']
        process = processes[PID]
        arrival_time = process.get_arrival_time()
        start_time = finished_process['start']
        end_time = finished_process['finish']
        wait_times.append(start_time -arrival_time)
        turnaround_times.append(end_time-arrival_time)
    try:
        print('avg. wait time: ' + str(sum(wait_times)/len(wait_times)), '\navg. turnaround time: ' + str(sum(turnaround_times)/len(turnaround_times)))
    except:
        pass
    
    df = pd.DataFrame(CPU)
    df.to_csv('results.csv', index=False)
    