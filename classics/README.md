# Classic Children's Novels

Sources:

- 夏洛的网
  - https://www.99csw.com/book/2141/index.htm
  - https://xialuodewang.chibaba.cn (formatting issues)
  - https://www.kanunu8.com/book3/8145/index.html (formatting issues)
- 蝇王
  - https://yingwang.chibaba.cn/
  - https://www.99csw.com/book/9253/index.htm
- 秘密花园
  - https://mimihuayuan.chibaba.cn/
  - https://www.99csw.com/book/1723/index.htm
- 记忆传授人
  - https://www.99csw.com/book/6158/index.htm

## Script to collect chapter links

```javascript
{
  const host = `${document.location.protocol}//${document.location.hostname}`
  const chapters =
    [...document.querySelectorAll('#dir a')]
    .map(node => {
      return {
        title: node.innerText,
        link: `${host}${node.getAttribute('href')}`
      }
    })

  const toc = JSON.stringify(chapters, null, 2)
  console.log(toc)
  localStorage.setItem('toc', toc)
}
```

## Bookmarklet to scrape chapter contents

```javascript
const lines =
  [...document.querySelectorAll('#content div')]
  .filter(node => node.offsetParent !== null)
  .map(node => node.innerText);
const content = JSON.stringify(lines, null, 2);
console.log(content);
localStorage.setItem(window.location.href, content);
```

## Script to collate JSON for all captured chapters

```javascript
{
  const toc = JSON.parse(localStorage.getItem('toc'))
  const chapters = []
  for (const chapter of toc) {
    const content = localStorage.getItem(chapter.link)
    if (content !== null) {
      chapter.content = JSON.parse(content)
      chapters.push(chapter)
    }
  }
  const output = JSON.stringify(chapters, null, 2)
  console.log(output)
}
```

## Script to clear localStorage

```javascript
{
  const toc = JSON.parse(localStorage.getItem('toc'))
  for (const chapter of toc) {
    localStorage.removeItem(chapter.link)
  }
  localStorage.removeItem('toc')
}
```
