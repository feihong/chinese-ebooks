# Chinese eBooks

Some examples of how to generate Chinese ebooks

## Prerequisites

    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    # Update ~/.profile and ~/.bashrc according to instructions, then logout and login

    apt-get install calibre

## Installation

Install Python dependencies

    make install

## Links

[ebook-convert documentation](https://manual.calibre-ebook.com/generated/en/ebook-convert.html)

## Notes

The hanzi list comes from http://crr.ugent.be/programs-data/subtitle-frequencies/subtlex-ch.

The `chardet` package isn't very good at detecting GBK-encoded text, it tends to confuse it with GB2312.
