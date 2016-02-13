**ESSA**
====
Embeddable SCADA for Small Applications
---------------------------------------
![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/1.jpg)

**Definições de Projeto**

Este software consiste em desenvolver um software de IHM como uma interface gráfica do usuário (GUI) baseada em software de código aberto com protocolos de comunicação e de dados. Devendo possuir as mesmas funções dos SCADAs comerciais, ele usa o conceito de módulos, e como é software de fonte aberta, por meio de modificação, poderia ser aplicável ou alterado a qualquer momento, sem a necessidade de qualquer autorização, qualquer licença de qualquer autoridade, etc. Simplesmente é um sistema aberto em todo o hardware e software, apenas necessita de um conhecimento básico para quem o implementar.

Em relação a interface gráfica, foi adotado o Qt, por possuir muitos widgets e ser uma biblioteca independente de sistema operacional e linguagem de programação. Utilizado em conjunto com o Qt, a biblioteca Qwt(Qt Widgets para aplicações técnicas) fornece vários widgtes comumente usados em telas de supervisão SCADA, onde a partir da herança, alguns widgets específicos foram desenvolvidos, outros adaptados, e esta biblioteca foi definida como GUI, juntamente com o Qt Designer usado para desenhar graficamente as telas.

---

Componentes SCADA
-----------------
![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/2.jpg)
A partir de pesquisas e levantamentos, componentes de aplicação SCADA foram listados. Embora existam algumas diferenças de terminologia entre produtos, classes de componentes são facilmente agrupados de acordo com a função e as características. Assim, uma aplicação típica SCADA possuis:

**Tags**
>Estes componentes armazenam dados de memória. O termo está relacionada com a área da instrumentação, e é aplicado não apenas a partir dos dados fornecidos pelo hardware supervisionado, mas também para as variáveis da aplicação. Tipos de dados habituais fornecidos pelo RTU/CLP são booleanos (on/off) ou inteiro. No entanto, hardware mais recente também lidam com o formato real (precisão fixa ou ponto flutuante), tempo e tipos textuais. Assim, as tags devem ser capazes de lidar com estes tipos de dados diferentes, juntamente com diferentes fontes de dados. Alguns produtos também oferecem tags simuladas (ou tags demo), onde o valor delas variam de acordo com alguma função ao longo do tempo, o que é interessante durante o desenvolvimento de aplicações;

**Drivers**
>Aplicações SCADA devem usar o protocolo de comunicação adequada para trocar dados com hardware externo. Há um grande número de equipamentos disponíveis, cada um utilizando protocolos proprietários/exclusivos ou um dos diferentes protocolos padrão, como Modbus, por exemplo. Então, para lidar com diferentes protocolos possíveis sem ter que carregar todos eles em um aplicativo, uma solução é usar os drivers, que são módulos carregáveis que gerenciam um determinado protocolo/equipamento de comunicação. Normalmente, as tags estão ligadas ao driver que lida com a comunicação com o equipamento remoto, que fornece os dados que elas armazenam;

**IHM**
>A IHM de uma aplicação SCADA é composta por telas que contêm widgets. Estes elementos podem ser ligados a tags para exibir seus dados ou para modificá-los. Além disso, telas e widgets podem ser usadas para exibir alertas e responder a eventos do usuário ou dispositivos supervisionados. Pode haver uma grande variedade de widgets com aparência e comportamento diferente, por vezes refletindo a aparência de instrumentos físicos. 

**Alarmes**
>Esses componentes estão relacionadas as tags, a fim de automatizar o seu monitoramento. Um alarme geralmente tem alguma condição predefinida, como a faixa de valores permitidos para o tag, ou uma expressão booleana que é avaliada toda vez que a tag monitorada modificar o seu valor. Um alarme pode disparar eventos ou, se estiver ligada a algum widget, pode mostrar alguma indicação na IHM;

**Logger**
>O histórico do software e dispositivos é tratado por este tipo de componente. Pode ser armazenado em arquivos individuais ou em SGBD (Sistema de Gerenciamento de Banco de Dados), e para cada tipo de dado armazenamento deve ser utilizado um logger especializado. Em alguns produtos, eles têm nomes diferentes de acordo com a sua função, como histórico, referindo-se ao registro de Tags, e Log referente ao registro de alarmes e eventos;

**Scripts** 
>Há situações em que uma ação a ser executada que envolve vários componentes, ou o comportamento normal de tags, alarmes e widgets. O software SCADA fornece uma maneira de definir scripts de comando a ser executado quando ocorrer um evento. A linguagem de script pode se basear em uma linguagem de programação existente ou exclusivo para o produto. Eventualmente, assistentes gráficas estão disponíveis para definir a lógica desejada.

