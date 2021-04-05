# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:04:55 2021

@author: Hacha
"""

from functools import partial
import obstacles
import robot
import genetic
from analyze import timer

#things = obstacles.generate_things(8) # contain 40 bit
things = obstacles.second_example

time_limit = -1.0
time_curr  = 0.0

rbot = robot.Robot(alpha=1, delta= 4)

print("")
print("GENETIC ALGORITHM")
print("----------")

with timer():
	population, generations, min_time = genetic.run_evolution(
		populate_func=partial(genetic.generate_population, size=10,weight = 25, height = 20 ,genome_length=20),
		fitness_func=obstacles.fitness,
		time_limit=time_limit,
        time_curr= time_curr,
        rbot= rbot,
        obthings = things,
		generation_limit=20
	)

print(generations)
sack = obstacles.from_genome(population[0], things)
obstacles.print_stats(sack)
print(population[0])
print("Time min = {}".format(min_time))


