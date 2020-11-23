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
    return

def process_comments(video_id):
    file_in = f'dataset/{video_id}.json'
    file_out = f'dataset/{video_id}.txt'
    create_parents(file_out)

    # with (open(file_in), open(file_out, "w")) as (input_file, output_file):
    with open(file_in) as input_file:
        lines = [];
        line = input_file.readline()
        print("")
        while line:
            data = json.loads(line);
            line = f'{data["author"]}\n{data["text"]}\n{data["time"]}\n'
            print(line)
            line = input_file.readline()
            
    input_file.close()
    # output_file.close()

def main(argv):
    video_id = argv[0];
    process_comments(video_id)
    return

if __name__ == "__main__":
    main(sys.argv[1:])
