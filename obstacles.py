# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:03:49 2021

@author: Hacha
"""

from genetic import Genome
from collections import namedtuple
from forbid_thing import ForbitThing
# Thing = namedtuple('Thing', ['name', 'value', 'weight'])

# first_example = [
#     Thing('Laptop', 500, 2200),
#     Thing('Headphones', 150, 160),
#     Thing('Coffee Mug', 60, 350),
#     Thing('Notepad', 40, 333),
#     Thing('Water Bottle', 30, 192),
# ]

# second_example = [
#     Thing('Mints', 5, 25),
#     Thing('Socks', 10, 38),
#     Thing('Tissues', 15, 80),
#     Thing('Phone', 500, 200),
#     Thing('Baseball Cap', 100, 70)
# ] + first_example

Thing = namedtuple('Thing', ['name', 'infor'])
first_example = [
    #x = 200, y = 250
    Thing('Obstacle1', ForbitThing([0,0], [1, 1], 'forbit_0')),
    Thing('Obstacle2', ForbitThing([180,160], [3, 2], 'forbit_1')),
    Thing('Obstacle3', ForbitThing([100,200], [1, 6], 'forbit_2')),
    Thing('Obstacle4', ForbitThing([70,10], [-1, 1], 'forbit_3')),
    Thing('Obstacle5', ForbitThing([90,220], [-1, 0], 'forbit_4')),
    Thing('Obstacle6', ForbitThing([12,120], [4, 5], 'forbit_5')),
    Thing('Obstacle7', ForbitThing([30,300], [1, -2], 'forbit_6')),
    Thing('Obstacle8', ForbitThing([8,150], [1, 0], 'forbit_7'))
    ]

second_example = [
    #x = 200, y = 250
    ForbitThing([0,0], [1, 1], 'forbit_1'),
    ForbitThing([0,0], [3, 2], 'forbit_2'),
    ForbitThing([21,22], [1, 6], 'forbit_3'),
    ForbitThing([70,10], [3, 1], 'forbit_4'),
    ForbitThing([170,100], [-1, 0], 'forbit_5'),
    ForbitThing([12,10], [4, 5], 'forbit_6'),
    ForbitThing([20,0], [1, 2],'forbit_7'),
    ForbitThing([8,29], [0, 1], 'forbit_8'),
    ForbitThing([50,10], [4, 5], 'forbit_9'),
    ForbitThing([80,0], [1, 2],'forbit_10'),
    ForbitThing([8,29], [1, 1], 'forbit_11')
    ]


def generate_things(num: int) -> [Thing]:
    return [Thing(f"thing{i}", i, i) for i in range(1, num+1)]


def fitness(genome: Genome, time_limit, time_curr) -> int:
    if len(genome) != 40:
        raise ValueError("genome must be 40 bits")

    if time_limit < 0 :
        return 1, time_curr
    
    if time_limit > time_curr:
        time_limit = time_curr
        return 1, time_curr
    return 0, time_limit
    

def from_genome(genome: Genome, things: [ForbitThing]) -> [ForbitThing]:
    result = []
    for i, thing in enumerate(things):
        if genome[i] == 1:
            result += [thing]
    return result


def to_string(things: [ForbitThing]):
    #return f"[{', '.join([t.name for t in things])}]"
    return f"[{', '.join([t.name for t in things])}]"


def value(things: [ForbitThing]):
    return sum([t.value for t in things])


def weight(things: [ForbitThing]):
    return sum([p.weight for p in things])


def print_stats(things: [Thing]):
    print(f"Things: {to_string(things)}")
    #print(f"Value {value(things)}")
    #print(f"Weight: {weight(things)}")