import json
from pathlib import Path
from airium import Airium
import util

title, pages = util.get_highlight()
chapter = util.get_current_chapter()

lines = chapter['body'].splitlines()

a = Airium()

a('<!DOCTYPE html>')
with a.html(lang="en"):
  with a.head():
      a.meta(charset="utf-8")
      a.title(_t=title)
      a.style(_t="""
      body {
        font-size: 20px;
      }
      """)

  with a.body():
    a.h1(_t=title)

    for i, line in enumerate(lines, 1):
      with a.p():
        if i in pages:
          style = 'color:#eee;background-color:#900'
        else:
          style = 'color:#888'

        a.span(style=style, _t=i)
        a(line)

html_file = (util.output_dir / title).with_suffix('.html')
html_file.write_bytes(bytes(a))
