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
def calcul_nb_voisins_np(Z):
    """Cette fonction permet de calculer le nombre de voisins en utilisant le slicing.

    Les paramétres
    --------------
        Z : un tableau numpy. 

    Retour
    ------
        nb_vois : un tableau qui contient le nombre de voisins pour chaque entrée encore on s'intéresse pas au bord. 
    
    Exemple
    -------
        >>> Y = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
        >>> calcul_nb_voisins_np(Y)
        array([[ 0.,  0.,  0.,  0.,  0.,  0.], [ 0.,  2.,  4.,  2.,  2.,  0.], [ 0.,  2.,  5.,  4.,  3.,  0.], [ 0.,  4.,  5.,  4.,  2.,  0.], [ 0.,  2.,  2.,  3.,  1.,  0.], [ 0.,  0.,  0.,  0.,  0.,  0.]])
    """
    nb_vois = np.zeros(np.shape(Z))
    nb_vois[1:-1, 1:-1] = Z[0:-2, 0:-2] + Z[:-2, 2:] + Z[2:, :-2] + Z[:-2, 1:-1] + \
        Z[1:-1, 2:] + Z[1:-1, :-2] + Z[2:, 1:-1] + Z[2:, 2:]
    return(nb_vois)



## Fonction.05::
def iteration_jeu_np(Z):
    """Cette fonction permet de réaliser une itération de jeu rapide.

    Si une cellule a trois voisines vivantes, elle devient vivante peu importe son état initial(morte, vivante).
    Si une cellule a deux voisines vivantes, elle reste dans son état actuel.
    Si une cellule a strictement moins de deux ou strictement plus de trois voisines vivantes, elle devient morte.
    Tous les autres cas restent dans son état.
    
    Les paramétres
    ---------------
        Z : un tableau numpy.

    Retour
    ------
        Z : un tableau numpy de même dimension que le tableau initial , qui donne l'état de la cellule aprés une itération. 

    Example
    -------
        >>> tab_init = np.array([[0,0,0,0],[0,0,1,0],[0,0,1,0],[0,0,0,0]])
        >>> iteration_jeu_np(tab_init)
        [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
    """
    Z = np.array(Z)
    Nov_arr = Z.copy() #pour ne pas modifier le tableau initial Z.
    nb_vois = calcul_nb_voisins_np(Z) #on utilise la fonction de Question 8. 
    cellule_viv = np.where((Nov_arr == 0) & (nb_vois == 3)) #d'aprés la description de la fonction, la cellule devient vivante. 
    Z[cellule_viv] = 1
    cellule_mor = np.where((Nov_arr == 1) & ((nb_vois == 1) | (nb_vois > 3))) #d'aprés la description de la fonction, la cellule devient morte.
    Z[cellule_mor] = 0
    return Z

## Fonction.06::

def jeu_np(Z_in, nb_iter):
    """Cette fonction permet de retourner une matrice aprés nb_iter.
    
    Les paramétres
    --------------
    
        Z_in : un tableau qui définit l'état de la matrice à l'état initial.
        nb_iter : un entier positif qui permet de voir après combien d'étapes on souhaite notre jeu.
    Exemple
    -------
        >>> Z = np.array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 0, 0], [0, 1, 0, 1, 0, 0], [0, 0, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
        >>> jeu_np(Z, 4)
        array([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 1, 0, 1, 0], [0, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0]])
    """
    if nb_iter == 0:
        return(Z_in)
    else:
        return(jeu_np(iteration_jeu_np(Z_in), nb_iter-1))
    
## Fonction.06::






































def anim_game(im_init, fct_update, frames_nb, title):
    """Display the animation for the game from an initial grid.
    Keyword arguments:
        im_init -- 2D numpy array (binary for the game of life)
        fct_update -- the function which will update the data
                        in the grid for each iteration
        frames_nb -- int or iterable
                (for more : see matplotlib.animation.FuncAnimation help)
        title -- a string for the title of the movie.
    """
    plt.figure(num=title)
    fig = plt.gcf()
    im = plt.imshow(im_init, cmap='cool')
    plt.show()

    def animate(frame):
        im.set_data(fct_update(im_init))
        return im,

    anim = animation.FuncAnimation(fig, animate, frames=frames_nb)
    return(anim)

