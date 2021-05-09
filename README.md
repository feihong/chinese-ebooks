# Chinese eBooks

Scripts for generating some Chinese ebooks

## Installation

    pipenv install

To generate MOBI, ePub, or other non-plain-text ebooks, you must install [Calibre](https://calibre-ebook.com/).

Calibre's `ebook-convert` command must be on your path.

```
ln -s /Applications/calibre.app/Contents/console.app/Contents/MacOS/ebook-convert /usr/local/bin/ebook-convert
```

## Commands

Create ebook from script

    pipenv run scripts/mingchao_na_xie_shi.py

## References

[ebook-convert documentation](https://manual.calibre-ebook.com/generated/en/ebook-convert.html)
