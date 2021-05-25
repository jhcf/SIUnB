Essa aplicação pega os eventos contidos em um .Json as converte em Events() e os adicionam a um calendário criando um arquivo de saída .ics (formato de calendário compatível com Google Calendar/Agenda e Windows Calendar).

Para executar são necessárias as bibliotecas ics e pandas:

pip install ics

pip install pandas

Além disso é necessário um .json com o formato compatível, Eventos.json é o arquivo usado como exemplo.

O código opera chamando a função Json_to_Eventos que abre o arquivo, pega as suas informações e as coloca como eventos, para depois colocar no calendário e exportar para .ics.

O programa aceita dois tipos de eventos, o tipo 1, onde o evento acontece em apenas um dia, e o tipo dois onde o evento acontece em mais que um dia, com o diferencial sendo a criação de mais eventos no calendário.