---
Pacotes
-------
As classes são agrupados em pacotes de acordo com a sua função no software. As classes essenciais para a execução de uma aplicação SCADA estão no pacote app. O pacote comm tem as classes do driver de comunicação. A interface de usuário é baseada nas classes de pacotes HMI. Os dados e registro do evento são de responsabilidade de classes do pacote log. O pacote de aux compreende classes auxiliares para o SCADA. Estes pacotes são detalhados a seguir.

**[APP]**
>O pacote de aplicação contém as classes mínimas necessárias para a execução da aplicação SCADA. A classe principal é a SCADAApp. Sempre á apenas uma instância dela, que é responsável pela inicialização do programa e o loop da aplicação, onde os ciclos de analise são efetuados, seguido por atualizações de tela e log de dados relevantes. É um container para objetos que compõem a aplicação. 
A classe TAG tem a responsabilidade de armazenar dados, que podem ser originados a partir do hardware remoto, como RTU/PLCs, ou dados variáveis de memória, utilizados para fins auxiliares ou simulações. Para fins de simulação, DataGen pode ser utilizada, fornece dados de acordo com uma função em um ciclo de tempo. Instâncias de alarme são usadas para eventos de acordo com as regras determinadas, tais como mudança de valor ou intervalo válido. Script armazena comandos que são executados de acordo com os eventos disparados por alarmes.

**[COMM]**
>Gerencia a comunicação com os provedores remoto de dados. A classe link define a interface do aplicativo e classes derivadas implementam protocolos de comunicação especializados como ModbusLink e ArduinoLink, por exemplo. Um exemplo, link conecta com um hardware remoto de cada vez, e pode fornecer dados para vários objetos Tag. A classe LinkFactory é usado para abstrair a instanciação de vincular objetos especializados através da aplicação do método padrão de design pattern.

**[HMI]** 
>O pacote HMI (IHM) contém as classes usadas para criar a interface do usuário. É composto por diferentes telas, quais contendo os widgets que são ligados as tags por adaptadores. A classe Screen representa as telas. Widget é a classe base de widgets, de acordo com a sua funcionalidade. As instâncias do adapter conecta widgets as tags, transformando os valores de acordo com regras diferentes, a fim de fácil escalamento ou conversões. Widgets básicos a serem aplicadas são semelhantes às apresentadas na Figura 1. A Figura mostra uma possível hierarquia de classe widget e outras classes.

**[AWARE]** 
>Este pacote contém classes de acessórios para as outras classes. A classe Event define o comportamento de uma hierarquia de diferentes tipos de eventos. Para carregar uma aplicação SCADA especial de arquivos XML, as classes SCADAParser e associados (CfgParser e HMIParser) são utilizados para analisar o conteúdo do arquivo, criar os componentes do aplicativo e inicializá-los. %A classe Timer pode ser usado para programar eventos para ser disparadas a uma certa quantidade de tempo de execução, repetidamente ou não.

**[LOG]** 
>O pacote de log tem classes usadas para dados de registro e mensagens para destinatários de armazenamento, tais como arquivos de texto e bancos de dados. A classe Logger pretende gravar dados em arquivos de texto, enquanto instâncias DBLogger gerenciar as conexões do sistema de gerenciamento de banco de dados relacionais. 

---

ESSA - Embeddable SCADA for Small Applications
----------------------------------------------

![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/3.jpg)
A partir desta subseção se inicia o detalhamento do software desenvolvido, que teve uma nomeoclatura de produto definido, ESSA - Embeddable SCADA for Small Applications, (SCADA Embarcado para Pequenas Aplicações, em portugues). %O escopo do presente trabalho será realizado sobre o módulo {Runtime/Main}, que é o sistema que realiza a aquisição, supervisão e controle dos dados.
A seguir é detalhado as caracteristicas do SCADA desenvolvido. Cada sessão, não necessáriamente é um módulo do software, esses podem ser compostos por demais classes criadas.

Para o funcionamento do sistema SCADA pretendido, tem-se a definição de quatro pacotes, indispensáveis ao sistema:

 - Comunicação  
 - Data  
 - IHM  
 - TAGS

**{Runtime}**
É o sistema SCADA, que fica em execução responsável por efetuar o monitoramento e processamento dos dados das *tag* disponíveis, bem como iniciar uma atuação. A partir de eventos, repassa dados para atualizar aos componentes da IHM, para que se tenha uma visualização gráfica das variáveis dos equipamentos a que elas representam. 
Cada *tag* é passível de emitir um alarme, que pode ser um ato como gravar informação, gerar um relatório, ou emitir um alerta, para que o operador analise se o comportamento do equipamento esta adequado.  

