""" This file was creted to test a simple feature of python 3.9

The | (pipe) operator for dicts
"""


a = {
    "k1": "ovo",
    "k2": "bala",
    "k3": "pedra"
}

b = {
    "k2": "carro",
    "k6": "oculos"
}

c ={
    "k7": "casa",
    "k9": "brinquedo"
}

print("DICT A: ", a)
print("DICT B: ", b)

print()
print("Operation (a | b): ", a | b)
print()

print("B before Operation: ", b)
print("C before Operation: ", c)

b |= c
print()
print("B after Operation (b |= c): ", b)

