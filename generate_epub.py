import subprocess
import util

cmd = [
  'ebook-convert',
  util.markdown_file,
  util.epub_file,
  '--authors', util.author,
  '--title', util.title,
  '--comments', util.description,
  '--chapter', "//*[name()='h2' or name()='h3']"
]
subprocess.run(cmd)
