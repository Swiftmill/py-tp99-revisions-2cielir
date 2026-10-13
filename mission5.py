# =====================================================
#  Mission 5 - Analyser un motif
# =====================================================
# Le motif est fourni. Vous devez le mesurer.
# Affichages attendus, dans cet ordre et avec exactement ce texte :
#   LED allumees : ...
#   Courant total : ... mA
#   Ligne la plus allumee : i (n LED)
#   Colonne la plus allumee : j (n LED)
# En cas d'egalite, on garde la plus petite ligne / colonne.

TAILLE = 8
COURANT_LED = 20   # milliamperes consommes par une LED allumee
nb_led = 0

# --- motif fourni : ne pas modifier ---
matrice = [
    [0, 0, 1, 1, 1, 1, 0, 0],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 0, 0, 0, 0, 0, 1],
    [1, 0, 1, 0, 0, 1, 0, 1],
    [1, 0, 1, 1, 1, 1, 0, 1],
    [0, 1, 0, 0, 0, 0, 1, 0],
    [0, 0, 1, 1, 1, 1, 0, 0],
]

# --- affichage du motif (donne) ---
for i in range(TAILLE):
    texte = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            texte = texte + "# "
        else:
            texte = texte + ". "
    print(texte)

print()

# --- 1. nombre total de LED allumees ---
# TODO
for i in range(TAILLE):
    text = ""
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            nb_led += 1
print("LED allumees : ", nb_led)
# --- 2. courant total consomme (en mA) ---
# TODO
print("Courant total : ", COURANT_LED * nb_led, " mA")


# --- 3. ligne la plus allumee ---
# TODO : compter les LED de chaque ligne et retenir la meilleure
record_led = 0
most_allumed_line = 0
for i in range(TAILLE):
    nb_led = 0
    for j in range(TAILLE):
        if matrice[i][j] == 1:
            nb_led += 1
    if nb_led > record_led:
        record_led = nb_led
        most_allumed_line = i
print("Ligne la plus allumee : ", most_allumed_line, "(", record_led, "LED)")


# --- 4. colonne la plus allumee ---
# TODO : attention, ici la boucle des colonnes est a l'exterieur
record_led = 0
most_allumed_line = 0
for j in range(TAILLE):
    nb_led = 0
    for i in range(TAILLE):
        if matrice[i][j] == 1:
            nb_led += 1
    if nb_led > record_led:
        record_led = nb_led
        most_allumed_line = j
print("Colonne la plus allumee : ", most_allumed_line, "(", record_led, "LED)")
