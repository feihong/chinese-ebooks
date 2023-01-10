import util


def generate_chapter(chapter):
  template = util.get_template('site-chapter.html')
  output = template.render(title=chapter['title'], body_lines=chapter['body'].splitlines())
  output_file=(util.output_dir / chapter['title']).with_suffix('.html')
  output_file.write_text(output)


def generate_index(chapters):
  template = util.get_template('site-index.html')
  output = template.render(title=util.title, chapters=chapters)
  output_file = util.output_dir / 'index.html'
  output_file.write_text(output)
  

if __name__ == '__main__':
  chapters = util.get_chapters()

  generate_index(chapters)

  for chapter in chapters:
    generate_chapter(chapter)
