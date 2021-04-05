# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 15:45:45 2021

@author: Hacha
"""
import analyze 
import math
from typing import List


# basic rulde
# =============================================================================
# ----------------------------
#    | L  | AL | A  | AR | R |
# ----------------------------
# VN | A  | AR | AL | AL | A |
# ----------------------------
# N  | A  | A  | AL | A  | A |
# ----------------------------
# F  | A  | A  | AR | A  | A |
# ----------------------------
# VF | A  | A  | A  | A  | A |
# ----------------------------
# =============================================================================

class Robot:
    alpha = 2
    delta_t = 4 

    start_point = [100,0]
    end_point = [100, 250] # Area = 25 * 20 m^2,width = 25, height = 10

    current_point = [100,0]
    past_point =[100,0]
    rb_vector = [0, 1];# ax + by - c = 0; function: x = 10
    
    below_thres = 2
    above_thres = 200
    
    below_angle = -1 # -90
    above_angle = 1  # 90

    
    def __init__(self, alpha, delta):
        self.alpha = alpha
        self.delta_t = delta
        
        

    def update_point(self, status: int):
        if len(self.current_point) != len(self.rb_vector):
            raise ValueError("Point rb and vector must be of same length")  
        v = 0
        self.past_point = self.current_point
        vector_len = math.pow(self.rb_vector[0], 2) + math.pow(self.rb_vector[1], 2)
        if status == 0:
            v = 0
            s = (self.delta_t/ 4 * self.delta_t/ 4 * self.alpha) * 1/2 
            dv = s / math.sqrt(vector_len)
            self.current_point[0] = self.current_point[0] + (self.rb_vector[0] * dv)
            self.current_point[1] = self.current_point[1] + (self.rb_vector[1] * dv)
        if status == 1:          
            v = self.delta_t / 4 * self.alpha + v
            s = v * self.delta_t/ 2
            dv = s / math.sqrt(vector_len)
            self.current_point[0] = self.current_point[0] + (self.rb_vector[0] * dv)
            self.current_point[1] = self.current_point[1] + (self.rb_vector[1] * dv)
        if status == 2:
            v = self.delta_t / 4 * self.alpha + v
            s = ((-self.delta_t/ 4 * self.delta_t/ 4 * self.alpha) * 1/2 + self.delta_t/4 * v)
            dv = s / math.sqrt(vector_len)
            self.current_point[0] = self.current_point[0] + (self.rb_vector[0] *dv)
            self.current_point[1] = self.current_point[1] + (self.rb_vector[1] * dv)
    
    def set_vector(self, new_vector):
        self.rb_vector = new_vector
        
    def get_vector(self):
        return self.rb_vector
    
    def get_threshold(self) :
        return [self.below_thres, self.above_thres, self.below_angle, self.above_angle]
            
    def devia_angle(self, obs_vector) : 
        if len(obs_vector) != len(self.rb_vector):
            raise ValueError("Velocity vectors of robot and obstacles must be of same length")
        return analyze.angle(self.rb_vector, obs_vector)

    def distance_to_target(self):
        return math.sqrt(pow(self.end_point[1] - self.current_point[1], 2) + pow(self.end_point[0] - self.current_point[0], 2))
    
    
    
