import random
def endevina():
    x = random.randrange(1,101)     #Número aleatori entre 1 i 100
    print("Endevina el número misteriós entre l'1 i el 100: ")
    ans = int(input("Quin número creus que és?: "))     #Número introduit per l'usuari
    while ans != x:         #Bucle while per indicar a l'usuari si la seva resposta és més gran
        if ans > x:         # o més petita que el número misteriós
            print("El número misteriós és més petit!")
            ans = int(input("Quin número creus que és?: "))
        elif ans < x:
            print("El número misteriós és més gran!")
            ans = int(input("Quin número creus que és?: "))
    return("L'has endevinat! el número misteriós era {x}".format(x=x))