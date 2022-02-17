# CS337 Project 1
# Ben Raivel
# process scheduling algorithm implementations

import numpy as np
import process

def FCFS_scheduler(processes, ready, CPU, time, verbose = True):
    '''
    first come first served scheduling algorithm
    '''
    # get process with lowest arrival
    current_process = find_lowest_arrival(ready)

    # set start time
    start_time = time

    # while burst time remains
    while(current_process.get_burst_time() > 0):

        #decrement burst time
        current_process.set_burst_time(current_process.get_burst_time()-1)

        # increment time
        time += 1

        # move newly arrived processes to ready queue
        add_ready(processes, ready, time)

    # set end time
    end_time = time
    
    # record process data to CPU list
    CPU.append(dict(process = current_process.get_PID(), 
                    start = start_time,
                    finish = end_time,
                    priority = current_process.get_priority()))

    # print process summary
    if(verbose):
        print('process'+ str(current_process.get_PID()) + 
            '\tstart time: ' + str(start_time) +  
            '\tend time: ' + str(end_time))

    return time

def SJF_scheduler(processes, ready, CPU, time, verbose = True):
    '''
    shortest job first scheduling algorithm
    '''
    # get shortest process
    current_process = find_shortest(ready)

    # set start time
    start_time = time

    # while burst time remains
    while(current_process.get_burst_time() > 0):

        #decrement burst time
        current_process.set_burst_time(current_process.get_burst_time()-1)

        # increment time
        time += 1

        # move newly arrived processes to ready queue
        add_ready(processes, ready, time)

    # set end time
    end_time = time
    
    # record process data to CPU list
    CPU.append(dict(process = current_process.get_PID(), 
                    start = start_time,
                    finish = end_time,
                    priority = current_process.get_priority()))

    # print process summary
    if(verbose):
        print('process'+ str(current_process.get_PID()) + 
            '\tstart time: ' + str(start_time) +  
            '\tend time: ' + str(end_time))

    return time

def priority_scheduler(processes, ready, CPU, time, verbose = True):
    '''
    priority scheduling algorithm
    '''
    # get process with highest
    current_process = find_highest_priority(ready)

    # set start time
    start_time = time

    # while burst time remains
    while(current_process.get_burst_time() > 0):

        #decrement burst time
        current_process.set_burst_time(current_process.get_burst_time()-1)

        # increment time
        time += 1

        # move newly arrived processes to ready queue
        add_ready(processes, ready, time)

    # set end time
    end_time = time
    
    # add process data to CPU list
    CPU.append(dict(process = current_process.get_PID(), 
                    start = start_time,
                    finish = end_time,
                    priority = current_process.get_priority()))

    # print process summary
    if(verbose):
        print('process'+ str(current_process.get_PID()) + 
            '\tstart time: ' + str(start_time) +  
            '\tend time: ' + str(end_time))

    return time

def find_lowest_arrival(ready):
    '''
    helper function to return earliest-arrived process from the ready queue
    '''
    # list for arrival times
    arrival = []

    # get arrival time of each process
    for process in ready:
        arrival.append(process.get_arrival_time())
    
    # find index of lowest arrival
    lowest = np.argmin(np.asarray(arrival))

    # remove and return lowest arrival
    return ready.pop(lowest)

def find_shortest(ready):
    '''
    helper function to find shortest processes in ready
    '''
    # list for burst times
    burst = []

    # add burst times to list
    for process in ready:
        burst.append(process.get_burst_time())

    # find index of shortest burst time
    lowest = np.argmin(np.asarray(burst))

    # remove and return
    return ready.pop(lowest)

def find_highest_priority(ready):
    priority = []
    for process in ready:
        priority.append(process.get_priority())

    highest = np.argmax(np.asarray(priority))

    return ready.pop(highest)

def add_ready(processes, ready, time):
    '''
    helper function, moves processes into ready queue at correct time
    '''
    for process in processes:
        if process.get_arrival_time() == time:
            ready.append(process)
            


def main():
    p0 = process.Process(0, 3, 0, 4)
    p1 = process.Process(1, 6, 3, 7)
    p2 = process.Process(2, 2, 9, 2)
    p3 = process.Process(3, 12, 10, 6)

    ready = [p0, p1]

    lowest_arrival = find_lowest_arrival(ready)

    print(lowest_arrival.get_arrival_time())

    ready = [p3, p2, p1]

    lowest_arrival = find_lowest_arrival(ready)

    print(lowest_arrival.get_arrival_time())

    processes = [p0, p1, p2, p3]

    ready = []

    time = 0

    add_ready(processes, ready, time)

    print(ready, processes)

if __name__ == '__main__':
    #main()
    pass