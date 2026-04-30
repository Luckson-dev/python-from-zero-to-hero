"""

    INTRODUCTION AUX VARIABLES

    Cette section explique le fonctionnement des variables,
    leur déclaration et comment les utiliser dans un programme Python.

    ---

    DEFINITION

    Une variable en programmation est un espace mémoire nommé
    utilisé pour stocker une donnée (nombre, texte, etc.) qui peut
    changer au cours de l'exécution d'un programme.

    Elle fonctionne comme une "boîte" étiquetée :
    on utilise son nom (identifiant) pour lire ou modifier sa valeur.

    Exemple : nom = "Alice"

"""

# -----------------------------
#  INTRODUCTION AUX VARIABLES
# -----------------------------

# Une variable stocke une valeur

# On crée une variable "nom" qui stocke une chaîne de caractères (string)
# Ici, "Alice" représente le nom d'une personne
nom = "Alice"

# On crée une variable "age" qui stocke un entier (integer)
# 25 représente l'âge de la personne
age = 25

# On crée une variable "genre" qui stocke une chaîne de caractères
# "F" signifie féminin (Female)
genre = "F"

# On crée une variable "nationalite" qui stocke une chaîne de caractères
# Elle indique le pays ou l'origine de la personne
nationnalite = "Congolaise"

# is_active est une variable de type booléen (bool)
# Un booléen représente un état logique :
# True  -> vrai / activé / oui
# False -> faux / désactivé / non
is_active = True

# etat_civil est une variable qui contient None
# None signifie "aucune valeur" ou "vide"
# C’est utilisé quand une variable n’a pas encore de donnée définie
etat_civil = None


# -----------------------------
# AFFICHAGE DES DONNÉES
# -----------------------------

# La fonction print() permet d'afficher une valeur dans la console

# Affiche le contenu de la variable nom
print(nom)

# Affiche l'âge stocké dans la variable age
print(age)

# Affiche le genre (F ou M)
print(genre)

# Affiche la nationalité
print(nationnalite)

# Affiche l'état de la variable is_active
print(is_active)

# Affiche la valeur de etat_civil (ici None)
print(etat_civil)


# -----------------------------
# LES COMMENTAIRES EN PYTHON
# -----------------------------

"""
    DÉFINITION

    Un commentaire est un texte dans le code qui n'est pas exécuté par Python.

    Il sert à :
    - expliquer le code
    - rendre le programme plus lisible
    - aider les autres développeurs (ou toi-même plus tard)

"""

# ------ COMMENTAIRE SIMPLE -------

# Ceci est un commentaire
# Python ignore cette ligne

nom = "Alice"  # Ceci est un commentaire à la fin d'une ligne


# ------ COMMENTAIRE MULTILIGNE -------

"""
    Ceci est un commentaire sur plusieurs lignes.

    On l'utilise pour :
    - expliquer une section entière
    - documenter le code
    - écrire des descriptions longues
"""

age = 25

# ----- EXEMPLE COMPLET -----

# On stocke le nom d'une personne
nom = "Alice"

# On stocke son âge
age = 25

# On affiche les informations
print(nom)
print(age)

# À SAVOIR SUR LE COMMENTAIRE

# Les commentaires ne sont jamais exécutés
# Ils servent uniquement à expliquer le code
# Un bon code = code + commentaires clairs
# Trop de commentaires inutiles = mauvais aussi (reste simple et clair)


# ----------------------------------------
#  REMARQUES IMPORTANTES SUR LES VARIABLES
# ----------------------------------------

# Règles de nommage des variables en Python :

# Une variable ne doit PAS commencer par un chiffre
# Exemple interdit :
# 1nom = "Alice" ----> ERREUR

# Une variable ne doit PAS contenir de tiret (-)
# Exemple interdit :
# nom-utilisateur = "Alice" -----> ERREUR

# On utilise plutôt le underscore (_) pour séparer les mots
# Exemple correct :
# nom_utilisateur = "Alice" ---> OK

# Les mots réservés Python ne peuvent pas être utilisés comme variables
# Exemple interdit :
# print = 10 -----> ERREUR

# Les variables sont sensibles à la casse
# age et Age sont deux variables différentes
