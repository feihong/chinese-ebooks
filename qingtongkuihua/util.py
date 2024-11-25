import json
import re
from pathlib import Path
import jinja2

here = Path(__file__).parent

title = '青铜葵花'
author = '曹文轩'

input_file = here / 'book.txt'

json_file = here / 'book.json'
highlights_file = here / 'highlights.txt'
output_dir = here / 'output'

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(here / 'templates'),
    autoescape=jinja2.select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True)

def get_template(template_name):
  return env.get_template(template_name)

def get_chapters():
  with json_file.open() as fp:
    chapters = json.load(fp)
  return chapters

class HighlightChapter:
  def __init__(self, block):
    lines = block.splitlines()
    self.title = lines[0]
    self.items = [HiglightLine(l) for l in lines[1:]]

  def __iter__(self):
    return iter(self.items)

class HiglightLine:
  """
  One or more phrases that appear on the given line number
  """
  def __init__(self, line):
    match = re.match(r'(\d+) (.+)', line)
    self.num = int(match.group(1))
    self.content = match.group(2).split(' ')


def get_highlights():
  blocks = re.split(r'\n{2,}', highlights_file.read_text())
  return [HighlightChapter(block) for block in blocks]
