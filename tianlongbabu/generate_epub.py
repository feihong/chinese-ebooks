"""
Generate epub file. Breaks down each chapter into subsections where each subsection has at most 50 paragraphs.

Works by generating a markdown file, then converting that markdown file to epub.
"""
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
    '--chapter', "//*[name()='h1' or name()='h2']"
  ]
  subprocess.run(cmd)

def generate_markdown_file(markdown_file, chapters):
  with markdown_file.open('w') as fp:
    for chapter in chapters:
      lines = chapter['body'].splitlines()

      title = chapter['title']
      fp.write(f'# {title}\n\n') 
      for i, line in enumerate(lines, 1):
        if (i-1) % 50 == 0:
          end = min(len(lines), i+49)
          fp.write(f'## {title} {i}-{end}\n\n')

        fp.write(f'<span style="font-size:x-small;color:#888">{i}</span> {line}\n\n')


markdown_file = (util.output_dir / util.title).with_suffix('.md')
generate_markdown_file(markdown_file, util.get_chapters())
generate_epub(markdown_file, title=util.title, author=util.author)
