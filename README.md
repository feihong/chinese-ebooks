# Chinese eBooks

Scripts for generating some Chinese ebooks

## Prerequisites

    curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
    # Update ~/.profile and ~/.bashrc according to instructions, then logout and login

    apt-get install calibre

## Installation

    make install

## Commands

Create ebook from script

    pipenv run python scripts/mingchao_na_xie_shi.py

## References

[ebook-convert documentation](https://manual.calibre-ebook.com/generated/en/ebook-convert.html)

## Notes

The hanzi list comes from http://crr.ugent.be/programs-data/subtitle-frequencies/subtlex-ch
