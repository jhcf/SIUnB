import requests
import json

def get_format_date(date):
    new_date =  date[8:-10] +  "-" + date[5:-13] + "-" + date[0:-16]
    return new_date

class YTstats: 
    def __init__(self,api_key,video_id, complete_video_id):
        self.api_key = api_key
        self.video_id = video_id
        self.complete_video_id = complete_video_id
        self.video_data = None

    def get_video_data(self):
        url = f'https://www.googleapis.com/youtube/v3/videos?part=statistics&id={self.video_id}&key={self.api_key}'
        
        json_url = requests.get(url)
        data = json.loads(json_url.text)
        
        try:
           viewCount = data ["items"] [0] ["statistics"] ["viewCount"]
           likeCount = data ["items"] [0] ["statistics"] ["likeCount"]
           dislikeCount = data ["items"] [0] ["statistics"] ["dislikeCount"]
           commentCount = data ["items"] [0] ["statistics"] ["commentCount"]

        except :
            data = None
            viewCount = "Nao encontrado"
            likeCount = "Nao encontrado"
            dislikeCount = "Nao encontrado"
            commentCount = "Nao encontrado"


        #print('url do video: ' + self.complete_video_id)
        #print ('Views: ' + viewCount)
        #print ('Likes: ' + likeCount)
        #print ('Dislikes: ' + dislikeCount)
        #print ('Comentarios: ' + commentCount)
        
        #informado: 
        #url
        #numero de comentarios

        #falta ainda:
        #id do wikidata
        #nome do evento

        information_dict = {
            "id": self.video_id,
            "url": self.complete_video_id,
            "views": viewCount,
            "likes": likeCount,
            "dislikes:": dislikeCount,
            "num_comments": commentCount
        } 
        return information_dict

    def get_video_comments(self, num_comments):
        num = num_comments
        #num = int(self.num_comments)
        dictlist = [dict() for x in range(num)]
        url = f'https://www.googleapis.com/youtube/v3/commentThreads?key={self.api_key}&textFormat=plainText&part=snippet&videoId={self.video_id}&order=relevance&maxResults={num}'
        json_url = requests.get(url)
        comments = json.loads(json_url.text)
        
        try: 
            for i in range(num): 
                dictlist[i] ['name_person'] = comments ["items"] [i] ["snippet"] ["topLevelComment"] ["snippet"] ["authorDisplayName"]
                dictlist[i] ['date_comment'] = comments ["items"] [i] ["snippet"] ["topLevelComment"] ["snippet"] ["publishedAt"]
                dictlist[i] ['comment_text'] = comments ["items"] [i] ["snippet"] ["topLevelComment"] ["snippet"] ["textOriginal"]
                #dictlist[i] ['date_comment'] = get_format_date(dictlist[i] ['date_comment'])
            
            #for i in range (num):
            #    print("Usuario: " + dictlist[i] ["name_person"])
            #    print("Data: " + dictlist[i] ["date_comment"])
            #    print("comentario: " + dictlist[i] ["comment_text"])
            
            return dictlist
    
        except:
            error_message = "Comentarios nao encontrados"
            print(error_message)
            return error_message

    
