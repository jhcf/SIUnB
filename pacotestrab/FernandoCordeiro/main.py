from manage_data import *
from manage_files import *

import pandas as pd
import io, os, sys
import json

API_KEY = "Coloque sua chave do youtube aqui"
database_path = "./db" 

def main(argv):
  if (len(argv) < 1):
    print("Faltou passar o arquvo do dataset.")
    print("Use o script assim: python3 main.py <arquivo>")
    print("Saindo...")
    return

  file = os.path.join('./', argv[0])
  yt_objects = list_yt_objects(file, API_KEY)
                                                     
  make_directory(database_path)                                             # Cria diretorio (folder) para o dataset

  df = list_data_frame(yt_objects, database_path)
  result2 = ranking_eval(df)
  
  ranked_file(result2)

if __name__ == "__main__":
    main(sys.argv[1:])



