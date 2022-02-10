# CS337 Project 1
# Ben Raivel
# process scheduling algorithm implementations

def FCFS_scheduler(processes, ready, CPU, time, verbose = True):
    '''
    first come first served scheduling algorithm
    '''
    pass

def SJF_scheduler():
    '''
    shortest job first scheduling algorithm
    '''
    pass

def priority_scheduler():
    '''
    priority scheduling algorithm
    '''
    pass

def find_lowest_arrival(ready):
    '''
    helper function to return earliest-arrived process from the ready queue
    '''
    lowest_arrival = ready[0]
    
    for process in ready:
        if process.get_arrival_time() < lowest_arrival.get_arrival_time():
            lowest_arrival = process

    return lowest_arrival

def add_ready(processes, ready, time):
    '''
    helper function, moves processes into ready queue at correct time
    '''
    pass