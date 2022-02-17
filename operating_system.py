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
    # initialize CPU, ready queue
    CPU = []
    ready = []

    # if a list of processes isn't provided
    if processes == None:
        processes = [p.Process(0, 3, 0, 4),
                 p.Process(1, 6, 1, 7),
                 p.Process(2, 2, 2, 2),
                 p.Process(3, 12, 3, 6)]
    
    # set time to zero
    time = 0

    # move processes into ready queue
    s.add_ready(processes, ready, time)

    # loop while 
    while len(CPU) < len(processes):
        if len(ready) == 0:
            # increment time
            time += 1

            # move newly arrived processes to ready queue
            s.add_ready(processes, ready, time)
        
        else:
            time = scheduler(processes, ready, CPU, time, verbose)

    # lists for wait and turnaround times
    wait_times = []
    turnaround_times = []

    # loop over CPU
    for finished_process in CPU:

        # get PID of process
        PID = finished_process['process']

        # get process object
        process = processes[PID]

        # get arrival time from process
        arrival_time = process.get_arrival_time()

        # get start and end time from process 
        start_time = finished_process['start']
        end_time = finished_process['finish']

        # calculate and add wait and turnaround times to lists
        wait_times.append(start_time -arrival_time)
        turnaround_times.append(end_time-arrival_time)


    print('avg. wait time: ' + str(sum(wait_times)/len(wait_times)), '\navg. turnaround time: ' + str(sum(turnaround_times)/len(turnaround_times)))

    df = pd.DataFrame(CPU)
    df.to_csv('results.csv', index=False)
    