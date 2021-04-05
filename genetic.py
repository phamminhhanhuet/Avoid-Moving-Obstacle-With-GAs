# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:00:12 2021

@author: Hacha
"""

from random import choices, randint, randrange, random, uniform, randint
from typing import List, Optional, Callable, Tuple
from robot import Robot
from forbid_thing import ForbitThing
import analyze
import math

Genome = List[int]
Population = List[Genome]
PopulateFunc = Callable[[], Population]
FitnessFunc = Callable[[Genome], int]
SelectionFunc = Callable[[Population, FitnessFunc], Tuple[Genome, Genome]]
CrossoverFunc = Callable[[Genome, Genome], Tuple[Genome, Genome]]
MutationFunc = Callable[[Genome], Genome]
PrinterFunc = Callable[[Population, int, FitnessFunc], None]


def generate_genome(length: int, weight: int, height:int) -> Genome:
    """This function is to generate random genomes"""
    # 20 first bit = possible rules, 10 bit = distance, 10 bit = angle
    limit_dis = math.sqrt((weight) * (weight) + height * height)  # convert m -> dm
    dis_rand = uniform(0.2, limit_dis/10)
    agl_rand = uniform(0.0, 90.0)
    l =  choices([0, 1], k=length) + analyze.float_bin(agl_rand, places=10)  +analyze.float_bin(dis_rand, places=10) 
    #print(len(l))
    return l


def generate_population(size: int, weight: int, height: int,  genome_length: int) -> Population:
    return [generate_genome(genome_length , weight, height) for _ in range(size)]


def single_point_crossover(a: Genome, b: Genome) -> Tuple[Genome, Genome]:
    if len(a) != len(b):
        raise ValueError("Genomes a and b must be of same length")

    length = len(a)
    if length < 2:
        return a, b

    p = randint(1, length - 20 -1)
    q = randint(length - 20 +1, length - 10 -1)
    r = randint(length - 10 +1, length - 1)
    
    first_m = a[0:p] + b[p:20]
    first_n = b[0:p] + a[p:20] 
    second_m = a[20:q]
    second_n = b[20:q] 
    
    for i in range(q, 30):
        if b[i] != '.'and a[i] != '.':
            second_m.append(b[i])
        else :
            second_m.append(a[i])
    
    for i in range(q, 30):
        if a[i] != '.' and b[i] != '.':
            second_n.append(a[i])
        else :
            second_n.append(b[i])
    
    third_m = a[30:r]
    third_n =b[30:r]
    
    for i in range(r,40):
        if b[i] != '.'and a[i] != '.':
            third_m.append(b[i])
        else :
            third_m.append(a[i])
            
    for i in range(r,40):
        if a[i] != '.'and b[i] != '.':
            third_n.append(a[i])
        else :
            third_n.append(b[i])
    m = first_m + second_m + third_m
    n = first_n + second_n + third_n
    return m, n


def mutation(genome: Genome, num: int = 1, probability: float = 0.5) -> Genome:
    for _ in range(num):
        index = randrange(len(genome) - 20)
        genome[index] = genome[index] if random() > probability else abs(int(genome[index] - 1))
        index = randrange(len(genome) - 20 , len(genome) - 10)
        genome[index] = str(abs(int(genome[index])-1)) if random() <= probability and genome[index] != '.' else genome[index]
        index = randrange(len(genome) - 10,  len(genome))
        genome[index] = str(abs(int(genome[index]) -1)) if random() <= probability and genome[index] != '.' else genome[index]
    return genome


def population_fitness(population: Population, fitness_func: FitnessFunc) -> int:
    return sum([fitness_func(genome) for genome in population])


def selection_pair(population: Population, fitness_func: FitnessFunc, time_limit: float) -> Population:
    m = len(population)
    index1 = randint(0, m-1)
    while True:
        index2 = randint(0, m-1)
        if (index2 != index1):
            break
        
    individual_s = population[index1]
    if index2 > index1:
        individual_s = population[index2]
        
    return individual_s


def sort_population(population: Population, fitness_func: FitnessFunc) -> Population:
    return sorted(population, key=fitness_func, reverse=True)


def genome_to_string(genome: Genome) -> str:
    return "".join(map(str, genome))


def print_stats(population: Population, generation_id: int, fitness_func: FitnessFunc):
    print("GENERATION %02d" % generation_id)
    print("=============")
    print("Population: [%s]" % ", ".join([genome_to_string(gene) for gene in population]))
    print("Avg. Fitness: %f" % (population_fitness(population, fitness_func) / len(population)))
    sorted_population = sort_population(population, fitness_func)
    print(
        "Best: %s (%f)" % (genome_to_string(sorted_population[0]), fitness_func(sorted_population[0])))
    print("Worst: %s (%f)" % (genome_to_string(sorted_population[-1]),
                              fitness_func(sorted_population[-1])))
    print("")

    return sorted_population[0]


def run_evolution(
        populate_func: PopulateFunc,
        fitness_func: FitnessFunc,
        time_limit: float,
        time_curr: float, 
        rbot: Robot,
        obthings: [ForbitThing],
        selection_func: SelectionFunc = selection_pair,
        crossover_func: CrossoverFunc = single_point_crossover,
        mutation_func: MutationFunc = mutation,
        generation_limit: int = 10,
        printer: Optional[PrinterFunc] = None) -> Tuple[Population, int, int]:
    population = populate_func()

    
    for test_time in range(generation_limit):
        gene_dictionary = {}
        
        #print("population len: {}".format(len(population)))
        count = 0
        for gene in population:
            things = obthings
            
            #for thing in things:
            #    print("{}, {}".format(thing.current_point[0], thing.current_point[1]))
            
            rbot.start_point= [100, 0]
            rbot.current_point = [100,0]
            isContinue = True
            isforward = False
            isfinish = False
            time_curr = 0
            total_time = 0.0
            if len(gene) != 40:
                    raise ValueError("Length of each gene is not equal 40!")
                
            delta_t = rbot.delta_t
            dis_lst = gene[30:40]
            dis_str = ""
            for i in range(10):
                dis_str += dis_lst[i]
            dis_random = analyze.bin_to_float(dis_str) * 10
            print("distance random: {}".format(dis_random))
            agl_lst = gene[20:30]
            agl_str = ""
            for i in range(10):
                agl_str += agl_lst[i]
            agl_random = analyze.bin_to_float(agl_str)
            #print("angle random: {}".format(agl_random))
                
                
              ############ Start looping #####################3   
            while isContinue == True:
                #print("count___{}".format(count))
                
                
                if isforward == False:
                    for step in range(round(delta_t/4)):
                        rbot.update_point(0)
                    for step in range(round(delta_t/4)):
                        rbot.update_point(1)
                        #constant
                    for step in range(round(delta_t/4)):
                        rbot.update_point(2)
                else :
                    for step in range(round(delta_t/2)):
                        rbot.update_point(1)
                        #constant
                for step in range(round(delta_t)):
                    for thing in things:
                        thing.update_point()
                
                     #print("{}, {}".format(thing.current_point[0], thing.current_point[1]))
                
                thing_id =  -1
                min_dis = 0.0
                min_agl = 0.0
                for i in range(len(things)):
                    thing = things[i]
                    angle = rbot.devia_angle(thing.get_vector())* 180 / 3.141592653589793
                    #print("angle : {}".format(angle))
                    if abs(angle) > abs(agl_random):
                        
                        continue
                    thing_predict = thing.predict_point()
                    #print("Point__OBSTACLE_FORMAL {},{}".format(thing.current_point[0], thing.current_point[1]))
                    #print("Point__OBSTACLE {},{}".format(thing_predict[0], thing_predict[1]))
                    distance = math.sqrt(math.pow((rbot.current_point[0] - thing_predict[0]), 2) + math.pow((rbot.current_point[1] - thing_predict[1]), 2))
                    #print("distance : {}".format(distance))
                    if distance > dis_random:
                        continue
                    if min_dis > distance:
                        min_dis = distance
                        min_agl = angle
                        thing_id = i
                if thing_id  < 0:
                    time_curr += 4
                    #gene_dictionary[count] = time_curr
                    #count = count +1
                    isforward = True
                    #print("NOT____thing_id")
                    #print("time___current: {} s".format(time_curr))
                    #print("point__current: {},{}".format(rbot.current_point[0], rbot.current_point[1]))
                    
                else: 
                    isforward = False
                    
                
                if rbot.current_point[1] >= rbot.end_point[1]:
                    if rbot.current_point[0] < rbot.end_point[0]:
                        while rbot.current_point[0] != rbot.end_point[0]:
                            rbot.current_point[0]  = int(rbot.current_point[0]) + 1
                            time_curr += 1
                    else :
                        while rbot.current_point[0] != rbot.end_point[0]:
                            rbot.current_point[0]  = int(rbot.current_point[0]) -1 
                            time_curr += 1
                    isfinish = True
                    gene_dictionary[count] = [time_curr, isfinish]
                    count +=1
                    
                    print("OUT____normal ")
                    #print("time___current: {} s".format(time_curr))
                    #print("point__current: {},{}".format(rbot.current_point[0], rbot.current_point[1]))
                    isContinue = False
                
                #check VN, N, F, VF
                dis_status =-1
                if isforward == False:
                    check = randint(0, 2)
                    if min_dis <= 2 + dis_random/ 6:
                        if check == 0:
                            dis_status = 1
                        else:
                            dis_status = 0
                    elif min_dis<= 2 +dis_random /6 * 2:
                        if check == 0:
                            dis_status = 0
                        else:
                            dis_status = 1
                    elif min_dis <= 2 + dis_random /6 *3:
                        if check == 0:
                            dis_status = 1
                        else:
                            dis_status = 2
                    elif min_dis <= 2 + dis_random/ 6 *4:
                        if check == 0:
                            dis_status = 2
                        else:
                            dis_status = 1
                    elif min_dis <= 2 + dis_random/ 6 *5:
                        if check == 0:
                            dis_status = 3
                        else:
                            dis_status = 2
                    elif min_dis <= 2 + dis_random/ 6 *6:
                        if check == 0:
                            dis_status = 2
                        else:
                            dis_status = 3
                    else:
                        dis_status = 3
                    
                    #check L, AL, A, AR, A
                    agl_status =-1
                    agl_random = abs(agl_random)
                    check = randint(0, 2)
                    if min_agl <=  -agl_random:
                        agl_status = 0
                    elif min_agl <= -agl_random/4 * 3:
                        if check ==0:
                            agl_status = 1
                        else:
                            agl_status = 0
                    elif min_agl <= -agl_random/ 4 *2:
                        if check ==0:
                            agl_status = 0
                        else:
                            agl_status = 1
                    elif min_agl <= -agl_random/ 4 *1:
                        if check ==0:
                            agl_status = 2
                        else:
                            agl_status = 1
                    elif min_agl <= 0.0:
                        if check ==0:
                            agl_status = 1
                        else:
                            agl_status = 2
                    elif min_agl <= agl_random/ 4:
                        if check ==0:
                            agl_status = 3
                        else:
                            agl_status = 2
                    elif min_agl <= agl_random/ 4 * 2:
                        if check ==0:
                            agl_status = 2
                        else:
                            agl_status = 3
                    elif min_agl <= agl_random/ 4 * 3:
                        if check ==0:
                            agl_status = 4
                        else:
                            agl_status = 3
                    elif min_agl <= agl_random/ 4 * 4:
                        if check ==0:
                            agl_status = 3
                        else:
                            agl_status = 4
                    else:
                        agl_status = 4
                    
                    rules_lst =  gene[0:20]
                    rule_base = rules_lst[dis_status * 5 + agl_status]
                    if rule_base ==0:
                        time_curr += 4
                        isfinish = False
                        gene_dictionary[count] = [time_curr, isfinish]
                        count = count +1
                        print("OUT____not found rule base")
                        #print("time___current: {} s".format(time_curr))
                        #print("point__current: {},{}".format(rbot.current_point[0], rbot.current_point[1]))
    
                        isContinue = False
                        break
                    
                    deviation_vector = [0,0]
                    
                    if (dis_status == 2 and agl_status == 2) or (dis_status == 0 and agl_status == 1): 
                        #AR
                        if rbot.rb_vector[0] ==0 and rbot.rb_vector[1] >0:
                            deviation_vector = [1, 0]
                        elif rbot.rb_vector[0] ==0 and rbot.rb_vector[1] <0:
                            deviation_vector = [-1, 0]
                        elif rbot.rb_vector[0] < 0 and rbot.rb_vector[1] ==0:
                            deviation_vector = [0, 1]
                        elif rbot.rb_vector[0] >0 and rbot.rb_vector[1] ==0:
                            deviation_vector = [0, -1]
                        elif (rbot.rb_vector[0] >0 and rbot.rb_vector[1] >0) or (rbot.rb_vector[0] <0 and rbot.rb_vector[1] >0):
                            deviation_vector = [1, -rbot.rb_vector[0] /rbot.rb_vector[1]]
                        else:
                            deviation_vector = [-1, rbot.rb_vector[0] /rbot.rb_vector[1]]
                    elif (dis_status == 0 and agl_status == 2) or (dis_status == 0 and agl_status == 3) or (dis_status == 1 and agl_status == 3):
                        #AL
                        if rbot.rb_vector[0] ==0 and rbot.rb_vector[1] >0:
                            deviation_vector = [-1, 0]
                        elif rbot.rb_vector[0] ==0 and rbot.rb_vector[1] <0:
                            deviation_vector = [1, 0]
                        elif rbot.rb_vector[0] < 0 and rbot.rb_vector[1] ==0:
                            deviation_vector = [0, -1]
                        elif rbot.rb_vector[0] >0 and rbot.rb_vector[1] ==0:
                            deviation_vector = [0, 1]
                        elif (rbot.rb_vector[0] >0 and rbot.rb_vector[1] >0) or (rbot.rb_vector[0] <0 and rbot.rb_vector[1] >0):
                            deviation_vector = [-1, -rbot.rb_vector[0] /rbot.rb_vector[1]]
                        else:
                            deviation_vector = [+1, rbot.rb_vector[0] /rbot.rb_vector[1]]
                        pass
                    else:
                        pass
                    rbot.set_vector([rbot.rb_vector[0] + deviation_vector[0], rbot.rb_vector[1]+ deviation_vector[1]])
                    time_curr = time_curr + 4
                    print("Lan thu thu {} co thoi gian{}".format(count, time_curr))
                
        print(test_time)
        if len(population) != len(gene_dictionary):
            raise ValueError("Current Population and its dictionary have to be same length")
        for i in range(len(population)):
            con_1 = gene_dictionary[i]
            for j in range(i+1, len(population)):
                con_2 = gene_dictionary[j]
                print("")
                print("{}       {}".format(con_1[1], con_2[1]))
                print("")
                #print("keyL generaion{}".format(gene_dictionary[0]))
                if con_1[0] > con_2[0] and con_1[1] == True and con_2[1] == True:
                    time_limit = con_2[0]
                    gen = population[i]
                    population[i] = population[j]
                    population[j] = gen
                time_limit = con_1[0]
    
        if printer is not None:
            printer(population, i, fitness_func)
     
        next_generation = population[0:2]
    
        for j in range(int(len(population) / 2) - 1):
            parents = [selection_func(population, fitness_func, time_limit), selection_func(population, fitness_func, time_limit)]
            offspring_a, offspring_b = crossover_func(parents[0], parents[1])
            offspring_a = mutation_func(offspring_a)
            offspring_b = mutation_func(offspring_b)
            next_generation += [offspring_a, offspring_b]
    
        population = next_generation
        

    return population, test_time, time_limit