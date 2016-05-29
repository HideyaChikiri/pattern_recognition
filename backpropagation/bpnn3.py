# -*- coding: utf-8 -*-

import math
import random
import string
# import numpy as np

random.seed(1)

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
    # return 1.0/(1.0 + math.exp(-x))
    

def dsigmoid(x):
    return 1.0 - x**2
    # return sigmoid(x)*(1.0-sigmoid(x))
    # return x*(1.0-x)

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
        
        # set them to random vaules
        for i in range(self.ni):
            for j in range(self.nh):
                self.wi[i][j] = rand(-0.2, 0.2)
        for j in range(self.nh):
            for k in range(self.no):
                self.wo[j][k] = rand(-2.0, 2.0)

    def update(self, inputs):
        if len(inputs) != self.ni-1:
            raise ValueError('wrong number of inputs')

        # input activations
        for i in range(self.ni-1):
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
            # print("ao:" + str(self.ao[k]))
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

        # update input weights
        for i in range(self.ni):
            for j in range(self.nh):
                change = hidden_deltas[j]*self.ai[i]
                self.wi[i][j] -= rho*change

        # calculate error
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5*(self.ao[k]-targets[k])**2
            
        return error

    # for test
    def test(self, patterns):
        total_e = 0
        for p in patterns:
            result = self.update(p[0])
            e = 0
            e_list = []
            for i in range(len(p[1])):
                e_list.append(p[1][i] - result[i])
                e += math.fabs(p[1][i] - result[i])
            print p[0],p[1], '->', result, 'e=',e_list
            print "e =", e
            total_e += e**2
        print 'total_e =', total_e
        

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

    patterns = []
    
    f = open('dataset.txt')
    line = f.readline()
    
    # from textfile to list
    while line:
        pattern = []
        x = line.split("\t")
        x.pop(0)
        omega = x[-1]
        x.pop(-1)
        b = []
        
        for i in range(len(x)):
            x[i] = float(x[i])
        
        if omega.find('setosa') >= 0:
            b = [1,0,0]
        elif omega.find('versicolor') >= 0:
            b = [0,1,0]
        elif omega.find('virginica') >= 0:
            b = [0,0,1]
        
        pattern.append(x)
        pattern.append(b)
        patterns.append(pattern)
        
        line = f.readline()
        
    f.close()
    
    # lerning 50%(odd), test 50%(enen)
    testPatterns = []
    p_size = len(patterns)
    for i in range(p_size):
        # print i
        if i%2 == 0:
            testPatterns.append(patterns[i])
    
    for i in range(p_size):
        if i%2 == 1:
            del patterns[(p_size-1)-i]
    
    # print "patterns\n",patterns
    # print "testPatterns\n",testPatterns
    
    epoch = 500
    rho = 0.2
    
    # create a network with two input, two hidden, and one output nodes
    n = NN(4, 3, 3)
    n.train(patterns, epoch, rho)
    n.test(patterns)
    
    print "=========================================="
    print "=========================================="
    print "=========================================="
    print "=========================================="
    print "=========================================="
    n.test(testPatterns)

if __name__ == '__main__':
    demo()