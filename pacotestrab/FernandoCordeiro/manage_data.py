import pandas as pd
from manage_files import *
from youtube_statistics import YTstats
from sklearn.preprocessing import MinMaxScaler

def list_yt_objects(file, API_KEY):
    with open(file) as f:
        complete_videos_id = f.read().splitlines()                          # Retorna lista com a url de cada video
  
    videos_id = []
    for url in complete_videos_id:
        videos_id.append(url[32:])                                          # Retorna lista com o id da url 
 
    yt_objects = [YTstats(API_KEY,video_id,complete_video_id) 
                  for video_id, complete_video_id in zip(videos_id, complete_videos_id)] # Criando lista de objetos da classe YTstats

    return yt_objects

def list_data_frame(yt_objects, parent_path):
    old_data_frame = pd.DataFrame(columns=['views','likes','num_comments'])

    for yt in yt_objects:               
        video_information = yt.get_video_data()                               # Retorna informacoes sobre o video
        num_comm = int(video_information.get('num_comments'))                 # Retorna o numero de comentarios no video
        
        comments_information = yt.get_video_comments(num_comm)

        info = []
        info.append(video_information)
        info.append(comments_information)

        
        filename = video_information.get('id')
        path = parent_path + '/' + filename + '.json'

        
        write_json(path, info[0], info[1])                                    # Criando arquivo Json
        write_txt(info)                                                       # Criando arquivo Txt

        with open(path, 'r') as f:
            data = json.load(f)
            df = pd.json_normalize(data['video_information'])
            old_data_frame = pd.concat([old_data_frame, df])

    # End for

    return old_data_frame

def ranking_num_comments(listStructData, listUrl):
    listOfRows = []
    
    for i, df in enumerate(listStructData, start=0):
        my_tuple = (i,len(df), listUrl[i])
        listOfRows.append(my_tuple)

    listOfRows.sort(key=lambda tup: tup[1], reverse=True)

    return listOfRows

def ranking_eval(old_data_frame):
    new_data_frame = old_data_frame[['views','likes', 'num_comments']].copy().astype(str).astype(int)
  
    scaler = MinMaxScaler(feature_range = (0,1))
    scaled_data = scaler.fit_transform(new_data_frame)
    
    scaled_df = pd.DataFrame(data=scaled_data, index=["1", "2", "3"], columns=["views", "likes", "num_comments"])
    scaled_df['eval'] = scaled_df.eval('(views + 2*likes + 3*num_comments)/5')
    
    final_df = pd.DataFrame()
    final_df['eval'] = scaled_df['eval'].to_numpy()
    final_df['url'] = old_data_frame['url'].to_numpy().astype(str)

    return final_df.sort_values(by=['eval'], ascending=False)