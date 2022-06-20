# -*- coding: iso-8859-15 -*-
#Rodrigo Pita - Turma A
#Astronomia - Sistema Solar

x = 0

#Vesta
Dves = 530

#Ceres
Rcer = 480
dcers = 2.8

#Cintur�o de Kuiper
dkuis = 55

#Cometas
Dcom = 50

#Nuvem de Oort
dpoors = 30000
dloors = 80000

print( "Astronomia - Sistema Solar" )
print()
print()
while x != "Fim":
    print( "0 - Cintur�o de Aster�ides" )
    print( "1 - Cintur�o de Kuiper" )
    print( "2 - Nuvem de Oort" )
    print()
    a = input("Digite o n�mero referente ao lugar: ")
    print()
    print()
    if a == "0":
        print( "CINTUR�O DE ASTER�IDES" )
        print()
        print( "- A primeira detec��o foi em 1801, de Ceres (Agora j� classificado como planeta an�o) entre Marte e J�piter" )
        print( "- Cont�m mais de meio milh�o de aster�ides" )
        print( "- A teoria mais aceita � que esses peda�os de mat�ria s�o restos da forma��o planet�ria que nunca chegaram a formar um planeta" )
        print( "- Os aster�ides n�o est�o em distribui��o uniforme no Cintur�o, alguns est�o agrupados e parecem ter uma rela��o f�sica (S�o chamados de fam�lias)" )
        print( "- Dos milhares de objetos presentes, Vesta � o segundo maior, com um di�metro de ", Dves, "km" )
        print( "- Ceres � o maior objeto do Cintur�o de Aster�ides e o �nico planeta an�o do SS interno" )
        print( "     - Tem um raio de ", Rcer, "km" )
        print( "     - Est� localizado a ", dcers, "UA do Sol" )
        print( "     - Tem um dos menores dias do SS" )
        print()
        x = input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
        print()
    elif a == "1":
        print( "CINTUR�O DE KUIPER" )
        print()
        print( "- Regi�o em forma de disco repleto de objetos congelados" )
        print( "- Estende-se desde a �rbita de Netuno at� ", dkuis, "UA" )
        print( "- Estima-se que abriga mais de 1*10^9 cometas" )
        print( "- Os objetos do CK s�o remanescentes da forma��o do SS h� cerca de 4,6 bilh�es de anos" )
        print( "- Um planeta an�o (De acordo com a Uni�o Astron�mica Internacional) � um corpo que:" )
        print( "     - Orbita o Sol" )
        print( "     - Tem massa suficiente para se tornar aproximadamente redondo" )
        print( "     - N�o limpou a vizinhan�a em torno de sua �rbita (Diferen�a entre planetas an�es e planetas)" )
        print( "     - N�o � uma lua" )
        print()
        print( "- Tabela do Planetas an�es:" )
        print( "     - Plut�o *" )
        print( "     - Ceres" )
        print( "     - Makemake" )
        print( "     - Haumea" )
        print( "     - Eris" )
        print( "     - Sedna" )
        print( " - Planetas an�es al�m de Netuno s�o chamados Plut�ides, Ceres n�o est� nessa categoria" )
        print()
        print( "* Plut�o � o maior planeta an�o conhecido" )
        print()
        print( "- Cometas:" )
        print( "     - Compostos de gelo e poeira, podendo conter rochas e metais" )
        print( "     - Di�metro de at� ", Dcom, "km" )
        print( "     - N�o s�o vis�veis quando est�o longe do Sol" )
        print( "     - A 5 UA, come�am a evaporar-se formando uma bola de vapor ao seu redor (coma ou cabeleira)" )
        print( "     - A 2 UA, a press�o da radia��o e o vento solar empurram os gases e a poeira da cabeleira, produzingo longas caudas" )
        print( "     - A cauda sempre aponta no sentido contr�rio ao Sol (de g�s - mais reta, de poeira - mais curva)" )
        print( "     - A fina cauda azul � composta de gases, e a larga cauda branca, de part�culas de p� microsc�picas" )
        print()
        x = input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
        print()
    elif a == "2":
        print( "NUVEM DE OORT" )
        print()
        print( "- � te�rica" )
        print( "- Segundo Oort, existe uma imensa 'nuvem' de n�cleos coment�rios orbitando (�rbitas circulares) o Sol" )
        print( "- Essas �rbitas est�o a dist�ncias que variam de ", dpoors, "UA a mais de ", dloors, "UA do Sol" )
        print( "- Seriam mais de um trilh�o de objetos, dos mais variados tamanhos" )
        print( "- A ideia desta regi�o foi primeiramente proposta para explicar a origem dos cometas que levam milhares de anos para orbitar o Sol(cometas de longo per�odo)" )
        print()
        print( "- Para se ter uma ideia das dimens�es:" )
        print( "     - Na sua velocidade atual de 1,5*10^6 km/dia, a nave espacial Voyager 1 n�o alcan�ar� a Nuvem de Oort por cerca de 300 anos" )
        print( "     - Levar� cerca de mais 30 mil anos para ela chegar ao outro lado" )
        print()
        x = input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
        print()
    else:
        x = 0
