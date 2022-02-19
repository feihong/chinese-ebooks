import jieba
import util
import generate_ebook as ebook


def segment(text): return

def get_known_hanzi():
  known = set()
  with util.hanzi_file.open('r') as fp:
    for line in fp:
      parts = line.split(' ')
      if len(parts) > 1:
        known.add(parts[0])
  return known

def get_unknown_words(text):
  for word in jieba.cut(text):
    if not word.strip():
      continue
    if word in ignore:
      continue

    unknown_count = sum(map(lambda c: c not in known, word))
    if unknown_count > 0:
      yield word

def get_chapter_word_lists():
  for _url, title, content in ebook.get_chapters():
    text = title + '\n\n' + content
    yield title, set(get_unknown_words(text))

known = get_known_hanzi()
ignore = set(util.ignore_file.read_text())
print(f'You know {len(known)} hanzi')
print(ignore)

with util.vocab_file.open('w') as fp:
  for title, words in get_chapter_word_lists():
    fp.write(f'\n## {title}\n\n')
    for word in words:
      fp.write(f'{word}\n')
