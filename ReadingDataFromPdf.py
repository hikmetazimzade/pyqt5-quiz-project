from PyPDF2 import PdfReader
pdf_name = input("Input pdf name:")

with open("data/tests.txt", mode ="r", encoding ='utf-8') as read_file:
    length = len(read_file.readlines())

if length == 0:
    reader = PdfReader(pdf_name)
    with open("data/tests.txt", mode ="a", encoding="utf-8") as file:
        for i in reader.pages:
            file.write(i.extract_text())