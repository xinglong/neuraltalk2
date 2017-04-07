import re
import sys
import json

if __name__ == '__main__':

    inputfile = sys.argv[1]

    images = []
    cp_line = re.compile('^cp\s"(.*?)".*')
    image_line = re.compile('^image\s\d+:(.*)$')
    cnt = 0
    lines = 0
    with open(inputfile, 'r') as f:
        img = None
        caption = None
        for line in f:
            lines+=1
            cp_line_match = cp_line.match(line.strip())
            image_line_match = image_line.match(line.strip())
            if cp_line_match:
                img = cp_line_match.group(1)
            elif image_line_match:
                caption = image_line_match.group(1).strip()
            if img and caption:
                cnt+=1
                images.append({'img_uri':img, 'caption':caption})
                img = None
                caption = None
    print(json.dumps(images))







