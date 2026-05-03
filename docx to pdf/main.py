from docx2pdf import convert

#docx file path 
docx = 'docs/docx_file_name.docx'
#pdf file name to save
pdf_name = input("Enter pdf file name to save: ")

def docxConverter(doc, name):
    return convert(doc, f"pdfs/{name}.pdf")

save_1 = docxConverter(docx, pdf_name)
if save_1 == None:
    print("docx converted to pdf")
else:
    print("ERROR")
