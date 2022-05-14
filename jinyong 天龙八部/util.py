import sqlite3
from pathlib import Path
import pyquery

here = Path(__file__).parent

index_url = 'https://www.kanunu8.com/wuxia/201102/1626.html'
encoding = 'gbk'
title = '天龙八部'
author = '金庸'
description = '小说以宋哲宗时代为背景，通过宋、辽、大理、西夏、吐蕃及女真等王国之间的武林恩怨和民族矛盾，从哲学的高度对人生和社会进行审视和描写，展示了一幅波澜壮阔的生活画卷。所谓“天龙八部”是佛经用语，包括八种神道怪物，作者以此为书名，旨在象征大千世界之中形形色色的人物。小说叙云南大理国武林世家镇南王之子段誉，为逃避习武，来至无量山中，因种种机遇，学得一身古怪奇妙的武功，并先后结识少女钟灵、木婉清，互相悦慕，岂料此二人是父亲段正淳四处留情的私生女。四大恶人之首段延庆本该是大理国王位的真正继承人，因宫中内乱流落江湖。。。。'
links = '''
https://www.kanunu8.com/wuxia/201102/1626/37105.html
https://www.kanunu8.com/wuxia/201102/1626/37106.html
https://www.kanunu8.com/wuxia/201102/1626/37107.html
https://www.kanunu8.com/wuxia/201102/1626/37108.html
https://www.kanunu8.com/wuxia/201102/1626/37109.html
https://www.kanunu8.com/wuxia/201102/1626/37110.html
https://www.kanunu8.com/wuxia/201102/1626/37111.html
https://www.kanunu8.com/wuxia/201102/1626/37112.html
https://www.kanunu8.com/wuxia/201102/1626/37113.html
https://www.kanunu8.com/wuxia/201102/1626/37114.html
https://www.kanunu8.com/wuxia/201102/1626/37115.html
https://www.kanunu8.com/wuxia/201102/1626/37116.html
https://www.kanunu8.com/wuxia/201102/1626/37117.html
https://www.kanunu8.com/wuxia/201102/1626/37118.html
https://www.kanunu8.com/wuxia/201102/1626/37119.html
https://www.kanunu8.com/wuxia/201102/1626/37120.html
https://www.kanunu8.com/wuxia/201102/1626/37121.html
https://www.kanunu8.com/wuxia/201102/1626/37122.html
https://www.kanunu8.com/wuxia/201102/1626/37123.html
https://www.kanunu8.com/wuxia/201102/1626/37124.html
https://www.kanunu8.com/wuxia/201102/1626/37125.html
https://www.kanunu8.com/wuxia/201102/1626/37126.html
https://www.kanunu8.com/wuxia/201102/1626/37127.html
https://www.kanunu8.com/wuxia/201102/1626/37128.html
https://www.kanunu8.com/wuxia/201102/1626/37129.html
https://www.kanunu8.com/wuxia/201102/1626/37130.html
https://www.kanunu8.com/wuxia/201102/1626/37131.html
https://www.kanunu8.com/wuxia/201102/1626/37132.html
https://www.kanunu8.com/wuxia/201102/1626/37133.html
https://www.kanunu8.com/wuxia/201102/1626/37134.html
https://www.kanunu8.com/wuxia/201102/1626/37135.html
https://www.kanunu8.com/wuxia/201102/1626/37136.html
https://www.kanunu8.com/wuxia/201102/1626/37137.html
https://www.kanunu8.com/wuxia/201102/1626/37138.html
https://www.kanunu8.com/wuxia/201102/1626/37139.html
https://www.kanunu8.com/wuxia/201102/1626/37140.html
https://www.kanunu8.com/wuxia/201102/1626/37141.html
https://www.kanunu8.com/wuxia/201102/1626/37142.html
https://www.kanunu8.com/wuxia/201102/1626/37143.html
https://www.kanunu8.com/wuxia/201102/1626/37144.html
https://www.kanunu8.com/wuxia/201102/1626/37145.html
https://www.kanunu8.com/wuxia/201102/1626/37146.html
https://www.kanunu8.com/wuxia/201102/1626/37147.html
https://www.kanunu8.com/wuxia/201102/1626/37148.html
https://www.kanunu8.com/wuxia/201102/1626/37149.html
https://www.kanunu8.com/wuxia/201102/1626/37150.html
https://www.kanunu8.com/wuxia/201102/1626/37151.html
https://www.kanunu8.com/wuxia/201102/1626/37152.html
https://www.kanunu8.com/wuxia/201102/1626/37153.html
https://www.kanunu8.com/wuxia/201102/1626/37154.html
https://www.kanunu8.com/wuxia/201102/1626/37155.html
https://www.kanunu8.com/wuxia/201102/1626/37156.html
https://www.kanunu8.com/wuxia/201102/1626/37157.html
https://www.kanunu8.com/wuxia/201102/1626/37158.html
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
  text = data.decode(encoding, errors='replace')
  doc = pyquery.PyQuery(text)
  title = doc('h2 font').text()
  content = doc('p').text()
  return (title, content)

if not db_file.exists():
  with connect() as conn:
    conn.execute("CREATE TABLE dump (url TEXT PRIMARY KEY, data BLOB);")
