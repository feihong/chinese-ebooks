"""
Parse plain text file and output the book's contents as JSON
"""
import re
import json
import util

def get_lines():
  with util.input_file.open('r') as fp:
    for line in fp:
      line = line.strip()
      if line:
        yield line

class Chapter:
  def __init__(self, title):
    self.title = title
    self.body = []

  def append(self, line):
    self.body.append(line)

def get_chapters(lines):
  chapter = None

  for line in lines:
    if re.match(r'^\d{1,2} ', line) or re.match(r'^第[一二三四五]部 ', line):
      if chapter is not None:
        yield chapter
      chapter = Chapter(line)
    else:
      if chapter is not None:
        chapter.append(line)

  if chapter is not None:
    yield chapter


def main():
  lines = get_lines()
  chapters = get_chapters(lines)
  # Ignore chapters that contain no content
  # chapters = [chapter for chapter in get_chapters(lines) if len(chapter.body) > 1]

  with util.json_file.open('w') as fp:
    obj = [dict(title=c.title, body='\n'.join(c.body)) for c in chapters]
    json.dump(obj, fp, indent=2, ensure_ascii=False)
    print(f'Generated {util.json_file}')

if __name__ == '__main__':
  main()
