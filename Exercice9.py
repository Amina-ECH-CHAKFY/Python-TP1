def calculer_montant_ttc(prix_ht, quantite):
    tva = 0.20  
    montant_ht = prix_ht * quantite
    montant_ttc = montant_ht + montant_ht * tva
    return montant_ht, montant_ttc

articles = []

for i in range(2):
    nom_article = input(f"Donnez le nom du {i + 1}er article : ")
    quantite = int(input(f"Donnez la quantité du {i + 1}er article : "))
    prix_unitaire = float(input(f"Donnez le prix unitaire du {i + 1}er article : "))
    montant_ht, montant_ttc = calculer_montant_ttc(prix_unitaire, quantite)
    articles.append((nom_article, montant_ht, montant_ttc))

total_ht = 0
total_ttc = 0

for nom, montant_ht, montant_ttc in articles:
    print(f"Total pour l'article {nom}: {montant_ht} dh (ht)")
    total_ht += montant_ht
    total_ttc += montant_ttc

print(f"Le total de votre facture est : {total_ttc} dh (TTC)")
