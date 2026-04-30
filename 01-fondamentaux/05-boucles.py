"""
    LES BOUCLES

    Les boucles permettent de répéter un bloc de code plusieurs fois.

    Elles sont utilisées pour :
    - éviter de répéter le même code
    - parcourir des données (listes, textes, etc.)
    - automatiser des tâches

"""

# ----------------
# LES BOUCLES
# ----------------

# Sans boucle (répétition manuelle) :
print("Bonjour")
print("Bonjour")
print("Bonjour")

# Avec une boucle → on automatise

# -----------------
# BOUCLE FOR
# -----------------

"""
    DÉFINITION

    La boucle for permet de répéter un bloc de code plusieurs fois
    en parcourant une séquence de valeurs.

    Une séquence peut être :
    - une liste
    - une chaîne de caractères
    - ou une suite de nombres générée avec range()

"""

# ------ COMMENT ÇA FONCTIONNE ? -------

"""
    Structure :

    for variable in sequence:
        instruction

    - "variable" prend une valeur différente à chaque tour
    - "sequence" est l'ensemble des valeurs à parcourir
"""

# ------ UTILISATION DE range() -------

"""
    range() est une fonction qui génère une suite de nombres.

    range(3) → génère : 0, 1, 2

    ⚠️ IMPORTANT :
    - On commence toujours à 0
    - Le dernier nombre (3) n'est PAS inclus
"""

# Exemple :

for i in range(3):
    print("Bonjour")

# Explication détaillée :

# Étape 1 : range(3) → [0, 1, 2]
# Étape 2 : la boucle va parcourir ces valeurs une par une

# Tour 1 :
# i = 0 → print("Bonjour")

# Tour 2 :
# i = 1 → print("Bonjour")

# Tour 3 :
# i = 2 → print("Bonjour")

# Fin → la boucle s'arrête

# ------ AFFICHER LA VARIABLE i ------

for i in range(5):
    print(i)

# Explication :

# range(5) → [0, 1, 2, 3, 4]

# i représente l'index (position) dans la séquence

# Résultat :
# 0
# 1
# 2
# 3
# 4

# ----- NOTION D'INDEX ------

"""
    Un index est une position dans une séquence.

    En Python, l'index commence toujours à 0.

    Exemple :
    0 → premier élément
    1 → deuxième élément
    2 → troisième élément
"""

# ------ POINT IMPORTANT SUR range() ------

# range(début, fin)

for i in range(1, 5):
    print(i)

# Explication :
# range(1, 5) → [1, 2, 3, 4]
# Le 5 n'est PAS inclus

# ----- PAS (STEP) ------

# On peut ajouter un "pas" (step)

for i in range(0, 10, 2):
    print(i)

# Résultat : 0, 2, 4, 6, 8

# ------ RÉSUMÉ SIMPLE -------

# range(n) → de 0 à n-1
# range(a, b) → de a à b-1
# range(a, b, c) → de a à b-1 avec un pas de c

# for i → i change à chaque itération
# une itération = un tour de boucle

# ----------------
# BOUCLE WHILE
# ----------------

"""
    La boucle while répète un bloc de code tant qu'une condition est vraie.
"""

compteur = 0

while compteur < 3:
    print("Bonjour")
    compteur += 1  # On incrémente pour éviter une boucle infinie

# Explication :
# compteur = 0 → print
# compteur = 1 → print
# compteur = 2 → print
# compteur = 3 → stop

# ------------------
# ⚠️ BOUCLE INFINIE
# ------------------

# Attention :
# Si la condition ne devient jamais False → boucle infinie

# Exemple dangereux :
# while True:
#     print("Infini")  ❌ tourne sans arrêt

# ------------------------
# DIFFÉRENCE FOR vs WHILE
# ------------------------

# for → utilisé quand on connaît le nombre de répétitions
# while → utilisé quand on dépend d'une condition

# ----------------
# RÉSUMÉ SIMPLE
# ----------------

# for   → nombre de répétitions connu
# while → condition à respecter