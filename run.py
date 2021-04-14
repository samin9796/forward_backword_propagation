class NeuralNetwork(object):
  def __init__(self):
    self.inputLayerSize = 1
    self.hiddenLayerSize = 1
    self.outputLayerSize = 1

    self.W1 = np.random.randn(inputLayerSize, hiddenLayerSize)
    self.W2 = np.random.randn(hiddenLayerSize, outputLayerSize)

  def forwardPropagation(self, X):
    self.z2 = np.dot(X, self.W1)
    self.a2 = self.relu(self.z2)
    self.z3 = np.dot(self.a2, self.W2)
    y = self.sigmoid(self.z3)
    return y

  def back_propagate(self, W1, W2, cache):
    A1 = cache['A1']
    A2 = cache['A2']
  
    dZ2 = A2 - Y
    dW2 = (1 / m) * np.dot(dZ2, A1.T)
  
    dZ1 = np.multiply(np.dot(W2.T, dZ2), 1 - np.power(A1, 2))
    dW1 = (1 / m) * np.dot(dZ1, X.T)
    
    W1 = W1 - learning_rate * dW1
    
    W2 = W2 - learning_rate * dW2
    
    return W1, W2, b1, b2
    

  def sigmoid(self, z):
    return 1/(1+np.exp(-z))

  def relu(self,z):
    return np.maximum(0,z)
