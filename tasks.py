from pathlib import Path
from invoke import task
import markdown2


@task
def md_to_html(ctx, input_file, output_file):
    output = markdown2.markdown(
        Path(input_file).read_text(),
        extras=['toc'])
    html = HTML_TEMPLATE.format(body=output.toc_html + '\n\n' + output)
    Path(output_file).write_text(html)


HTML_TEMPLATE = """\
<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <title>EBook</title>
  <link rel="stylesheet" href="//fonts.googleapis.com/css?family=Roboto:300,300italic,700,700italic">
  <link rel="stylesheet" href="//cdn.rawgit.com/necolas/normalize.css/master/normalize.css">
  <style>
    body {{
        font-family: 'Roboto', 'Helvetica Neue', 'Helvetica', 'Arial', sans-serif;
    }}
  </style>
</head>
<body>
  <main class="container">
    {body}
  </main>
</body>
</html>"""
