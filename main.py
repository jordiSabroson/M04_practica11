import exercici1_B as masgrande             #esta importa otra archivo
import exercici2_B as par
import exercici3_B as declaracion
import exercici1_A as ex1A
import exercici2_A as ex2A
import exercici3_A as ex3A
print("aquesta funcio es dir quin és el més gran i quin el més petit")
print(masgrande.mesgran())                      #forma de llama el funcio de otra archivo
print("aquesta funcio es dir si el parell o senal")
print(par.parell())
print("aquesta funcio es dir si es pot fer declaració")
print(declaracion.declaracio())

print("Funció per saber quin número és més gran o més petit o igual")
print(ex1A.mesGran())
print("Funció que proporciona una llista de 5 noms i segons el que introdueixis et retornarà una frase acord al nom")
print(ex2A.cincNoms())
print("Funció on has d'endevinar un nombre entre 1 i 100")
print(ex3A.endevina())