O Runtime faz a integração de todos os módulos que compõe o sistema SCADA.
Pode emitir eventos, como disparo de scripts que realizam determinadas tarefas e atualizar a interface gráfica.
Este módulo engloba as principais funções do SCADA, como a processamento do arquivo de definição e conexão das Tags com os Widgets da IHM, à partir do seu ciclo de varredura que atualiza os valores dos componentes em supervisão. 

**{TAG}**

O principal objeto dentro do ESSA. Comprende o objeto que carrega as caracteristicas e valor para o contexto do SCADA. É a aquisição de dados para o Runtime. 

Uma Tag pode ser provedora de dados, assim o valor dela é de acordo com o seu objeto de comunicação ou de dados. Se ela não for provedora, é uma Tag de valor estático. 
Pode possui qualquer tipo de dado válido, menos um objeto. 
Quando seu valor é alterado, dispara eventos pertinentes que notificam seus observadores para que os mesmo alterem de acordo com a Tag.
E é quem possui alarmes vinculados. 

Tag possui um atributo de temporização, em que é definido o seu ciclo de varredura, para se saber de quanto em quanto tempo ela deve ser atualizada. 

Ao criar uma *tag*, suas características podem compreender três tipos possíveis, que são: 

 - 
**[Tag de Comunicação]** 
Responsável pelo link de protocolo que se comunica com o equipamento
   de aquisição e que prove os dados com alto grau de variação.

 **[Tag Var]** 
		Tag de variável armazenada na memória, é uma variável de característica mais constante, sofrendo pouca ou nenhuma variação ao longo de sua vida. 

		
 **[Data Gen]** 
		Prove uma tag em modo simulado. Uma tag comunicação estando inativa, pode ter seu *data gen* ativado, simulando o comportado real da *tag*, a partir da simulação de valores gerados por função de curvas e de tempo definida. Também pode fornecer data e hora para o sistema.

---


**{Adapter}**

A IHM possui componentes Widget que podem ou não se comunicar com Tags. Havendo comunicação, ela é realizado por um Adapeter. 

Quando uma Tag é atualizada por um objeto de comunicação, ela pode estar vinculada a um Widget, necessitando o widget atualizar seu valor com o novo valor da Tag. Este valor nem sempre esta na mesma escala, ou unidade que o widget trabalha, necessitando de uma adaptação. Um botão de estado que trabalha com 0 e 1, pode corresponder a um Widget display que representa na IHM a mensagem de "Aberto" ou "Fechado", por exemplo, o adaptador é responsável por essa mudança de comportamento. 

O Adapter também é quem faz com que uma mudança em um Widget, reflita em uma mudança na Tag. Se um botão é pressionado na IHM, ele atualiza o valor da Tag, que por sua vez, reflete na alteração do componente a tag vinculado pela comunicação. Se um botão Liga/Desliga é pressionado, então o dispositivo ou componente industrial é deligado ou ligado, por exemplo. 

Assim percebe-se a existência de algumas possibilidades de fluxo de dados. A implementação contempla a definição deste fluxo seguindo uma enumeração:

- **[Direction]** 

 1. Corresponde a uma comunicação de dados no sentido "Tag para Widget". O Valor da Tag somente e unicamente é recebido pelo Widget, toda mudança de valor Tag, corresponde a uma mudança no Widget.
 
 2. Corresponde a uma comunicação de dados no sentido "Widget para Tag". O valor do Widget somente e unicamente corresponde ao valor da Tag.  Toda alteração do Widget corresponde a uma mudança no valor da Tag.
 
 3. Corresponde a uma comunicação de dados no sentido "Tag para Widget ou Widget para Tag". É um fluxo bidirecional. Tanto a Tag atualiza o widget, quanto uma mudança no Widget reflete na Tag. Por exemplo, um botão que tem sem valor correspondente ao estado de Ligado/Desligado de um equipamento, se pressionado, o desliga, assim um único componente faz a supervisão e atuação.

 4. Corresponde a uma comunicação de dados no sentido "Tag para Tag". A característica da primeira *tag* é refletida na segunda.

Juntamente com a definição do fluxo da informação é necessário informar a propriedade a que a informação corresponde da Tag e também do Widget. 

São essas as propriedades possiveis para Tag:

 - **[Propriedades de Tag]**
	 - [provider] Lê ou Grava sobre o estado de provedor da Tag. 
	 - [state] Lê ou Grava sobre o o estado de ativo da Tag. 
	 - [value] Lê ou Grava sobre o valor da Tag.

E essas as propriedades possiveis para Widget:

 - **[Propriedades de Widget]** 
	 - [state] Lê ou Grava sobre o o estado de do Widget. 
	 - [text] Lê ou Grava sobre o valor texto da Tag. 
	 - [value] Lê ou Grava sobre o valor da Tag.

Com esses fluxos definidos, é possível gerenciar a totalidade de possibilidade de fluxo de dados dentro do contexto do SCADA. 

