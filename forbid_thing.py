# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 20:10:12 2021

@author: Hacha
"""
import math
class ForbitThing:
    start_point = []
    name = 'forbithing'
    current_point = [0,0]
    past_point = [0,0]
    obs_vector = [1, 0]
    
    v = 1/8
    
    def __init__(self, start , vector, name):
        self.start_point = start
        self.current_point = start
        self.past_point = start
        self.obs_vector = vector
        self.name = name
        
    def get_current(self):
        return self.current_point
        
    def set_vector(self, new_vector):
        self.obs_vector = new_vector
        
    def get_vector(self):
        #print(len(self.obs_vector))
        return self.obs_vector
    
    def predict_point(self):
        if len(self.current_point) != len(self.past_point):
            raise ValueError("Point obs curr and pass must be of same length")  
        
        return [self.current_point[0] * 2 - self.past_point[0], self.current_point[1] * 2 - self.past_point[1]]
    
    def update_point(self):
        if len(self.current_point) != len(self.obs_vector):
            raise ValueError("Point obs and vector must be of same length")               
        s = self.v #trong 1 don vi thoi gian
        vector_len = math.pow(self.obs_vector[0], 2) + math.pow(self.obs_vector[1], 2)
        dv = s / math.sqrt(vector_len)
        self.past_point = self.current_point                 
        self.current_point[0] = self.current_point[0] + (self.obs_vector[0] * dv)
        self.current_point[1] = self.current_point[1] + (self.obs_vector[1] * dv) 
    