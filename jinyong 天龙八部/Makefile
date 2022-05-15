download:
	PYTHONPATH=. python ../download_content.py

book:
	PYTHONPATH=. python ../generate_ebook.py

vocab:
	PYTHONPATH=. python ../generate_vocab.py

serve:
	PYTHONPATH=. FLASK_APP=../app.py flask run

clean:
	rm *.markdown; rm *.epub; rm *.txt
