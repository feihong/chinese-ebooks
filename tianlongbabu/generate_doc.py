"""
Generate HTML for that can be pasted into review document in Google Docs
"""
from collections import UserString
import util

chapters = util.get_chapters()
highlight_chapter = util.get_highlights()[-1]
chapter = [c for c in chapters if c['title'] == highlight_chapter.title][0]

# Map line numbers to highlight lines
highlight_map = dict((line.num, line.content.copy()) for line in highlight_chapter)

class Chunk(UserString):
  """
  Part of a paragraph which may be highlighted
  """
  def __init__(self, line, highlighted=False):
    super().__init__(line)
    self.highlighted = highlighted

def find_substring(s, ss):
  start = s.find(ss)
  return (start, start + len(ss))

def highlight_line_to_chunks(line, highlights):
  while highlights != []:
    highlight = highlights.pop(0)
    start, end = find_substring(line, highlight)
    yield Chunk(line[0:start])
    yield Chunk(line[start:end], highlighted=True)
    line = line[end:-1]

  if line != '':
    yield Chunk(line)

def get_paragraphs():
  body_lines = chapter['body'].splitlines()
  for num, line in enumerate(body_lines, 1):
    if num in highlight_map:
      highlights = highlight_map[num]
      yield highlight_line_to_chunks(line, highlights)
    else:
      yield [Chunk(line)]

title = chapter['title']
output = util.get_template('doc.html').render(title=title, paragraphs=get_paragraphs())  
output_file = (util.output_dir / (chapter['title'] + '_doc')).with_suffix('.html')
output_file.write_text(output)
