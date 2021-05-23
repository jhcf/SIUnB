from function import add_section
import sys
import json
# alterar o path para a pasta core do local onde o pywikibot foi instalado caso nao tenha exito em instalar ele
sys.path.append('../core')
import pywikibot as pwb
import re
from function import *

# arquivo de demonstracao de alguns usos das funcoes feitas por mim
site = pwb.Site('pt', 'wikiversity') # site onde se encontra a pagina a ser editada

page = pwb.Page(site, "Utilizador:SI2021") # substituir pelo nome da pagina que deseja criar ou editar

FILE = open("teste.json")
archive = json.load(FILE)
FILE.close()

clear_page(page)

text = page.text

text = add_section('Descrição', text,archive['groups'][1]['description'])

text = add_section('Acervo',text,'')

text = gen_table(text,archive['groups'][1]['assets'],'assets')

text = add_section('Eventos',text,'')

text = gen_table(text,archive['groups'][1]['events'],'events')

page.text = text

save_page(page)