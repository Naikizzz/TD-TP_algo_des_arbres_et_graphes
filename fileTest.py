import binary_tree as bt

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