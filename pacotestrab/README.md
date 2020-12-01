# Pacotes de trabalho
Cada pasta contém os trabalhos individualmente desenvolvidos pelos membros do projeto, cujos nomes correspondem aos seus usernames git.

Arquivos usados para apoiar a especificação dos pacotes de trabalho estão na pasta especificacao.

Os resultados iniciais dos pacotes de trabalho #2, #3, #4 e #5 devem ser depositados até as 10h do dia 26/11.

Segue uma especificação de cada pacote.

# 1 - PACOTE TRAB #1 - MEMBRO M1 DO PROJETO - GUIA DO USUÁRIO

# Responsável
O membro M1 é o aluno Ricardo Silva Moreira.

## Casos de uso a realizar
O pacote de trabalho #1 visa desenvolver os artefatos que apoiam o usuário na realização dos seguintes casos de uso:
### UC1
Usuário responsável por um espaço cultural cria e mantém na Wikidata um registro uma edificação ou espaço físico de interesse cultural  
### UC2
Usuário responsável por um espaço cultural cria o registro geo da edificação no OpenStreetMap e o vincula ao registro da edificação na Wikidata
### UC3
Usuário responsável por um evento cria ou atualiza o registro do evento da Wikidata, e o vincula a uma edificação cultural registrada na Wikidata
### UC7
Usuário de uma mídia social faz registros de comentários sobre um evento no facebook, youtube etc, que podem ser usados para promover a visibilidade e avaliação do evento

## Entregáveis
O membro M1 do projeto não desenvolverá programas de computadores.
Ele produzirá um Guia do Usuário, formado por um conjunto de artefatos na forma de documentos com texto, gráficos e imagens.
Podem ser desenvolvidos documentos em texto e em vídeo. 

Deve-ser considerado que o usuário dos casos de uso UC1, UC2, UC3, e UC7 é alguém que tem conhecimentos básicos de computação, 
e que precisa usar minimanente o OpenStreetMap e o Wikidata para fazer os registros necessários à promoção da fruição cultural.

É recomendado orientar o usuário sobre
OpenStreetMap: https://wiki.openstreetmap.org/wiki/Pt-br:Beginners%27_guide
Wikidata: 

## Formato da entrega
Para a produção do texto, deve-ser usar o editor de texto LaTeX, usando o repositório de documento LaTeX sincronizado com o Overleaf em 
https://github.com/jhcf/SIUnB.2020.1.TA-Relatorio

Para a produção de vídeos, deve-se colocar os mesmos disponíveis no youtube, informando o link dos mesmos no documento texto Guia do Usuário

## Avaliação inicial feita pelo professor
### UC3
O conteúdo do guia sobre o UC 3 é crítico para o sucesso do projeto, e deve ser feito com a maior brevidade.

### Demais casos de uso
Os demais casos de uso ainda não descritos (UC4/UC9, UC5/UC8, UC6, e UC5-Twitter) deve ser citados no guia do usuário.

### Apresentação inicial do sistema
Uma apresentação inicial do sistema deve ser feita antes da apresentação dos casos de uso específicos. Tomar como base o que já se encontra no Protótipo_v4.pdf. 

### Conceitos e justificativa para o sistema
Devem ser feitos no documento de relato do projeto

# 2 - PACOTE TRAB #2 - MEMBRO M2 DO PROJETO

# Responsável
M2 é Mateus Luiz Oliveira.

## Descrição
O pacote de trabalho #2 visa desenvolver o SCRIPT 1 para realizar o UC4.

### UC4 
Usuário final do sistema usa o front-end para buscar uma lista de eventos relacionados a uma edificação ou organização no sistema de fruição cultural, que apresenta o resultado da busca numa interface (textual ou gráfica), listando o conjunto dos eventos ocorridos ou ocorrer na edificação ou próximos a ela, (possívelmente ranqueados, ver UC9)

## Experiência e interface com o usuário
Ver detalhamento do documento Prototipo_v4.pdf ou Prototipo_v4.odp, disponível no Overleaf.

## Entregáveis
### Script1.py

## Formato da entrega
Script em python3.9 que recebe como entrada um nome de edificação e retorna a lista sequencialmente numerada de eventos ocorridos ou a ocorrer na edificação, conforme os registros disponíveis no OpenStreetMap e Wikidata.

