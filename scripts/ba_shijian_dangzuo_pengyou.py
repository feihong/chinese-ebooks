from shu import KanunuMultiVolumeScraper, make_ebook


# class MyScraper(KanunuMultiVolumeScraper):


make_ebook(
    KanunuMultiVolumeScraper,
    index_url = 'http://www.kanunu8.com/book3/8064/index.html',
    title = '把时间当作朋友',
    author = '李笑来',
    output_file='books/ba shijian dangzuo pengyou')
