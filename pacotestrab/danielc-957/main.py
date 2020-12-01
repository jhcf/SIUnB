
from youtube_statistics import YTstats
import sys
import json

API_KEY = "Sua API Key aqui"
complete_video_id = sys.argv[1]
num_comm = sys.argv[2]

video_id = complete_video_id[32:]
#print(video_id)

yt = YTstats(API_KEY,video_id,complete_video_id,num_comm)

video_information = yt.get_video_data()
comments_information = yt.get_video_comments()

info = []
info.append(video_information)
info.append(comments_information)

def write_json(file):
    with open('youtube_info.json', 'w', encoding='utf-8') as f:
        json.dump(file, f, ensure_ascii=False, indent=4)

def write_txt(file):
  with open('youtube_info.txt', 'w') as filehandle:
    for listitem in file:
        filehandle.write('%s\n' % listitem)

write_json(info)
write_txt(info)

#video_id= "R-1ndCVLCLk"
#complete_video_id = "https://www.youtube.com/watch?v=R-1ndCVLCLk"

