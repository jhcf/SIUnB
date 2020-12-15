import io, os, sys
import json

def make_directory(dir_name):
    folder = dir_name

    try:
        os.mkdir(folder)
    except OSError:
        print ("Criação do diretório %s falhou, é possivel que o diretório já exista" % folder)
    else:
        print ("Sucesso na criação do diretório %s " % folder)


def write_json(path, video, comments):
  with open(path, 'w', encoding='utf-8') as f:
    json.dump({'video_information':video, 'comments_information':comments}, f, ensure_ascii=False, indent=4)

def write_txt(file):
  with open('youtube_info.txt', 'w') as filehandle:
    for listitem in file:
      filehandle.write('%s\n' % listitem)

def ranked_file(ranked_df):
    parent_path = './'
    filename = "/ranqueado.txt"
    
    path = parent_path + filename

    f = open(path,"w+")
    f.write("Local: Teatro de Arena da UnB\nEventos Passados:\r\n")

    for num, df in enumerate(ranked_df.iterrows(), start=1):
        f.write("#%d -  %.2f nível de ranqueamento (0 a 1)  %s\r\n" % (num, df[1][0], df[1][1]))

    f.close()
    print ("Arquivo de ranqueamento criado.\n\n")