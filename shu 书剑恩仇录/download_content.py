import requests
import util

with util.connect() as conn:
  for (url, num) in conn.execute('SELECT * FROM links ORDER BY num'):
    print(f'{num} {url}')
    cur = conn.execute('SELECT url FROM dump WHERE url = ?', (url,))
    if cur.fetchone() is None:
      r = requests.get(url)
      conn.execute('INSERT INTO dump VALUES (?, ?)', (url, r.content))
