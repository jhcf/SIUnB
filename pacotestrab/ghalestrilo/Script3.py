import io
import os
import re
import sys
from collections import Counter

from wordcloud import WordCloud

def skipline(line):
    return line.startswith('http') \
        or line.startswith('views ') \
        or line.startswith('likes ') \
        or line.startswith('dislikes ') \
        or line.endswith(' atrás')

def sort_by_frequency(words):
    print(Counter(words).most_common())
    return [word for (word, freq) in Counter(words).most_common()]


def filtrar(filename):
    with open(filename) as video_data:
        text = video_data.read()
    video_data.close()
    lines = re.split('\n', text)
    lines = [line for line in lines if not skipline(line)]
    text = " ".join(lines)
    text = re.split(' ', text)
    text = sort_by_frequency(text)
    text = "\n".join(text)
    # print(text)
    return text

def main(argv):
    if (len(argv) < 1):
        print("Faltou o id do video na chamada do script.")
        print("Use o script assim: python3 Script3.py <id_do_video>, onde id do vídeo = seu identificador, como descrito na documentacao")
        print("Saindo...")
        return
    video_id = argv[0]
    file_in = f'dataset/{video_id}.txt'
    file_out = f'img/{video_id}.png'
    wordcloud = WordCloud(stopwords=["", "A", "O", "a", "o"])
    texto = filtrar(file_in)
    wordcloud.generate(texto)
    wordcloud.to_file(file_out)
    
    

if __name__ == "__main__":
    main(sys.argv[1:])