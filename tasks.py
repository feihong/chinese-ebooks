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
    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css" integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb" crossorigin="anonymous">
  </head>
<body class="container">
{body}
</body>
</html>"""
