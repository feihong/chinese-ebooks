
from airium import Airium
import util


def generate_page(title, body_callback, output_file):
  a = Airium()

  a('<!DOCTYPE html>')
  with a.html(lang="en"):
    with a.head():
        a.meta(charset="utf-8")
        a.meta(name="viewport", content="width=device-width, initial-scale=1")
        a.title(_t=title)
        a.link(rel='stylesheet', href='https://fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic')
        a.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/normalize/8.0.1/normalize.css')
        a.link(rel='stylesheet', href='https://cdnjs.cloudflare.com/ajax/libs/milligram/1.4.1/milligram.css')
        a.style(_t="""
        p { font-size: 2rem; }
        span { font-size: 1rem; color: #888; }
        body { padding: 0 1rem; }
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
        a.span(_t=i)
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
