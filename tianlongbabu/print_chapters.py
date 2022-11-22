import util

for i, chapter in enumerate(util.get_chapters(), 1):
  print(f"{i}. {chapter['title']}")