Atualmente existe três tipos de adaptadores disponíveis no ESSA:

 1. **{AdapterContinuous}** 
 É o adaptador basico do ESSA, tem a funcionalidade básica de fazer a adaptação das Tags com os Widgets.
    Durante o fluxo de dado do adaptador, o valor não sofre nenhuma
    interferencia. Porém pode ser definido uma escala para este valor,
    sendo ele mapeado para uma nova faixa correspondente. As
    propriedades de escala disponíveis são:
    
    [Scale]     
     - [minimum] Atual valor mínimo. 
     - [maximum] Atual valor máximo.   
     - [newMinimum] Novo valor mínimo 
     - [newMaximum] novo valor máximo.
    
    Por padrão não executa a faixa, mas se definido o valor apresentado será o valor de correspondência a faixa. Um valor de 0 à 100 pode corresponder a um valor na faixa de 100 à 1000, assim, o zero equivale ao novo mínimo que é 100, por exemplo. Deve-se definir os limites originais e novos.

 2. **{AdapterRange:}** 
 É um adaptador como o Continuous, mas com as funções adicionais de *Regra* e *Condição*. É possivel configurar 4
    limites de valor e para cada limite uma condição equivalente. Por
    exemplo, se o valor for acima de 100, o valor equivar a "Muito
    Quente". As propriedades definidas são:
    
    [Limits]
    
     - [minimum] Valor de limite mínimo para condição. 
     - [average] Valor de limite médio para condição. 
     - [maximum] Valor de limite máximo para condição. 
     - [limit] Valor de limite máximo total para condição.
    
    E para as condições, deve-se seguir este padrão: [Conditions]
    
     - [Cond1] Valor equivalente a condição de minimum. 
     - [Cond2] Valor equivalente a condição de average. 
     - [Cond3] Valor equivalente a condição de maximum. 
     - [Cond4] Valor equivalente a condição de limit.

 

 3. **{AdapterDiscret:}** 
 Por fim, tem o adaptador discreto, o qual possui um valor equivalente aos valores booleanos False e True.
    [DiscretValues] 
    
     - [valueTrue] Valor correspontente a True. 
     - [valueFalse] Valor correspondente a False.

	Permite ter um valor texto mais apropriado a apresentação na IHM.

---

**{Comunicação}**

Este pacote é o responsável pela comunicação do CLP, placa de aquisição de dados, microcontrolador, ou dispositivo externo que realize a aquisição e a atuação sobre o dispositivo ou equipamento a ser monitorado. 

A comunicação é realizada através da rede \textit{Serial}, sendo que o equipamento de aquisição necessita de um protocolo para que realize esta tarefa. 

Foi projetado o conceito de \textit{factory method }(método de fabricação), um padrão que define uma interface para criar um objeto, mas permite às classes decidirem qual classe instanciar. Nesse contexto, em que a partir da definição de duas estruturas de protocolos definidas, o usuário cria um objeto de comunicação do protocolo escolhido.

Um objeto de comunicação pode ser definido para dois protolos existentes no ESSA, ArduinoLink ou ModbusLink. O objeto comunicação criado é o endereço de um dispositivo ligado a porta serial, corresponde a um equipamento de aquisição, esse equipamento pode possuir mais de uma saida ou entrada de dados, assim sendo, um objeto pode ter mais de uma leitura/gravação ao mesmo tempo, necessitando que seu objeto seja compartilhado com mais de uma Tag. Por isso essa definição, de um objeto comunicação ser criado primeiramente, para depois ser utilizado pelos seu Links apropriados.
 
O link é associado a \textit{tag comunicação}, que detém as informações sobre o endereço e o tipo de dado a ser transportado.


A comunicação é feita utilizando o módulo pySerial\{pySerial:2014}, que encapsula o acesso as portas seriais, pelo Python.

O objeto é criado pelo \textit{Factory Method}, para isso é necessário o usuário definir qual é o tipo da comunicação, em conjunto com as seguintes definições que são necessárias para cada tipo:

Obs: Ambas comunicações compartilham essas propriedades:

> **[name]** Nome do objeto de comunicação, necessário aos links. 

> **[port]** Porta de Comunicação. O Padrão '/dev/ttyACM0'. 

> **[baudrate]** Taxa de transmissão de dados. O Padrão '9600'.

 1. **{ArduinoLink}**
