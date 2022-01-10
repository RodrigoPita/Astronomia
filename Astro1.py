# -*- coding: iso-8859-15 -*-
#Rodrigo Pita - Turma A
#Astronomia - Sistema Solar

x = 0

#Sol
Msol = 1.988
Tsolnuc = 14000000
Tsol = 6000
Psol = 340000000000
dsolt =149600000

#Mercurio
Tdmerc = 480
Tnmerc = -176

#Venus
Tven = 482
Pven = 92

#Terra
Dter = 12650
Tternuc = 5000
Pternuc = 1.3

#Lua
dluat = 384403
Dlua = 3476

#Marte
Tfmar = -63
Tqmar = 20

#Jupiter
Mjup = 317.8

#Ganimedes
Dgan = 5262

#Saturno
Tsatnuv = -125

#Tita
Ptit = 1.5
Ptit2 = 2
Ttit = -180

#Urano
duras = 19
Erotura = 84
Tura = -190

#Miranda
Dmir = 480

#Titania
Dtita = 1578

#Netuno
dnets = 30
Tnet = -220

#Tritao
Dtri = 2700

print "Astronomia - Sistema Solar"
print ""
print ""
print "Caracteristicas dos Planetas:"
print ""
while x != "Fim":
    print "Tabela dos corpos celestes:"
    print "0 - Sol"
    print "1 - Mercurio"
    print "2 - Venus"
    print "3 - Terra"
    print "4 - Marte"
    print "5 - Jupiter"
    print "6 - Saturno"
    print "7 - Urano"
    print "8 - Netuno"
    print ""
    a = raw_input("Digite o numero referente ao astro: ")
    print ""
    print ""
    if a == "0":
        print "SOL"
        print ""
        print "- Unica estrela do sistema solar"
        print "- Ativo por 4,6 bilhoes de anos"
        print "- Estrela jovem, ainda no processo de queima de H"
        print "- Tem massa igual a ", Msol, "x10^30 kg", ", uma massa solar"
        print "- Seu nucleo estah aproximadamente a ", Tsolnuc, "ºC"
        print "- Sua temperatura na fotosfera (Camada externa visivel do Sol) eh de aproximadamente ", Tsol, "°C"
        print "- Sua pressao no nucleo eh de ", Psol, "atm, permitindo a ocorrencia de reacoes nucleares"
        print "- Distancia de ", dsolt, "km (1UA) da Terra"
        print ""
        x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
        print ""
    elif a == "1":
        print "MERCURIO - O primeiro planeta"
        print ""
        print "- O menor e mais interno planeta do sistema solar"
        print "- Chega a ", Tdmerc, "°C ao meio-dia eh ", Tnmerc, "a meia-noite"
        print ""
        x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
        print ""
    elif a == "2":
        print "VENUS - O segundo planeta"
        print ""
        print "- Sua orbita ao redor do Sol eh a mais circular"
        print "- Corpo celeste mais brilhante no ceu (Estrela D'alva), depois do Sol e da Lua"
        print "- Eh envolto por uma pesada atmosfera de CO2 e sem vapor d'agua"
        print "- Sua temperatura estah em torno de ", Tven, "ºC"
        print "- Sua pressao na superficie eh de ", Pven, "atm"
        print "- Pelo menos 85% de sua superficie eh coberta de rocha vulcanica"
        print ""
        x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
        print ""
    elif a == "3":
        print "TERRA - O terceiro planeta"
        print ""
        print "- Tem um diametro de ", Dter, "km"
        print "- Seu nucleo eh composto de um envoltorio de ferro liquido em temperaturas acima de ", Tternuc, "ºC"
        print "- Sua pressao no nucleo eh de mais de ", Pternuc, " milhao de atm"
        print "- Ha 200 milhoes de anos, os continentes estavam todos juntos na denominada 'Pangea' (Teoria da Deriva Continental)"
        print "- Os principais contituintes da Terra sao: Nitrogenio(77%) e o oxigenio(21%)"
        print "- A terra tem um satelite natural: A Lua"
        print ""
        b = raw_input("Digite 'a' se quiser saber mais sobre a Lua, ou aperte 'enter' para continuar: ")
        if b == "a":
            print ""
            print "LUA"
            print ""
            print "- Sua Origem eh desconhecida, porem, a teoria mais provavel eh a de que apos multiplos impactos, a Lua se formou a partir da Terra"
            print "- Distancia de ", dluat, "km em relacao à Terra"
            print "- Sempre eh vista a mesma face da Lua, devido a sincronia (Prot = Ptrans)"
            print ""
            x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
            print ""
        else:
            x = 0
            print ""
    elif a == "4":
        print "MARTE - O quarto planeta"
        print ""
        print "- A calota de gelo no Polo sul de Marte eh praticamente toda composta de agua, com alguma 'sujeira' (15% do material presente)"
        print "- O gelo seco (CO2 solido) forma uma camada fina sobre a agua congelada"
        print "- A temperatura varia de ", Tfmar, "°C a ", Tqmar, "°C"
        print "- Seu solo apresenta moleculas de agua ligadas a minerais"
        print "- Prot eh muito semelhante ao nosso, com apenas 40 min a mais do que o da Terra"    
        print ""
        x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
        print ""
    elif a == "5":
        print "JUPITER - O quinto planeta"
        print ""
        print "- Primeiro planeta gasoso"
        print "- Maior planeta do SS (Sistema Solar)"
        print "- Sua massa eh de ", Mjup, "massas terrestres (2,5 vezes a massa de todos os outros planetas juntos)"
        print "- Teve importante participacao no arranjo dinamico do SS, sua gravidade atuou na distribuicao dos planetas, cometas asteroides, objetos do cinturao de Kuiper e da Nuvem de Oort"
        print "- 'Guardiao da Terra', eh assim denominado, pois captura cometas (Que poderiam vir a ser ameacas para a Terra)"
        print "- Exceto pelo Sol, Jupiter tem o maior e mais forte campo magnetico"
        print "- Irradia mais calor do que absorve do Sol"
        print "- Objetivo da missao JUNO"
        print "- Possui 60 luas (2016), 4 que circulam praticamente dentro da sua atmosfera, os Satelites Galileanos (Io, Europa, Ganimedes e Calisto)"
        print ""
        c = raw_input("Digite 'a' se quiser saber mais sobre Ganimedes, ou aperte 'enter' para continuar: ")
        if c == "a":
            print ""
            print "GANIMEDES"
            print ""
            print "- Maior lua de Jupiter eh do nosso sistema solar, com diametro de ", Dgan, "km"
            print "- Provavelmente composto de um nucleo rochoso com um manto de agua/gelo e uma crosta de rocha e gelo"
            print ""
            x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
            print ""
        else:
            x = 0
            print ""
    elif a == "6":
        print "SATURNO - O sexto planeta"
        print ""
        print "- Segundo planeta gasoso"
        print "- Segundo maior planeta do SS"
        print "- Prot eh em torno de 10h e 30min"
        print "- Temperatura media das nuvens eh de ", Tsatnuv, "°C"
        print "- Cassini-Huygens foi lancada em 1997 e estuda Saturno desde 2004"
        print "- Maior lua: Tita"
        print ""
        d = raw_input("Digite 'a' se quiser saber mais sobre Tita, ou aperte 'enter' para continuar: ")
        if d == "a":
            print ""
            print "TITA"
            print ""
            print "- Unico satelite com atmosfera, 95%(Nitrogenio) e por volta de 5%(Metano)"
            print "- A pressao na superficie eh de ", Ptit, " a ", Ptit2, "bar"
            print "- Sua temperatura eh de ", Ttit, "°C"
            print ""
            x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
            print ""
        else:
            x = 0
            print ""
    elif a == "7":
        print "URANO - O setimo planeta"
        print "- Distancia de ", duras, "UA"
        print "- Seu eixo de rotacao eh inclinado ", Erotura, "° em relacao ao plano orbital da Terra (Ecliptica)"
        print "- Temperatura de aproximadamente ", Tura, "°C"
        print "- O metano na alta atmosfera absorve a luz vermelha, dando a Urano a sua cor azul-esverdiada"
        print "- Tem mais de 30 luas, com composicao parecida com os satelites jovianos (de Jupiter)"
        print "- As luas mais famosas sao: Miranda, Titania e Ariel"
        print ""
        e = raw_input("Digite 'a' se quiser saber mais sobre esses satelites, ou aperte 'enter' para continuar: ")
        if e == "a":
            print ""
            print "MIRANDA"
            print ""
            print "- O mais interno eh muito peculiar, devido a varias formacoes geologicas superpostas e misturadas"
            print "- O menor dentre os 5 maiores satelites de Urano"
            print "- Diametro de aproximadamente ", Dmir, "km"
            print ""
            print "TITANIA"
            print ""
            print "- Maior satelite de Urano"
            print "- Oitavo maior do SS"
            print "- Diametro de aproximadamente ", Dtita, "km"
            print "- Nucleo rochoso e um manto de gelo"
            print ""
            print "ARIEL"
            print ""
            print "- Tem o maior brilho e deve se a mais jovem dentre as luas de Urano"
            print ""
            x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
            print ""
        else:
            x = 0
            print ""
    elif a == "8":
        print "NETUNO - O oitavo planeta"
        print ""
        print "- Ditancia de ", dnets, "UA"
        print "- Temperatura de aproximadamente ", Tnet, "°C"
        print "- Tem 13 luas, sendo 3 delas relativamente grandes (Tritao, Nereida e Proteus)"
        print ""
        f = raw_input("Digite 'a' se quiser saber mais sobre Tritao, ou aperte 'enter' para continuar: ")
        if f == "a":
            print ""
            print "TRITAO"
            print ""
            print "- Tao fria, que a maior parte do nitrogenio(N) eh condensado como uma geada"
            print "- Unico satelite conhecido do SS que tem a superficie feita principalmente de gelo de nitrogenio"
            print "- Unica com a rotacao retrograda"
            print "- Depositos rosados constituem um vasto leito polar do sul que se acredita conter gelo metano"
            print "- Diametro de ", Dtri, "km"
            print "- Possui geiseres"
            print ""
            x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
            print ""
        else:
            x = 0
            print ""
    else:
        x = 0
