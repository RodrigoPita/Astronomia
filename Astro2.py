# -*- coding: iso-8859-15 -*-
#Rodrigo Pita - Turma A
#Astronomia - Sistema Solar

x = 0

#Vesta
Dves = 530

#Ceres
Rcer = 480
dcers = 2.8

#Cinturão de Kuiper
dkuis = 55

#Cometas
Dcom = 50

#Nuvem de Oort
dpoors = 30000
dloors = 80000

print "Astronomia - Sistema Solar"
print ""
print ""
while x != "Fim":
    print "0 - Cinturão de Asteróides"
    print "1 - Cinturão de Kuiper"
    print "2 - Nuvem de Oort"
    print ""
    a = raw_input("Digite o número referente ao lugar: ")
    print ""
    print ""
    if a == "0":
        print "CINTURÃO DE ASTERÓIDES"
        print ""
        print "- A primeira detecção foi em 1801, de Ceres (Agora já classificado como planeta anão) entre Marte e Júpiter"
        print "- Contém mais de meio milhão de asteróides"
        print "- A teoria mais aceita é que esses pedaços de matéria são restos da formação planetária que nunca chegaram a formar um planeta"
        print "- Os asteróides não estão em distribuição uniforme no Cinturão, alguns estão agrupados e parecem ter uma relação física (São chamados de famílias)"
        print "- Dos milhares de objetos presentes, Vesta é o segundo maior, com um diâmetro de ", Dves, "km"
        print "- Ceres é o maior objeto do Cinturão de Asteróides e o único planeta anão do SS interno"
        print "     - Tem um raio de ", Rcer, "km"
        print "     - Está localizado a ", dcers, "UA do Sol"
        print "     - Tem um dos menores dias do SS"       
        print ""
        x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
        print ""
    elif a == "1":
        print "CINTURÃO DE KUIPER"
        print ""
        print "- Região em forma de disco repleto de objetos congelados"
        print "- Estende-se desde a órbita de Netuno até ", dkuis, "UA"
        print "- Estima-se que abriga mais de 1*10^9 cometas"
        print "- Os objetos do CK são remanescentes da formação do SS há cerca de 4,6 bilhões de anos"
        print "- Um planeta anão (De acordo com a União Astronômica Internacional) é um corpo que:"
        print "     - Orbita o Sol"
        print "     - Tem massa suficiente para se tornar aproximadamente redondo"
        print "     - Não limpou a vizinhança em torno de sua órbita (Diferença entre planetas anões e planetas)"
        print "     - Não é uma lua"
        print ""
        print "- Tabela do Planetas anões:"
        print "     - Plutão *"
        print "     - Ceres"
        print "     - Makemake"
        print "     - Haumea"
        print "     - Eris"
        print "     - Sedna"
        print " - Planetas anões além de Netuno são chamados Plutóides, Ceres não está nessa categoria"
        print ""
        print "* Plutão é o maior planeta anão conhecido"
        print ""
        print "- Cometas:"
        print "     - Compostos de gelo e poeira, podendo conter rochas e metais"
        print "     - Diâmetro de até ", Dcom, "km"
        print "     - Não são visíveis quando estão longe do Sol"
        print "     - A 5 UA, começam a evaporar-se formando uma bola de vapor ao seu redor (coma ou cabeleira)"
        print "     - A 2 UA, a pressão da radiação e o vento solar empurram os gases e a poeira da cabeleira, produzingo longas caudas"
        print "     - A cauda sempre aponta no sentido contrário ao Sol (de gás - mais reta, de poeira - mais curva)"
        print "     - A fina cauda azul é composta de gases, e a larga cauda branca, de partículas de pó microscópicas"
        print ""
        x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
        print ""
    elif a == "2":
        print "NUVEM DE OORT"
        print ""
        print "- É teórica"
        print "- Segundo Oort, existe uma imensa 'nuvem' de núcleos comentários orbitando (órbitas circulares) o Sol"
        print "- Essas órbitas estão a distâncias que variam de ", dpoors, "UA a mais de ", dloors, "UA do Sol"
        print "- Seriam mais de um trilhão de objetos, dos mais variados tamanhos"
        print "- A ideia desta região foi primeiramente proposta para explicar a origem dos cometas que levam milhares de anos para orbitar o Sol(cometas de longo período)"
        print ""
        print "- Para se ter uma ideia das dimensões:"
        print "     - Na sua velocidade atual de 1,5*10^6 km/dia, a nave espacial Voyager 1 não alcançará a Nuvem de Oort por cerca de 300 anos"
        print "     - Levará cerca de mais 30 mil anos para ela chegar ao outro lado"
        print ""
        x = raw_input("Para continuar, aperte 'enter', se quiser terminar, digite 'Fim': ")
        print ""
    else:
        x = 0
