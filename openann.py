# import "/home/kushashwaravishrimali/Documents/projects/January_2k18/Deep_Learning/Neural_Networks_Implementation/openann_python/include/Neuron.py"
from Neuron import Neuron
from Matrix import Matrix
# from Neuron import *
import math

m = Matrix(3, 2, True)
m.printToConsole()

n = Neuron(1.9);
print(n)
print("Value: ", n.getVal());
print("\nActivated Value: ", n.getActivatedVal());
print("\nDerivded Value: ", n.getDerivedVal());
