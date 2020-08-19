# Exrcice 01: additionner les chifres d'un nombre 

nombre = 209812
a = 0
for i in str(nombre):
    a += int(i)
print(a)

a = sum([int(i) for i in str(nombre)])
print(a)

# Exercice 02 : Remplacer un élément dans une liste 

liste = ["Pierre", "Marie", "Julie", "Adrien", "Julie"]
nom_a_chercher = "Julie"
nouveau_nom = "Julien"

liste = [x.replace(nom_a_chercher, nouveau_nom) for x in liste]
print(liste)

# Exercice 03 : Enlever les doublons d'une liste

nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10] 
nombres = set(nombres)
print(nombres)
nombres = list(nombres)
print(nombres)

nombres = [1, 2, 2, 3, 4, 5, 5, 5, 6, 7, 7, 8, 9, 10]
nombres_sans_doublons = []
for i in nombres:
    if i not in nombres_sans_doublons:
        nombres_sans_doublons.append(i)
print(nombres_sans_doublons)