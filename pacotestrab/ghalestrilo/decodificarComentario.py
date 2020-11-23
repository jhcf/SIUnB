import io
import json
import os
import sys
import time

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

def process_comment(comment_data):
    data = json.loads(comment_data)
    return f'{data["author"]}\n{data["text"]}\n{data["time"]}\n'

def process_comments(video_id):
    file_in = f'dataset/{video_id}.json'
    file_out = f'dataset/{video_id}.txt'
    create_parents(file_out)

    # Escrever Headers
    with open(file_out, "w") as output_file:
        print("creating headers")


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
    # output_file.close()

def main(argv):
    video_id = argv[0];
    process_comments(video_id)
    return

if __name__ == "__main__":
    main(sys.argv[1:])
