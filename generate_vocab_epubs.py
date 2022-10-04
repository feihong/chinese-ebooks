"""
Generate a vocab epub file for each markdown file found in the output directory
"""
# from pathlib import Path
import collections
import subprocess
import json
import jieba
import util


# Global vars
ignore = set(util.ignore_file.read_text())  # symbols to ignore


def get_known_hanzi():
  known = set()
  with util.hanzi_file.open('r') as fp:
    for line in fp:
      if line.startswith('#'):
        continue

      # Only add hanzi that have an example next to them
      parts = line.split(' ')
      if len(parts) > 1:
        known.add(parts[0])

  return known

def some(seq, pred):
  for item in seq:
    if pred(item):
      return True
  return False

def get_unknown_words(text, known_hanzi):
  unknown_words = collections.Counter()

  for word in jieba.cut(text):
    if not word.strip():
      continue
    if word in ignore:
      continue

    # Add to unknown_words if word contains unknown hanzi
    if some(word, lambda c: c not in known_hanzi):
      unknown_words[word] += 1

  # Convert counter to list sorted by frequency
  return unknown_words.most_common()


def main():
  known_hanzi = get_known_hanzi()

  chapters = json.loads(util.json_file.read_bytes())
  for chapter in chapters:
    title = f'{util.title} {chapter["title"]} VOCAB'
    vocab_file = (util.output_dir / title).with_suffix('.md')

    text = f'{chapter["title"]}\n\n{chapter["body"]}'
    unknown_words = get_unknown_words(text, known_hanzi)

    with vocab_file.open('w') as fp:
      fp.write(f'# {title}\n\n')
      for word, count in unknown_words:
        fp.write(f'{word} {count} usages\n\n')

    # Convert markdown vocab file to epub
    epub_file = vocab_file.with_suffix('.epub')
    cmd = ['ebook-convert', vocab_file, epub_file, '--title', title]
    subprocess.run(cmd, stdout=subprocess.DEVNULL)
    print(f'Generated {epub_file}')

if __name__ == '__main__':
  main()
