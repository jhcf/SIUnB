from ics import Calendar, Event
import pandas


def Json_to_Eventos():#abre o json e pega seus eventos, depois os coloca no .ics
    c = Calendar()
    data = pandas.read_json('Eventos.json')
    for evento in data['eventos']:
        nome = (evento['nome'])
        categoria = (evento['categoria'])
        description = (evento['description'])
        tipo = (evento['tipo'])
        dias = (evento['dias'])
        horas = (evento['horas'])
        osm = (evento['osm'])
        wikidata = (evento['wikidata'])
        wikipedia = (evento['wikipedia'])
        facebook = (evento['facebook'])
        instagram = (evento['instagram'])
        twitter = (evento['twitter'])
        youtube = (evento['youtube'])
        teams = (evento['teams'])
        stream = (evento['stream'])
        DefEv(nome, categoria, description, tipo, dias, horas, osm, wikidata, wikipedia, facebook, instagram, twitter, youtube, teams, stream, c)
    with open('calendario.ics', 'w') as my_file:
         my_file.writelines(c)
    

#Define e adiciona o evento no calendario dependendo do tipo
def DefEv (nome, categoria, description, tipo, dias, horas, osm, wikidata, wikipedia, facebook, instagram, twitter, youtube, teams, stream, c):
    if  tipo == "1": #quando o evento só acontece em um dia
        DefEv1(nome, categoria, description, tipo, dias, horas, osm, wikidata, wikipedia, facebook, instagram, twitter, youtube, teams, stream, c)
    elif tipo == "2": #quando o evento acontece em mais de um dia
        nOcorrencias = dias.count(',') + 1 #número de vezes que o evento occore
        Descricao = ConcatenarDescrição(categoria, description, wikidata, wikipedia, facebook, instagram, twitter, youtube, teams, stream)
        i = 1
        while(i <= nOcorrencias):
            DefEv2(i, nOcorrencias, nome, Descricao, osm, horas, dias, c)
            i = i+1

#concatena (categoria, description, wikidata, wikipedia, facebook, instagram, twitter, youtube, teams, stream) para formar a descrição do evento
def ConcatenarDescrição (categoria, description, wikidata, wikipedia, facebook, instagram, twitter, youtube, teams, stream):
    Descricao = ""
    if categoria != "":
        Descricao = Descricao + "Categorias:" + categoria + "\n"
    if description != "":
        Descricao = Descricao + "Descrição:" + description + "\n"
    if wikidata != "":
        Descricao = Descricao + "wikidata:" + wikidata + "\n"
    if wikipedia != "":
        Descricao = Descricao + "wikipedia:" + wikipedia + "\n"
    if facebook != "":
        Descricao = Descricao + "facebook:" + facebook + "\n"
    if instagram != "":
        Descricao = Descricao + "instagram:" + instagram + "\n"
    if twitter != "":
        Descricao = Descricao + "twitter:" + twitter + "\n"
    if youtube != "":
        Descricao = Descricao + "youtube:" + youtube + "\n"
    if teams != "":
        Descricao = Descricao + "teams:" + teams + "\n"
    if stream != "":
        Descricao = Descricao + "stream:" + stream
        
    return Descricao

#definicao de evento do tipo 2, evento que ocorre em mais de um dia e o coloca no calendario
def DefEv2(i, nOcorrencias, nome, Descricao, osm, horas, dias, c):
        a = Event()
        auxH=(i - 1)*11 + i-1
        auxD=((i - 1)*10)+i-1
        a.name = "[" + str(i)  + "/"+ str(nOcorrencias) +']' + nome
        a.description =  Descricao
        a.location = osm
        soma= int(horas[0+ auxH:2+ auxH])
        soma = soma + 3
        strsoma= str(soma)
        hinicio=dias[0 +auxD:4 +auxD] + '-'+dias[5+auxD:7+auxD] + '-' + dias[8+auxD:10+auxD] + ' ' + strsoma+ horas[2+ auxH:5+ auxH]+ ':00'
        soma = int(horas[6+ auxH:8+ auxH])
        soma = soma + 3
        strsoma= str(soma)
        hfinal= dias[0 +auxD:4 +auxD] + '-'+dias[5+auxD:7+auxD] + '-' + dias[8+auxD:10+auxD] + ' ' + strsoma + horas[8+auxH:11+auxH]+ ':00' 
        a.begin =hinicio
        a.end = hfinal
        c.events.add(a)

#definicao de evento quando o evento acontece somente em um dia e o coloca no calendario
def DefEv1(nome, categoria, description, tipo, dias, horas, osm, wikidata, wikipedia, facebook, instagram, twitter, youtube, teams, stream, c):
    e = Event()
    e.name = nome
    Descricao = ConcatenarDescrição(categoria, description, wikidata, wikipedia, facebook, instagram, twitter, youtube, teams, stream)
    e.description =  Descricao
    e.location = osm
    soma = int(horas[0:2])
    soma = soma + 3
    strsoma= str(soma)
    hinicio=dias[0:4] + '-'+dias[5:7] + '-' + dias[8:10] + ' ' + strsoma+ horas[2:5]+ ':00' 
    soma = int(horas[6:8])
    soma = soma + 3
    strsoma= str(soma)
    hfinal= dias[0:4] + '-'+dias[5:7] + '-' + dias[8:10] + ' ' + strsoma + horas[8:11]+ ':00' 
    e.begin =hinicio
    e.end = hfinal
    c.events.add(e)

Json_to_Eventos()