No desenvolvimento da comunicação com Arduino, foi utilizado o módulo pyFirmata\citep{pyFirmata:2014} que é uma interface Python para protocolo Firmata \citep{Firmata:2014} biblioteca que implementa o protocolo Firmata para se comunicar com o software no computador host. Permite escrever um firmware personalizado sem ter que criar um protocolo e objetos próprios. 

 Firmata é um protocolo genérico para se comunicar com os microcontroladores de software em um computador host. Ele destina-se a trabalhar com qualquer pacote de software de computador hospedeiro. Basicamente, este firmware estabelece um protocolo para comunicar com o Arduino de um software host. O objetivo é permitir um completo controle do Arduino.

 A partir dessa biblioteca que prove a abstração de maneira simplificada em python do protocolo Firmata, foi desenvolvido um objeto de comunicação em que o usuário configura a sua comunicação, e posteriormente definir as configurações para o ArduinoLink:

 Para o objeto de comunicação que será compartilhado com os Links, é necessário definir três parametros de configuração: (name, port e baudrate), que corresponde respectivamente ao nome do Link, porta serial em que se encontra o dispositivo de aquisição e a taxa de transmissão de dados. O objeto é definifo pelo arquivo de descrição.

 Definido o objeto, é necessário definir os Links. Um ArduinoLink tem os seguintes parâmetros necessários, board e pin, que são respectivamente o nome do objeto de comunicação desse link e o pino de comunicação utilizado no Arduino.

 A definição do pino de comunicação segue o padrão "tipo:pino:modo":
> **[tipo]** Tipo de pino Arduino: a ou d. ("a" referente a Analógico e "d" referente a Digital)

> **[pino]** Numero do pino

> **[modo]** Modo do Pino: i, o ou p. ("i" equivale Input, "o" para Output e "p" é pwm)



 Um ArduinoLink tem a sequinte assinatura e deve ser descrito como um *provider*, quando definido a uma Tag: 

	 `ArduinoLink(board=commArduino,pin='a:1:i')`


 2. **{ModbusLink}**
 	Se a comunicação for para um dispositivo com o protocolo Modbus, é necessário ao menos definir os seguintes parâmetros: (name, port, baudrate e address), correspondentes a nome do Link, porta serial em que se encontra o dispositivo de aquisição, taxa de transmissão e endereço do escravo. Uma comunicação Modbus possui alguns parametros adicionais de configuração, que se definidos, sobreescreves os valores padrão da comunicação, sendo estes adicionais: (bytesize, parity, timeout e mode).

	> **[address]** Endereço do escravo.

	> **[bytesize]** Tamanho dos Bits. O Padrão '8'.

	> **[parity]** Bit de paridade. O Padrão 'N'.

	> **[timeout]** Tempo Limite. O Padrão '0.05'.

	> **[mode]** Modo de Comunicação. O Padrão RTU.

 A comunicação com Modbus que é um protocolo de comunicação industrial foi possível com a utilização do MinimalModbus\{MinimalModbus:2014}, que é um módulo Python para comunicação com instrumentos (escravos) a partir de um computador (mestre) usando o protocolo Modbus. Suporta o protocolo RTU e o ASCII.

 Provendo esta abstração foi desenvolvido o ModbusLink, que é um objeto de comunicação Modbus que necessita de algumas configurações específica, que são: (name, board, register e type) que corresponde respectivamente à nome do Link, objeto de comunicação ModbusLink, endereço do escravo e tipo de dado da comunicação.
 
 Um link Modbus tem a sequinte assinatura, e deve ser descrito como um \emph{provider}, quando definido a uma Tag: 

	    ModbusLink(name="LedValor",board=commModbus, register=1, type="register")

---
**{Log}**

![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/4.jpg)
Uma {Tag} é definida para ser monitorada, então a supervisão desse dado passa pelo log de dados, que é o processo de registro de eventos relevantes no sistema. A {tag} pode requerer um log constante ou a partir do momento que ela dispara um alarme. 
Um arquivo de log armazena mensagens emitidas pelo sistema, tanto durante o funcionamento quanto em falhas que eles possam vir a ter.

{Text Logger}
Registro de texto, é o armazenamento deste log em formato texto. Tem por vantagem o baixo consumo de processamento, armazenamento e a rapidez pois não depende um programa adicional para realizar esse armazenamento. 

Para criação dos registros de Log utilizou-se a interface {*logging*} do python, que oferece um completo e flexível sistema de log. 

Os logs foram configurados utilizando a classe {*TimedRotatingFileHandler*}, que suporta rotação de arquivos de log em disco em determinados intervalos de tempo. A rotação acontece com base no arquivo criado e quando passar o intervalo de tempo definido. Também é configurado a quantidade de arquivos de log criados existentes, após esse limite ultrapassado, ele sobrescreve o mais antigo, e assim por diante. 

O padrão do software é configurado como um arquivo diário e de duração de 7 dias. 

