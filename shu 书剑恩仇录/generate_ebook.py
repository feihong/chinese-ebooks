"""
Generate markdown and epub files. The epub file is generated by Calibre using the
markdown files as input.
"""
import subprocess
from pyquery import PyQuery
import util


def get_chapters():
  with util.connect() as conn:
    cur = conn.cursor()
    for url in util.links:
      _, data = cur.execute('SELECT * FROM dump WHERE url = ?', (url,)).fetchone()
      text = data.decode(util.encoding)
      doc = PyQuery(text)
      title = doc('strong font').text()
      content = doc('p').text()
      yield url, title, content

def main():
  # Generate markdown file
  with util.markdown_file.open('w') as fp:
    for url, title, content in get_chapters():
      char_count = sum(1 for c in content if not c.isspace())
      print(url, title, char_count)
      fp.write(f'## {title}\n\n')
      fp.write(f'Source: {url}\n\n')
      fp.write(f'Characters: {char_count}\n\n')
      fp.write(f'{content}\n\n')

  # Generate epub file
  cmd = [
    'ebook-convert',
    util.markdown_file,
    util.epub_file,
    '--authors', util.author,
    '--title', util.title,
    '--comments', util.description,
    '--chapter', "//*[name()='h2' or name()='h3']"
  ]
  subprocess.run(cmd)

if __name__ == '__main__':
  main()
