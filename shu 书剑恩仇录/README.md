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

Paste the links into `util.py`
