book: markdown epub

epub:
	PYTHONPATH=. python ../generate_epub.py

markdown:
	python generate_markdown.py

vocab:
	PYTHONPATH=. python ../generate_vocab.py

serve:
	PYTHONPATH=. FLASK_APP=../app.py flask run

clean:
	rm *.markdown; rm *.epub; rm *.txt
