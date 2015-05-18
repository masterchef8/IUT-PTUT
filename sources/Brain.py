# -*- coding: utf-8 -*-

"""

__author__ = 'Somebody'
Philippe Giraudeau <philippe@giraudeau.eu>
"""

# Modules
import math
import random
import pylab as pl
# import gdal as gd
import numpy as np
import hyperopt as hp
import pickle as pkl
import time as t


def rand(a, b):
    return (b - a) * random.random() + a

# Number of neuron in Input, Hidden and output layer.
li = 24
lh = 30
lo = 1
iterations = 2000  # Number of iterations during training step.
pas = 0.3  # pas d'apprentissage (Par défaut le laisser à 0.1).
momentum = 0.1

data = np.array([0,1,1,1,0,0,1,0,
                 0,1,1,1,0,0,1,0,
                 0,1,1,1,0,0,1,0])
result = np.array([])  # Valeur boolean (?)

# Others
mErrorTesting = []


class Brain:
    def __init__(self, lh, lo, pas, momentum, iterations, data):
        """
        Cette classe permet de créer un perceptron multicouches à 3 couches.

       :param li: Number of neurons in input layer
       :param lh: Number of neurons in hidden layer
       :param lo: Number of neurons in output layer
       :param pas: Used for change weight between neurons
       :param momentum: Used for avoid to stay local minimun
       :param iterations: Number of iterations in learning phase.

       """
        """
        if (type(data) != np.ndarray ):
            raise ValueError("Error ")
        """
        self.data = data
        self.li = data.size


        # variable de remplissage avec une valeur
        self.remp = 0.0

        # LI LH LO
        self.li = li
        self.lh = lh
        self.lo = lo

        # Les meta parametres du reseau de neurones
        self.iterations = iterations
        self.momentum = momentum
        self.pas = pas

        # create 2D weight matrix
        self.wIH = mm(self.li, self.lh)
        self.wHO = mm(self.lh, self.lo)
        # checking(self.wIH)

        # create activates matrix
        self.aLi = [self.remp] * self.li
        self.aLh = [self.remp] * self.lh
        self.aLo = [self.remp] * self.lo
        #checking(self.maLO)

        # Les matrices qui vont stocker les delta
        self.output_deltas = [self.remp] * self.lo
        self.hidden_deltas = [self.remp] * self.lh

        # On sauvegarde le dernier état des matrices.
        self.chgIH = self.wIH  # Matrice Input => Hidden
        self.chgHO = self.wIH  # Matrice Hidden => Output

        """
        initialisation des poids des matrices avec des valeurs aléatoires comprises entre -0.2 et 0.2
        On initialise la matrice Input-Hidden et la matrice Hidden-Output
        """
        for i in range(self.li):
            for j in range(self.lh):
                self.wIH[i][j] = rand(-0.2, 0.2)
        for j in range(self.lh):
            for k in range(self.lo):
                self.wHO[j][k] = rand(-0.2, 0.2)




    def checking(*parem):
        """
            Useful if you are changing this file.
            :param parem:
            :return:
            """
        print(parem)


    def sigmoid(x):
        """
            sigmoid function used for calculate neurons activations
            :rtype : double
            """
        return math.tanh(x)


    def dsigmoid(y):
        """
            function which compute the sigmoid derivation used for backpropagation algorithm
            :param y: Result of sigmoid computation
            :return: return sigmoid derivation
            """
        return 1.0 - y ** 2


    def summation(w, v):
        """
            Used for summation propagation function
            :param w: First var
            :param v: Second var
            :return: summation between weight and values
            """
        sum = sum + w * v
        return sum


    def propagation(self, data):
        """
        TODO : Rien normalement
        :param data: Inputs to feed Multi Layer Perceptron
        :return:
        """
        # On commence par propager l'information depuis la couche d'entrée
        for i in range(self.li):
            self.aLi[i] = data[i]

        # Propagation entre la couchée d'entée et la couche cachée
        for i in range(li):
            sum = 0
            for j in range(self.lo):
                """
                    Chaque neurones de la couche cachée est connecté à
                    chaque neurone de la couche d'entée.
                    On fait la summuation de toutes les entrées d'un neurone en
                    couche cachée.
                    """
                sum = summation(self.aLi[i], self.wIH[i][j])
            self.aLh[i] = sigmoid(sum)

            # Propagation entre la couchée cachée et la couche de sortie
        for i in range(self.lo):
            sum = 0
            for j in range(self.lh):
                # Meme chose que pour la boucle précédente
                sum = summation(self.aLh[j], self.wHO[j][i])
            self.aLo[i] = sigmoid(sum)

        return self.aLo


    def backpropagation(self, data, learningError, momentum):
        """
        TODO : Rien normalement
        :param data : Les inputs du réseau
        :param learningError :  Le taux d'erreur
        :param momentum : Ce que l'on décide de changer en + ou - selon le taux d'erreur. Currently 0.2

        :return error
        """

        for i in range(self.lo):
            error = data[i] - self.aOL[i]  # Différence entre
            output_deltas[i] = dsigmoid(self.aOL[i]) * error  # On utilise f', la dérivée de la f (sigmoid)

        """
        On parcours de la même façon la matrice entre la couche d'entrée et cachée:
        On initialise la variable error.

        """
        for i in range(self.lh):
            error = self.remp
            for j in range(self.lo):
                error = error + output_deltas[j] * self.wHO[i][j]
                hidden_deltas[i] = dsigmoid(self.aHL[i]) * error

        # On mes à jour les poids
        for i in range(self.lh):
            for j in range(self.lo):
                change = output_deltas[j] * self.aHL[i]
                self.wIH[i][j] = self.wHO[i][j] + learningError * change + momentum * self.chgHO[i][j]
                self.chgHO[i][j] = change

        # Mise à jour des poids
        for i in range(self.li):
            for j in range(self.lh):
                change = hidden_deltas[j] * self.aIL[i]
                self.wIH[i][j] = self.wIH[i][j] + learningError * change + momentum * self.chgIH[i][
                    j]  # ... pour changer les poids entre la couche cachée et la couche d'entrée
                self.chgIH[i][j] = change

        error = self.remp
        for i in range(len(data)):
            error = error + 0.5 * (data[i] - self.aOL[i]) ** 2

        return error

    def training(self):
        """
        TODO : Vérifier l'insertion des données
        Fonction d'entrainement utilisant la backpropagation
        """
        for i in range(self.iterations):
            error = 0.0
            data = d[0]
            result = d[1]
            self.propagation(data)
            error = error + self.backpropa(targets, self.pas, self.momentum)
            mErrorTesting.append([error])  # Pour ploter les erreurs dans le graphique
            print('error %-.5f' % error)

            return error

    def trainHyperOpt(self):
        """
        TODO : Ecrire la fonction
        Cette fonction va appeler trainning et récupérer son taux d'erreur.

        Fonction d'entrainement utilisant HyperOpt avec la fonction standard de la librairie fmin
        """

    def pickle(self):
        """
        TODO : Ecrire la fonction

        :return: retourne un pickle (un binaire de l'état de l'instance de la classe brain )
        """





if __name__ == '__main__':
    brain = Brain(li, lh, lo, iterations, pas, momentum)

    brain.trainHyperOpt()

    pl.plot(mErrorTesting, 'r', label='error during training', lw=1)
    pl.title('errors/iterations')
    pl.legend()
    pl.show()