def cincNoms():
    noms = ("Cardener", "Gratallops", "Botifler", "Xerrameca", "Curt de gambals") #Llista dels noms
    print("Introdueix un dels 5 noms següents (ben escrit ehh): ")
    for i in noms: #Bucle per mostrar els noms disponibles
        print(i)
    resposta = input("Introdueix el nom: ")
    if resposta == noms[0]:                #Condicionals per trobar la resposta
        a = "Qui no carda a Olot, no carda enlloc"
    elif resposta == noms[1]:
        a = "El llop, on cria, no hi fa mal."
    elif resposta == noms[2]:
        a = "A Cervera, botiflers, sense cap home de bé."
    elif resposta == noms[3]:
        a = "Xerres pels colzes."
    elif resposta == noms[4]:
        a = "Sou més curts de gambals! Com que només penseu en lluites i cops, mireu com heu acabat."
    else:
        a = "La resposta no és correcte!"
    return a