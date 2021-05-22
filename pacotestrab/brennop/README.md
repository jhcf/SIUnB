# 5.2020.2 - Analisador de Páginas da Wikiversity

## Responsável
Brenno

## Objetivo
### Original
Criar um conjunto de funções / scripts na linguagem python que recebe o texto html de uma página na wikiversity que contenha os elementos semânticos definidos na arquitetura do Sistema de Fruição Cultural, para os grupos vinculados a essa página.
### Aprimorado
Criar um conjunto de funções / scripts na linguagem python que recebe uma lista de nomes de páginas a wikiversity que contenha os elementos semânticos definidos na arquitetura do Sistema de Fruição Cultural para os grupos vinculados a essa página, e que gera uma representação sintética do conteúdo desses grupos, em um formato JSON.

## Pré-condições
Existe um conjunto de grupos cadastrados em páginas na Wikiversity em português, cada página com o seu próprio nome.

## Uso do artefato

1. Os nomes das páginas referentes aos grupos são informados em uma lista de entrada
2. Os textos das páginas informadas são recuperados 

3. É analisada a completude (e possivelmente a consistência) dos dados obtidos, tais como:
  * descrição do grupo promovtor de ações culturais
  * presença, consistência e completude de dados sobre eventos promovidos pelo grupo
  * presença, consistência e completude de dados sobre serviços promovidos pelo grupo
  * presença, consistência e completude de dados sobre itens de acervo mantidos pelo grupo

4. O artefato retorna um json contendo todo o resultado da análise, da tipagem de dados, de forma a facilitar a análise de informações sobre o que o(s) grupo(s) está(ão) ofertando.

## Pós-condições
A análise e apresentação das informações sobre os grupos fica bem fácil de ser trabalhada de forma algoritmica, de modo que o scripr pode ser facilmente incorporado a um back-end ou front-end de aplicação.

## Utilização

Clone o projeto e certifique-se que o flask está instalado.

```
pip install flask
```

Para rodar o projeto.

```
FLASK_APP=main flask run
```

O servidor estará rodando na porta 5000. O artefato aceita uma lista de grupos
da Wikiversity, separados por vírgula, como valor do parâmetro `groups`.

**Exemplo:** http://localhost:5000/?groups=Grupo_Explorat%C3%B3rio_Fict%C3%ADcio_de_Poesia_%C3%A0_Sombra_da_%C3%81rvore_Torta,Sistemas_de_Informa%C3%A7%C3%A3o_Territoriais
