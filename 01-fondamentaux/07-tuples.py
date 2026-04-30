"""
    LES TUPLES

    Les tuples sont une structure de données en Python.

    Ils ressemblent aux listes, mais avec une différence importante :
        un tuple est IMMUTABLE (on ne peut pas le modifier après sa création)

    Les tuples sont utilisés pour stocker des données qui ne doivent pas changer.

"""

# ---------------------
# CRÉATION D'UN TUPLE
# ---------------------

# Un tuple se crée avec des parenthèses ()

coordonnees = (10, 20)

print(coordonnees)

# ----- ACCÉDER AUX ÉLÉMENTS -----

# Comme les listes, les tuples utilisent des index

print(coordonnees[0])  # 10
print(coordonnees[1])  # 20

# ----- IMMUTABILITÉ (IMPORTANT) ------

# Un tuple ne peut PAS être modifié

# Exemple :
# coordonnees[0] = 50  ERREUR

# Pourquoi ?
# Parce qu'un tuple est IMMUTABLE (non modifiable)

# ------ TUPLE VS LISTE ------

# Liste → modifiable
fruits = ["pomme", "banane"]
fruits[0] = "mangue"  # OK

# Tuple → non modifiable
coordonnees = (10, 20)
# coordonnees[0] = 50  ❌ interdit

# ------ UTILISATION D'UN TUPLE ------

# Les tuples sont utilisés pour :
# - des données fixes (coordonnées, configuration)
# - protéger les données contre les modifications
# - améliorer la performance

# ----- PARCOURIR UN TUPLE ------

for valeur in coordonnees:
    print(valeur)


# ----- RÉSUMÉ SIMPLE ------

# - tuple = collection de valeurs
# - tuple = IMMUTABLE (non modifiable)
# - utilise ()
# - similaire aux listes mais sécurisé