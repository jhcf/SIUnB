import sys
import json
sys.path.append('../core')
import pywikibot as pwb
import re


def clear_page(page):  #essa funcao limpa o texto da pagina e salva ela e salva com a flag de bot ativada, ela recebe apenas a pagina recuperada pelo bot
    page.text = ""
    save_page(page)

def save_page(page): # essa funcao salva a pagin com a flag de bot ativada, ela recebe a pagina recuperada pelo bot
    page.save(botflag=True)
#essa funcao adiciona uma nova secao com um texto abaixo
#os parametros sao
#section = nome da secao a ser adicionada
#text = o texto da pagina a ser alterada
#add = o texto a ser adicionado, nulo por padrao
#o retorno dela e o texto alterado
def add_section(section,text,add=''): 
    text += '\n=='+section+'==\n'
    text += add
    return text

#essa funcao recebe uma lista de items, qual sera o sufixo e prefixo de cada item junto a uma flag dizendo se isso se encontra na ultima coluna da tabela
#o retorno dela e essa lista no formato de uma coluna da tabela
def list_items(items, prefix='', sufix='',last=False):
    aux = ""
    if len(items) == 0:
        if not last:
            aux = '||'
    elif len(items) == 1:
        if last:
            for i in items:
                aux += prefix+i+sufix
        else:
            for i in items:
                aux += prefix+i+sufix+'||'
    else:
        if(type(items) != str):
            for i in items:
                aux += prefix+i+sufix+'<br>'
            if not last:
                aux+= '||'
        else:
            if last:
                for i in items:
                    aux += prefix+i+sufix
            else:
                for i in items:
                    aux += prefix+i+sufix
                aux+='||'
    return aux
#essa funcao recebe uma tabela e um json de uma secao a ser convertida para tabela e retorna a tabela dessa secao
#exemplo json['groups'][x]['assets'] retornaria a tabela dos acervos
def gen_table(text,json,caption):
    text += '\n{|class ="wikitable"\n'
    if caption == 'assets':
        text += '|+ Acervo\n'
        text+= '!Nome!!Descrição!!Categorias!!Condições de Uso!!OSM!!Wikidata!!Wikipedia!!Facebook!!Instagram!!Twitter!!Youtube!!Teams!!Stream\n'
    elif caption == 'events':
        text += '|+ Eventos\n'
        text+= '! Nome!!Descrição!!Categorias!!Condições de Uso!!Horários!!OSM!!Wikidata!!Wikipedia!!Facebook!!Instagram!!Twitter!!Youtube!!Teams!!Stream\n'

    text+= '|-\n'
    for i in json:
        if caption == 'assets':
            text+= '!'+i['name']+'\n'
            text+='|'+i['description']+'||'
            text+= list_items(i['category'])
            text+= list_items(i['usage'])
            text+= list_items(i['osm'],'[',']')
            text+= list_items(i['wikidata'],'[',']')
            text+= list_items(i['wikipedia'],'[',']')
            text+= list_items(i['facebook'],'[',']')
            text+= list_items(i['instagram'],'[',']')
            text+= list_items(i['twitter'],'[',']')
            text+= list_items(i['youtube'],'[',']')
            text+= list_items(i['teams'],'[',']')
            text+= list_items(i['stream'],'[',']',True)
            text+='\n'
        elif caption == 'events':
            text+= '!'+i['name']+'\n'
            text+='|'+i['description']+'||'
            text+= list_items(i['category'])
            text+= list_items(i['usage'])
            text+= list_items(i['timeInterval'])
            text+= list_items(i['osm'],'[',']')
            text+= list_items(i['wikidata'],'[',']')
            text+= list_items(i['wikipedia'],'[',']')
            text+= list_items(i['facebook'],'[',']')
            text+= list_items(i['instagram'],'[',']')
            text+= list_items(i['twitter'],'[',']')
            text+= list_items(i['youtube'],'[',']')
            text+= list_items(i['teams'],'[',']')
            text+= list_items(i['stream'],'[',']',True)
            text+='\n'
    text+='|}'
    return text