O ESSA possui três sistemas de log: 
**[Logs]**

 - [LogCreate]  		
 Gera um log contendo a configuração de todos as Tags e Adaptadores existêntes.
 
 - [LogAlarm] 
 Log fixo de Alarme. Toda e qualquer registro de alarme e ciência do mesmo, aqui fica registrado de maneira fixa
 ![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/5.jpg)
 - [LogAlarmWarning]  		
 Um registro de alarme corrente, disponível na IHM do ESSA. Quando ocorer um alarme, ele alem de ser registrado pelo {*LogAlarm*}, ele é registrado pelo {*LogAlarmWarning*}. Esse registro causa um evento na IHM que altera a propriedade do Led de status. O usuário quando clica no Led para verificar qual evento desencadeou esse alerta, recebe o registro gerado por {*LogAlarmWarning*}, que é apagado após o usuário fechar a tela que apresenta o registro.
 ![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/6.jpg)

Um Text Logger pode ser utilizado para gerar um gráfico.

---

**{Analise}**

Um  SCADA deve possuir geração de gráficos e relatórios com o histórico do processo, e esse componente existe dentro do ESSA, como um Histograma em que as Tags existentes apresentam valores de acordo com algumas caracteristicas, em que o gráfico mostre uma variação de valor nos intervalos escolhidos pelo usuário, que podem ser à cada 5, 15, 30 ou 60 minutos ou quando um valor ultrapassa a média das ultimas 4 leituras, sendo detectado como anomalía. Uma visualização do histograma de análise de dados é apresentado:  
 ![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/10.png)


**{IHM}**

IHM é a interface em que o operador visualiza as informações sobre os processos e interage com eles.
O pacote da IHM é composto por componentes gráficos e {widgets} Qt. Um widget seria a definição deste componente, como um button, slider, display, e ele é instanciado na tela {screen}, tanto o widget quanto a tela, trabalham com eventos, a IHM pode disparar ações para dispositivos externos, para a realização da atuação, por exemplo, e o widget para atualizar seu valor ou estado.

As informações que estão presentes na IHM, antes de instanciarem seu componente, quando ainda em {tags} passam pela classe {Adapter} {adaptadora) e da mesma forma, dados da IHM se comunicam com {adapter}, que então se comunica com a {tag}.

O processo intermediário do {adapter} é utilizado já que pode realizar o mapeamento das {tags}, processo em que o dado que a tag contém, pode segundo um contexto definido, assumir um valor diferente dado uma função, por exemplo, um dado de valor mínimo -20 e máximo 20 pode ter seu mapeamento para que o dado passe a trabalhar com a escala de valor mínimo zero e máximo igual a 40, ou um inteiro passar a ser um binário, isso possível realizando um mapeamento dessa {tag}.

---

**{Alarm}**

Classe que instancia um alarme vinculado a uma Tag. As propriedades a serem definidas para um alarme são:

> [Alarm] 

> **[id]** Id do alarme.

> **[tags]** Tags as quais ele será atribuído para supervisionar.

> **[type]** Tipo de alarme em relação ao valor.

> **[value]** Valor que dispara o Alarme.

> **[lifeGui]** Tempo de vida da janela de Alarme.

	

Quando definido, ele executa em razão do valor das tags a ele atribuido. Um alarme nem sempre necessita de alera quando um limite máximo é ultrapassado, pode ocorrer de um valor minimo tambem disparar uma sinalização. Pensando nisso, um alarme pode possuir estes limites:

> [Limits] 

> **[minmin]** Máximo valor mínimo que a Tag pode chegar e dispara alarme.

> **[min]** Valor mínimo, quando ultrapassar dispara Alarme.

> **[max]** Valor maximo, quando ultrapassar dispara Alarme.

> **[maxmax]** Máximo valor máximo para a tag. Dispara alarme quando ultrapassar.

	

Um alarme de minmin ou maxmax, quando ultrapassado, além do alarme pode tomar uma ação, como desativar o equipamento que a Tag supervisiona.

Quando ativo, o alarme executa um aviso sonoro, que somente é desativado quando o usuário mostrar ciencia deste alarme à partir do botão que o alerta do alarme exibe, figura \ref{figAlert}. Ao ser pressionado, ele desativa a janela, e também desativa o aviso sonoro, deixando um registro no Log de Alarme, que o usuário estáva ciente do mesmo. 

Esse registro compreende a Tag que disparou o Alarme, o tipo de alarme que foi disparado, a hora em que o Alarme foi disparado, a hora em que ele foi normalizado e registra também a hora em que o usuário visualizou esse alarme, figura \ref{figLogAlarm}. 


Caso o alarme esteja ativo e o usuário ausente, a propriedade {*lifeGui*} definida entra em ação e é ela quem define o tempo que o alerta visual ficará visível. O Alarme necessita dessa caracteristica para que um alarme não bloqueie a visualização da IHM de supervisão. Quando esse tempo é extrapolado, a tela de alerta do alarme se encerra, e o sistema registra no log que o usuário não visualizou o alarme. O alarme sonoro continua até que o alarme seja normalizado.
Tem-se dessa forma todas as informações necessárias para uma revisão e posterior identificação dos acontecimentos ocorridos desde que o alarme forá ativado, figura \ref{figLogAlarmText}. 

