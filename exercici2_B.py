"""
En aquest arxiu s’hi crearà una funció on demanarà a l’usuari
que indiqui un número i aquest li indicarà si és parell o senar.
"""
def parell():
    a=input("introtuce un numero:")
    if(int(a)%2==0):
        return("el {a} es un parell".format(a=a))
    else:
        return ("el {a} es un senal".format(a=a))
