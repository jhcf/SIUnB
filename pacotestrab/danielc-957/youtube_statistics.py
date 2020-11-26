import requests
import json

class YTstats: 
    def __init__(self,api_key,video_id, complete_video_id):
        self.api_key = api_key
        self.video_id = video_id
        self.complete_video_id = complete_video_id
        self.channel_statistics = None
        self.video_data = None

    def get_video_data(self):
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

        print('url do video: ' + self.complete_video_id)
        print ('Views: ' + viewCount)
        print ('Likes: ' + likeCount)
        print ('Dislikes: ' + dislikeCount)

    def get_video_comments(self): 
        dictlist = [dict() for x in range(3)]
        url = f'https://www.googleapis.com/youtube/v3/commentThreads?key={self.api_key}&textFormat=plainText&part=snippet&videoId={self.video_id}&order=relevance&maxResults=3'
        json_url = requests.get(url)
        comments = json.loads(json_url.text)
    
        for i in range(3): 
            dictlist[i] ['name_person'] = comments ["items"] [i] ["snippet"] ["topLevelComment"] ["snippet"] ["authorDisplayName"]
            dictlist[i] ['date_comment'] = comments ["items"] [i] ["snippet"] ["topLevelComment"] ["snippet"] ["publishedAt"]
            dictlist[i] ['comment_text'] = comments ["items"] [i] ["snippet"] ["topLevelComment"] ["snippet"] ["textOriginal"]

        #print(url)
        for i in range (3):
            print(dictlist[i] ["name_person"])
            print(dictlist[i] ["date_comment"])
            print(dictlist[i] ["comment_text"])
