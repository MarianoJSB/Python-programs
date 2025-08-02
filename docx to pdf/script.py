import os
import subprocess
try:
    # How i don't have Microsoft Word i use libreoffice
    libreoffice_path = r"C:\Program Files\LibreOffice\program\soffice.exe"
    docx_name = input("Enter full name script to convert: ")
    pdf_name = input("Enter the name of the pdf as you want to save it: ")

    os.makedirs("tmp")

    subprocess.run([libreoffice_path, "--headless", "--convert-to", "pdf", f"{docx_name}.docx", "--outdir", "tmp"], check=True)

    os.rename(os.path.join("tmp/document.pdf"), f"{pdf_name}.pdf")
    print("--!FILE CONVERTED¡--")
except Exception as e:
    print(F"AN ERROR HAS OCCURRED \n{e}")