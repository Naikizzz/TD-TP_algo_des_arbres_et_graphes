# -*- coding: utf-8 -*-
"""
Created on Thu Feb 20 15:48:10 2025

@author: ahuna
"""

from binary_tree import *

def MakeSMTree(key=lambda x:x, val=lambda x:x):

    class SMTree(MTree):
        
        def empty(self):
            
            self.set_empty()
        
        def insert(self, x):
            
            if self.empty():
                self.set_data(x)
            elif(key(x) < key(self.data())):
                self.left_son().insert(x)
            elif(key(x) > key(self.data())):
                self.right_son().insert(x)
            
        def mem(self, x):
            
            if self.empty():
                return False
            if key(x) == key(self.data()):
                return True
            elif key(x) < key(self.data()):
                return self.left_son().mem(x)
            else:
                return self.right_son().mem(x)
        
        def pop_max(self):
            ...
        
        def remove(self, x):
            ...
        
        def check():
            ...