
nombre1 = float(input("Entrez le premier nombre : "))
nombre2 = float(input("Entrez le deuxième nombre : "))

operation = input("Entrez l'opération (+, -, *, /) : ")


if operation == '+':
    resultat = nombre1 + nombre2
elif operation == '-':
    resultat = nombre1 - nombre2
elif operation == '*':
    resultat = nombre1 * nombre2
elif operation == '/':
    if nombre2 == 0:
        print("Erreur : Division par zéro n'est pas autorisée.")
    else:
        resultat = nombre1 / nombre2
else:
    print("Opération non reconnue. Veuillez entrer l'une des opérations suivantes : +, -, *, /")


if operation in ['+', '-', '*', '/']:
    print("Résultat :", nombre1, operation, nombre2, "=", resultat)
