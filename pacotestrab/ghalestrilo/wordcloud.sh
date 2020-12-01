#!/bin/bash

# Front-end para o Sistema
# Uso: ./wordcloud.sh <id_do_vídeo> [-force (opcional)]
# O <id_do_vídeo> é um identificador válido para um vídeo hospedado no youtube
# O uso do argumento "-force" faz com que

# Leitura de Argumentos de Linha de Comando
for var in "$@"; do
  # Recuperação do ID do vídeo (variável de ambiente VID)
  [[ $var = -* ]] && echo "argumento: ${var}" || VID="${var}"

  # Forcing: Caso solicitado, força-se o reprocessamento dos dados
  [[ $var = "-force" ]] && FORCE=true
done

WORDCLOUD_FILE="img/${VID}.png"
DATASET_FILE="dataset/${VID}.txt"

[[ ${FORCE} = true ]] && rm ${WORDCLOUD_FILE} ${DATASET_FILE}

# Caching: Verificar se já existem imagem e dataset
if [ ! -e ${WORDCLOUD_FILE} ]; then
  if [ ! -e ${DATASET_FILE} ]; then
    python3 baixarComentarios.py --youtubeid "$VID" --output "dataset/${VID}.json";
    python3 decodificarComentarios.py ${VID};
  fi
  python3 Script3.py ${VID}
fi

# Adaptar este comando para execução em ambiente Microsoft Windows
xdg-open ${WORDCLOUD_FILE}
xdg-open "https://youtube.com/watch?v=${VID}"