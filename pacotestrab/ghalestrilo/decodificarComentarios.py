import io
import json
import os
import sys
import time
import requests
from bs4 import BeautifulSoup

def parsecomment(filename):
    # json.dumps
    with open(filename) as input_file:
        content = json.load(input_file)
    input_file.close()
    return content

def create_parents(filename):
    if os.sep in filename:
        outdir = os.path.dirname(filename)
        if not os.path.exists(outdir):
            os.makedirs(outdir)

def build_headers(video_id):
    url = f'http://www.youtube.com/watch?v={video_id}'
    r = requests.get(url) 
    s = BeautifulSoup(r.text, "html.parser") 

    # tag = s.find("span", class_="view-count")
    tag = s.select("span.view-count")
    views = tag.text if tag else 0
    # print("span.view-count is empty") if (not tag)

    # tag = s.find("yt-formatted-string", class_="ytd-toggle-button-renderer")
    tag = s.select("yt-formatted-string#text")
    likes = tag.text if tag else 0
    # print("yt-formatted-string#text is empty") if (not tag)
 
    return f'{url}\nviews {views}\nlikes {likes}\n'

def process_comment(comment_data):
    data = json.loads(comment_data)
    return f'{data["author"]}\n{data["text"]}\n{data["time"]}\n'

def process_comments(video_id):
    file_in = f'dataset/{video_id}.json'
    file_out = f'dataset/{video_id}.txt'
    create_parents(file_out)

    # Escrever Headers
    with open(file_out, "w") as output_file:
        headers = build_headers(video_id)
        output_file.write(headers);


    # Escrever Comentários
    with open(file_in) as input_file:
        with open(file_out, "a") as output_file:
            comment = input_file.readline()
            while comment:
                line = process_comment(comment)
                print(line)
                output_file.write(line)
                comment = input_file.readline()
            
    input_file.close()
    output_file.close()

    print(f'Arquivo criado: {file_out}')

def main(argv):
    if (len(argv) < 1):
        print("Faltou o id do vídeo na chamada do script. Saindo...")
        return

    video_id = argv[0];
    process_comments(video_id)
    return

if __name__ == "__main__":
    main(sys.argv[1:])


"""
# creating function 
def scrape_info(url): 
    r = requests.get(url) 
    s = BeautifulSoup(r.text, "html.parser") 

    views = s.find("div", class_="watch-view-count").text       
    likes = s.find("span", class_="like-button-renderer").span.button.text 

    data = {'title':title, 'views':views, 'likes':likes} 
    return data 
  
# main function 
if __name__ == "__main__": 
      
    # URL of the video 
    url ="https://www.youtube.com/watch?time_continue=17&v=2wEA8nuThj8"
      
    # calling the function 
    data = scrape_info(url) 
      
    # printing the dictionary 
    print(data) 
"""