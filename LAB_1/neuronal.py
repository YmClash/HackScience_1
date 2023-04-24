from numpy import exp, array, random, dot
import time
import numpy as np

# ici j'apprends rudimentarement comment un reseau de neuronne fonctionne et cella en utilisant la librairie Numpy

# reseau de simple neurone


training_set_inputs = array([[0, 0, 1], [1, 1, 1], [1, 0, 1], [0, 1, 1]])
training_set_outputs = array([[0, 1, 1, 0]]).T
random.seed(2)
synaptic_weights = 2 * random.random((3, 1)) - 1

print("training Input ", + training_set_inputs)
print()
print("training Output", + training_set_outputs)

print("synatic Weight", + synaptic_weights)

print()
print()
reponse = np.array([0.99929937])

for iteration in range(100000) :
    output = 1 / (1 + exp(-(dot(training_set_inputs, synaptic_weights))))
    synaptic_weights += dot(training_set_inputs.T, (training_set_outputs - output) * output * (1 - output))
    print(output)
    print()
    # time.sleep(1)
    print(synaptic_weights)
    print()
    print("iteration : " + str(iteration))
    print()
    # time.sleep(2)

print()
print()
resultat = (1 / (1 + exp(-(dot(array([1, 0, 0]), synaptic_weights)))))
print("Resultat:")
print(resultat)
print()
print("reponse:")
print(reponse)
comparaison = resultat == reponse
equal_array = comparaison.all()
print(equal_array)

time.sleep(1)
if equal_array is False :
    print("nice ...you  make  a  good job")
else :
    print("I'am sorry but  the  resolution is not correct ")

print()
print()
print("Neuronal Network by Momo ")

print(type(reponse))
print(len(reponse))
print(type(resultat))
print(len(resultat))
print()

print(np.array_equal(resultat, reponse))
