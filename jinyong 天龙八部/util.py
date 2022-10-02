import sqlite3
from pathlib import Path
import pyquery

here = Path(__file__).parent

# index_url = 'https://www.kanunu8.com/wuxia/201102/1626.html'
# encoding = 'gbk'
title = '天龙八部'
author = '金庸'
description = '小说以宋哲宗时代为背景，通过宋、辽、大理、西夏、吐蕃及女真等王国之间的武林恩怨和民族矛盾，从哲学的高度对人生和社会进行审视和描写，展示了一幅波澜壮阔的生活画卷。所谓“天龙八部”是佛经用语，包括八种神道怪物，作者以此为书名，旨在象征大千世界之中形形色色的人物。小说叙云南大理国武林世家镇南王之子段誉，为逃避习武，来至无量山中，因种种机遇，学得一身古怪奇妙的武功，并先后结识少女钟灵、木婉清，互相悦慕，岂料此二人是父亲段正淳四处留情的私生女。四大恶人之首段延庆本该是大理国王位的真正继承人，因宫中内乱流落江湖。。。。'

markdown_file = (here / title).with_suffix('.markdown')
epub_file = (here / title).with_suffix('.epub')

hanzi_file = here.parent / 'hanzi.txt'
ignore_file = here.parent / 'ignore.txt'
vocab_file = here / (title + ' 生词.txt')
