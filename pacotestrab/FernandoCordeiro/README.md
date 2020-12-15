## PACOTE TRAB #5 - MEMBRO M6 DO PROJETO

Aqui temos a integração do script4_linha, que envolve mineração de texto e ranqueamento de dados, junto a parte do script2_linha que recupera dados do youtube.

1. **dataset**: Um conjunto de dados que guarda a url de vídeos relacionados ao evento da fruição cultural (youtube_url_data.txt).

2. **main**: Acessa o youtube atráves de uma api-key para recuperar os dados dos ids passados no dataset.

3. **Script de dados**: Um script que automatiza a geração da estrutura dos dados recuperados do youtube, e realiza seu ranquemanto de relevância para o usúario.

4. **Script de arquivos**: Um script que coordena a leitura de arquivos e a criação dos mesmo de forma automatizada.


### Adquirir a api-key de acesso ao youtube
-> Acessar o site https://console.cloud.google.com

-> Entrar com a conta google

-> Clicar na Aba APIs & Servicos

-> Criar um novo projeto

-> Selecionar um projeto

-> "Ir para visão geral de APIs"

-> Ativar APIS e Servicos

-> Pesquisar "Youtube data API v3"

-> ativar a api pesquisada acima

-> um codigo sera mostrado, copie e cole no arquivo main da pasta: danielc-957 e o arquivo estará pronto para uso


### Dependências e Bibliotecas 
-> Sistema: Python3, versão 3.9 para cima

-> Blibiotecas Python: 
    `pandas`
    `scikit-learn`
    `json`


### Executando o programa
**Lembre de adicionar sua api-key na `main.py`**

O script **main.py** pode ser executado através por meio de um terminal da seguinte forma: `python3 main.py`.
