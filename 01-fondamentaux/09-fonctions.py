"""
    LES FONCTIONS

    Une fonction est un bloc de code réutilisable qui permet d'exécuter
    une tâche spécifique.

    Elle permet de :
    - organiser le code
    - éviter les répétitions
    - rendre le programme plus lisible

    TYPES DE FONCTIONS

    Il existe deux types de fonctions en Python :

    1. LES FONCTIONS PRÉDÉFINIES (intégrées)

    Ce sont des fonctions déjà créées et fournies par Python.
    Tu peux les utiliser directement sans les définir.

    Exemples :
    - print() → affiche du texte
    - len() → retourne la longueur
    - type() → retourne le type d'une valeur

    Tu les utilises, mais tu ne les crées pas.


    2. LES FONCTIONS DÉFINIES PAR L'UTILISATEUR

    Ce sont des fonctions que TU crées toi-même avec le mot-clé "def".

    Elles servent à :
    - organiser ton code
    - créer tes propres outils
    - éviter la répétition

    Exemple :

    def dire_bonjour():
        print("Bonjour")

    Ici, c"est toi qui as défini la fonction.
"""


# ----------------------------
#   LES FONCTIONS PRÉDÉFINIES
# ----------------------------


# ------ La fonction print() -------

""" print() est utilisée afficher une valeur à l'écran """

print("Bonjour")

# ------ La fonction input() ------

"""
    input() → permet de récupérer une valeur saisie par l'utilisateur

    IMPORTANT :
    input() retourne toujours une chaîne de caractères (str)
"""

nom = input("Entrez votre nom : ")

print("Bonjour", nom)

# ------ La fonction int() -------

"""
    int() → convertit une valeur en entier (nombre sans virgule)
"""

age = int("25")

print(age)

# ------ La fonction str() -------

"""
    str() → convertit une valeur en chaîne de caractères
"""

nombre = 10
texte = str(nombre)

print(texte)

# ------ La fonction float() ------

"""
    float() → convertit une valeur en nombre à virgule
"""

prix = float("19.99")
print(prix)

# ------ La fonction len() ------

"""
    len() → retourne la longueur (nombre d'éléments)
"""

print(len("Python"))      # 6
print(len([1, 2, 3]))     # 3

# ------ La fonction type() -------

"""
    type() → retourne le type d'une variable
"""

print(type(10))        # int
print(type("Hello"))   # str

# ------ La fonction range() -------

"""
    range() → génère une suite de nombres

    Souvent utilisé avec les boucles
"""

for i in range(3):
    print(i)

# ------ La fonction sum() -------

"""
    sum() → additionne les éléments d'une liste
"""

print(sum([1, 2, 3, 4]))  # 10

# ------ RÉSUMÉ SIMPLE -------

# print() → afficher
# input() → lire une entrée utilisateur
# int() → convertir en entier
# str() → convertir en texte
# float() → convertir en nombre à virgule
# len() → taille
# type() → type
# range() → suite de nombres
# sum() → addition


# --------------------------------
#   CRÉER TA PREMIÈRE FONCTION
# ---------------------------------

"""
    SYNTAXE D'UNE FONCTION

    Pour créer une fonction en Python, on utilise le mot-clé "def".

    Structure :

    def nom_fonction():
        instructions

    Explication :
    - def → indique à Python que tu crées une fonction
    - nom_fonction → nom que tu choisis
    - () → parenthèses obligatoires (même si vides)
    - : → début du bloc de code
    - indentation → code qui appartient à la fonction
"""

def dire_bonjour():
    print("Bonjour")


# ----- EXÉCUTION D’UNE FONCTION ------

"""
    Créer une fonction ≠ exécuter une fonction

    Quand Python lit :

    def dire_bonjour():
        print("Bonjour")

    Il enregistre la fonction, mais il ne l'exécute pas.

    Pour exécuter une fonction, il faut l'appeler :
"""

dire_bonjour()

"""
Pourquoi ?

Parce qu'une fonction est comme un outil :
👉 elle ne s'utilise que si tu l'appelles

Sans appel → rien ne se passe
"""


# ------ LE MOT-CLÉ return ------

"""
    return signifie : "renvoyer une valeur"

    - Une fonction peut produire un résultat
    - return permet de récupérer ce résultat à l'extérieur

    Exemple :
"""

def addition():
    return 10 + 5

resultat = addition()

print(resultat)

"""
    Explication :

    1. Calcul de 10 + 5
    2. return 15
    3. la valeur 15 est envoyée à l'extérieur
    4. elle est stockée dans "resultat", on pourait l'utiliser
        ailleurs dans le code

"""


