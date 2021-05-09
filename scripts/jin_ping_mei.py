from urlpath import URL
from shu.base import Node, BookScraper


class EnjingScraper(BookScraper):
    def __init__(self, **kwargs):
        super(EnjingScraper, self).__init__(**kwargs)
        self.base_url = URL(self.index_url)

    def get_title_and_links(self, doc):
        for anchor in doc('div.book-list ul li a'):
            yield (
                anchor.text_content(),
                str(self.base_url / anchor.get('href')))

    def get_links(self, doc):
        for title, link in self.get_title_and_links(doc):
            yield link

    def get_content_tree(self, doc):
        root = Node(title='root')
        for title, link in self.get_title_and_links(doc):
            doc = self.get_doc(link)
            chapter = Node(title=title)
            paras = (p.text_content().strip() for p in doc('#nr1 p'))
            chapter.content = '\n\n'.join(paras)
            root.append(chapter)
        return root


index_url='https://www.enjing.com/jinping/'
title='金瓶梅'
author='兰陵笑笑生'
output_file='books/jin_ping_mei'
formats=['.md', '.mobi']

scraper = EnjingScraper(index_url=index_url, title=title, author=author)
scraper.download()
scraper.build_ebook(output_file, formats=formats)
