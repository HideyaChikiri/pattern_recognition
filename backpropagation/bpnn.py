# -*- coding: utf-8 -*-

import math
import random
import string
# import numpy as np

random.seed(0)

# calculate a random number where:  a <= rand < b
def rand(a, b):
    return (b-a)*random.random() + a

# Make a matrix (we could use NumPy to speed this up)
def makeMatrix(I, J, fill=0.0):
    m = []
    for i in range(I):
        m.append([fill]*J)
    return m

def sigmoid(x):
    return math.tanh(x)
    # return 1.0/(1.0 + math.e**(-x))

def dsigmoid(x):
    return 1.0 - x**2
    # return sigmoid(x)*(1.0-sigmoid(x))

class NN:
    def __init__(self, ni, nh, no):
        print "==============init==============="
        # number of input, hidden, and output nodes
        self.ni = ni + 1 # +1 for bias node
        self.nh = nh
        self.no = no

        # activations for nodes
        self.ai = [1.0]*self.ni
        self.ah = [1.0]*self.nh
        self.ao = [1.0]*self.no
        
        # create weights
        self.wi = makeMatrix(self.ni, self.nh)
        self.wo = makeMatrix(self.nh, self.no)
        
        print("wi : " + str(self.wi))
        print("wo : " + str(self.wo))
        
        # set them to random vaules
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)

        print("wi : " + str(self.wi))
        print("wo : " + str(self.wo))

        # last change in weights for momentum   
        self.ci = makeMatrix(self.ni, self.nh)
        self.co = makeMatrix(self.nh, self.no)
        
        print("ci : " + str(self.ci))
        print("co : " + str(self.co))

    def update(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.ni-1):
            #self.ai[i] = sigmoid(inputs[i])
            self.ai[i] = inputs[i]

        # hidden activations
        for j in range(self.nh):
            sum = 0.0
            for i in range(self.ni):
                sum = sum + self.ai[i] * self.wi[i][j]
            self.ah[j] = sigmoid(sum)

        # output activations
        for k in range(self.no):
            sum = 0.0
            for j in range(self.nh):
                sum = sum + self.ah[j] * self.wo[j][k]
            self.ao[k] = sigmoid(sum)

        return self.ao[:]


    def backPropagate(self, targets, rho):
        if len(targets) != self.no:
            raise ValueError('wrong number of target values')

        # calculate error terms for output
        output_deltas = [0.0] * self.no
        
        for k in range(self.no):
            error = self.ao[k] - targets[k]
            output_deltas[k] = dsigmoid(self.ao[k]) * error
            
        # calculate error terms for hidden
        hidden_deltas = [0.0] * self.nh
        for j in range(self.nh):
            error = 0.0
            for k in range(self.no):
                error += output_deltas[k]*self.wo[j][k]
            hidden_deltas[j] = dsigmoid(self.ah[j]) * error
        
        # update output weights
        for j in range(self.nh):
            for k in range(self.no):
                change = output_deltas[k]*self.ah[j]
                self.wo[j][k] -= rho*change
                self.co[j][k] = change

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] -= rho*change
                self.ci[i][j] = change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(self.ao[k]-targets[k])**2
            
        return error

    # for test
    def test(self, patterns):
        for p in patterns:
            print(p[0], '->', self.update(p[0]))

    # for debug
    def printWeights(self):
        print('\nInput weights:')
        for i in range(self.ni):
            print(self.wi[i])
        print('Output weights:')
        for j in range(self.nh):
            print(self.wo[j])

    # Stochastic Gradient Descent
    def train(self, patterns, epoch, rho):
        for e in range(epoch):
            error = 0.0
            for p in patterns:
                inputs = p[0]
                targets = p[1] 
                self.update(inputs)
                error += self.backPropagate(targets, rho)
            if e % 100 == 0:
                print('error %-.5f' % error)


def demo():
    # Teach network XOR function
    pattrns = [
        [[0,0], [0]],
        [[0,1], [1]],
        [[1,0], [1]],
        [[1,1], [0]]
    ]
    
    epoch = 1000
    rho = 0.5

    # create a network with two input, two hidden, and one output nodes
    n = NN(2, 2, 1)
    n.train(pattrns, epoch, rho)
    n.test(pattrns)

if __name__ == '__main__':
    demo()