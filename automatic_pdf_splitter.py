#!/usr/bin/python
import os

from PyPDF2 import PdfFileWriter, PdfFileReader

# Folder Path
path = "to-split"
  
os.chdir(path)

dirPath = os.path.dirname(os.path.realpath(__file__))

# Read File
def read_text_file(file_path):
    with open(file_path, 'r') as f:
        print(f.read())
  
# Iterate through all files
for file in os.listdir():
    # Check if file is in pdf format
    if file.endswith(".pdf"):
        file_path = f"{dirPath}/{path}/{file}"
        inputpdf = PdfFileReader(open(file_path , "rb"))

        for i in range(inputpdf.numPages):
            output = PdfFileWriter()
            output.addPage(inputpdf.getPage(i))
            with open(dirPath+"/splited/page_%s.pdf" % i, "wb") as outputStream:
                output.write(outputStream)