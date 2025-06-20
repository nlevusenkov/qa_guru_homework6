import os
from zipfile import ZipFile
from paths import TMP_DIR
import PyPDF2
from io import BytesIO, TextIOWrapper, StringIO
from openpyxl import load_workbook
import csv
def test_read_zip(operations_with_archive):
        # Чтение pdf
    with ZipFile(os.path.join(TMP_DIR, 'test_zip.zip')) as zip_file: # открываем архив
        pdf_data = zip_file.read('example.pdf')
        pdf_reader = PyPDF2.PdfReader(BytesIO(pdf_data))
        text = pdf_reader.pages[0].extract_text()
        assert 'PDF test file' in text  # Теперь проверка корректна

        # Чтение XLSX
        xlsx_data = zip_file.read('example.xlsx')
        workbook = load_workbook(BytesIO(xlsx_data))
        sheet = workbook.active  # Получаем активный лист

        assert sheet['A1'].value == 'XLSX test file'

        # Чтение csv

        with zip_file.open('example.csv') as csv_file1:
            content = csv_file1.read().decode('utf-8-sig')
            reader = csv.DictReader(StringIO(content))
            csvreader = list(csv.reader(content.splitlines()))  # читаем содержимое файла и преобразуем его в список
            second_row = csvreader[0]  # получаем вторую строку
            assert second_row[0].strip() == 'CSV test file'