
"""
    LES EXCEPTIONS (ERREURS)

    Une exception est un problème qui arrive pendant que ton programme tourne.

    Quand une exception apparaît et qu'elle n'est pas gérée,
    le programme s'arrête immédiatement.
"""


# ------ EXEMPLE D’ERREUR (SANS GESTION) -------

print(10 / 0)

"""
    Ici Python essaie de diviser 10 par 0.

    Problème :
    - en mathématiques, division par zéro est impossible.

    Résultat :
    - ZeroDivisionError

    Conséquence :
    - le programme s'arrête immédiatement.
"""

# ------ SOLUTION : TRY / EXCEPT -------

"""
    TRY = "j'essaie d'exécuter ce code"
    EXCEPT = "si une erreur arrive, je la gère"
"""

# Exemple avec TRY / EXCEPT

try:
    print(10 / 0)

except ZeroDivisionError:
    print("Erreur : on ne peut pas diviser par zéro")

"""
    Explication du fonctionnement :

    1. Python exécute le bloc try
    2. Il rencontre une erreur
    3. Il ne s'arrête pas
    4. Il va dans except
    5. Il affiche un message propre à cette erreur (ZeroDivisionError)

    Pourquoi c'est utile ?

    Parce que l'utilisateur peut faire des erreurs.
"""

# Autre exemple

try:
    age = int(input("Entrez votre âge : "))

    print("Vous avez", age, "ans")

except ValueError:
    print("Erreur : vous devez entrer un nombre valide")

"""
    Explication :

    - input() : l'utilisateur tape du texte
    - int() : essaie de convertir en nombre

    Si l'utilisateur tape "abc" :
    - Python ne peut pas convertir
    - erreur ValueError
    - except s'exécute
"""

# ------ PLUSIEURS TYPES D’ERREURS -------

#  On peut gérer plusieurs erreurs différentes.

try:
    x = int("abc")

except ValueError:
    print("Erreur de valeur : conversion impossible")

except Exception:
    print("Erreur inconnue")

"""
    Explication :

    - ValueError : erreur connue (conversion invalide)
    - Exception : toutes les autres erreurs possibles
"""

# POURQUOI C’EST IMPORTANT 

"""
    Sans gestion d'erreur :
    - le programme plante
    - l'utilisateur voit un crash

    Avec gestion d'erreur :
    - le programme continue
    - on affiche un message propre
    - l'application est plus professionnelle
"""


# -----------------------------
# TYPES D'EXCEPTIONS COURANTES
# -----------------------------

"""
    En Python, il existe plusieurs types d'erreurs (exceptions).

    Chaque exception correspond à un type de problème précis.
"""

# ------ ZeroDivisionError --------

"""
    Quand elle arrive :
    - quand on divise un nombre par 0

    Exemple :
        10 / 0
"""

# ------ ValueError -------

"""
    Quand elle arrive :
    - quand une valeur est incorrecte pour une conversion

    Exemple :
        int("abc")
"""

# ------ TypeError ------

"""
    Quand elle arrive :
    - quand on utilise un mauvais type de donnée

    Exemple :
        "5" + 10
"""

# ------ KeyError -------

"""
    Quand elle arrive :
    - quand une clé n'existe pas dans un dictionnaire

    Exemple :
        data["age"] si la clé "age" n'existe pas
"""

# ------ IndexError -------

"""
    Quand elle arrive :
    - quand on dépasse les limites d'une liste

    Exemple :
        liste[10] alors que la liste est petite
"""

# ------ FileNotFoundError --------

"""
    Quand elle arrive :
    - quand un fichier n'existe pas

    Exemple :
        open("fichier.txt")
"""

# ------ Exception (générale) -------

"""
    Quand elle arrive :
    - toutes les erreurs non spécifiées

    À utiliser avec précaution
"""

#  RÉSUMÉ SIMPLE

"""
    - ZeroDivisionError : division par zéro
    - ValueError : mauvaise valeur
    - TypeError : mauvais type
    - KeyError : clé inexistante
    - IndexError : index hors limite
    - FileNotFoundError : fichier introuvable
    - Exception : erreur générale
"""