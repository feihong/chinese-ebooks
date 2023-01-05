"""
Download all content pages and store them in JSON file
"""
import json
import pyquery
import requests
import util


def get_pages():
  for i, url in enumerate(util.links, 1):
    print(f'{i} {url}')
    # Have to use requests.get because urllib.request.urlopen results in 403 from server
    res = requests.get(url)
    yield res.content
  
def parse_page(data: bytes):
  text = data.decode('gbk')
  doc = pyquery.PyQuery(text)
  paras = doc('td[width="87%"] p')
  title = paras[2].text_content()
  lines = (line.strip() for line in paras[4].text_content().splitlines())
  body = '\n'.join(lines)
  return dict(title=title, body=body)


pages = get_pages()
chapters = [parse_page(p) for p in pages]

with util.json_file.open('w') as fp:
  json.dump(chapters, fp, ensure_ascii=False, indent=2)
