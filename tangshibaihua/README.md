# 唐诗百话

http://www.guoxue123.com/new/0002/tsbh/index.htm

## Get content page links

You need to grab the content links for the book, and this can be achieved by running a simple script in the browser.
Visit the index page (see `util.py`), open the dev console, and run the following code:

```
links = []
document.querySelectorAll('a').forEach(anchor => {
  let href = anchor.href
  let match = href.match(/(.*\/)(\d+\.htm)$/)
  if (match === null) {
    return
  }
  links.push(href)
})
console.log(`Found ${links.length} links:`)
console.log(links.join('\n'))
```

What it does: it prints out the links that end with `(number).html`.

Paste the links into `util.py`, inside the `link` multiline string.

# Commands

Download content pages

    make download

Generate ebook

    make book

Start web app on http://localhost:5000 to browse downloaded pages by URL

    make serve
