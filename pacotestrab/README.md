# Pacotes de trabalho
Cada pasta deste diretório contém os trabalhos individualmente desenvolvidos pelos membros do projeto nos semestres 2020.1 e 2020.2, cujos nomes correspondem aos seus usernames git.

Arquivos usados para apoiar a especificação dos pacotes de trabalho estão na pasta especificacao.

Em 2020.1, os resultados iniciais dos pacotes de trabalho #2, #3, #4 e #5 foram depositados até as 10h do dia 26/11/2020.

Em 2020.2, os resultados finais dos pacotes de trabalho devem ser depositados até as 10h do dia 25/05/2021.

Segue uma especificação de cada pacote.

# Pacotes de trabalho 2020.2

Atribuição de responsabilidades individuais dos alunos e alunas pela realização dos caso e uso na arquitetura do sistema 

## 1.2020.2 - Cloud Computing
### Responsável
William

### Objetivo
Desenvolver um conjunto de instruções detalhadas sobre como fazer o uso de uma plataforma de cloud computing para gerenciar melhor o back end das aplicações desenvolvidas no âmbito dos projetos. Em suma, prova de conceito de como usar infraestrutura de cloud para apoiar o projeto.

### Caso de Uso: Cloud Computing
#### Pré-condições
Professor e turma tem dificuldades para gerenciar os back-ends desenvolvidos durante o projeto.

#### Uso dos artefatos
Estudando os artefatos desenvolvidos, professor e turma aprender a gerenciar ambiente de máquinas virtuais que dão suporte à execução do back-end das aplicações desenvolvidas.

#### Pós-condiçao
Se torna facilitada a criação de back-ends demonstrativos de como o sistema pode funcionar.

## 2.2020.2 - Calendário da Fruição Cultural
### Responsável
Lucas

### Objetivo 
Criar um gerador de calendário para o sistema.

### Caso de Uso: Calendário de Fruição Cultural

#### Pré-condições
Os usuários do sistema de fruição cultural tem dificuldades para gerenciar a grande quantidade e qualidade de eventos que vão ocorrer ao longo do calendário.

#### Uso dos artefatos (como funciona):
##### 1
O usuário informa um conjunto de parâmettros
##### 2
O sistema faz a busca no OSM (com base em parâmetors geográficos), na Wikiversity (com base em parâmetros de itens ou serviços de interesse) e na Wikidata (com base em parâmetros de classificação semântica), por eventos de potencial interesse do usuário.
#### 3
O sistema gera um output no formato https://en.wikipedia.org/wiki/ICalendar, cujos eventos podem ser importados para uma agenda pessoal, ou grupal, ou global, do usuário.

#### Pós-condições
Uma lista de eventos relevantes pode ser facilmente registrada na agenda do usuário

## 3.2020.2 - Documentação de um caso de uso do sistema
### Responsável
Ayssa

