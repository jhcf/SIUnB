import io
import os
import sys
from wordcloud import WordCloud

def main(file_in):
    return

def main(argv):
    if (len(argv) < 1):
        print("Faltou o id do video na chamada do script.")
        print("Use o script assim: python3 Script3.py <id_do_video>, onde id do vídeo = seu identificador, como descrito na documentacao")
        print("Saindo...")
        return
    video_id = argv[0]
    file_in = f'dataset/{video_id}.txt'
    file_out = f'img/{video_id}.png'
    wordcloud = WordCloud(stopwords=["anos atrás"])
    with open(file_in) as video_data:
        wordcloud.generate(video_data.read())
    video_data.close()
    wordcloud.to_file(file_out)
    
    

if __name__ == "__main__":
    main(sys.argv[1:])