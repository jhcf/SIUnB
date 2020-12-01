import requests
import json

def get_format_date(date):
    new_date =  date[8:-10] +  "-" + date[5:-13] + "-" + date[0:-16]
    return new_date

class YTstats: 
    def __init__(self,api_key,video_id, complete_video_id,num_comments):
        self.api_key = api_key
        self.video_id = video_id
        self.complete_video_id = complete_video_id
        self.num_comments = num_comments
        self.video_data = None

    def get_video_data(self):
        num_comm = int(self.num_comments)
        url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={self.video_id}&key={self.api_key}'
        #print(url)
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        try:
           viewCount = data ["items"] [0] ["statistics"] ["viewCount"]
           likeCount = data ["items"] [0] ["statistics"] ["likeCount"]
           dislikeCount = data ["items"] [0] ["statistics"] ["dislikeCount"]

        except :
            data = None
            viewCount = "Nao encontrado"
            likeCount = "Nao encontrado"
            dislikeCount = "Nao encontrado"


        print('url do video: ' + self.complete_video_id)
        print ('Views: ' + viewCount)
        print ('Likes: ' + likeCount)
        print ('Dislikes: ' + dislikeCount)
        
        #informado: 
        #url
        #numero de comentarios

        #falta ainda:
        #id do wikidata
        #nome do evento

        information_dict = {
            "url": self.complete_video_id,
            "views": viewCount,
            "likes": likeCount,
            "dislikes:": dislikeCount,
            "num_comments": num_comm
        } 
        return information_dict

    def get_video_comments(self):
        num = int(self.num_comments)
        dictlist = [dict() for x in range(num)]
        url = f'https://www.googleapis.com/youtube/v3/commentThreads?key={self.api_key}&textFormat=plainText&part=snippet&videoId={self.video_id}&order=relevance&maxResults={self.num_comments}'
        json_url = requests.get(url)
        comments = json.loads(json_url.text)
        try: 
            for i in range(num): 
                dictlist[i] ['name_person'] = comments ["items"] [i] ["snippet"] ["topLevelComment"] ["snippet"] ["authorDisplayName"]
                dictlist[i] ['date_comment'] = comments ["items"] [i] ["snippet"] ["topLevelComment"] ["snippet"] ["publishedAt"]
                dictlist[i] ['comment_text'] = comments ["items"] [i] ["snippet"] ["topLevelComment"] ["snippet"] ["textOriginal"]
                dictlist[i] ['date_comment'] = get_format_date(dictlist[i] ['date_comment'])
            
            for i in range (num):
                print("Usuario: " + dictlist[i] ["name_person"])
                print("Data: " + dictlist[i] ["date_comment"])
                print("comentario: " + dictlist[i] ["comment_text"])
            
            return dictlist
    
        except:
            error_message = "Comentarios nao encontrados"
            print(error_message)
            return error_message
