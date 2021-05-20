from function import add_section
import sys
import json
# alterar o path para a pasta core do local onde o pywikibot foi instalado caso nao tenha exito em instalar ele
sys.path.append('../core')
import pywikibot as pwb
import re
from function import *
site = pwb.Site('pt', 'wikiversity')
page = pwb.Page(site, "Utilizador:SI2021")

FILE = open("teste.json")
archive = json.load(FILE)
FILE.close()
print(archive['groups'][1]['events'])
clear_page(page)
text = add_section('Descrição', archive['groups'][1]['description'])
text += add_section('Acervo','',text)
text = gen_table(text,archive['groups'][1]['assets'],'assets')
text += add_section('Eventos','',text)
text = gen_table(text,archive['groups'][1]['events'],'events')
page.text = text
page.save()
