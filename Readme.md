# Web version of Word Count
This is a simple web version of word count. 

It is implemented using Python and [PyScript](https://pyscript.net/).

The main motivation is to learn how to **implement a a file upload and processing in the browser**.

## Requirements
- Python 3.11
- Rich
- Click (CLI version of the APP)

## Installation
```make prepare ``` / ```pip install -r requirements.txt```

## Usage

### CLI
``` make run ``` / ```python app.py --file sample/wordcount.txt```
### Web
``` make serve ``` / ```python3 -m http.server 9000```

## Helpful sources
Some of the stuff used to learn how to implement this:
- https://docs.pyscript.net/2024.8.1/
- https://blog.logrocket.com/pyscript-run-python-browser/
- https://stackoverflow.com/questions/74859112/how-to-import-remote-python-files-using-pyscript
