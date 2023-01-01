# Chinese eBooks

Some examples of how to generate Chinese ebooks

## Prerequisites

Python 3.

On Linux, install Calibre by running

    apt-get install calibre

On Mac, download Calibre and install from dmg file. Add `/Applications/calibre.app/Contents/MacOS/` to your path to access Calibre's command line tools.

## Installation

Install Python dependencies

    make install

## Links

[ebook-convert documentation](https://manual.calibre-ebook.com/generated/en/ebook-convert.html)

## Notes

The hanzi list comes from http://crr.ugent.be/programs-data/subtitle-frequencies/subtlex-ch.

The `chardet` package isn't very good at detecting GBK-encoded text, it tends to confuse it with GB2312.
