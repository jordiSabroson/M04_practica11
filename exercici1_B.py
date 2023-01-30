"""
En aquest arxiu s’hi crearà una funció on demanarà a l’usuari que
inserti 2 números i el programa li dirà quin és el més gran i quin
el més petit. Si son iguals, no sortirà cap missatge.
"""
def mesgran ():
    a=input("introduce un numero:")
    b=input("introtuce otra numero:")
    if (a<b):
        return("el {b} es mes gran que el {a}".format(a=a,b=b))
    if (b<a):
        return("el {a} es mes gran que el {b}".format(a=a,b=b))
    if (b==a):
        return("")
