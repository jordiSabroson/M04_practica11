def mesGran():
    print("Programa per saber quin número es més gran: ") #Presentació del programa
    num1 = input("Introdueix el primer número: ")   #Sol·licitació dels valors a comparar
    num2 = input("Introdueix el segon número: ")
    if num1 > num2:     #Condicionals per saber quin número és més gran
        resposta = "El número {num1} és el més gran i el número {num2} és el més petit".format(num1=num1, num2=num2)
    elif num2 > num1:
        resposta = "El número {num2} és el més gran i el número {num1} és el més petit".format(num1=num1, num2=num2)
    else:
        resposta = "Els números {num1} i {num2} són iguals".format(num1=num1, num2=num2)
    return resposta
