# -*- coding: utf-8 -*- 

"""
Project Name : Cortana 
Created on December 30th 2013

@author: Philippe Giraudeau
Philippe Giraudeau <giraudeau.philip@gmail.com>
"""
#=========================================================================================
#	Cortana V1 
#=========================================================================================
#Modules
import math
import random
import string
import pylab as pl

def rand(a, b):
    return (b-a)*random.random() + a

# Number of neuron in Input, Hidden and output layer.
LI = 20
LH = 20
LO = 5
ITERATIONS = 2000 # Number of iterations during training step.
PAS = 0.3 # pas d'apprentissage (Par défaut le laisser à 0.1).
MOMENTUM = 0.1

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
class brain:
	def __init__ (self, LI, LH, LO) : 
		# __init__ (initialise la class)
		self.remp = 0.0 # Je sais pas si c'est une bonne idée mais c'est plus pratique
		
		self.li = LI 
		self.lh = LH 
		self.lo = LO
		#checking(self.li)
		
		# create 2D weight matrix
		self.wIH = mm(self.li, self.lh)
		self.wHO = mm(self.lh, self.lo)
		#checking(self.wIH)
		
		# create activates matrix
		self.aIL = [self.remp]*self.li
		self.aHL = [self.remp]*self.lh 
		self.aOL = [self.remp]*self.lo
		#checking(self.maLO)
		
		for i in range(self.li):
			for j in range(self.lh):
				self.wIH[i][j] = rand(-0.2, 0.2)
		for j in range(self.lh):
			for k in range(self.lo):
				self.wHO[j][k] = rand(-0.2, 0.2)
                
		# Save the last weights to compare with actual weights
		self.chgIH = self.wIH
		self.chgHO = self.wIH
		
		
	
	# propagatation fct
	def propa (self, data):
	
        # Starting with input layer
		for i in range(self.li):
			self.aIL[i] = data[i]
			
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
		
		#for i in range(len(self.aOL)):
		#	if self.aOL[i] < 0.99:
		#		self.aOL[i] = 1
		#	else:
		#		self.aOL[i] = 0
		return self.aOL
		
	# backpropagation fct
	def backpropa(self, data, learningError, MOMENTUM):	  
		output_deltas = [self.remp] * self.lo # On initialise la matrice output_deltas avec la valeur 0.0
		for i in range(self.lo): # On parcours ...
			error = data[i]-self.aOL[i] # ... les différences entre la target et la sortie réel est nommé 
			output_deltas[i] = dsigmoid(self.aOL[i]) * error # On utilise f', la dérivée de la f (sigmoid) 
				
		#On calcul la difference pour les poids de la couche cachée
		hidden_deltas = [self.remp] * self.lh
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

		# Mise o jour des poids
		for i in range(self.li): # On parcours ...
			for j in range(self.lh):
				change = hidden_deltas[j]*self.aIL[i]
				self.wIH[i][j] = self.wIH[i][j] + learningError*change + MOMENTUM*self.chgIH[i][j]	# ... pour changer les poids entre la couche cachée et la couche d'entrée
				self.chgIH[i][j] = change

		error = self.remp
		for i in range(len(data)):
			error = error + 0.5*(data[i]-self.aOL[i])**2
		return error

		
	def training(self, ITERATIONS, PAS, MOMENTUM): # Fonction d'entrainement utilisant la backpropagation
		iterations = ITERATIONS
		momentum = MOMENTUM
		pas = PAS
		#Le tableau retine contient les patterns d'activations ainsi que les réponses souhaitées
		data = [
        [[ 
        0,1,1,0,
        1,0,0,1,
        1,1,1,1,
        1,0,0,1,
        1,0,0,1], [0,0,0,1,1]],
        [[
        1,1,1,1,
        1,0,0,1,
        1,1,1,1,
        1,0,0,1,
        1,1,1,1], [0,0,0,1,0]],
        [[
        1,1,1,1,
        1,0,0,0,
        1,0,0,0,
        1,0,0,0,
        1,1,1,1], [0,0,1,1,0]],
        [[
        1,1,1,0,
        1,0,0,1,
        1,0,0,1,
        1,0,0,1,
        1,1,1,0], [0,1,0,1,1]],
        [[
        1,1,1,1,
        1,0,0,0,
        1,1,1,0,
        1,0,0,0,
        1,1,1,1], [1,0,0,1,1]],
        
   	 	]
		for i in range(iterations):
			error = self.remp
			for d in data:
				retine = d[0]
				targets = d[1]
				self.propa(retine)
				error = error + self.backpropa(targets, pas, momentum)
			mErrorTesting.append([error]) # Pour ploter les erreurs dans le graphique 
			print('error %-.5f' % error)
#=========================================================================================
#    Testing
#=========================================================================================
def test():
	patun = [
        [[
        1,1,1,1,
        1,1,0,1,
        1,0,1,1,
        1,0,0,1,
        1,1,1,1], [0,0,0,1,0]],
        [[
        1,1,1,1,
        1,1,0,0,
        0,0,0,0,
        1,0,0,0,
        1,1,1,1], [0,0,1,1,0]],
        [[
        1,1,1,0,
        1,0,0,1,
        0,0,0,1,
        1,0,0,1,
        1,0,1,0], [0,1,0,1,1]],
        [[
        1,1,1,1,
        1,0,0,0,
        1,0,1,0,
        1,0,0,0,
        1,1,1,1], [1,0,0,1,1]],
        [[
        0,0,1,1,
        1,1,0,1,
        1,1,1,1,
        1,0,0,1,
        1,0,0,1], [0,0,0,1,1]],
        
    ]
	for p in patun:
		print(p[0], p[1],'=>', br.propa(p[0]))
		
#=========================================================================================
#    Plots
#=========================================================================================
if __name__ == '__main__':
	br = brain(LI,LH,LO)
	br.training(ITERATIONS, PAS, MOMENTUM)
	test()
	pl.plot(mErrorTesting, 'r', label='error during training', lw = 1)
	pl.title('errors/iterations')
	pl.legend()
	pl.show()