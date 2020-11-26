O pacote Script1.py é composto por 4 funções que podem ser úteis para futuras implementações:

 - rank_names
 - request_wikidata
 - get_events
 - get_location


|Função                |Comportamento                          
|----------------|-------------------------------|
|get_location| Recebe uma String com termos de busca.<br> Retorna o código da location (Q102104636) com o nome mais próximo aos termos de busca.
|get_events|Recebe a location (Q102104636).<br> Retorna o JSON com todos os eventos vinculados à location.
|request_wikidata| Recebe uma query em formato SPARQL.<br> Retorna o JSON gerado pela query.          
|rank_names| Recebe a String de busca e o dicionário contendo os códigos das localizações.<br> Retorna o código da localização mais parecida com a busca.


Exemplos:
```mermaid
get_location("teatro a") #Retorna Q47189015 (Teatro Apolo)
get_location("teatro aca") #Retorna Q66942004 (Conjunto dos edifícios da Associação Académica de Coimbra, Teatro Académico de Gil Vicente e Cantinas)

get_events("Q102104636") #Retorna os eventos relacionados ao Q102104636 em formato JSON
```
O Script.py usa as 2 funções aninhadas:

```mermaid
location = get_location("teatro de arena") 

get_events(location)
```