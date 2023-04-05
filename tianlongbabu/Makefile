json:
	python generate_json.py

chapters:
	python print_chapters.py

site:
	python generate_site.py

epub:
	python generate_epub.py

doc:
	python generate_doc.py ${doc}

vocab:
	PYTHONPATH=. python ../generate_vocab_epubs.py

clean:
	rm output/*.md; rm output/*.epub; rm output/*.html
