Index page: https://www.kanunu8.com/book/4600/index.html

Run this script in console to get all content links:

```
links = []
document.querySelectorAll('a').forEach(anchor => {
  let href = anchor.href
  let match = href.match(/(.*\/)(\d+\.html)$/)
  if (match === null) {
    return
  }
  if (location.href.startsWith(match[1])) {
    links.push(href)
  }
})
console.log(links.join('\n'))
```

What it does: Only grabs the links that like https://www.kanunu8.com/book/4600/61044.html, e.g. end with
`(number).html` and have a common path with the index page.

Paste the links into `util.py`
