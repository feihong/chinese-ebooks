import collections
import jieba
import util
import generate_ebook


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

    unknown_count = sum(map(lambda c: c not in known_hanzi, word))
    if unknown_count > 0:
      unknown_words[word] += 1  # update global unknown_words counter
      yield word

def get_chapter_word_lists():
  for _url, title, content in generate_ebook.get_chapters():
    text = title + '\n\n' + content
    yield title, set(get_unknown_words(text))

unknown_words = collections.Counter()
known_hanzi = get_known_hanzi()
ignore = set(util.ignore_file.read_text())
print(f'You know {len(known_hanzi)} hanzi')
chapter_word_lists = list(get_chapter_word_lists())

with util.vocab_file.open('w') as fp:
  for title, words in chapter_word_lists:
    fp.write(f'\n## {title}\n\n')

    words = list((w, unknown_words[w]) for w in words)
    words.sort(key=lambda pair: pair[1], reverse=True)
    for word, occurrences in words:
      fp.write(f'{word}  {occurrences}\n')
