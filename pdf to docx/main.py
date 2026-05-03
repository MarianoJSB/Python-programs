from pdf2docx import Converter

#pdf file path to convert
pdf = 'pdfs/pdf_file_name.pdf'
#docx file path to save
word = 'docs/doc_file_name.docx'

cv = Converter(pdf)
cv.convert(word)
cv.close()