import sqlite3
from pathlib import Path

here = Path(__file__).parent

index_url = 'https://www.kanunu8.com/book/4600/index.html'
title = '书剑恩仇录'
author = '金庸'
description = '清乾隆年间，江南武林帮会红花会总舵主于万亭带同四当家(奔雷手)文泰来夜闯清廷禁宫。总舵主于万亭见过乾隆后，遭清兵毒手，死前立下遗命，由年轻义子陈家洛接任总舵主之位，并要帮众誓必护卫拥戴这位翩翩风度的世家公子，红花会上下马上准备最隆重的接任大礼，准备迎接陈家洛继位总舵主之位。隐身于陕西扶风延绥镇总兵李可秀家为西宾的武当派名宿陆菲青，随主人新迁浙江水陆提督前往江南的途中，遇上参加(千里接龙头)仪式，却被朝廷鹰爪困在三道沟客栈的红花会四当家文泰来与其妻骆冰，陆菲青出手相救，将他们荐至西北武林英雄铁胆周仲英处避难。适逢周仲英外出，以陆菲青之师弟、武当派高手、卖身清廷的火手判官张召重为首的朝廷鹰爪尾随前来，周仲英之幼子不慎透露出文泰来等人藏身之处，激战之余，文泰来被捕，骆冰与红花会坐十四把交椅的余鱼同逃出。周仲英外出归来，恼怒异常，红花会众英雄赶来铁胆庄，因误以为文泰来被出卖，双方交手，混战一场。红花会新任总舵主陈家洛赶来以百花错拳胜周仲英，后得知周仲英之子只有十岁，才知错怪对方，握手言和。为救文泰来，众英雄堵截镖行车队与为抢回圣物《可兰经》的回族人相遇，陈家洛出手相救，与人称翠羽黄衫的族长之女霍青桐彼此惺惺相惜，并肩作战，几经波折，终于为霍青桐取回圣典《可兰经》.....'
links = '''
https://www.kanunu8.com/book/4600/61015.html
https://www.kanunu8.com/book/4600/61016.html
https://www.kanunu8.com/book/4600/61017.html
https://www.kanunu8.com/book/4600/61018.html
https://www.kanunu8.com/book/4600/61019.html
https://www.kanunu8.com/book/4600/61020.html
https://www.kanunu8.com/book/4600/61021.html
https://www.kanunu8.com/book/4600/61022.html
https://www.kanunu8.com/book/4600/61023.html
https://www.kanunu8.com/book/4600/61024.html
https://www.kanunu8.com/book/4600/61025.html
https://www.kanunu8.com/book/4600/61026.html
https://www.kanunu8.com/book/4600/61027.html
https://www.kanunu8.com/book/4600/61028.html
https://www.kanunu8.com/book/4600/61029.html
https://www.kanunu8.com/book/4600/61030.html
https://www.kanunu8.com/book/4600/61031.html
https://www.kanunu8.com/book/4600/61032.html
https://www.kanunu8.com/book/4600/61033.html
https://www.kanunu8.com/book/4600/61034.html
https://www.kanunu8.com/book/4600/61035.html
https://www.kanunu8.com/book/4600/61036.html
https://www.kanunu8.com/book/4600/61037.html
https://www.kanunu8.com/book/4600/61038.html
https://www.kanunu8.com/book/4600/61039.html
https://www.kanunu8.com/book/4600/61040.html
https://www.kanunu8.com/book/4600/61041.html
https://www.kanunu8.com/book/4600/61042.html
https://www.kanunu8.com/book/4600/61043.html
https://www.kanunu8.com/book/4600/61044.html
https://www.kanunu8.com/book/4600/61045.html
https://www.kanunu8.com/book/4600/61046.html
https://www.kanunu8.com/book/4600/61047.html
https://www.kanunu8.com/book/4600/61048.html
https://www.kanunu8.com/book/4600/61049.html
https://www.kanunu8.com/book/4600/61050.html
https://www.kanunu8.com/book/4600/61051.html
https://www.kanunu8.com/book/4600/61052.html
https://www.kanunu8.com/book/4600/61053.html
https://www.kanunu8.com/book/4600/61054.html
'''.strip().splitlines()

markdown_file = (here / title).with_suffix('.markdown')
epub_file = (here / title).with_suffix('.epub')

db_file = here / 'dump.db'

def connect():
  return sqlite3.connect(db_file)

if not db_file.exists():
  with connect() as conn:
    conn.execute("CREATE TABLE dump (url TEXT PRIMARY KEY, data BLOB);")
