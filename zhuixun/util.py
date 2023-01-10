import json
from pathlib import Path
import jinja2

here = Path(__file__).parent

title = '追寻现代中国'
author = '史景迁'

input_file = here / 'book.txt'
json_file = here / 'book.json'
highlights_file = here / 'highlights.txt'
output_dir = here / 'output'

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(here.parent / 'tianlongbabu/templates'),
    autoescape=jinja2.select_autoescape(),
    trim_blocks=True,
    lstrip_blocks=True)

def get_template(template_name):
  return env.get_template(template_name)

def get_chapters():
  with json_file.open() as fp:
    chapters = json.load(fp)
  return chapters
