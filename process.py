# CS337 Project 1
# Ben Raivel
# process class

class Process():
    
    def __init__(self, PID, burst_time, arrival_time, priority):
        '''
        init process with PID, burst time, arrival time, and proiority
        '''
        self.PID = PID
        self.burst_time = burst_time
        self.arrival_time = arrival_time
        self.priority = priority

        # set wait time and turnaround time to zero
        self.wait_time = 0
        self.turnaround_time = 0


    # getter and setter methods for process
    def get_PID(self):
        return self.PID

    def get_burst_time(self):
        return self.burst_time

    def set_burst_time(self, burst_time):
        self.burst_time = burst_time

    def get_arrival_time(self):
        return self.arrival_time

    def get_priority(self):
        return self.priority

    def set_priority(self, priority):
        self.priority = priority
