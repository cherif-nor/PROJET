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
    
## Fonction.07::

def jeudevie(init, msj):
    """Cette fonction permet de faire l'animation de jeu de la vie.
    
    Les paramétres
    --------------
        init : tableau initial (on peut dire que c'est "le plan" dans laquel on va faire l'animation)
        msj : tableau de même dimension que le tableau initial.
    """
    plt.figure()
    fig = plt.gcf()
    shw = plt.imshow(init)
    plt.title(" Jeu de la vie avec Z_huge")
    plt.show()

    def animate():
        shw.set_data(msj(init))
        return shw,

    anim = FuncAnimation(fig, animate,frames=200, interval=20, blit=True)
    return(anim)

## Fonction.08::
def animate(i):
    jeu_np(Z_huge, 1)
    shw = plt.imshow(Z_huge)
    return shw,

## Fonction.09::

def Jeudevie_grph(Z):
    """cette fonction permet d'afficher les 10 premières itérations de jeu de la vie.
    
    Les paramétres
    --------------
        Z : tableau numpy (matrice)
        
    """
    fig, ax = plt.subplots()
    plt.imshow(np.array(Z))
    plt.title("Jeu de la vie après l'itr")
    for i in range(1, 10):
        fig, ax = plt.subplots()
        iteration_jeu_np(Z)
        A = np.array(Z)
        plt.imshow(A)
        plt.title("Jeu de la vie après l'itr " 
                  + str(i))
        plt.show()

## Fonction 10::
class JeuDeLaVie:

    def __init__(self, init_state, _time_T):
        self.init_state = init_state # initialisation de self
        self.n_1 = init_state.shape[0] # creation des deux dimension 
        self.n_2 = init_state.shape[1]
        self._historic_state = np.ndarray((self.n_1, self.n_2, _time_T+1))
        self._historic_state[:, :, 0] = self.init_state 
    def play(self):
        t = 1
        while(t <= self._time_T):
            self._historic_state[:, :, t-1] = \
                iteration_jeu_np(self._historic_state[:, :, t])
            self.average_life = np.mean(self._historic_state, axis=(2))
            t = t + 1

    def __plot__(self, init_state, _time_T):
        """Cette fonction permet de jouer le jeux de la vie jusqu'à _time_T et stocke dans la le tranche du
           tenseur, l'état du jeu au temps t pour tous les t de 0 à _time_T. On mettra aussi à jour l'attribut
           average_life qui permet de visualiser le temps de vie moyen de chaque cellule au cours du jeu
        """   
        self.average_life = 1/_time_T*self.average_life
        fig, ax = plt.subplots()
        plt.imshow(self.average_life)
        fig.suptitle()
        plt.show()
        self.init_state = init_state
        self._time_T = _time_T
        self._dimension = (n_1, n_2) = init_state.shape
        self._historic_state = np.zeros((n_1, n_2, _time_T+1))
        self._historic_state[:, :, 0] = self.init_state
        self.average_life = np.zeros((n_1, n_2))

    def play(self):
        """affiche la matrice average_life avec la palette viridis.
        """
        t = 1
        while(t <= self._time_T):
            self._historic_state[:, :, t] = iteration_jeu_np(
                self._historic_state[:, :, t-1]) 
            self.average_life = np.mean(self._historic_state, axis=(2))
            t += 1

    def plot(self):
        display_one_plot(
            self.average_life, "10".format(self._time_T))
        plt.colorbar()

