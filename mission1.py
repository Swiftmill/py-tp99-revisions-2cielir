# =====================================================
#  Mission 1 - Controle de la commande d'une LED
# =====================================================
# L'operateur donne les coordonnees d'une LED (ligne, colonne).
# Votre programme doit dire de quel type de LED il s'agit.
#
# Regles, DANS CET ORDRE :
#   1. coordonnee hors de 0..7 -> "Erreur : coordonnees hors de la matrice"
#   2. LED du pourtour         -> "LED de bordure"
#   3. LED de la diagonale     -> "LED de la diagonale"
#   4. sinon                   -> "LED interne"
#
# Ne modifiez pas les 3 lignes ci-dessous.

TAILLE = 8

ligne = int(input("Ligne : "))
colonne = int(input("Colonne : "))

if ligne<0 or ligne >7 or colonne <0 or colonne >7:
    print("Erreur : coordonnees hors de la matrice")

elif ligne==0 or ligne ==7 or colonne ==0 or colonne == 7:
    print("LED de bordure")

elif ligne==colonne:
    print("LED de la diagonale")

else:
    print("LED interne")

# TODO : ecrire la structure alternative (if / elif / else)
