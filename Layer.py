from Neuron import Neuron
import math

class Layer(object):
    """docstring for Layer."""
    def __init__(self, size):
        # super(Layer, self).__init__()
        self.size = size
        self.Neurons = []
        for i in range(0, size):
            n = Neuron(0.00);
            self.Neurons.append(n)
