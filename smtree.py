# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:48:10 2025

@author: ahuna
"""

from binary_tree import *

class SMTree(MTree):
    
    def empty(self):
        
        self.set_empty()
    
    def insert(self, x):
        
        if self.empty():
            return self.set_data(x)
        elif(x < self.data()):
            return self.left_son().insert(x)
        elif(x > self.data()):
            return self.right_son().insert(x)
        
    def mem(self, x):
        
        if self.empty():
            return False
        if x == self.data():
            return True
        elif x < self.data():
            return self.left_son().mem(x)
        else:
            return self.right_son().mem(x)