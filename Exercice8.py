
notes = []
coefficient = []

for i in range(4):
    note = float(input(f"Entrer la note {i+1} : "))
    coef = float(input(f"Entrer le coefficient {i+1} : "))
    notes.append(note)
    coefficient.append(coef)

moyenne = 0
totale_coef = 0

for i in range(4):
    moyenne = moyenne + (notes[i] * coefficient[i])
    totale_coef += coefficient[i] 

resultat = moyenne/totale_coef
print(f"la moyenne est : {resultat}")
if(resultat >= 10):
    print("Semestre valide.")
elif(resultat >=7):
    print("Rattrapage.")
else:
    print("Semestre non valide.")