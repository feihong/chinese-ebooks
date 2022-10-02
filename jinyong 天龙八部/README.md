Source: https://github.com/hankinghu/literature-books/blob/master/天龙八部.txt


## Get content page links

You need to grab the content links for the book, and this can be achieved by running a simple script in the browser.
Visit the index page (see `util.py`), open the dev console, and run the following code:

```
prefix = 'https://www.kanunu8.com/wuxia/201102/1626/'
links = []
document.querySelectorAll('a').forEach(anchor => {
  let href = anchor.href
  let match = href.match(/(.*\/)(\d+\.html)$/)
  if (match === null) {
    return
  }
  if (href.startsWith(prefix)) {
    links.push(href)
  }
})
console.log(`Found ${links.length} links:`)
console.log(links.join('\n'))
```

What it does: it prints out the links that look like https://www.kanunu8.com/book/4600/61044.html, i.e. end with
`(number).html` and have a common path with the index page.

Paste the links into `util.py`, inside the `link` multiline string.

# Commands

Generate ebook

    make book

Generate vocabulary document

    make vocab

Start web app on http://localhost:5000 to browse downloaded pages by URL

    make serve
