"""
Download index page
"""
import requests
import util

with util.connect() as conn:
  cur = conn.execute('SELECT * FROM dump WHERE url = ?', (util.index_url,))
  if cur.fetchone() is None:
    r = requests.get(util.index_url)
    conn.execute('INSERT INTO dump VALUES(?, ?)', (util.index_url, r.content))