# 3 - PACOTE TRAB #3 - MEMBRO M3M5 DO PROJETO
# Responsável
M3M5 é Daniel Carvalho Moreira.

## Descrição
O pacote de trabalho #2 visa desenvolver o SCRIPT 2 para realizar o UC5
### UC5 
Usuário final usa o front-end, informa o nome da a edificação ou organização anteriormente usado no UC4, e acrescenta na busca o número sequencial do evento específico no qual tem interesse, por exemplo, o 5o evento da lista retornado no UC4. 
O front-end apresenta na interface textual (adicionamente uma janela gráfica) com o detalhamento dos dados do evento específico solicitado, inclusive URLs para mídias sociais que contenham maior descrição do evento, se for o caso.
Adicionalmente, é apresentada uma síntese dos comentários registrados na mídia social relativos ao evento, conforme detalha o UC8.

## Experiência e interface com o usuário
Ver detalhamento do documento Prototipo_v4.pdf ou Prototipo_v4.odp, disponível no Overleaf.

## Entregáveis
### Script2_linha.py
Script que recebe como entrada uma URL de vídeo, faz acesso à API do Youtube, retorna um string com 4+n*3 linhas, contendo a síntese dos n feedbacks recebidos sobre o vídeo, conforme o modelo a seguir descrito, composto pelas seguintes linhas, gerando um dataset a ser gravado no disco em um arquivo com nome no formato: <identificador-do-video>.txt, por exemplo: R-1ndCVLCLk.txt. Veja exemplo de arquivo incompleto em [especificacao/ExemploDataset/R-1ndCVLCLk.txt](especificacao/ExemploDataset/R-1ndCVLCLk.txt).

#### Estrutura de um dataset de um vídeo
```
<Linha 1> ::= url do vídeo
<Linha 2> ::= "views "+Quantidade de visualizações do vídeo
<Linha 3> ::= "likes "+Quantidade de likes para o vídeo
<Linha 4> ::= "dislines "+Quantidade de dislikes para o vídeo
<Linha 5+n*3> ::= Nome do usuário que realizou o n-ésimo comentário mais recente
<Linha 5+n*3+1> ::= Texto descritivo do tempo decorrido desde que o n-ésimo comentário mais recente foi realizado
<Linha 5+n*3+2> ::= Texto do n-ésimo comentário mais recente
```

#### Exemplo de um dataset de um vídeo
```
http://www.youtube.com/watch?v=R-1ndCVLCLk
views 3.000
likes 200
dislikes 10
Gustavo Dutra
3 semanas atrás
Esse show. Esse dia. O homem é a música. Quanto às paradas do Racionais, da hora.
Eleakim Silva
3 semanas atrás
O monstro do RAP NACIONAL! Mano Brown.
João Carlos
3 semanas atrás
Fera demais!!!
Eleakim Silva
3 semanas atrás
Faltou fazer mais perguntas, mas tá show
```

### Script2.py
Integração entre o Script1.py e Script2_linha.py, que realiza o UC5 

## Formato da entrega
Script em python3.9
 
# 4 - PACOTE TRAB #4 - MEMBRO M4 DO PROJETO
# Responsável
M4 é Thales Grilo

# Descrição
O pacote de trabalho #4 visa desenvolver o Script3.py, que realiza o UC6
## UC6 
Usuário final usa o front-end para obter detalhamento de um dos eventos que ocorreu ou vai ocorrer vinculado a uma edificação de interesse cultural, e apresenta uma síntese dos comentários de feedback relacionados a esse evento na forma de uma nuvem de palavras, gerada a partir do texto dos comentários feitos nas mídias sociais, e aciona automaticamente um dos links da lista de links relativa ao evento numa mídia social, como o youtube, de modo que o navegador do usuário é direcionado para a página do evento na mídia social.

## Experiência e interface com o usuário
Ver detalhamento do documento Prototipo_v4.pdf ou Prototipo_v4.odp, disponível no Overleaf.

## Entregáveis
### 3 Datasets exemplos
Gerar três arquivos com datasets reais, para testar o gerador de wordcloud, produzidos a partir de vídeos reais no youtube, conforme a estrutura de dataset descrita no pacote de trabalho #3. Os nomes dos arquivos devem ser <identificador-do-video>.txt, por exemplo: R-1ndCVLCLk.txt.

