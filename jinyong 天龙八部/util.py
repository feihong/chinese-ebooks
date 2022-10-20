import json
import re
from pathlib import Path


here = Path(__file__).parent

title = '天龙八部'
author = '金庸'
description = '小说以宋哲宗时代为背景，通过宋、辽、大理、西夏、吐蕃及女真等王国之间的武林恩怨和民族矛盾，从哲学的高度对人生和社会进行审视和描写，展示了一幅波澜壮阔的生活画卷。所谓“天龙八部”是佛经用语，包括八种神道怪物，作者以此为书名，旨在象征大千世界之中形形色色的人物。小说叙云南大理国武林世家镇南王之子段誉，为逃避习武，来至无量山中，因种种机遇，学得一身古怪奇妙的武功，并先后结识少女钟灵、木婉清，互相悦慕，岂料此二人是父亲段正淳四处留情的私生女。四大恶人之首段延庆本该是大理国王位的真正继承人，因宫中内乱流落江湖。。。。'

# Download text file from
# https://raw.githubusercontent.com/hankinghu/literature-books/master/%E5%A4%A9%E9%BE%99%E5%85%AB%E9%83%A8.txt
input_file = Path(title).with_suffix('.txt')

json_file = input_file.with_suffix('.json')
highlights_file = here / 'highlights.txt'
output_dir = here / 'output'

hanzi_file = here.parent / 'hanzi.txt'
ignore_file = here.parent / 'ignore.txt'

def get_chapters():
  with json_file.open() as fp:
    chapters = json.load(fp)
  return chapters

def get_current_chapter_title():
  chapter = None

  with highlights_file.open() as fp:
    for line in fp:
      line = line.strip()
      if line and not re.match(r'[\d ]+', line):
        chapter = line

  return chapter

def get_current_chapter():
  title = get_current_chapter_title()
  for chapter in get_chapters():
    if chapter['title'] == title:
      return chapter
