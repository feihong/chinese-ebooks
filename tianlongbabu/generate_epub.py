"""
Generate a markdown file for each chapter, then convert each markdown file to epub
"""
from pathlib import Path
import subprocess
import util

def generate_epub(markdown_file: Path, title, author, description):
  cmd = [
    'ebook-convert',
    markdown_file,
    markdown_file.with_suffix('.epub'),
    '--authors', author,
    '--title', title,
    '--comments', description,
  ]
  subprocess.run(cmd)

def generate_markdown_file(markdown_file, chapter, title):
  with markdown_file.open('w') as fp:
    lines = chapter['body'].splitlines()

    fp.write(f'# {title}\n\n')
    for i, line in enumerate(lines, 1):
      fp.write(f'<span style="font-size:x-small;color:#888">{i}</span> {line}\n\n')


chapter = util.get_current_chapter()
title = util.title + ' ' + chapter['title']

markdown_file = (util.output_dir / title).with_suffix('.md')

generate_markdown_file(markdown_file, chapter, title)

generate_epub(markdown_file, title=title, author=util.author, description=util.description)