run:
	@python app.py --file sample/wordcount.txt

serve:
	@python srv.py

pip-clean:
	@pip freeze | xargs pip uninstall -y

prepare:
	@pip install -r requirements.txt
	@pip freeze
