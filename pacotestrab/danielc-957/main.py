
from youtube_statistics import YTstats
import sys

API_KEY = "Insira sua API aqui"
complete_video_id = sys.argv[1]

video_id = complete_video_id[32:]

yt = YTstats(API_KEY,video_id,complete_video_id)

yt.get_video_data()
yt.get_video_comments()

#video_id= "R-1ndCVLCLk"
#* Adaptar o codigo para mais urls * 
#complete_video_id = "https://www.youtube.com/watch?v=R-1ndCVLCLk"