# ----- POURQUOI UTILISER return ? ------

"""
    Sans return :
    - tu ne peux pas réutiliser le résultat
    - la fonction affiche seulement

    Avec return :
    - tu peux stocker le résultat
    - tu peux le réutiliser ailleurs
    - tu peux faire d'autres calculs avec

    return rend la fonction utile et réutilisable
"""


# ----- DIFFÉRENCE ENTRE print() ET return ------

def exemple_print():
    print("Bonjour")

def exemple_return():
    return "Bonjour"

# Cas 1
x = exemple_print()
print(x)

# Résultat :
#           Bonjour
#           None

"""
    Pourquoi ?

    print() :
    - affiche à l'écran
    - ne renvoie aucune valeur, si tu récuère la valeur à l'exterieur de la fonction
     ça affiche "None"
"""

# Cas 2
y = exemple_return()
print(y)

# Résultat :
#           Bonjour

"""
    return :
    - ne montre rien directement
    - renvoie une valeur que tu peux utiliser

    Différence clé :

    print() → afficher
    return → renvoyer une valeur
"""


# ------------------------------
#  LES PARAMÈTRES ET ARGUMENTS
# ------------------------------

"""
    Une fonction peut recevoir des données pour travailler.
    Ces données passent par :

    - les PARAMÈTRES
    - les ARGUMENTS

    👉 PARAMÈTRE vs ARGUMENT

    - PARAMÈTRES → variables définies dans la fonction
    - ARGUMENTS → valeurs envoyées lors de l'appel
"""

# EXEMPLE SIMPLE

def dire_bonjour(nom):  # "nom" est un PARAMÈTRE
    print("Bonjour", nom)

dire_bonjour("Alice")   # "Alice" est un ARGUMENT
dire_bonjour("Bob")

"""
    Quand tu appelles :
    dire_bonjour("Alice")

    Python fait :
    nom = "Alice"

    Puis exécute :
    print("Bonjour", nom)
"""

# ------ AVEC PLUSIEURS PARAMÈTRES -------

def addition(a, b):  # a et b sont des PARAMÈTRES
    return a + b

resultat = addition(5, 3)  # 5 et 3 sont des ARGUMENTS

print(resultat)

# ------ ORDRE DES ARGUMENTS -------

def afficher_infos(nom, age):
    print(nom, age)

afficher_infos("Alice", 25)

# Ici :
#     nom = "Alice"
#     age = 25

# Si tu inverses :
afficher_infos(25, "Alice")
# La valeur du "nom" dévient 25 et la valeur de "age" dévient "alice"

# ------ ARGUMENTS NOMMÉS -------

# Tu peux préciser le nom du paramètre

afficher_infos(age=25, nom="Alice")

# Avantage :
#   - l’ordre n’a plus d’importance

# ------ VALEURS PAR DÉFAUT -------

def saluer(nom="Utilisateur"):
    print("Bonjour", nom)

saluer()           # utilise la valeur par défaut
saluer("Alice")    # remplace la valeur

# ------ PLUSIEURS VALEURS -------

def afficher_infos_complet(nom, age, ville):
    print(nom, age, ville)

afficher_infos_complet("Alice", 25, "Paris")


# ----------------------------
# 🧠 RÉSUMÉ : LES FONCTIONS
# ----------------------------

"""
    DÉFINITION

    Une fonction est un bloc de code réutilisable qui exécute une tâche spécifique.
"""

# TYPES DE FONCTIONS

"""
    1. FONCTIONS PRÉDÉFINIES
    - Déjà créées par Python
    - Exemples : print(), input(), len(), type()

    2. FONCTIONS DÉFINIES
    - Créées par le programmeur avec "def"
"""

# CRÉATION D'UNE FONCTION

"""
    def nom_fonction():
        instructions
"""

# EXÉCUTION

"""
    Une fonction ne s'exécute QUE si on l'appelle.

    Exemple :

    nom_fonction()
"""

# PARAMÈTRES

"""
    Les paramètres sont des variables dans la fonction.

    Exemple :

    def dire(nom):
        print(nom)
"""

# RETURN

"""
    return renvoie une valeur à l'extérieur de la fonction.

    Exemple :

    def add(a, b):
        return a + b
"""

# PRINT vs RETURN

"""
    print() : affiche
    return : renvoie une valeur
"""

# 🧠 À RETENIR

# - une fonction = outil réutilisable
# - def = création
# - () = appel
# - return = sortie
# - print = affichage