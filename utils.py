# Ces codes seront appelés depuis le Jupyter Notebook.


########################################################### EXERCICE 1 #########################################################

## Fonction.01::

def calcul_nb_voisins(Z):
    """Cette fonction permet de calculer le nombre de voisins.
        
    Les paramétres
    ---------------
        Z : une liste de liste contient que des 0 et 1.

    Retour
    --------
        N : une liste de liste de même taille que Z ainsi chaque éléments de N contient la somme des 8 voisinages.
    
    Exemple
    ---------
        >>> Z = [[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]]
        >>> calcul_nb_voisins(Z)
        [[0, 0, 0, 0, 0, 0], [0, 1, 3, 1, 2, 0], [0, 1, 5, 3, 3, 0], [0, 2, 3, 2, 2, 0], [0, 1, 2, 2, 1, 0], [0, 0, 0, 0, 0, 0]]
    """
    forme = len(Z), len(Z[0])
    N = [[0, ] * (forme[0]) for i in range(forme[1])]
    for x in range(1, forme[0] - 1):
        for y in range(1, forme[1] - 1):
            N[x][y] = Z[x-1][y-1]+Z[x][y-1]+Z[x+1][y-1] \
                + Z[x-1][y] + Z[x+1][y] \
                + Z[x-1][y+1]+Z[x][y+1]+Z[x+1][y+1]
    return N


## Fonction.02:: 

def iteration_jeu(Z):
    """Cette fonction permet de réaliser une itération de jeu.

    Si une cellule a trois voisines vivantes, elle devient vivante peu importe son état initial(morte, vivante).
    Si une cellule a deux voisines vivantes, elle reste dans son état actuel.
    Si une cellule a strictement moins de deux ou strictement plus de trois voisines vivantes, elle devient morte.
    Tous les autres cas restent dans son état.
    
    Les paramétres
    ---------------
        Z : c'est une liste de listes.

    Retour
    ------
        Z : c'est une liste de listes, qui donne l'état de la cellule aprés une itération. 

    Example
    -------
        >>> cellule_init = [[0,0,0,0],[0,0,1,0],[0,1,1,0],[0,0,0,0]]
        >>> iteration_jeu(cellule_init)
        [[0, 0, 0, 0], [0, 1, 1, 0], [0, 1, 1, 0], [0, 0, 0, 0]]
    """
    forme = len(Z), len(Z[0])
    N = calcul_nb_voisins(Z)
    for x in range(1, forme[0]-1):
        for y in range(1, forme[1]-1):
            if Z[x][y] == 1 and (N[x][y] < 2 or N[x][y] > 3):
                Z[x][y] = 0
            elif Z[x][y] == 0 and N[x][y] == 3:
                Z[x][y] = 1
    return Z

## Fonction.03:: 

def iterations_10(Z):
    """Cette fonction affiche la simulation de 10 premièrs itérations pour la cellule Z, affiché sous forme de 2 lignes et 5 colonnes.
    
    Les paramétres
    --------------
        Z : une liste de listes (cellule initial)
    
    """
    plt.subplots(figsize=(15,10))
    for i in range(10):
        ax = plt.subplot(2,5,i+1)
        plt.imshow(Z, extent=[0,len(Z[0]),0,len(Z)])
        plt.grid(True)
        ax.set_xticks(range(0,len(Z[0]),1))
        plt.title('Itération ' + str(i))              
        Z = iteration_jeu(Z) 

    plt.show()

    
## Fonction.04::



