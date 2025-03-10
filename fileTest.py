import binary_tree as bt
import smtree_corrige as sm

A = bt.random_tree(5)
# A = bt.MEmpty()
print(A)

l = []
A.iter_prefix(lambda d: l.append(d))
print("Parcours Préfixe :", l)

l = []
A.iter_infix(lambda d: l.append(d))
print("Parcours Infixe :", l)

l = []
A.iter_postfix(lambda d: l.append(d))
print("Parcours Postfixe :",l)

l = []
A.iter_breadth(lambda d: l.append(d))
print("Parcours en Largeur :",l)

"""
Toujours pensé à instancier MakeSMTree dans un objet SMTree
car MakeTree créer une classe, mais pas une instance de l'arbre
"""

print("Test d'insertion:")
SMTree =sm.MakeSMTree()
tree = SMTree()
tree.insert(10)
tree.insert(4)
tree.insert(6)
tree.insert(16)

print("Test de recherche de clé k dans l'arbre")
print(tree.mem(6))
print(tree.mem(0))

DicoSMTree = sm.MakeSMTree(key=lambda x:x[0], val=lambda x:x[1])
dico_tree = DicoSMTree()
dico_tree.insert((6,"Ahunaiki"))
dico_tree.insert((5,"Edwin"))
dico_tree.insert((1,"Tama"))
dico_tree.insert((8,"Teko"))

print("Test de recherche, retour de la valeur de la clé k")
print(dico_tree.find(5))
print(dico_tree.find(9))

print("Test de suppression dans un arbre, arbre avant ", tree)
tree.remove(4)
print("Arbre après", tree)