# Exercice 51 : Calcul de l'age d'un chien en années humaines

age_chien = input("Entrer l'âge vrai de chien : ")

if age_chien.isdigit():
    if int(age_chien) < 0:
        print("vous devez entrer un âge posirif")
    elif int(age_chien) <= 2 and int(age_chien) > 0:
        print(f"L'âge de chien en âge humain est : {int(age_chien)*10.5} ")
        i = 1
    elif int(age_chien) > 2:
        print(f"L'âge de chien en âge humain est : {21 + (int(age_chien) - 2) * 4} ")
        i = 1
    else:
        print("vous devez entrer un nombre")
