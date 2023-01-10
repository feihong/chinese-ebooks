"""
Generate epub file for the chapter with the given title.

Works by generating a markdown file for each chapter, then converting that markdown file to epub.
"""
import sys
from pathlib import Path
import subprocess
import util

def generate_epub(markdown_file: Path, title, author):
  cmd = [
    'ebook-convert',
    markdown_file,
    markdown_file.with_suffix('.epub'),
    '--authors', author,
    '--title', title,
  ]
  subprocess.run(cmd)

def generate_markdown_file(markdown_file, chapter, title):
  with markdown_file.open('w') as fp:
    lines = chapter['body'].splitlines()

    fp.write(f'# {title}\n\n')
    for i, line in enumerate(lines, 1):
      fp.write(f'<span style="font-size:x-small;color:#888">{i}</span> {line}\n\n')


argument = sys.argv[1]
if argument.isdigit():
  index = int(argument)
  chapter = util.get_chapters()[index - 1]
else:
  print(f'Looking for chapter with title "{title}"')
  chapter = [c for c in util.get_chapters() if c['title'] == title][0]

title = util.title + ' ' + chapter['title']

markdown_file = (util.output_dir / title).with_suffix('.md')

generate_markdown_file(markdown_file, chapter, title)

generate_epub(markdown_file, title=title, author=util.author)
