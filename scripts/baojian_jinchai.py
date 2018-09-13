from shu.kanunu import make_ebook


make_ebook(
    index_url='https://www.kanunu8.com/wuxia/201103/2335.html',
    title='宝剑金钗',
    author='王度庐',
    index_table_selector='table[cellpadding="7"]',
    output_file='books/baojian jinchai',
    formats=['.md', '.mobi', '.epub'])
