"""
Parse plain text file and output the book's contents as JSON
"""
import re
import json
import subprocess
import util


class Chapter:
  def __init__(self, title):
    self.title = title
    self.body = []

  def append(self, line):
    self.body.append(line)

def get_lines():
  with util.input_file.open('r', encoding='utf16') as fp:
    for line in fp:
      line = line.strip()
      if line:
        yield line

def get_chapters(lines):
  chapter = None

  for line in lines:
    if line == '（全书完）':
      break

    if re.match(r'[一二三四五六七八九十]{1,3} ', line):
      if chapter is not None:
        yield chapter
      chapter = Chapter(line)
    else:
      if chapter is not None:
        chapter.append(line)

  if chapter is not None:
    yield chapter


def main():
  # Print the encoding
  subprocess.run(['chardetect', util.input_file])

  lines = get_lines()
  # Ignore chapters that contain no content
  chapters = [chapter for chapter in get_chapters(lines) if len(chapter.body) > 1]

  with util.json_file.open('w') as fp:
    obj = [dict(title=c.title, body='\n'.join(c.body)) for c in chapters]
    json.dump(obj, fp, indent=2, ensure_ascii=False)
    print(f'Generated {util.json_file}')

if __name__ == '__main__':
  main()
