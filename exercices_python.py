age = int(input("Entrez l'âge du chien: "))
 
if age < 0:
    print("Vous devez entrer un âge positif!")
    exit()
elif age <= 2:
    d_age = age * 10.5
else:
    d_age = 21 + (age - 2) * 4
 
print("L'âge du chien en âge humain est", d_age)

# Exercice 52 : Fonction de base

a = 4
b = 6
c = 2

a1 = min(a, b, c)
a3 = max(a, b, c)
a2 = (a + b + c) - a1 - a3
 
print("Les nombres dans l'ordre sont {}, {} et {}".format(a1, a2, a3))

# exercice 53 : Sortir d'une boucle infinie
i = 0

while i < 10:
	i+=1
	
print("Exercice réussi !")

# Exercice 54 : Trouver l'erreur dans une boucle for

mot = "Python"

for i in range(len(mot)):
	print(i)

# Exercice 55 : Trouver l'erreur dans une fonction 

# def multiplicateur_mot(mult=5, mot):
# 	return mot * mult

# mot_multiplie = multiplicateur_mot(mult,mot="Bonjour")
# print(mot_multiplie)

def multiplicateur_mot(mot, mult=5):
    return mot * mult
 
mot_multiplie = multiplicateur_mot(mot="Bonjour")
print(mot_multiplie)

# Exercice 56 : Trouver l'erreur dans la fonction 
# def addition(a, b):
# 	c = a + b


# resultat = addition(5, 10)
# print(resultat)

def addition(a, b):
	return a + b

resultat = addition(5, 10)
print(resultat)

def addition(a, b):
    c = a + b
    return c
 
resultat = addition(5, 10)
print(resultat)

# Exercice 57 : Afficher la table de multiplicaton d'un nombre 

for i in range(11):
    print(f"{i} * {7} = {i*7}")
nombre = 7 
for i in range(11):
    print("{} * {} = {}".format(i, nombre, i*nombre))

# Exercice 58 : Récuperer l'incice de l'itération dans une boucle

liste = ["Pierre", "Paul", "Marie"]
for x, y in enumerate(liste):
    print(f"{x} {y}")

# Exercice 59 : Récuperer seulement paire d'une liste 

nombres = range(50)
nombres_pairs = []
for i in nombres:
    if i % 2 == 0:
        nombres_pairs.append(i)
print(nombres_pairs)

# Exercice 60 : Récuperer seulement les nombres pairs avec une compréhension de liste

nombres = range(50)

nombres_pairs = [i for i in nombres if i % 2== 0]
print(nombres_pairs)