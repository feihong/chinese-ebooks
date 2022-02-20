from flask import Flask, g, request, make_response
import jinja2
import util

app = Flask(__name__)

def get_db():
  db = getattr(g, '_database', None)
  if db is None:
    db = g._database = util.connect()
  return db

@app.teardown_appcontext
def close_connection(_exception):
  db = getattr(g, '_database', None)
  if db is not None:
    db.close()

@app.route("/")
def index():
  urls = (url for (url,) in get_db().execute('SELECT url FROM dump'))
  return index_tmpl.render(urls=urls)

@app.route("/row")
def row():
  url = request.args['url']
  data, = get_db().execute('SELECT data FROM dump WHERE url = ?', (url,)).fetchone()
  response = make_response(data)
  response.headers.set('Content-Type', 'text/html')
  return response

@app.route("/pretty")
def pretty():
  url = request.args['url']
  data, = get_db().execute('SELECT data FROM dump WHERE url = ?', (url,)).fetchone()
  title, content = util.parse_page(data)
  paragraphs = (p for p in content.split('\n') if p.strip())
  return pretty_tmpl.render(title=title, paragraphs=paragraphs)

index_tmpl = jinja2.Template("""
<!doctype html>
<html lang="en">
<body>
  <ol>
    {%for url in urls %}
      <li>
        <a href="/row?url={{ url }}"> {{ url }} </a>
        (<a href="/pretty?url={{ url }}">pretty</a>)
      </li>
    {% endfor %}
  </ol>
</body>
</html>
""")

pretty_tmpl = jinja2.Template("""
<!doctype html>
<html lang="en">
<head>
  <style>
  body { font-size: 14pt; }
  span { font-size: 10pt; color: #999; }
  </style>
</head>
<body>
  <b>{{ title }}</b>
  {% for para in paragraphs %}
    <p><span>{{ loop.index }}</span> {{ para }}</p>
  {% endfor %}
</body>
</html>
""")
