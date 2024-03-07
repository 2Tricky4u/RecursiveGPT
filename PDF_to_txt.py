from PyPDF2 import PdfReader

LOCATION = 'test.pdf'

reader = PdfReader(LOCATION)

file_name = 'Devillers_u.txt'
with open(file_name, 'a+', encoding="utf-8") as f:
    for i,page in enumerate(reader.pages):
        f.write(page.extract_text())