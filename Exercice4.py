
secondes = int(input("Entrez un nombre de secondes : "))

# Copie de la valeur des secondes pour affichage
secondes_affichage = secondes


heures = secondes // 3600  # 1 heure = 3600 secondes
secondes %= 3600  # Met à jour le nombre de secondes restantes
minutes = secondes // 60  # 1 minute = 60 secondes
secondes %= 60  # Met à jour le nombre de secondes restantes

print(secondes_affichage, "secondes = ",heures,"h",minutes,"min",secondes,"sec")