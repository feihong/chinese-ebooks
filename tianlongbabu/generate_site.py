import json
from pathlib import Path
from airium import Airium
import util


def generate_page(title, body_callback, output_file):
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
      body_callback(a)

    output_file.write_bytes(bytes(a))

def generate_chapter(chapter):
  title = chapter['title']

  def callback(a):
    lines = chapter['body'].splitlines()
    for i, line in enumerate(lines, 1):
      with a.p():
        a.span(style='color:#888;font-size:small', _t=i)
        a(line)

  generate_page(
    title=title,
    body_callback=callback,
    output_file=(util.output_dir / title).with_suffix('.html'),
  )

def generate_index(chapters):
  def callback(a):
    with a.ol():
      for chapter in chapters:
        with a.li():
          title = chapter['title']
          link = title + '.html'
          a.a(href=link, _t=title)

  generate_page(
    title=util.title,
    body_callback=callback,
    output_file=util.output_dir / 'index.html',
  )


if __name__ == '__main__':
  chapters = util.get_chapters()

  generate_index(chapters)

  for chapter in chapters:
    generate_chapter(chapter)
