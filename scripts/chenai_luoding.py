from shu.kanunu import make_ebook


make_ebook(
    index_url='https://www.kanunu8.com/book3/7092/index.html',
    title='尘埃落定',
    author='阿来',
    index_table_selector='table[cellpadding="8"]',
    output_file='books/chenai luoding',
    formats=['.md', '.mobi'])
