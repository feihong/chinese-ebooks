"""
Download all content pages and store them in the database
"""
import requests
import util

with util.connect() as conn:
  for i, url in enumerate(util.links, 1):
    print(f'{i} {url}')
    cur = conn.execute('SELECT url FROM dump WHERE url = ?', (url,))
    if cur.fetchone() is None:
      # Have to use requests.get because urllib.request.urlopen results in 403 from server
      res = requests.get(url)
      conn.execute('INSERT INTO dump VALUES (?, ?)', (url, res.content))
