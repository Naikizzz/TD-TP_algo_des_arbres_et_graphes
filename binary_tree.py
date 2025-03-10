"""
Classe des arbres binaires
"""

class Tree:
    """Classe sans constructeur pour les arbres binaires"""
    def __str__(self):
        if self._empty:
            return "_"
        else:
            return ("[" + str(self._left_son) + ","
                        + str(self._data) + ","
                        + str(self._right_son) + "]")

    def __repr__(self): return str(self)
         
    def left_son(self): 
        """renvoie le fils gauche de l'arbre, ou None si l'arbre est vide"""
        return None if self._empty else self._left_son
    
    def right_son(self): 
        """renvoie le fils droit de l'arbre, ou None si l'arbre est vide"""
        return None if self._empty else self._right_son
    
    def data(self): 
        """renvoie la donnée dans l'arbre ou None pour l'arbre vide"""
        return None if self._empty else self._data
    
    def empty(self): 
        """Test si l'arbre est vide"""  
        return self._empty
    
    def __bool__(self):
        """ 'if t:' = 'if t != None' """
        return not self._empty
    
    def mk_empty(self):
        """Return an empty tree of the same class"""
        t = Empty()
        t.__class__ = self.__class__
        return t
    
    def size(self):
        """Renvoie le nombre de noeud dans l'arbre"""
        if self.empty(): return 0
        return 1 + self.left_son().size() + self.right_son().size()

    def height(self):
        """Renvoie la hauteur de l'arbre"""
        if self.empty(): return 0
        return 1 + max(self.left_son().height(), self.right_son().height())

    def iter_prefix(self, fn):
        """Appelle la fonction fn sur toutes les données de l'arbre dans 
           l'ordre préfixe""" 
        if not self.empty():
            fn(self.data())
            self.left_son().iter_prefix(fn)
            self.right_son().iter_prefix(fn)

    def iter_infix(self, fn):
        """Appelle la fonction fn sur toutes les données de l'arbre dans 
           l'ordre infix""" 
        if not self.empty():
            self.left_son().iter_infix(fn)
            fn(self.data())
            self.right_son().iter_infix(fn)
            
            
    def iter_postfix(self, fn):
        """Appelle la fonction fn sur toutes les données de l'arbre dans 
           l'ordre postfixe""" 
        if not self.empty():
            self.left_son().iter_postfix(fn)
            self.right_son().iter_postfix(fn)
            fn(self.data())
        
    def iter_breadth(self, fn):
        """Appelle la fonction fn sur toutes les données de l'arbre dans 
           l'ordre largeur d'abord
        """ 
        
        from collections import deque
        
        file = deque()
        def push(t):
            if t:
                file.append(t)
                
        push(self)
        
        while len(file) != 0:
            t = file.popleft()
            push(t.left_son())
            push(t.right_son())
            fn(t.data())
                 
class Empty(Tree):
    """Constructeur pour l'arbre vide"""
    def __init__(self):
        self._empty = True

class Node(Tree):
    """Constructeur pour les noeuds"""
    def __init__(self,data,left_son=None,right_son=None):
        assert left_son == None or isinstance(left_son, Tree)
        assert right_son == None or isinstance(right_son, Tree)
        self._empty = False
        self._data = data
        self._left_son = self.mk_empty() if left_son == None else left_son
        self._right_son = self.mk_empty() if right_son == None else right_son
        
class MTree(Tree):
    """Classe des arbres mutables"""
    
    def set_empty(self):
        """rend l'arbre vide"""
        del self._data
        del self._left_son
        del self._right_son
        self._empty = True
        
    def set_node(self):
        """rend larbre non vide avec deux fils vide et data = None"""
        if self.empty():
            self._empty = False
            self._left_son = self.mk_empty()
            self._right_son = self.mk_empty()
            self._data = None
            
    def set_data(self,data):
        """change la donnée d'un noeud et rend l'arbre non vide si il l'était"""
        self.set_node()
        self._data = data
        
    def set_left_son(self,left_son):
        """change le fils gauche d'un noeud et rend l'arbre non vide si il l'était"""
        assert isinstance(left_son, self.MTree)
        self.set_node()
        self._left_son = left_son       
    
    def set_right_son(self,right_son):
        """change le fils droit d'un noeud et rend l'arbre non vide si il l'était"""
        assert isinstance(right_son, self.MTree)
        self.set_node()
        self._right_son = right_son    
    
    def set_parent(self, new_node):
        """Remplace le nœud courant par un autre"""
        self.set_data(new_node.data())
        self.set_left_son(new_node.left_son())
        self.set_right_son(new_node.right_son())

           
class MEmpty(MTree,Empty): 
    """Constructeur pour un arbre vide mutable"""

class MNode(MTree): 
    """Constructeur pour un noeud mutable"""
    def __init__(self,data,left_son=None,right_son=None):
        assert left_son == None or isinstance(left_son, MTree)
        assert right_son == None or isinstance(right_son, MTree)
        Node.__init__(self,data,left_son,right_son)

def random_tree(size, rand_data=None, mutable=False):
    """Construction d'un arbre aléatoire d'une taille donnée.
       la fonction rand_data(), si fournie, sera appelée pour créer
       les étiquettes. Sinon on utilise random.randint(0,size*10)"""
    from random import randint
    
    if size <= 0:
        if mutable: return MEmpty()
        return Empty()
    rand_data = rand_data if rand_data else lambda: randint(0,size*10)
    left_size = randint(0,size - 1)
    right_size = size - 1 - left_size
    left_son = random_tree(left_size, rand_data, mutable)
    data = rand_data()
    right_son = random_tree(right_size, rand_data, mutable)
    if mutable:
        return MNode(data, left_son, right_son)
    else:
        return Node(data, left_son, right_son)
