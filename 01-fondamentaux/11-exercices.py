
"""
    MINI-SYSTÈME DE BANQUE

    OBJECTIF :
    Créer un système simple de gestion bancaire.

    Le programme doit permettre :

    - consulter un solde
    - déposer de l'argent
    - retirer de l'argent
    - afficher un historique des opérations
"""

# ----- DONNÉES INITIALES ------

compte = {
    "nom": "Alice",
    "solde": 1000,
    "historique": []
}

# Fonciton pour afficher le solde du client
def afficher_solde():
    print("Solde actuel :", compte["solde"], "$")


# Fonction pour déposer un montant
def deposer(montant):
    if montant >= 5:
        compte["solde"] += montant
        compte["historique"].append(f"+{montant} dépôt")
        print("Dépôt effectué :", montant, "$")
    else:
        print("Dépôt insuffisant (minimum 5$)")


# Fonction pour retirer de l'argent
def retirer(montant):
    if montant <= 0 or montant > compte["solde"]:
        print("Erreur : fonds insuffisants")
    else:
        compte["solde"] -= montant
        compte["historique"].append(f"-{montant} retrait")
        print("Retrait effectué :", montant, "$")


# Affichage de l'historique des opérations
def afficher_historique():
    print("Historique :")
    for operation in compte["historique"]:
        print("-", operation)


# ------- SIMULATION -------

"""
    ------ MENU PRINCIPAL DE LA BANQUE ------

    Ce programme fonctionne en boucle infinie (while True),
    ce qui permet à l'utilisateur de rester dans le système
    jusqu'à ce qu'il choisisse de quitter.

    Fonctionnement général :

    1. Le menu est affiché à chaque tour de boucle
    2. L'utilisateur choisit une option (1 à 5)
    3. Le programme exécute une action selon le choix
    4. En cas d'erreur de saisie, une exception est gérée
"""

while True:

    print("\n--- MENU BANQUE ---\n")
    print("1 - Consulter solde")
    print("2 - Déposer argent")
    print("3 - Retirer argent")
    print("4 - Historique")
    print("5 - Quitter \n")

    choix = input("Choisissez une option : ")

    try:

        if choix == "1":
            afficher_solde()

        elif choix == "2":
            montant = int(input("Montant à déposer : "))
            deposer(montant)

        elif choix == "3":
            montant = int(input("Montant à retirer : "))
            retirer(montant)

        elif choix == "4":
            afficher_historique()

        elif choix == "5":
            print("Au revoir")
            break

        else:
            print("Option invalide")

    except ValueError:
        
        """
            GESTION DES ERREURS :

            ValueError se produit lorsque :
            - l'utilisateur entre du texte au lieu d'un nombre
            - ex: "abc" au lieu de 100

            Dans ce cas, le programme ne crash pas,
            il affiche simplement un message d'erreur.
        """

        print("Erreur : veuillez entrer un nombre valide")