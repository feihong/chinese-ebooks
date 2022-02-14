import subprocess
import chardet
from pyquery import PyQuery
import util

query = '''
SELECT dump.url, dump.data
FROM dump JOIN links ON dump.url = links.url
ORDER BY links.num'''

def get_content():
  with util.connect() as conn:
    for (url, data) in conn.execute(query):
      result = chardet.detect(data)
      text = data.decode(result['encoding'], errors='replace')
      doc = PyQuery(text)
      title = doc('strong font').text()
      content = doc('p').text()
      yield url, title, content

with util.markdown_file.open('w') as fp:
  for url, title, content in get_content():
    char_count = sum(1 for c in content if not c.isspace())
    print(url, title, char_count)
    fp.write(f'## {title}\n\n')
    fp.write(f'Source: {url}\n\n')
    fp.write(f'Characters: {char_count}\n\n')
    fp.write(f'{content}\n\n')

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
