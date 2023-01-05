from PyPDF2 import PdfFileWriter, PdfFileReader
from getpass import getpass

pdfwriter = PdfFileWriter()
pdf = PdfFileReader('encrypt-pdf\Python. К вершинам мастерства.pdf')

for page in range(pdf.numPages):
    pdfwriter.add_page(pdf.pages[page]) #читаем и добавляем каждую страницу

password = getpass(prompt='Введите пароль: ')
pdfwriter.encrypt(password)

with open('encrypt-pdf\protected.pdf', 'wb') as file: #открываем файл на запись в бинарном режиме
    pdfwriter.write(file)
