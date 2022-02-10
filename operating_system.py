import process
import scheduler
import pandas as pd
import random

from scipy.stats import dlaplace, boltzmann, planck


def kernel(scheduler, verbose = True):
    CPU = []
    ready = []

    time = 0


# generate 100 random arrival times, evenly distributed
arrival_times = []
for i in range(100):
    arrival_times.append(random.randint(0,100))
arrival_times.sort()

# generate 100 random burst times following planck distribution
burst_times = planck.rvs(0.4, size = 100) + 1

print(arrival_times, burst_times, sum(burst_times)/100)
