'''
intro to neural nets
recognizing handwritten language

'''
import numpy as np
import random

class Network:
    def __init__(self, sizes):
        self.num_layers = len(sizes)
        self.sizes = sizes
        self.biases = [np.random.randn(y,1) for y in sizes[1:]]
        self.weights = [np.random.randn(y,x) for x,y in zip(sizes[:1], sizes[1:])]
        

net = Network([3,2,1])
#print(net)
'''
The biases and weights in the Network object are all initialized randomly, 
using the Numpy np.random.randn function to generate Gaussian distributions 
with mean 0 and standard deviation 1
'''

print(net.weights[0]) # matrix storing weights connecting other 2


'''
a′ = σ(wa+b) - 
a  is the vector of activations
w - weight matrix
vector b of biases

'''

def sigmoid(z):
    return 1.0/(1.0 + np.exp(-z))

# if z is a vector or numpy array, it automatically
# applies it elementwise

def feedforward(self, a):
    ''' return the output if input is 'a' '''
    for b,w in zip(self.biases, self.weights):
        a = sigmoid(np.dot(w,a) + b)
    return a

''' SGD function - stochastic gradient descent'''
def SGD(self, training_data, epochs, mini_batch_size, eta,
            test_data=None):
    
    if test_data: n_test = len(test_data)
    n = len(training_data)
    for j in range(epochs):
        random.shuffle(training_data)
        mini_batches = [
                training_data[k:k+mini_batch_size]
                for k in range(0,n,mini_batch_size)]
        for mini_batch in mini_batches:
            self.update_mini_batch(mini_batch, eta)
        if test_data:
            print('Epoch {0} : {1} / {2}').format(j, self.evaluate(test_data, n_test))
        else:
            print('Epoch {0} complete').format(j)

'''
The training_data is a list of tuples (x, y) representing the training inputs 
and corresponding desired outputs.

1. we randomly sample the training set
2. we apply the sgd for each set

'''
def update_mini_branch(self, mini_branch, eta):
    """Update the network's weights and biases by applying
        gradient descent using backpropagation to a single mini batch.
        The "mini_batch" is a list of tuples "(x, y)", and "eta"
        is the learning rate."""
    nabla_b = [np.zeros(b.shape) for b in self.biases]
    nabla_w = [np.zeros(w.shape) for w in self.weights]
    
    for x,y in mini_branch:
        # most of the work is done by this
        delta_nabla_b, delta_nabla_w = self.backdrop(x,y)
        nabla_b = [nb+dnb for nb, dnb in zip(nabla_b, delta_nabla_b)]
        nabla_w = [nw+dnw for nw, dnw in zip(nabla_w, delta_nabla_w)]
        
    self.weights = [w - (eta/len(mini_branch))*nw for w,nw in zip(self.weights, nabla_w)]
    self.biases = [b - (eta/len(mini_branch))*nb for b,nb in zip(self.biases, nabla_b)]
    
    
'''
Basic Definitions: 
    zip function -
    backdrop - returning the appropriate gradient for the 
               cost associated to the training example x.
    

'''