### Objetivo
Criação de uma documentação completa de um caso de uso significativo do sistema, usando o modelo proposto no capítulo 7 do livro do Schneider, em [https://www.ibm.com/developerworks/rational/library/content/legacy/parttwo/1000/0670/0670_Schneider_Ch07.pdf]

### Pré-condição
Turma não sabe como realiar uma documentação de um caso de uso, contendo os principais diagramas passíveis de uso

### Uso do artefato
#### 1
Turma estuda o artefato disponivel, qu apresenta de forma didática e exemplar, como documentar um caso de uso

### Pos-condição
Turma sabe identificar o que precisa estar presente em uma documentação de caso de uso de um sistema de informação

## 4.2020.2 - Mural Digital

### Responsável
João victor

### Objetivo
Fazer um projeto gráfico do mural digital, e um script para criar uma versão inicial do mural.

### Pré-condição
Um mural precisa ser gerado para ser exposto em uma área de grande circulação no Campus Darcy Ribeiro da UnB

### Uso do artefato

#### 1
O artefato consulta o OSM para buscar todos os itens geográficos do campus darcy ribeiro

#### 2 
O artefato identifica os eventos que vão ocorrer em data próxima ao momento em que está gerando o mural digital

#### 3
O artefato sintetiza ou apresenta a visualizaço de um mapa com indicação do que vai ocorrer no dia ou na semana, em termos de eventos culturais, ou (e) serviços. Usar o QGIS? "mão na roda".

## 5.2020.2 - Analisador de Páginas da Wikiversity

### Responsável
Breno

### Objetivo
#### Original
Criar um conjunto de funções / scripts na linguagem python que recebe o texto html de uma página na wikiversity que contenha os elementos semânticos definidos na arquitetura do Sistema de Fruição Cultural, para os grupos vinculados a essa página.
#### Aprimorado
Criar um conjunto de funções / scripts na linguagem python que recebe uma lista de nomes de páginas a wikiversity que contenha os elementos semânticos definidos na arquitetura do Sistema de Fruição Cultural para os grupos vinculados a essa página, e que gera uma representação sintética do conteúdo desses grupos, em um formato JSON.

### Pré-condições
Existe um conjunto de grupos cadastrados em páginas na Wikiversity em português, cada página com o seu próprio nome.

### Uso do artefato

# 1
Os nomes das páginas referentes aos grupos são informados em uma lista de entrada

# 2
Os textos das páginas informadas são recuperados 

# 3
É analisada a completude (e possivelmente a consistência) dos dados obtidos, tais como:
* descrição do grupo promovtor de ações culturais
* presença, consistência e completude de dados sobre eventos promovidos pelo grupo
* presença, consistência e completude de dados sobre serviços promovidos pelo grupo
* presença, consistência e completude de dados sobre itens de acervo mantidos pelo grupo

# 4
O artefato retorna um json contendo todo o resultado da análise, da tipagem de dados, de forma a facilitar a análise de informações sobre o que o(s) grupo(s) está(ão) ofertando.

### Pós-condições
A análise e apresentação das informações sobre os grupos fica bem fácil de ser trabalhada de forma algoritmica, de modo que o scripr pode ser facilmente incorporado a um back-end ou front-end de aplicação.

## 6.2020.2 - App Android Front-end para Fruição Cultural

### Responsável
Pedro

### Objetivo 
Desenvolver um app para android, usando qualquer tecnologia, que seja capaz de ler um qrcode referente a um objeto no OSM, e recuperar os dados de fruição cultural vinculados a esse objeto OSM.

### Pré-condições
O usuário dispõe de um smartphone que tem instalado o app

### Passos de uso
#### 1
O usuário aciona o app e lê um QRCode

#### 2
Caso o QRCode seja relativo ao OSM, recupera o objeto OSM

#### 3
Verifica se existe um tag para a wikiversity nesse objeto OSM

##### 3.1
Se existir, recupera as informações relacionadas com as ações e itens de interesse cultural (Obtendo um json, que vai ser gerado pelo trabalho do Breno. usar uns json padronizados - exemplos feitos a mãO.

#### 4
Apresenta na interface com o usuário a lista dos eventos, serviços e itens disponíveis vinculados a um ou mais grupos que atuam junto àquele objeto OSM.

#### 5
Se o usuário clicar em um item dessa lista, são apresenatdos os detalhes do registro.

### Pós-condições
O usuário obtém maio informação sobre eventos que ocorre naquele local geográfico

## 7.2020.2 - Rede Semântica

### Responsável
Rafael

### Objetivo
Dada uma lista de páginas de grupos na wikiversity, ou uma lista de objetos no OSM que contém links para a Wikidata, gerar uma representação da rede semântica usando a integração com gephi, ou com outro software de visualização de grafos. Fazer uma app web que produza o resultado. Referência para analisar: https://gist.github.com/UncleCJ/2408aef8eab09cc1da3404c5af43537b

### Passos
# 1
O artefato recebe um JSON contendoas informações sobre grupos de promoção da fruição cultural 
# 2
Alternativas de impelemtação
# 2.1 Alternativa 1
O artefato gera um png com o grafo dos objetos semânticos Wikidata vinculados ao JSON obtido.
# 2.2 Alternativa 2 (caso viável)
Apresentar uma interface web para navegação no grafo dos objetos semânticos Wikidata vinculados ao JSON obtido. Preferivelmente, a interface apresenta links para navegação, que apontam para os registros na wikidata.

## 8.2020.2 - Create, Update, Delete para Informações sobre grupos na Wikiversidade

### Responsável
Yuri

### Objetivo
Estudar a api wikimedia (https://www.mediawiki.org/wiki/API:Main_page) e criar um módulo de back end ou front-end para edição user-friendly de grupo e membros de grupo na Wikiversity, permitindo com facilidade, que os usuários possam definir descriçes de grupos, serviços, eventos e itens de acervo mantidos pelo grupo, bem como os seus usuários. As informações editadas seriam registradas nas correspondentes páginas do grupos na wikiversity.

### Produtos
1. protótiṕo / wireframe do módulo de gerenciamento de grupos
2. implementação em python das fuções de gerenciamento (interface em json)

### Pré-condições
Os usuários do sistema que querem registrar informações sobre grupos, eventos, serviços e acervos tem que editar manualmente as informações na Wikiversity, o que torna o processo bastante sujeito a erros. Eles sentem falta de uma interface amigável e estruturada para entrada de dados, fazendo a criação de grupos, e a atualização ou remoção de uma ou mais informações.

### Passos
#### 1
Usuário informa o grupo que quer editar ou criar

#### 2
Usuário insere ou edita informações sobre o grupo, usando uma interface mais amigável e menos sujeita a erros, mesmo que seja em uma linha de comando

#### 3
As informações são atualizadas na correspondente página da Wikiversidade

### Pós-condições
A qualidade dos dados sobre grupos mantidas na wikiversidade fica mais controlada, enquanto permitindo que o usuário continue a fazer a edição manual das páginas na wiki, caso queira fazer ajustes mais detalhados.



# Pacotes de trabalho 2020.1

# 1.2020.1 - PACOTE TRAB #1 - MEMBRO M1 DO PROJETO - GUIA DO USUÁRIO

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

# 2.2020.1 - PACOTE TRAB #2 - MEMBRO M2 DO PROJETO

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
 
# 4.2020.1 - PACOTE TRAB #4 - MEMBRO M4 DO PROJETO
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

# 5.2020.1 PACOTE TRAB #5 - MEMBRO M6 DO PROJETO 
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


# 3.2020.1 - PACOTE TRAB #6 - UC5-Twitter - MEMBRO M6 DO PROJETO
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
