"""
    LES DICTIONNAIRES (DICT)

    Les dictionnaires sont une structure de données en Python.

    Ils permettent de stocker des données sous forme de :
        clé : valeur

    Contrairement aux listes :
    - on n'utilise pas des index (0, 1, 2...)
    - on utilise des clés personnalisées

    Exemple :
    nom -> "Alice"
    age -> 25

"""

# -------------------------------
# CRÉATION D'UN DICTIONNAIRE
# -------------------------------

personne = {
    "nom": "Alice",
    "age": 25,
    "genre": "F",
    "nationalite": "Congolaise"
}

print(personne)

# ----- ACCÉDER AUX VALEURS ------

# On utilise la clé pour accéder à la valeur

print(personne["nom"])   # Alice
print(personne["age"])   # 25

# ----- MODIFIER UNE VALEUR ------

personne["age"] = 26

print(personne)

# ----- AJOUTER UNE NOUVELLE CLÉ ------

personne["profession"] = "Développeuse"

print(personne)

# ----- SUPPRIMER UNE CLÉ -----

del personne["genre"]

print(personne)


# ------  MÉTHODES IMPORTANTES DES DICTIONNAIRES ------

# 1. keys() → récupère toutes les clés

print(personne.keys())

# Résultat: dict_keys(['nom', 'age', 'nationalite', 'profession'])

# 2. values() → récupère toutes les valeurs

print(personne.values())
# Résultat: dict_values(['Alice', 26, 'Congolaise', 'Développeuse'])

# 3. items() → récupère clés + valeurs

print(personne.items())

# Résultat: dict_items([('nom', 'Alice'), ('age', 26), ('nationalite', 'Congolaise'), ('profession', 'Développeuse')])

# ------ PARCOURIR UN DICTIONNAIRE ------

# ----- Parcourir les clés -----

for cle in personne:
    print(cle)

# Résultat:
#     nom
#     age
#     nationalite
#     profession


# ----- Parcourir les valeurs -----

for valeur in personne.values():
    print(valeur)

# Résultat:
#     Alice
#     26
#     Congolaise
#     Développeuse

# ----- Parcourir clés + valeurs -----

for cle, valeur in personne.items():
    print(cle, ":", valeur)

# Résultat:
#     nom           Alice
#     age           26
#     nationalite   Congolaise
#     profession    Développeuse

# ------  VÉRIFIER SI UNE CLÉ EXISTE -------

if "nom" in personne:
    print("La clé 'nom' existe")

# ------- MÉTHODE get() -------

# get() permet d'éviter les erreurs si la clé n'existe pas

print(personne.get("nom"))        # Alice
print(personne.get("adresse"))    # None (pas d'erreur)

# Avec valeur par défaut :
print(personne.get("adresse", "Non définie"))


# ----- MÉTHODE copy() -----

copie_personne = personne.copy()

print(copie_personne)

# ----- MÉTHODE clear() -------

# Supprime tout le dictionnaire

personne.clear()
print(personne)


# -------------
# RÉSUMÉ
# -------------

# - dict = clé : valeur
# - accès par clé (pas index)
# - modifiable (mutable)
# - très utilisé en Python (API, JSON, backend)



# -----------------------------
#       EXERCICE PRATIQUE
# -----------------------------

"""
    Tu dois créer et manipuler un dictionnaire représentant un étudiant.

    Instructions :

    1. Crée un dictionnaire "etudiant" avec les clés suivantes :
    - nom
    - age
    - classe
    - note

    2. Affiche toutes les informations de l'étudiant
    3. Affiche uniquement le nom et la note
    4. Modifie la note de l'étudiant
    5. Ajoute une nouvelle clé "ville"
    6. Supprime la clé "classe"
    7. Vérifie si la clé "age" existe dans le dictionnaire
    8. Utilise la méthode get() pour récupérer :
    - "nom"
    - "adresse" (qui n'existe pas)

    IMPORTANT :
    - Utilise les méthodes vues (get, items, keys si besoin)
    - Essaie de comprendre la logique clé → valeur
"""