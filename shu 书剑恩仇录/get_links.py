import re
import urllib.parse
from pyquery import PyQuery
import util


def get_links(data):
  doc = PyQuery(data)
  for anchor in doc('a'):
    href = anchor.get('href')
    if href is not None and re.match(r'\d+\.html', href):
      yield urllib.parse.urljoin(util.index_url, href)

with util.connect() as conn:
  _, data = conn.execute('SELECT * FROM dump WHERE url = ?', (util.index_url,)).fetchone()
  for i, link in enumerate(get_links(data), 1):
    print(f'{i}. {link}')
    conn.execute('INSERT INTO links(url, num) VALUES (?, ?) ON CONFLICT(url) DO UPDATE SET num=excluded.num', (link, i))
