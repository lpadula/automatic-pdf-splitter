# Automatic PDF Splitter

This script can create new single-page PDFs files from multipaged PDFs.

## Requirements

Python 3.0+

```
# Debian distros
sudo apt-get install python3
```

PyPDF2

```
pip install PyPDF2
```

## Usage

1. First copy all PDFs files you want to split into "to-split" directory.
2. Execute in the terminal: 

```
automatic_pdf_splitter.py
```

3. You will find splitted files on "splitted" directory.