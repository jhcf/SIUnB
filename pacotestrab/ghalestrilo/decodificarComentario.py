import io
import json
import os
import sys
import time

video_id = ""

def parsecontent(filename):
    # json.dumps
    with open(filename) as input_file:
        content = json.load(input_file)
    input_file.close()
    return content



def write(content,filename):
    if os.sep in filename:
        outdir = os.path.dirname(filename)
        if not os.path.exists(outdir):
            os.makedirs(outdir)
    with open(filename) as output:
        output.write(f'http://www.youtube.com/watch?v={video_id}')
    output.close()

def main(argv):
    video_id = argv[0];
    file_in = f'dataset/{video_id}.json'
    file_out = f'dataset/{video_id}.txt'
    content = parsecontent(file_in)
    write(content,file_out)
    return

if __name__ == "__main__":
    main(sys.argv[1:])