### Script3_linha.py
Script que recebe um identificador de um vídeo, por exemplo, "R-1ndCVLCLk", e apresenta uma janela pop-up com a nuvem de palavras relativas aos comentários de um vídeo específico, a partir da leitura de um dos três datasets gerados, e dispara o navegador do usuário para visitar esse vídeo no youtube, por exemplo: http://www.youtube.com/watch?v=R-1ndCVLCLk.

### Script3.py
Integração entre o Script2.py e o Script3_linha.py.

# 5 PACOTE TRAB #5 - MEMBRO M6 DO PROJETO 
#Responsável
M6 é Fernado Cordeiro

# Descrição
O pacote de trabalho #5 visa desenvolver o Script4.py, que realiza o UC9

## UC9
Usuário final usa o front-end para obter uma listagem dos eventos que irão ocorrer ou ocorreram vinculado a uma edificação de interesse cultural, conforme o UC4. Adicionalmente, as listas dos eventos, agrupados nas três distintas categorias, são ranqueadas conforme um algoritmo de ranqueamento desenvolvido a partir da análise dos feedbacks recebidos para cada evento, conforme esses feedbacks são recuperados a partir da API do youtube. Existem várias formas de ranqueamento, sendo a mais simples delas o ranqueamento pela quantidade de comentários recebidos. Devem ser exploradas pelo menos duas formas de ranqueamento.

## Experiência e interface com o usuário
Ver detalhamento do documento Prototipo_v4.pdf ou Prototipo_v4.odp, disponível no Overleaf.

## Entregáveis
### Script4_linha.py
Recebe um nome de diretório contendo um conjunto de datasets sumários de eventos e os processa gerando um raqueamento, sejam os datasets gerados manualmente no pacote de trabalho #4, sejam os datasets gerados automaticamente pelo Script2_linha.py, no pacote de trabalho #3.

### Script4.py
Resultado da integração entre os scripts Script4_linha.py, Script1.py e Script2_linha.py, para produzir uma saída análoga à gerada no UC4, só que ranqueada conforme o modelo de ranqueamento criado.

### Orientações
No início, usar os três datasets desenvolvidos no pacote de trabalho #4 para testar as distintas formas de ranqueamento (pelo menos duas).
Avaliar o uso de técnicas de text mining.


# 3 - PACOTE TRAB #6 - UC5-Twitter - MEMBRO M6 DO PROJETO
# Responsável
M6 é Mikael Melo.

## Descrição
O pacote de trabalho #6 visa desenvolver o SCRIPT 5 para realizar uma modificação do UC5, onde o twitter é a fonte de informação dos comentários sobre o evento

### UC5-Twitter
Usuário final usa o front-end, informa o nome da edificação ou organização anteriormente usada no UC4, e acrescenta na busca o número sequencial do evento específico no qual tem interesse, por exemplo, o 5o evento da lista retornado no UC4. 
O front-end apresenta na interface textual (adicionamente uma janela gráfica) um detalhamento dos dados do evento específico solicitado, inclusive URLs para mídias sociais que contenham maior descrição do evento, se for o caso.
Se entre as URLs do evento, existe uma vinculada ao twitter, então é apresentada uma síntese dos comentários registrados na mídia social Twitter, relativos ao evento, conforme detalha o UC8.

## Experiência e interface com o usuário
Ver detalhamento do documento Prototipo_v4.pdf ou Prototipo_v4.odp, disponível no Overleaf.

## Entregáveis
### Script5_linha.py
Script que recebe como entrada uma URL de um tweet ou de um usuário, faz acesso à API do Youtube, retorna:
* caso a url seja de um usuário, uma lista dos textos dos tweets mais recentes desse usuário (tweets da última semana);
* caso a url seja de um tweet, uma lista dos textos de todos os comentários feitos sobre esse tweet;
Usando essa lista de textos, o script deve apresentar numa janela pop-up uma nuvem de palavras sintetizando os textos, bem como no console deve ser apresentada a lista dos textos correspondentes, usados na produção da novem.

### Script5.py
Integração entre o Script1.py e Script5_linha.py, que realiza o UC5-Twitter 

## Formato da entrega
Script em python3.9
