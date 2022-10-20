import json
from pathlib import Path
from airium import Airium
import util

title = '一 青衫磊落险峰行'
pages = '1 4 8 9 10 11 14 19 23 34 36 45 51 52 56 57 64 65 68 70 72 73 75 76 79 83 84 85 88 90 91 96 107 108 113 118 123 126 129 134 145 146 148 150 151 152 160 171 178 181 182 185 188 194 195 201 206 207 209 210'
pages = [int(p) for p in pages.split()]

chapters = json.loads(util.json_file.read_bytes())

chapter = next(c for c in chapters if c['title'] == title)

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

html_file = Path(title).with_suffix('.html')
html_file.write_bytes(bytes(a))
