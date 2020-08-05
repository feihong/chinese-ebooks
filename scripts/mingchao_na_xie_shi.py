from pathlib import Path
from shu.kanunu import make_ebook


urls = """
http://www.kanunu8.com/files/chinese/201102/1777.html
http://www.kanunu8.com/files/chinese/201102/1778.html
http://www.kanunu8.com/files/chinese/201102/1766.html
http://www.kanunu8.com/files/chinese/201102/1779.html
http://www.kanunu8.com/files/chinese/201102/1780.html
http://www.kanunu8.com/files/chinese/201102/1767.html
http://www.kanunu8.com/files/chinese/201102/1781.html
""".strip().splitlines()


def make(index_url, number, index_table_selector):
    output_file = f'books/mingchao na xie shi {number}'
    print(output_file)
    make_ebook(
        index_url=index_url,
        title=f'明朝那些事儿{number}',
        author='当年明月',
        output_file=output_file,
        formats=['.md', '.mobi'],
        index_table_selector=index_table_selector,
    )


if __name__ == '__main__':
    for number, url in enumerate(urls, 1):
        its = ('table[cellpadding="7"]'
            if number in (3, 6)
            else 'table[cellpadding="8"]')
        make(index_url=url, number=number, index_table_selector=its)
