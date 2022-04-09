
"""
1. définir la liste : liste =[1, 18, 0, 21, 27, 9, 29, 32], puis effectuez les actions suivantes :
– triez et affichez la liste ;
- renversez et affichez la liste ;
– ajoutez le nombre 12 à la liste et affichez la liste ;
– affichez l’indice de l’élément 21 ;
– supprimez des nombres et affichez la liste ;
– affichez la sous-liste du début au 2eélément ;
– affichez la sous-liste du 3eélément à la fin de la liste ;
- créer une boucle ;
- arêter un boucle ;
"""

# ------------------ P R O G R A M M E --------------------

nombres = [1, 18, 0, 21, 27, 9, 29, 32]
print(" Liste initiale ".center(15, '-'))
print(nombres, '\n')

"""
"""

quitter = input('"Taper" ')
print(" Tri ".center(15, '-'))
nombres.sort()
print(nombres, '\n')
"""
"""

quitter = input('"Taper" ')
print(" Renversement ".center(15, '-'))
nombres.reverse()
print(nombres, '\n')
quitter = input('"Taper" ')
"""
"""

print(" ----- Ajout d'un nombre ----- ".center(15, '-'))
nombres.append(12)
print(nombres, '\n')
quitter = input('"Taper" ')
"""
"""

print(" ----- Indice d'un nombre ----- ".center(15, '-'))
if 2022 in nombres:
    print("le nombre est à la position {0} des nombres")
else:                                                             
    print("le nombre 2022 n'est pas parmis les nombres" '\n')
quitter = input('"Taper" ')


print(" ----- Indice d'un nombre ----- ".center(15, '-'))
if 21 in nombres:
    print(" le nombre 21 est à la position {0} des nombres" '\n'.format(nombres.index(21)))
else:                                                             
    print(" le nombre 21 n'est pas dans nombres")
quitter = input('"Taper" ')
"""
"""

print(" ----- Supprimer des nombres ".center(15, '-'))
del nombres[3:6]
print(nombres, '\n')
quitter = input('"Taper" ')
"""
"""

print(" ----- Indiquer ----- ".center(15, '-'))
print(" ----- montrez la sous liste du debut au 2ième nombre ----- ".center(15, '-'))
print("nombres[2:] =", nombres[2:])
print(" ----- montrez la sous liste du 3ième nombre à la fin ----- ".center(15, '-'))
print("nombres[:] =", nombres[:])
quitter = input('"Taper" ')
"""
"""

print(" ----- faire une boucle ----- ".center(15, '-'))
nombres = [1, 18, 0, 21, 27, 9, 29, 32]
for i in nombres:
    print(i)
quitter = input('"Taper" ')
"""
"""

print(" ----- Arreter la boucle ----- ".center(15, '-'))
nombres = [0, 1, 9, 18, 21, 27, 29, 32]
for i in nombres:
    if i > 21:
        print("arrêt de la boucle")
        break
    print(i)
quitter = input('"Taper" ')


