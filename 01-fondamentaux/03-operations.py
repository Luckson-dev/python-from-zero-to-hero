"""
LES OPÉRATIONS

    Cette section explique comment effectuer des opérations sur les variables en Python.

    Les opérations permettent de manipuler les données :
    - faire des calculs (addition, soustraction, etc.)
    - comparer des valeurs
    - combiner du texte

    Elles sont essentielles pour donner de la logique à un programme.

"""

# -------------------------
# OPÉRATIONS ARITHMÉTIQUES
# -------------------------

a = 10
b = 5

# Addition
print(a + b)  # 15

# Soustraction
print(a - b)  # 5

# Multiplication
print(a * b)  # 50

# Division
print(a / b)  # 2.0

# Division entière
print(a // b)  # 2

# Modulo (reste de la division)
print(a % b)  # 0

# Puissance
print(a ** b)  # 100000

# ----------------------------
# OPÉRATIONS SUR LES STRINGS
# ----------------------------

# Une string (chaîne de caractères) est du texte entouré de guillemets
prenom = "Alice"
nom = "Dupont"

# ----- CONCATÉNATION -----

# La concaténation consiste à assembler plusieurs chaînes de caractères

# Ici :
# - prenom contient "Alice"
# - " " est un espace (très important pour séparer les mots)
# - nom contient "Dupont"

# Le symbole + permet de coller les textes entre eux
print(prenom + " " + nom)

# Résultat :
# Alice Dupont

# IMPORTANT :
# Si tu oublies l'espace " ", le résultat sera collé :
print(prenom + nom)

# Résultat :  AliceDupont

# ----- RÉPÉTITION -----

# On peut répéter une chaîne de caractères avec l'opérateur *

# Ici, Python répète "Alice" 3 fois
print(prenom * 3)

# Résultat :  AliceAliceAlice

# Attention :
# Il n’y a pas d’espace automatiquement ajouté
# Si tu veux un espace entre les répétitions :

print((prenom + " ") * 3)

# Résultat : Alice Alice Alice 

# -----------------------
# REMARQUES IMPORTANTES
# -----------------------

# 1. On ne peut concaténer que des strings avec des strings
# Exemple incorrect :
# print("Age: " + 25)  ERREUR

# Solution :
print("Age: " + str(25))  # conversion en string

# 2. Le + assemble les textes
# 3. Le * répète les textes


# --------------------
# OPÉRATIONS LOGIQUES
# --------------------

"""
    DÉFINITION

    Une opération logique est une opération qui permet de travailler avec
    des valeurs booléennes (True ou False).

    Elle sert à prendre des décisions dans un programme.

    Les opérations logiques sont souvent utilisées dans :
    - les conditions (if)
    - les boucles
    - les validations

"""

x = True
y = False

# ------- AND (ET logique) -------

# AND retourne True uniquement si les DEUX valeurs sont True
print(x and y)

# Explication :
# True AND False = False
# Parce que les deux ne sont pas vrais

# Tableau de vérité (important à comprendre) :

# True  and True  → True
# True  and False → False
# False and True  → False
# False and False → False

# ------- OR (OU logique) --------

# OR retourne True si AU MOINS une des valeurs est True
print(x or y)

# Explication :
# True OR False = True
# Parce qu'au moins une valeur est vraie

# Tableau de vérité :

# True  or True  → True
# True  or False → True
# False or True  → True
# False or False → False

# ------- NOT (NON logique) ---------

# NOT inverse la valeur
print(not x)

# Explication :
# not True = False
# not False = True

# ----- DIFFÉRENCE ENTRE AND ET OR -----

# AND → exige que TOUT soit vrai
# OR  → accepte qu'au moins UNE condition soit vraie

# Exemple concret :

age = 20
est_etudiant = True

# Cas avec AND (les deux conditions doivent être vraies)
print(age > 18 and est_etudiant)  # True

# Cas avec OR (une seule condition suffit)
print(age > 18 or est_etudiant)   # True


# --------------------------
# OPÉRATIONS DE COMPARAISON
# --------------------------

a = 10
b = 5

print(a == b)  # False (égal)
print(a != b)  # True (différent)
print(a > b)   # True (supérieur)
print(a < b)   # False (inférieur)
print(a >= b)  # True (supérieur ou égal)
print(a <= b)  # False (inférieur ou égal)

# -----------------
# REMARQUE
# -----------------

# Les opérations permettent de créer de la logique dans un programme.
# Elles sont utilisées dans :
# - les conditions (if)
# - les boucles
# - les calculs