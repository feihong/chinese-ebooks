from shu.kanunu import KanunuScraper
from shu.base import Node

class MyScraper(KanunuScraper):
    def get_title_and_links(self, doc):
        table = doc('dl')
        for anchor in table('dd a'):
            yield (
                anchor.text_content(),
                str(self.base_url / anchor.get('href')))

    def get_content_tree(self, doc):
        root = Node(title='root')
        for title, link in self.get_title_and_links(doc):
            doc = self.get_doc(link)
            chapter = Node(title=title)
            paras = (p.text_content().strip() for p in doc('div.text p:not([align])'))
            chapter.content = '\n\n'.join(paras)
            root.append(chapter)
        return root


index_url='https://www.kanunu8.com/book2/11011/index.html'
title='半生缘'
author='张爱玲'
output_file='books/ban_sheng_yuan'
formats=['.md', '.mobi']

scraper = MyScraper(index_url=index_url, title=title, author=author)
scraper.download()
scraper.build_ebook(output_file, formats=formats)
