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
        section.append(line)

  if section is not None:
    yield section


def main():
  lines = get_lines()
  # Ignore sections that contain no content
  sections = [section for section in get_sections(lines) if len(section.body) > 1]

  with util.markdown_file.open('w') as fp:
    for section_num, section in enumerate(sections, 1):
      print(section_num, section.title, len(section.body))

      fp.write(f'## {section.title}\n\n')
      for i, line in enumerate(section.body, 1):
        fp.write(f'<span style="font-size:x-small;color:#888">{i}</span> {line}\n\n')

if __name__ == '__main__':
  main()
