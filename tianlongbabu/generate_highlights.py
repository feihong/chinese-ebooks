import sys
import collections
from pathlib import Path
import util

try:
  input_file = Path(sys.argv[1])
except IndexError:
  print('You must provide an input file')

def get_highlights():
  for line in input_file.read_text().splitlines():
    if line.startswith('//'):
      continue

    match line.split('[', 1):
      case [_]:
        continue
      case [phrase, _]:
        yield phrase

def get_highlight_lines(body_lines):
  highlights = collections.deque(get_highlights())
  for num, line in enumerate(body_lines, 1):
    if highlights[0] in line:
      local_highlights = []

      while highlights[0] in line:
        local_highlights.append(highlights.popleft())
        if len(highlights) <= 0:
          break

      yield num, ' '.join(local_highlights)
      if len(highlights) <= 0:
          break

chapters = util.get_chapters()
chapter = [c for c in chapters if c['title'] == input_file.stem][0]

body_lines = chapter['body'].splitlines()
for num, highlight in get_highlight_lines(body_lines):
  print(num, highlight)
