run:
	python app.py --file sample/wordcount.txt

serve:
	python3 -m http.server 9000

pip-clean:
	pip freeze | xargs pip uninstall -y

prepare:
	pip install -r requirements.txt
	pip freeze
