# le programe principal
# Taille de l'échiquier
TAILLE = 5

def main():
    # Déclaration du tableau M carré à 2 dimensions
    M = [[0] * TAILLE for _ in range(TAILLE)]

    # Appel de la fonction ConfigInit
    ConfigInit(M)

    # Demande à l'utilisateur de saisir le nombre d'étapes
    nombre_etapes = int(input("Entrez le nombre d'étapes du Jeu de la vie : "))

    # Boucle d'autant d'étapes
    for _ in range(nombre_etapes):
        # Appel de la fonction ChangeEtat
        ChangeEtat(M)

        # Appel de la fonction Imprime
        Imprime(M)

# Ètape 2 fonction imprime
    def Imprime(M):
        for ligne in M:
            print(" ".join(map(str, ligne)))
    print("\n")

# Ètape 4 Fonction nbVoisins
    def nbVoisins(M, i, j):
    # Définir les positions des voisins (pas en diagonale)
        voisins_positions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    # Initialiser le nombre de voisins à 1
    nb_voisins = 0

    # Parcourir les positions des voisins
    for di, dj in voisins_positions:
        ni, nj = i + di, j + dj

        # Vérifier si la position est à l'intérieur de l'échiquier
        if 0 <= ni < len(M) and 0 <= nj < len(M[0]):
            nb_voisins += M[ni][nj]

    return nb_voisins

# Ajoutez ici les fonctions ConfigInit, ChangeEtat et Imprime

if __name__ == "__main__":
    main()