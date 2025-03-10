#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from binary_tree import MEmpty

def MakeSMTree(cmp= lambda x, y:0 if x == y else 1 if x <= y else -1,
               key= lambda x: x,
               val= lambda x: x):
    class SMTree(MEmpty):
        
        def insert(self,x):
            """insert x in the search tree"""  
            if self.empty() or (c := cmp(key(x),key(self.data()))) == 0:
                self.set_data(x); return         
            (self.left_son() if c > 0 else self.right_son()).insert(x)
            
        def mem(self,k):
            """return True is k (as a key) is in tree"""
            if self.empty(): return False
            if (c:= cmp(k, key(self.data()))) == 0: return True
            return (self.left_son() if c > 0 else self.right_son()).mem(k)
        
        def find(self,k):
            """return value associated to key k or None if absent"""
            if self.empty(): return None
            if (c := cmp(k, key(self.data()))) == 0: return val(self.data())
            return (self.left_son() if c > 0 else self.right_son()).find(k)
        
        def _popmin(self,set_parent):
            if self.empty(): raise ValueError("popmin: empty_tree")
            if self.left_son().empty(): 
                set_parent(self.right_son());
                return self.data()
            else: 
                return self.left_son()._popmin(self.set_left_son)
            
        def _popmax(self,set_parent):
             if self.empty(): raise ValueError("popmax: empty_tree")
             if self.right_son().empty(): 
                 set_parent(self.left_son());
                 return self.data()
             else: 
                 return self.right_son()._popmax(self.set_right_son) 
             
        def remove(self,k):
            """remove k from tree"""
            if self.empty(): raise ValueError("remove: not found")
            if (c := cmp(k, key(self.data()))) == 0:
                if self.left_son(): # pop max from left_son
                    self.set_data(self.left_son()._popmax(self.set_left_son))
                elif self.right_son(): # pom min from right son
                    self.set_data(self.right_son()._popmin(self.set_right_son))
                else:
                    self.set_empty()
            else:
                (self.left_son() if c > 0 else self.right_son()).remove(k)
                
        def check(self,mini=None,maxi=None):
            if self.empty(): return True
            if mini != None and not key(self.data()) > mini: return False
            if maxi != None and not key(self.data()) < maxi: return False
            return (self.left_son().check(mini = mini, 
                                          maxi = key(self.data())) and
                    self.right_son().check(mini = key(self.data()), 
                                           maxi = maxi))
            
            
    return SMTree

if __name__ == "__main__":            
    SMTree = MakeSMTree()
    DicoSMTree = MakeSMTree(key=lambda x:x[0], val=lambda x:x[1])
    t = SMTree()
    import random
    for i in range(10):
        t.insert(random.randint(0,10))
    d = DicoSMTree()
    import random
    for i in range(10):
        d.insert((random.randint(0,10),random.randint(0,10)))