''' poids = float(input("Donner le poids : "))
taille = float(input("Donner la taille : "))
if taille == 0:
    print("taille invalide.")
else:
    IMC = poids/(taille ** 2)

if IMC >= 40:
    print("obésité morbide ou massive")
elif (35 < IMC < 40):
    print("obésité sévère")
elif (30 < IMC < 35):
    print("obésité modérée")
elif (25 < IMC < 30):
    print("Surpoids")
elif (18.8 < IMC < 25):
    print("corpulence normale")
elif (16.5 < IMC < 18.5):
    print("Maigreure")
elif (IMC < 16.5):
   print("Famine") '''


poids = float(input("Donner le poids : "))
taille = float(input("Donner la taille : "))

if taille == 0:
    print("Taille invalide.")
else:
    IMC = poids / (taille ** 2)


imc_categories = [ 
    # (seuil , "descriptions")
    (40, "obésité morbide ou massive"), 
    (35, "obésité sévère"),
    (30, "obésité modérée"),
    (25, "Surpoids"),
    (18.5, "corpulence normale"),
    (16.5, "Maigreur"),
    (0, "Famine")
]


categorie = "IMC invalide"
for seuil, description in imc_categories:
    if IMC >= seuil:
        categorie = description
        break

print(categorie)
