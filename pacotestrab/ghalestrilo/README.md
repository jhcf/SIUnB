## Entregável 4 - Dataset e Script de Integração e Front-End

Os principais entregáveis presentes nessa pasta, conforme especificado no trabalho, são:

1. **Dataset**: Um Dataset composto de 3 arquivos txt base foi disponibilizado na pasta `dataset`. Junto a ele, 3 wordclouds base se encontram na pasta `img`, onde são depositados aqueles connstruídos dinamicamente

2. **Script**: Um script que automatiza a geração de um wordcloud a partir do conteúdo textual dos comentários do vídeo.

3. **Script de Front-End**: Um script que recebe um ID de um vídeo e retorna ao usuário o wordcloud gerado a partir de seus comentários, além de abrir no youtube o vídeo solicitado.

### Executando o programa

O script **wordcloud.sh** pode ser executado através de um terminal com uso da seguinte sintaxe: `./wordcloud.sh <id_do_video>`. Opcionalmente, um argumento (flag) extra pode ser passado: `./wordcloud.sh <id_do_video> -force`. Aqui, o `<id_do_vídeo>` é um identificador válido para um vídeo hospedado no youtube. Caso contrário, o script não gerará um resultado coerente.

Por padrão, caso o vídeo solicitado já tenha sido processado, o script apenas apresenta os resultados já obtidos (caching). O uso do argumento `-force` sobrepõe esse comportamento, forçando o reprocessamento da wordcloud.