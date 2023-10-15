
grade = input("Entrez le grade de l'employé (A, B, C, D, ou E) : ")
heures_travaillees = int(input("Entrez le nombre d'heures travaillées : "))


tarif_horaire = 0
prime = 0
heures_par_prime = 0


if grade == 'A':
    tarif_horaire = 200
    prime = 1000
    heures_par_prime = 20
elif grade == 'B':
    tarif_horaire = 150
    prime = 800
    heures_par_prime = 20
elif grade == 'C':
    tarif_horaire = 120
    prime = 500
    heures_par_prime = 15
elif grade == 'D':
    tarif_horaire = 100
    prime = 350
    heures_par_prime = 15
elif grade == 'E':
    tarif_horaire = 80
    prime = 100
    heures_par_prime = 10
else:
    print("Grade invalide")
    exit()


salaire = (tarif_horaire * heures_travaillees) + (prime * (heures_travaillees // heures_par_prime))

print(f"Le salaire de l'employé est de {salaire} DH.")
