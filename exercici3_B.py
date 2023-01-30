"""
 En aquest arxiu s’hi crearà una funció on li demanarà a l’usuari l’edat i els ingressos que té mensuals.
 Si la resposta de l’edat és ser igual o major de 18 anys i els ingressos son majors de 1200,
 el missatge per consola serà “És necessari que facis la declaració d’hisenda”.
 En cas que alguna de les dues opcions no es compleixi, el missatge serà “Encara no pots fer la declaració”.
"""
def declaracio():
    a = input("intrutuce tu edat:")
    b = input("intrutuce  ingressos que té mensuals:")
    if(int(a)>=18 and int(b)>1200):
        return ("És necessari que facis la declaració d’hisenda.")
    else:
        return("Encara no pots fer la declaració")
