import sys
import os
from PyQt4 import Qt, QtCore, QtGui


sys.path.append(os.path.join(os.path.dirname(__file__), '../..'))
from hmi import *
from aware import *
from main import *
from data import *
from aware import _globals  

"""
from essa.data.adapter03 import *
from adapter03 import *
from tag02 import *
from geradores01 import *
import threading
from scan import *
from thermo import *
from display import *
from led import *
from onButton import *
from dial import *
from plot import *
"""
#real, digital, inteiro
#led, servo(slider), led(brilho)


#tela, widgets, adaptor
app = QtGui.QApplication(sys.argv)  
window = QtGui.QWidget()
window2 = QtGui.QWidget()
window3 = QtGui.QWidget()

""" WIDGET 1 - STATIC"""
font = QtGui.QFont()
font.setPointSize(20)
font.setBold(False)
font.setWeight(50)
displayTitulo = Display()
displayTitulo.value = u"Simulacao de Supervisao"
displayTitulo.setFont(font)

""" Widget 2 - WIDGET <-> TAG """
thermo = Thermo()
thermo.setRange(0,100)
thermo.setValue(88.88)

""" WIDGET 3 - TAG -> WIDGET """
font2 = QtGui.QFont()
font2.setPointSize(15)
font2.setBold(False)
font2.setWeight(30)
display = Display()
display.setFont(font2)
display.value = "Temperatura"

""" WIDGET 4 - TAG -> WIDGET """
led = Led()
display.value = "Off"

""" WIDGET 5 - TAG -> WIDGET """
displayStatusTag = Display()
displayStatusTag.value = "False"
displayStatusTag.staticText = "Status TagGeradora: "

""" WIDGET 6 - TAG -> WIDGET """
dial = Dial()
dial.setRange(0,10)
dial.setScale(0,1.0,1.0)

""" WIDGET 7 - WIDGET -> TAG """
botao = OnOffButton()
botao.textTrue = "Ligado"
botao.textFalse = "Desligado"

""" WIDGET 8 - STATIC """
displayTitulo3 = Display()
displayTitulo3.value = u"Simulacao de Analise Grafica"
displayTitulo3.setFont(font)

""" WIDGET 9 - TAG -> WIDGET """
plota = Plot()
plota.amostras(100)

""" WIDGET 10 - TAG -> WIDGET """
displayPlota = Display()
displayPlota.value = "PLOT"

""" WIDGET 11 - WIDGET -> TAG """
botaoPlot = OnOffButton()
botaoPlot.textTrue = "Ligado"
botaoPlot.textFalse = "Desligado"

""" WIDGET 12 - STATIC"""
displayTitulo2 = Display()
displayTitulo2.value = u"Simulacao de Supervisao"
displayTitulo2.setFont(font)

## TAG 1 ##
"""Tag Geradora de Dados e com Codicao de Faixa"""
tagGeradora = Tag()
tagGeradora._scan = 0.5
adaptador = AdapterRange(0,0,display,"value",tagGeradora,"value",1)
adaptador.limits(minimum=20,average=40,maximum=80,limit=100)
adaptador.condition({"Cond1":"Frio","Cond2":"Morno","Cond3":"Quente","Cond4":u"Explosao"})

tagGeradora._adapter = adaptador
tagGeradora.providerEnable = True
tagGeradora._provider =  SequenceGenerator(1,min=0,max=100,step=5)

"""Adaptador que Conecta Widget aos Dados"""
AdapterRange(0,"Temperatura",thermo,"value",tagGeradora,"value",1)

"""Adaptador que Cria uma Nova Faixa e Adiciona ao Widget LED"""
adaptador2 = AdapterRange(0,0,led,"value",tagGeradora,"value",1)
adaptador2.limits(minimum=20,average=40,maximum=80,limit=100)
adaptador2.condition({"Cond1":"Blue","Cond2":"Normal","Cond3":"Warning","Cond4":u"Emergency"})



## TAG 2 ##
"""Tag Geradora de Dados"""
tagGera2 = Tag()
adaptador3 = AdapterContinuous(0,0,dial,"value",tagGera2,"value",1)
tagGera2._adapter = adaptador3
tagGera2._provider = SequenceGenerator(1,min=0,max=10,step=1)
tagGera2.providerEnable = True
tagGera2._scan = 0.2

## TAG 3 ##
"""TAG BOTAO - Desliga o Provedor de Dados"""
tagBotao = Tag(Identity(0,),True,True)
adaptador =  AdapterRange(0,True,botao,"state",tagGera2,"provider",2)
tagBotao._adapter = adaptador
tagBotao.providerEnable = False

## TAG 4 ##
"""TAG Display - Conecta o Status da TAG a um Display de Tela"""
tagDysplayStatus = Tag()
adaptador4 = AdapterRange(0,True,displayStatusTag, "value", tagGera2,"state",1)
tagDysplayStatus._adapter = adaptador4
tagDysplayStatus.providerEnable = False

## TAG 5 ##
"""TAG Grafica - Gera Dados em Seno envia os dados a um grafico de Tela"""
tagPlota = Tag()
adaptador5 = AdapterContinuous(0,0,plota,"value",tagPlota,"value",1)
tagPlota._adapter = adaptador5
tagPlota.providerEnable = True
tagPlota._provider = SineGenerator(1,min=-1,max=1,step=10)
tagPlota._scan = 0.01
"""Adaptador que Conecta Widget Display aos Dados"""
AdapterContinuous(0,0,displayPlota,"value",tagPlota,"value",1)

## TAG 6 ##
"""TAG BOTAO - Desliga o Provedor de Dados do Grafico"""
tagBotaoPlot = Tag(Identity(0,),True,True)
adaptador6 =  AdapterRange(0,True,botaoPlot,"state",tagPlota,"provider",2)
tagBotaoPlot._adapter = adaptador6
tagBotaoPlot.providerEnable = False
"""
layout = QtGui.QVBoxLayout()
layout.addWidget(displayTitulo)
layout.addWidget(led)
layout.addWidget(display)
layout.addWidget(thermo)

layout2 = QtGui.QVBoxLayout()
layout2.addWidget(displayTitulo2)
layout2.addWidget(displayStatusTag)
layout2.addWidget(dial)
layout2.addWidget(botao)
"""
layout3 = QtGui.QVBoxLayout()
layout3.addWidget(displayTitulo3)
layout3.addWidget(displayPlota)
layout3.addWidget(plota)
layout3.addWidget(botaoPlot)



scan = Scan()
#scan.add(tagGeradora)
#scan.add(tagBotao)
#scan.add(tagGera2)
#scan.add(tagDysplayStatus)
scan.add(tagPlota)
scan.add(tagBotaoPlot)


scan.start()
"""
window.setLayout(layout)
window.setGeometry(50,100,300,500)
window.show()

window2.setLayout(layout2)
window2.setGeometry(475,100,300,300)
window2.show()
"""
window3.setLayout(layout3)
window3.setGeometry(900,100,400,500)
window3.show()


#adaptador.process_event(Event())

sys.exit(app.exec_())  