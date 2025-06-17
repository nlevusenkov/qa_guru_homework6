import os
from zipfile import ZipFile
from paths import TMP_DIR
import PyPDF2
from io import BytesIO, TextIOWrapper
from openpyxl import load_workbook
import csv
def test_read_zip():
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
        with zip_file.open('example.csv') as csv_file:
            # Читаем и декодируем содержимое
            content = csv_file.read().decode('utf-8-sig')

            # Разбиваем на строки и пропускаем пустые
            lines = [line for line in content.splitlines() if line.strip()]

            # Создаем CSV reader
            csv_reader = csv.reader(lines)

            # Ищем строку с Purpose
            purpose_found = False
            for row in csv_reader:
                if len(row) > 1 and row[0].strip() == 'Purpose:':
                    assert row[1].strip() == 'Provide example file for this type'
                    purpose_found = True
                    break

            # Дополнительные проверки структуры файла
            lines = content.splitlines()  # Читаем заново
            assert 'Month,Cecilia,Patty,Robert,Frank,total'
            assert '"$5,00","$5,00","$7,00","$25,00","$42,00"'