import sqlite3
from pathlib import Path

here = Path(__file__).parent

index_url = 'https://www.kanunu8.com/book/4600/index.html'
title = '书剑恩仇录'
author = '金庸'
description = '清乾隆年间，江南武林帮会红花会总舵主于万亭带同四当家(奔雷手)文泰来夜闯清廷禁宫。总舵主于万亭见过乾隆后，遭清兵毒手，死前立下遗命，由年轻义子陈家洛接任总舵主之位，并要帮众誓必护卫拥戴这位翩翩风度的世家公子，红花会上下马上准备最隆重的接任大礼，准备迎接陈家洛继位总舵主之位。隐身于陕西扶风延绥镇总兵李可秀家为西宾的武当派名宿陆菲青，随主人新迁浙江水陆提督前往江南的途中，遇上参加(千里接龙头)仪式，却被朝廷鹰爪困在三道沟客栈的红花会四当家文泰来与其妻骆冰，陆菲青出手相救，将他们荐至西北武林英雄铁胆周仲英处避难。适逢周仲英外出，以陆菲青之师弟、武当派高手、卖身清廷的火手判官张召重为首的朝廷鹰爪尾随前来，周仲英之幼子不慎透露出文泰来等人藏身之处，激战之余，文泰来被捕，骆冰与红花会坐十四把交椅的余鱼同逃出。周仲英外出归来，恼怒异常，红花会众英雄赶来铁胆庄，因误以为文泰来被出卖，双方交手，混战一场。红花会新任总舵主陈家洛赶来以百花错拳胜周仲英，后得知周仲英之子只有十岁，才知错怪对方，握手言和。为救文泰来，众英雄堵截镖行车队与为抢回圣物《可兰经》的回族人相遇，陈家洛出手相救，与人称翠羽黄衫的族长之女霍青桐彼此惺惺相惜，并肩作战，几经波折，终于为霍青桐取回圣典《可兰经》.....'

markdown_file = (here / title).with_suffix('.md')
epub_file = markdown_file.with_suffix('.epub')

db_file = here / 'dump.db'

def connect():
  return sqlite3.connect(db_file)

if not db_file.exists():
  with connect() as conn:
    conn.execute("CREATE TABLE dump (url TEXT PRIMARY KEY, data BLOB);")
    conn.execute("CREATE TABLE links (url TEXT PRIMARY KEY, num INT);")
