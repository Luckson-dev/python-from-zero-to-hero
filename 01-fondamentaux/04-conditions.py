"""
    LES CONDITIONS

    Les conditions permettent à un programme de prendre des décisions.

    Elles permettent d'exécuter du code uniquement si une certaine condition est vraie.

    On utilise les conditions pour :
    - contrôler le comportement du programme
    - vérifier des valeurs
    - créer de la logique (choix, décisions)

"""

# -----------------
# CONDITION SIMPLE
# -----------------

age = 20  # On crée une variable qui contient l'âge

# Structure :
# if condition:
#     instruction

# Explication :

# - "if" signifie "si"
# - Python va vérifier si la condition est vraie (True) ou fausse (False)
# - Si c'est vrai → il exécute le code en dessous
# - Si c'est faux → il ignore le bloc

if age >= 18:
    print("Tu es majeur")

# Détail de la condition :
# age >= 18 signifie :
# "est-ce que l'âge est supérieur ou égal à 18 ?"

# Ici :
# age = 20 → donc 20 >= 18 → True
# Donc le message s'affiche

# Si age = 15 :
# 15 >= 18 → False
# Donc rien ne s'affiche

# -----------------
# IF / ELSE
# -----------------

age = 16

# Structure :
# if condition:
#     code si vrai
# else:
#     code si faux

if age >= 18:
    print("Tu es majeur")
else:
    print("Tu es mineur")

# Explication :

# Python teste d'abord :
# 16 >= 18 → False

# Comme c'est faux :
# il ne rentre pas dans le if
# il passe directement dans le else

# Donc résultat :
# Tu es mineur

# -----------------
# IF / ELIF / ELSE
# -----------------

note = 15

# Structure :
# if condition1:
#     ...
# elif condition2:
#     ...
# elif condition3:
#     ...
# else:
#     ...

if note >= 16:
    print("Très bien")
elif note >= 12:
    print("Bien")
elif note >= 10:
    print("Passable")
else:
    print("Échec")

# Explication :

# Python lit de haut en bas

# 1. note >= 16 → 15 >= 16 → False
# il passe au elif suivant

# 2. note >= 12 → 15 >= 12 → True
# il exécute : print("Bien")
# ET IL S'ARRÊTE ICI (très important)

# Les autres conditions ne sont même pas vérifiées

# ------ POINT TRÈS IMPORTANT ------

# Python s'arrête dès qu'une condition est vraie

# Exemple :
# même si 15 >= 10 est aussi vrai,
# ce bloc ne sera jamais exécuté ici

# ------ RÉSUMÉ SIMPLE ------

# if   → premier test
# elif → autres tests si les précédents sont faux
# else → cas final si tout est faux


# ------------------------------------
# CONDITIONS AVEC OPÉRATIONS LOGIQUES
# ------------------------------------

age = 20
est_etudiant = True

if age >= 18 and est_etudiant:
    print("Accès autorisé")

# Explication :
# AND → les deux conditions doivent être vraies


# -------------------------------------
#  REMARQUES IMPORTANTES : INDENTATION
# -------------------------------------

"""
    DÉFINITION

    L'indentation correspond au décalage du code vers la droite.

    En Python, elle est OBLIGATOIRE et fait partie de la syntaxe du langage.
    Elle permet de définir quels blocs de code appartiennent à une condition,
    une boucle ou une fonction.

    Contrairement à d'autres langages (comme C, Java, JavaScript),
    Python n'utilise pas {} pour délimiter les blocs.
    Il utilise l'indentation.

"""

# ------ EXEMPLE INCORRECT ------

# Ici, il n'y a pas d'indentation après le if
# Python ne sait pas quel code appartient à la condition

# if age >= 18:
# print("Erreur")  ERREUR : Indentation manquante

# ------ EXEMPLE CORRECT ------

age = 20

if age >= 18:
    print("Tu es majeur")  # Ce code appartient au if

# ------- COMMENT PYTHON COMPREND ÇA ? --------

# Python lit :
# "tout ce qui est indenté après le if fait partie du bloc"

# Exemple :

if age >= 18:
    print("Ligne 1")
    print("Ligne 2")
    print("Ligne 3")

# Les 3 lignes seront exécutées si la condition est vraie

# ------- ERREUR COURANTE --------

# Mauvais alignement :

# if age >= 18:
#     print("OK")
#   print("Erreur")  ❌ ERREUR d'indentation

# Pourquoi ?
# Parce que l'alignement n'est pas cohérent

# ------- RÈGLE STANDARD --------

# On utilise 4 espaces pour indenter (standard recommandé)

if age >= 18:
    print("Bonne indentation")

# ------ POINT TRÈS IMPORTANT -------

# L'indentation détermine la logique du programme

age = 16

if age >= 18:
    print("Majeur")

print("Fin du programme")

# Ici :
# "Fin du programme" sera TOUJOURS exécuté
# car il n'est PAS dans le bloc if


# ----------------------
# RÉSUMÉ SIMPLE
# ----------------------

# - L'indentation est obligatoire en Python
# - Elle remplace les accolades {}
# - Elle définit les blocs de code
# - Une mauvaise indentation = erreur

# Une condition retourne toujours True ou False

# Les conditions sont utilisées partout :
# - validation
# - contrôle d'accès
# - logique métier