---
**{Scan}**

O ESSA possui as Tags que trocam informações com os componentes de comunicação. As Tags possuem um tempo definido de {Scan}, que após passado este tempo, a Tag deve consultar com o componente se o seu valor alterou desde a ultima consulta. Caso o valor tenha alterado, então a Tag atualiza seu valor e seu atributo de tempo, e então preve conforme o seu tempo de scan, quando deve ser a nova atualização.
Esse processo é executado dentro da classe {Scan}, que é uma {Thread} de varredura. Um ciclo constante que verifica para todas as Tags sua atualização.

---

**{Design}**

![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/7.jpg)
Responsável por projetar e configurar a tela, IHM do supervisório. Foi desenvolvido um template, figura \ref{figTemplate}, próprio para o desenvolvimento do SCADA dentro do Qt Designer. Este template engloba botões de menu que acessam funções internas do software e também disponibiliza um componente Led de execução, em que ao ocorrer alguma notificação, altera sua cor para que o usuário operador possa visualizar o ocorrido e ficar ciente da situação. 



A partir da criação de componentes espeficicos, como dials, thermos, led, lcd, display, button, gráfico, etc, que estão inseridos dentro do contexto do Qt Designer, figura \ref{figWidgetsDesigner}, juntamente com o template SCADA, possibilita que o usuário projete sua tela de maneira simplificada, somente selecionando Widgets, e posicionando na tela. Estes widgets contém propriedades configuráveis que foram inseridas no seu contexto de propriedade, dentor do Qt Designer, isso proporciona a totalidade da configuração dos widgets e tela unicamente nessa plataforma. Configurações como limites inferior, limite superior, passo, valor padrão, etc, são um exemplo. Com essas definições tem-se a IHM pronta. Também  estará disponível a utilização de componentes {widgets} como janela, frame, labels, imagem, campos de texto, componente escala, e demais {widgets} e componentes gráfico, atualmente disponíveis no Qt e QWT, que são bibliotecas de interface gráficas. 

A IHM de supervisão criada, deve ser salva dentro do pacote {Config} do SCADA onde o usuário programador também configura o arquivo de descrição XML. Assim que o software é executado, ele carrega ambos arquivos, compilando a tela e processando o arquivo de definição para que o software seja configurado e inicie sua supervisão.

    A após a sua correta configuração a partir da análise do XML de descrição, é carregado o {parser} {Cfg Parse/Qt Parser} que é um pedaço de código que faz a leitura do documento XML, analisa a sua estrutura e compila esse arquivo de descrição em um programa Python, tendo como resultado uma interface gráfica de supervisão, executável, que é sistema {SCADA Runtime }.

---

**{Definindo uma instância do ESSA}**

![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/8.jpg)

![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/11.jpg)
Os modulos desenvolvidos proporcionam uma ferramenta para criação de um supervisórios SCADA, de maneira simplificada frente aos principáis sistemas disponíveis no mercados, que possuem certa complexidade de programação e inaplicabilidade em hardwares de baixo consumo. O ESSA é multiplataforma, podendo ser portado de um computador para um hardware embarcado, por exemplo. O motor de supervisão já está configurado para gerar a supervisão de Tags que seram definidas pelo usuário, necessitando que o usuário defina para o sistema, qual é a tela IHM que será utilizada, e quais as Tags e Adaptadores definidos, além de configurações opcionais, como Alarme, por exemplo.
Duas etapas são necessárias para se gerar um supervisorio SCADA à partir do ESSA.

Foi desenvolvido alguns componentes visuais, widgets, próprios e alguns adaptados do Qt e QWT, comuns em supervisórios como dials, thermos, led, lcd, display, button, gráfico, etc, para serem utilizados na IHM.
Esses componentes, embutidos dentro do contexto do Qt Designer, figura \ref{figWidgetsDesigner}, juntamente com o template SCADA, possibilita que o usuário projete sua tela de maneira simplificada, somente selecionando Widgets, e posicionando na tela. Esta não é uma ferramenta definitiva de desenvolvimento IHM, é uma solução que fora concebida até o presente momento, e que satisfaz as atuais necessidades de desenvolvimento IHM.

O template definido, figura \ref{figTemplate}, próprio para o desenvolvimento do ESSA dentro do Qt Designer, engloba botões de menu que acessam funções internas do software e também disponibiliza um componente Led de execução, em que ao ocorrer alguma notificação, altera sua cor para que o usuário operador possa visualizar o ocorrido e ficar ciente da situação. 

