import sys
import json
sys.path.append('../core')
import pywikibot as pwb
import re


def clear_page(page):
    page.text = ""
    page.save()

def add_section(section,text,add=''):
    text += '\n=='+section+'==\n'
    text += add
    return text
    


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

