
from scipy import constants as K  # alias scipy.constants to save typing

print("pi: {0}".format(K.pi))  # some constants are built in
print("Planck: {0}".format(K.Planck))  # some constants are built in
print("c (speed of light): {0}".format(K.c))  # some constants are built in

print("natural unit of energy: {0}".format(K.value('natural unit of energy')))
print("natural unit of energy (Unit): {0}".format(K.unit('natural unit of energy')))
