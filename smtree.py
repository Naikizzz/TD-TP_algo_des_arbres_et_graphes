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
            
            if self.empty():
                return None
            
            if self.right_son().empty():
                max_val = self.data()
                if self.left_son().empty():
                    self.set_empty()
                else:
                    self._replace(self.left_son())
                return max_val
            else:
                return self.right_son().pop_max()
        
        def _replace(self, node):
            """
            Méthode permettant de remplacer
            le noeud courant par un noeud donné
            """
            self.set_data(node.data())
            self.set_left_son(node.left_son())
            self.set_right_son(node.right_son())
            
        
        def remove(self, x):
            ...
        
        def check():
            ...