Com a definição de uma IHM, é necessario definir no mínimo, as Tags, Adaptadores e Comunicação para que o sistema execute alguma supervisão.


Para definir essas propiedades foi utilizado o conceito de um arquivo de descrição. Esse arquivo será criado utilizando um padrão de marcação, em que cada marcador, corresponde a um elemento de configuração dentro do ESSA. Para isso, foi utilizando a linguagem de marcação XML, que possui essas caracteristicas e proporciona a criação de marcadores específicos para cada aplicação, e que após definidos, o usuário os especifica para que o ESSA possa ser configurado dinamicamente.
 
Este arquivo segue uma pequena hierarquia na sua definição.

 1. Deve-se indicar o path da instalação do software. 
 2. Deve-se indicar o path do armazenamento dos logs. 
 3. Deve-se indicar o nome do arquivo corresponde a IHM, \textit{.ui}.  
 4. Deve-se indicar o tempo para o ciclo de varredura do software.  
 5. Deve-se descrever os objetos de comunicação.  
 6. Deve-se descrever as tags do sistema.  
 7. Deve-se descrever os adaptadores.  
 8. Deve-se descrever os alarmes.

Com a completa definição desse arquivo XML,Figura \ref{figXMLESSA}, ele deve ser salvo dentra da pasta \emph{Config}, dentro do ESSA, nessa pasta também deve estar o arquivo criado com o Qt Designer da IHM, e que foi referenciado no arquivo de descrição. 

Após, o ao criar uma instância do Runtime, o usuário deve passar o nome deste arquivo, e executar o programa Python.
Assim que entra em execução, o ESSA processa este arquivo XML através do {ESSAParser}. 


Esse processamento é realizado com a utilização da API Python {ElementTree XML}. XML é um formato de dados inerentemente hierárquico, e a forma mais natural para representá-lo é com uma árvore. A API tem duas classes para essa finalidade. {ElementTree} representa o documento XML inteiro como uma árvore, e {element} representa um único nó nesta árvore. São realizadas interações com o documento inteiro, desde o nível raiz, até chegar no nível {element}, que representa os elementos descritos no XML. 

O ESSA recebe esse documento executa seu \emph{Parse}, em que os elementos descritos são reconhecidos e então o ESSAParse carrega essa configuração para a aplicação, deixando tudo pronto para a execução.

A execução do sistema depende de duas caracteristicas fundamentais. A criação da IHM de supervisão e a criação do arquivo de configuração. Este conjunto, com uma correta decrição do arquivo de configuração, proporcionam o funcionamento do ESSA.

A IHM de supervisão criada, deve ser salva dentro do pacote {Config} do SCADA onde o usuário programador também configura o arquivo de descrição XML. 

![](https://raw.githubusercontent.com/marcosscholl/essa/master/sample/9.jpg)



### Table of contents

* [ESSA](#ESSA")
-    * [Embeddable SCADA for Small Applications](#Embeddable-SCADA-for-Small-Applications")
-    * [Componentes SCADA](#Componentes-SCADA")
-      * [Tags](#Tags")
-      * [Drivers](#Drivers")
-      * [IHM](#IHM")
-      * [Alarmes](#Alarmes")
-      * [Logger](#Logger")
-      * [Scripts](#Scripts")
-    * [Pacotes](#Pacotes")
-      * [APP](#APP")
-      * [COMM](#COMM")
-      * [HMI](#HMI")
-      * [AWARE](#AWARE")
-      * [LOG](#LOG")
-  * [ESSA - Embeddable SCADA for Small Applications](#ESSA-Embeddable-SCADA-for-Small-Applications")
-    * [Runtime](#Runtime")
-    * [TAG](#TAG")
-      * [Tag de Comunicação](#Tag-de-Comunicação")
-      * [Tag Var](#Tag-Var")
-      * [Data Gen](#Data-Gen")
-    * [Propriedades de Tag](#Propriedades-de-Tag")
-    * [Propriedades de Widget](#Propriedades-de-Widget")
-    * [Adapter](#Componentes-SCADA")
-      * [Direction](#Direction")
-      * [AdapterContinuous](#AdapterContinuous")
-      * [AdapterRange:](#AdapterRange:")
-      * [AdapterDiscret:](#AdapterDiscret:")
-    * [Comunicação](#Comunicação")
-      * [ArduinoLink](#ArduinoLink")
-      * [ModbusLink](#ModbusLink")
-    * [Log](#Log")
-    * [IHM](#IHM")
-    * [Alarm](#Alarm")
-    * [Scan](#Scan")
-    * [Design](#Design")
-  * [Definindo uma instância do ESSA](#Definindo-uma-instância-do-ESSA")



[TOC]





