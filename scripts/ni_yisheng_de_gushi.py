from shu.kanunu import make_ebook


make_ebook(
    index_url='https://www.kanunu8.com/book3/6460/index.html',
    title='你一生的故事',
    author='特德·姜',
    index_table_selector='table[cellpadding="8"]',
    output_file='books/ni yisheng de gushi',
    formats=['.md', '.mobi'])
