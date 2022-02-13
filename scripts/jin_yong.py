"""
All Jin Yong novels:

https://en.wikipedia.org/wiki/Jin_Yong#Novels

"""
from shu.kanunu import make_ebook


BOOKS = """
http://www.kanunu8.com/book/4600/index.html 书剑恩仇录 shu jian en chou lu
http://www.kanunu8.com/wuxia/201102/1622.html 碧血剑 bi xue jian
http://www.kanunu8.com/wuxia/201102/1625.html 射雕英雄传 she diao yingxiong zhuan
""".strip().splitlines()
BOOKS = [line.split(' ', 2) for line in BOOKS]


for url, title, output_file in BOOKS:
    make_ebook(
        index_url=url,
        title=title,
        author='金庸',
        formats=['.mobi', '.epub'],
        output_file=f'books/{output_file}'
    )
