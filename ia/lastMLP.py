# -*- coding: utf-8 -*- 

"""

@author: Philippe Giraudeau
Philippe Giraudeau <philippe@giraudeau.eu>
"""

#Modules
import math
import random
import pylab as pl
import gdal as gd #

def rand(a, b):
    return (b-a)*random.random() + a

# Number of neuron in Input, Hidden and output layer.
li = 24
lh = 30
lo = 1
iterations = 2000 # Number of iterations during training step.
pas = 0.3 # pas d'apprentissage (Par défaut le laisser à 0.1).
momentum = 0.1

# Others
mErrorTesting = []
#mErrorTraining = []

def mm(a, b) : # Make your matrix
	m = []
	remp = 0.0
	for i in range(a):
		m.append([remp]*b)
	return m

def checking(*parem): # Useful if you are changing this file.
	print(parem)


def sigmoid(x):
    return math.tanh(x)
    
def dsigmoid(y):
    return 1.0 - y**2

# Sum fct
def summation(w, v):
	sum = sum + w*v
	return sum


#=========================================================================================
#    Network Class
#=========================================================================================
class Network:
	def __init__ (self, li, lh, lo, pas, momentum, iterations) : 
		# __init__ (initialise la class)
		
		#variable de remplissage avec une valeur
		self.remp = 0.0 
		
		# LI LH LO
		self.li = li 
		self.lh = lh 
		self.lo = lo

		#Les meta parametres du reseau de neurones
		self.iterations = iterations
		self.momentum = momentum
		self.pas = pas
		
		# create 2D weight matrix
		self.wIH = mm(self.li, self.lh)
		self.wHO = mm(self.lh, self.lo)
		#checking(self.wIH)
		
		# create activates matrix
		self.aIL = [self.remp]*self.li
		self.aHL = [self.remp]*self.lh 
		self.aOL = [self.remp]*self.lo
		#checking(self.maLO)
		
		# Les matrices qui vont stocker les delta 
		self.output_deltas = [self.remp] * self.lo 
		self.hidden_deltas = [self.remp] * self.lh

		# On sauvegarde le dernier état des matrices. 
		self.chgIH = self.wIH
		self.chgHO = self.wIH
		

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
        
		
	
	# propagatation fonction
	def propa (self, data):
	
        # Starting with input layer
		for i in range(self.li):
			self.aIL[i] = # data[i] # On lui donne à manger un tableau de valeur.
			
		# hidden layer propagation
		for i in range(self.li):
			sum = self.remp
			for j in range(self.lh):
				#sum = sum + summation(self.aIL, self.wIH[i][j])
			sum = sum + self.aIL[i] * self.wIH[i][j]
			self.aHL[j] = sigmoid(sum)
			
        # output layer propagation
		for i in range(self.lo):
			sum = self.remp
			for j in range(self.lh):
				#sum = sum + summation(self.aHL[j] * self.wHO[j][i])
				sum = sum + self.aHL[j] * self.wHO[j][i]
			self.aOL[i] = sigmoid(sum)
		
		return self.aOL
		
	# backpropagation fct
	def backpropa(self, data, learningError, MOMENTUM):	  
		"""	
		On va parcourir la couche de sortie:
			- la matrice d'erreur 'error' prend la différence entre ce que l'on veut 
			obtenir et ce que le réseau obtiens. 
			
			- On calcul la dérivée de la fonction qui prend en parametre la 
			sortie d'un neurone de la couche de sortie et qui multiplie ce résultat 
			par l'erreur (error)

		"""		
		for i in range(self.lo):
			error = """data[i]"""-self.aOL[i] # ... les différences entre la target et la sortie réel est nommé 
			output_deltas[i] = dsigmoid(self.aOL[i]) * error # On utilise f', la dérivée de la f (sigmoid) 
		
		"""
		On parcours de la même façon la matrice entre la couche d'entrée et cachée:
			On initialise la variable error.
			Puis on parcours à nouveau 
		"""
		#On calcul la difference pour les poids de la couche cachée
		for i in range(self.lh):
			error = self.remp
			for j in range(self.lo):
				error = error + output_deltas[j]*self.wHO[i][j]
				hidden_deltas[i] = dsigmoid(self.aHL[i]) * error
				
		# On mes à jour les poids
		for i in range(self.lh):
			for j in range(self.lo):
				change = output_deltas[j]*self.aHL[i]
				self.wIH[i][j] = self.wHO[i][j] + learningError*change + MOMENTUM*self.chgHO[i][j]
				self.chgHO[i][j] = change

		# Mise à jour des poids
		for i in range(self.li): # On parcours ...
			for j in range(self.lh):
				change = hidden_deltas[j]*self.aIL[i]
				self.wIH[i][j] = self.wIH[i][j] + learningError*change + MOMENTUM*self.chgIH[i][j]	# ... pour changer les poids entre la couche cachée et la couche d'entrée
				self.chgIH[i][j] = change

		error = self.remp
		for i in range(len(data)):
			error = error + 0.5*(data[i]-self.aOL[i])**2
		return error

		
	def training(self): # Fonction d'entrainement utilisant la backpropagation
		for i in range(self.iterations):
			error = self.remp
			for d in data:
				retine = d[0]
				targets = d[1]
				self.propa(retine)
				error = error + self.backpropa(targets, self.pas, self.momentum)
			mErrorTesting.append([error]) # Pour ploter les erreurs dans le graphique 
			print('error %-.5f' % error)
#=========================================================================================
#    Testing
#=========================================================================================


		
#=========================================================================================
#    Plots
#=========================================================================================
if __name__ == '__main__':
	network = Network(LI,LH,LO)
	network.training(ITERATIONS, PAS, MOMENTUM)
	test()
	pl.plot(mErrorTesting, 'r', label='error during training', lw = 1)
	pl.title('errors/iterations')
	pl.legend()
	pl.show()