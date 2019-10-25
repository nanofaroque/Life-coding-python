from tika import parser
import glob

import PyPDF2

# creating an object
file = open('sample_crid.pdf', 'rb')

# creating a pdf reader object
fileReader = PyPDF2.PdfFileReader(file)

# print the number of pages in pdf file
print(fileReader.numPages)

pageObj = fileReader.getPage(15)
print(pageObj.extractText())

import slate3k as slate

with open('test.pdf', 'rb') as f:
    extracted_text = slate.PDF(f)
    print(extracted_text)

print(extracted_text)
