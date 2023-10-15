distance_km = float(input("Entrez la distance en kilomètres : "))
temps_minute = float(input("Entrez le temps en minutes : "))


distance_metres = distance_km * 1000

temps_secondes = temps_minute * 60

vitesse = distance_metres / temps_secondes

print("La vitesse en mètre par seconde est " ,vitesse, "m/s.")
