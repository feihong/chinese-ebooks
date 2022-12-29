"""
Generate HTML for that can be pasted into review document in Google Docs
"""
from collections import UserString
import util

chapters = util.get_chapters()
highlight = util.get_highlights()[-1]
chapter = [c for c in chapters if c['title'] == highlight.title][0]

item_map = dict((item.num, item.content) for item in highlight.items)

class LineItem(UserString):
  def __init__(self, line, highlighted=False):
    super().__init__(line)
    self.highlighted = highlighted

def get_body_lines():
  body_lines = chapter['body'].splitlines()
  for num, line in enumerate(body_lines, 1):
    if num in item_map:
      substring = item_map[num]
      start = line.find(substring)
      end = start + len(substring)
      yield [
        LineItem(line[0:start]), 
        LineItem(line[start:end], highlighted=True),
        LineItem(line[end:-1])
      ]
    else:
      yield [LineItem(line)]

title = chapter['title']
output = util.get_template('doc.html').render(title=title, body_lines=get_body_lines())  
output_file = (util.output_dir / (chapter['title'] + '_doc')).with_suffix('.html')
output_file.write_text(output)

