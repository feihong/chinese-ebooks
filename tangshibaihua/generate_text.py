import json
import util

chapters = json.loads(util.json_file.read_bytes())

with util.txt_file.open('w') as fp:
  for chapter in chapters:
    fp.write(f'{chapter["title"].strip()}\n\n')

    lines = (l.strip() for l in chapter['body'].split('\n\n'))

    for line in lines:
      fp.write(f'{line}\n\n')
