"""
    TYPE DE VARIABLES

    Cette section explique les différents types de données que l'on peut stocker
    dans des variables en Python.

    Chaque variable possède un type, qui définit la nature de la valeur qu'elle contient :
    nombre, texte, booléen, etc.

    Comprendre les types de variables est essentiel pour manipuler correctement
    les données dans un programme.

"""

# ---------------------
# TYPE DE VARIABLES
# ---------------------

# ---------------------
# STRING (str)
# ---------------------

# Une string est une chaîne de caractères (du texte)
nom = "Alice"
message = "Bonjour le monde"

print(nom)
print(message)

# ---------------------
# INTEGER (int)
# ---------------------

# Un integer est un nombre entier (sans virgule)
age = 25
annee = 2025

print(age)
print(annee)

# ---------------------
# FLOAT (float)
# ---------------------

# Un float est un nombre à virgule
taille = 1.75
prix = 19.99

print(taille)
print(prix)

# ---------------------
# BOOLEAN (bool)
# ---------------------

# Un booléen représente deux valeurs : True ou False
is_active = True
is_admin = False

print(is_active)
print(is_admin)

# ---------------------
# NONE (NoneType)
# ---------------------

# None signifie "aucune valeur"
# Utilisé quand une variable n’est pas encore définie
etat_civil = None

print(etat_civil)

# VÉRIFIER LE TYPE

# La fonction type() permet de connaître le type d’une variable

print(type(nom))          # str

print(type(age))          # int

print(type(taille))       # float

print(type(is_active))    # bool

print(type(etat_civil))   # NoneType


# ------- REMARQUE --------

# Python détermine automatiquement le type de la variable
# On n’a pas besoin de déclarer le type manuellement

# Exemple :

x = 10        # int
x = "Bonjour" # devient str


# ----------------------------
# LES MÉTHODES DE STRING (str)
# ----------------------------

"""
    DÉFINITION

    En Python, une variable n'est pas seulement une valeur.

    C'est un OBJET.

    Un objet est quelque chose qui :
    - contient une valeur
    - possède des actions intégrées appelées MÉTHODES

    Une méthode permet de manipuler la valeur de la variable.
"""

texte = "bonjour python"

# upper() → mettre lext en majuscules

print(texte.upper())
# BONJOUR PYTHON

# lower() → mettre le text en minuscules

print(texte.lower())
# bonjour python

# capitalize() → première lettre en majuscule

print(texte.capitalize())
# Bonjour python

# title() → chaque mot commence par une majuscule

print(texte.title())
# Bonjour Python

# strip() → supprimer les espaces début/fin

texte2 = "   hello   "
print(texte2.strip())
# hello

# replace() → remplacer un mot

print(texte.replace("python", "monde"))
# bonjour monde

# split() → découper une chaîne en liste

phrase = "je suis dev"
print(phrase.split())
# ['je', 'suis', 'dev']

# find() → chercher une position

print(texte.find("python"))
# retourne l’index où commence "python"

# startswith() / endswith() : vérifie si le mot commence avec ou se termine avec

print(texte.startswith("bonjour"))  # True
print(texte.endswith("python"))     # True


# ------ RÉSUMÉ SIMPLE -------

# str = objet texte
# .upper() → majuscule
# .lower() → minuscule
# .capitalize() → première lettre
# .replace() → remplacer
# .split() → découper
# .strip() → nettoyer espaces