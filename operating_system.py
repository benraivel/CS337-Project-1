import process
import scheduler
import pandas as pd
import random

from scipy.stats import dlaplace, boltzmann, planck


def kernel(scheduler, verbose = True):
    CPU = []
    ready = []

    time = 0

arrival_times = []
for i in range(100):
    arrival_times.append(random.randint(0,100))

arrival_times.sort()

burst_times = planck.rvs(0.4, size = 100) + 1

print(arrival_times, burst_times, sum(burst_times)/100)
