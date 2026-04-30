"""
    LES LISTES

    Les listes sont une structure de données en Python.

    Elles permettent de stocker plusieurs valeurs dans une seule variable.

    Une liste peut contenir :
    - des nombres
    - des chaînes de caractères
    - des booléens
    - ou un mélange de tout ça

"""

# ---------------------
# CRÉATION D'UNE LISTE
# ---------------------

# Une liste se crée avec des crochets []

fruits = ["pomme", "banane", "orange"]

print(fruits)

# ----- ACCÉDER AUX ÉLÉMENTS (INDEX) ------

# Chaque élément dans une liste a une position appelée index (Cfr Boucles for -> range())

# L'index commence à 0 en Python

# Exemple :
# 0 → pomme
# 1 → banane
# 2 → orange

print(fruits[0])  # pomme
print(fruits[1])  # banane
print(fruits[2])  # orange

# ----- MODIFIER UNE LISTE -----

fruits[1] = "mangue"

print(fruits)

# on remplace "banane" par "mangue"

# ----- AJOUTER DES ÉLÉMENTS ------

# append() ajoute un élément à la fin de la liste

fruits.append("ananas")

print(fruits)

# ----- SUPPRIMER DES ÉLÉMENTS -----

# remove() supprime un élément précis

fruits.remove("orange")

print(fruits)

# ----- LONGUEUR D'UNE LISTE -----

# len() permet de connaître le nombre d'éléments

print(len(fruits))
# Résultat: 3 -> Y a 3 élèments dans la liste fruits = [...]

# ------ PARCOURIR UNE LISTE ------

for fruit in fruits:
    print(fruit)

# Explication :
# la boucle prend chaque élément un par un
# fruit devient successivement :
# - pomme
# - mangue
# - ananas

# ------ AVEC enumerate() -------

"""
    La fonction enumerate() permet de parcourir une liste
    tout en récupérant à la fois :

    - l'index (position de l'élément)
    - la valeur de l'élément
"""

for index, fruit in enumerate(fruits):
    print(index, fruit)

# Explication :

# enumerate(fruits) transforme la liste en paires :
# (index, valeur)

# Exemple :
# (0, "pomme")
# (1, "mangue")
# (2, "ananas")

# donc :
# index → position dans la liste
# fruit → valeur à cette position

# Résultat :
# 0 pomme
# 1 mangue
# 2 ananas

# enumerate() est utilisé quand on veut :
    # - connaître la position d'un élément
    # - modifier une liste selon l'index
    # - afficher proprement des données numérotées

# ------ COMPARAISON SIMPLE -------

# Sans enumerate → uniquement les valeurs
# Avec enumerate → index + valeurs


# ----- LISTE MIXTE ------

data = ["Alice", 25, True]

print(data)

# Une liste peut contenir plusieurs types de données


# ------ RÉSUMÉ SIMPLE -------

# - Une liste stocke plusieurs valeurs
# - Les index commencent à 0
# - On peut ajouter, modifier, supprimer
# - On peut parcourir avec une boucle for



# -----------------------------
#      EXERCICE PRATIQUE
# -----------------------------

"""
EXERCICE :

    Crée une liste appelée "etudiants" contenant les noms suivants :
    - Alice
    - Mireille
    - Luckson
    - David

    Ensuite, fais les actions suivantes :

    1. Affiche toute la liste
    2. Affiche le premier et le dernier élément
    3. Remplace "Alice" par "Gueye"
    4. Ajoute "Cathérine" à la liste
    5. Supprime "David"
    6. Affiche la taille de la liste
    7. Parcours la liste avec une boucle for et affiche chaque étudiant
    8. Utilise enumerate() pour afficher les index et les noms

    IMPORTANT :
        Essaie de faire l'exercice sans regarder les exemples précédents.
"""