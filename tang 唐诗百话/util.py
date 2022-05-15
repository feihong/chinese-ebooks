import sqlite3
from pathlib import Path
import pyquery

here = Path(__file__).parent

index_url = 'http://www.guoxue123.com/new/0002/tsbh/index.htm'
encoding = 'gbk'
title = '唐诗百话'
author = '施蜇存'
description = '《唐诗百话》面世以来，深受海内外学术界高度评价和广大读者热烈赞誉，美国耶鲁大学等名校也将这本书作为汉学研究课程的教材。施蛰存将数十年来对中国古典诗学的潜心探索，以严谨考证和比较文学研究的方法融贯于一书，尤其是毫不因袭前人的选诗、说诗视角和贯通中外古今的大家气度，在唐诗研究上别开生面，极具新意。'
links = '''
http://www.guoxue123.com/new/0002/tsbh/000.htm
http://www.guoxue123.com/new/0002/tsbh/001.htm
http://www.guoxue123.com/new/0002/tsbh/002.htm
http://www.guoxue123.com/new/0002/tsbh/003.htm
http://www.guoxue123.com/new/0002/tsbh/004.htm
http://www.guoxue123.com/new/0002/tsbh/005.htm
http://www.guoxue123.com/new/0002/tsbh/006.htm
http://www.guoxue123.com/new/0002/tsbh/007.htm
http://www.guoxue123.com/new/0002/tsbh/008.htm
http://www.guoxue123.com/new/0002/tsbh/009.htm
http://www.guoxue123.com/new/0002/tsbh/010.htm
http://www.guoxue123.com/new/0002/tsbh/011.htm
http://www.guoxue123.com/new/0002/tsbh/012.htm
http://www.guoxue123.com/new/0002/tsbh/013.htm
http://www.guoxue123.com/new/0002/tsbh/014.htm
http://www.guoxue123.com/new/0002/tsbh/015.htm
http://www.guoxue123.com/new/0002/tsbh/016.htm
http://www.guoxue123.com/new/0002/tsbh/017.htm
http://www.guoxue123.com/new/0002/tsbh/018.htm
http://www.guoxue123.com/new/0002/tsbh/019.htm
http://www.guoxue123.com/new/0002/tsbh/020.htm
http://www.guoxue123.com/new/0002/tsbh/021.htm
http://www.guoxue123.com/new/0002/tsbh/022.htm
http://www.guoxue123.com/new/0002/tsbh/023.htm
http://www.guoxue123.com/new/0002/tsbh/024.htm
http://www.guoxue123.com/new/0002/tsbh/025.htm
http://www.guoxue123.com/new/0002/tsbh/026.htm
http://www.guoxue123.com/new/0002/tsbh/027.htm
http://www.guoxue123.com/new/0002/tsbh/028.htm
http://www.guoxue123.com/new/0002/tsbh/029.htm
http://www.guoxue123.com/new/0002/tsbh/030.htm
http://www.guoxue123.com/new/0002/tsbh/031.htm
http://www.guoxue123.com/new/0002/tsbh/032.htm
http://www.guoxue123.com/new/0002/tsbh/033.htm
http://www.guoxue123.com/new/0002/tsbh/034.htm
http://www.guoxue123.com/new/0002/tsbh/035.htm
http://www.guoxue123.com/new/0002/tsbh/036.htm
http://www.guoxue123.com/new/0002/tsbh/037.htm
http://www.guoxue123.com/new/0002/tsbh/038.htm
http://www.guoxue123.com/new/0002/tsbh/039.htm
http://www.guoxue123.com/new/0002/tsbh/040.htm
http://www.guoxue123.com/new/0002/tsbh/041.htm
http://www.guoxue123.com/new/0002/tsbh/042.htm
http://www.guoxue123.com/new/0002/tsbh/043.htm
http://www.guoxue123.com/new/0002/tsbh/044.htm
http://www.guoxue123.com/new/0002/tsbh/045.htm
http://www.guoxue123.com/new/0002/tsbh/046.htm
http://www.guoxue123.com/new/0002/tsbh/047.htm
http://www.guoxue123.com/new/0002/tsbh/048.htm
http://www.guoxue123.com/new/0002/tsbh/049.htm
http://www.guoxue123.com/new/0002/tsbh/050.htm
http://www.guoxue123.com/new/0002/tsbh/051.htm
http://www.guoxue123.com/new/0002/tsbh/052.htm
http://www.guoxue123.com/new/0002/tsbh/053.htm
http://www.guoxue123.com/new/0002/tsbh/054.htm
http://www.guoxue123.com/new/0002/tsbh/055.htm
http://www.guoxue123.com/new/0002/tsbh/056.htm
http://www.guoxue123.com/new/0002/tsbh/057.htm
http://www.guoxue123.com/new/0002/tsbh/058.htm
http://www.guoxue123.com/new/0002/tsbh/059.htm
http://www.guoxue123.com/new/0002/tsbh/060.htm
http://www.guoxue123.com/new/0002/tsbh/061.htm
http://www.guoxue123.com/new/0002/tsbh/062.htm
http://www.guoxue123.com/new/0002/tsbh/063.htm
http://www.guoxue123.com/new/0002/tsbh/064.htm
http://www.guoxue123.com/new/0002/tsbh/065.htm
http://www.guoxue123.com/new/0002/tsbh/066.htm
http://www.guoxue123.com/new/0002/tsbh/067.htm
http://www.guoxue123.com/new/0002/tsbh/068.htm
http://www.guoxue123.com/new/0002/tsbh/069.htm
http://www.guoxue123.com/new/0002/tsbh/070.htm
http://www.guoxue123.com/new/0002/tsbh/071.htm
http://www.guoxue123.com/new/0002/tsbh/072.htm
http://www.guoxue123.com/new/0002/tsbh/073.htm
http://www.guoxue123.com/new/0002/tsbh/074.htm
http://www.guoxue123.com/new/0002/tsbh/075.htm
http://www.guoxue123.com/new/0002/tsbh/076.htm
http://www.guoxue123.com/new/0002/tsbh/077.htm
http://www.guoxue123.com/new/0002/tsbh/078.htm
http://www.guoxue123.com/new/0002/tsbh/079.htm
http://www.guoxue123.com/new/0002/tsbh/080.htm
http://www.guoxue123.com/new/0002/tsbh/081.htm
http://www.guoxue123.com/new/0002/tsbh/082.htm
http://www.guoxue123.com/new/0002/tsbh/083.htm
http://www.guoxue123.com/new/0002/tsbh/084.htm
http://www.guoxue123.com/new/0002/tsbh/085.htm
http://www.guoxue123.com/new/0002/tsbh/086.htm
http://www.guoxue123.com/new/0002/tsbh/087.htm
http://www.guoxue123.com/new/0002/tsbh/088.htm
http://www.guoxue123.com/new/0002/tsbh/089.htm
http://www.guoxue123.com/new/0002/tsbh/090.htm
http://www.guoxue123.com/new/0002/tsbh/091.htm
http://www.guoxue123.com/new/0002/tsbh/092.htm
http://www.guoxue123.com/new/0002/tsbh/093.htm
http://www.guoxue123.com/new/0002/tsbh/094.htm
http://www.guoxue123.com/new/0002/tsbh/095.htm
http://www.guoxue123.com/new/0002/tsbh/096.htm
http://www.guoxue123.com/new/0002/tsbh/097.htm
http://www.guoxue123.com/new/0002/tsbh/098.htm
http://www.guoxue123.com/new/0002/tsbh/099.htm
http://www.guoxue123.com/new/0002/tsbh/100.htm
'''.strip().splitlines()

markdown_file = (here / title).with_suffix('.markdown')
epub_file = (here / title).with_suffix('.epub')

db_file = here / 'dump.db'

hanzi_file = here.parent / 'hanzi.txt'
ignore_file = here.parent / 'ignore.txt'
vocab_file = here / (title + ' 生词.txt')

def connect():
  return sqlite3.connect(db_file)

def parse_page(data: bytes):
  text = data.decode(encoding)
  doc = pyquery.PyQuery(text)
  paras = doc('td[width="87%"] p')
  title = paras[2].text_content()
  lines = paras[4].text_content().splitlines()
  content = '\n\n'.join(lines)
  return (title, content)

if not db_file.exists():
  with connect() as conn:
    conn.execute("CREATE TABLE dump (url TEXT PRIMARY KEY, data BLOB);")
