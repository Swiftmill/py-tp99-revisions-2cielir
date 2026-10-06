# =====================================================
#  Mission 2 - Construire et afficher la matrice
# =====================================================
# 1. Construire une matrice TAILLE x TAILLE remplie de 0, avec des boucles.
# 2. L'afficher : "# " pour une LED allumee, ". " pour une LED eteinte,
#    une ligne de la matrice = une ligne affichee.
# 3. Allumer les LED (2, 3) et (5, 5), afficher une ligne vide,
#    puis reafficher la matrice.
#
# ATTENTION : matrice = [[0] * 8] * 8 ne fonctionne PAS (voir RAPPELS-PYTHON.md).

TAILLE = 8

# --- 1. construction de la matrice eteinte ---
matrice = []
for i in range(TAILLE):
    ligne = []
    for j in range(TAILLE):
        ligne.append(0)
    matrice.append(ligne)
# --- 2. affichage ---
for i in range(TAILLE):
    texte = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            texte = texte+"# "
        else:
            texte = texte+". "
    print(texte)
# --- 3. allumage de deux LED puis nouvel affichage ---
matrice[2][3] = 1
matrice[5][5] = 1
print()
for i in range(TAILLE):
    texte = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            texte = texte + "# "
        else:
            texte = texte + ". "
    print(texte)
