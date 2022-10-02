import re
import subprocess
from pathlib import Path
import util

source = Path('~/Downloads/天龙八部.txt').expanduser()
# Print the encoding
subprocess.run(['chardetect', source])

class Section:
  def __init__(self, title):
    self.title = title
    self.body = []

  def append(self, line):
    self.body.append(line)

def get_lines():
  with source.open('r', encoding='utf16') as fp:
    for line in fp:
      yield line.strip()

def get_sections(lines):
  section = None

  for line in lines:
    if line == '（全书完）':
      break

    if re.match(r'[一二三四五六七八九十]{1,3} ', line):
      if section is not None:
        yield section
      section = Section(line)
    else:
      if section is not None:
        section.append(lines)

  if section is not None:
    yield section

lines = get_lines()
sections = [section for section in get_sections(lines) if len(section.body) > 1]
for i, section in enumerate(sections, 1):
  print(i, section.title, len(section.body))
