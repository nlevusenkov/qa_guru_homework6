import os

import requests
from selene import browser, query
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from paths import TMP_DIR


def test_downlodad_pdf():
    options = webdriver.ChromeOptions()
    prefs = {
        "download.default_directory": TMP_DIR,
        "download.prompt_for_download": False
    }
    options.add_experimental_option("prefs", prefs)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )
    browser.config.driver = driver
    # Скачивание pdf
    browser.open('https://www.online-convert.com/ru/file-type')
    browser.element("#file-format-search").type('pdf')
    browser.element('a[href="https://www.online-convert.com/ru/file-format/pdf"]').click()
    download_url = browser.element('a[href="https://example-files.online-convert.com/document/pdf/example.pdf"]').get(query.attribute("href"))
    content = requests.get(url=download_url).content

    file_path = os.path.join(TMP_DIR, 'example.pdf')  # Добавляем имя файла
    with open(file_path, 'wb') as file:
        file.write(content)

    # Скачивание xlsx
    browser.open('https://www.online-convert.com/ru/file-type')
    browser.element("#file-format-search").type('xlsx')
    browser.element('a[href="https://www.online-convert.com/ru/file-format/xlsx"]').click()

    download_url = browser.element('a[href="https://example-files.online-convert.com/spreadsheet/xlsx/example.xlsx"]').get(query.attribute("href"))
    content = requests.get(url=download_url).content
    file_path = os.path.join(TMP_DIR, 'example.xlsx')  # Добавляем имя файла
    with open(file_path, 'wb') as file:
        file.write(content)
    # Скачивание csv
    browser.open('https://www.online-convert.com/ru/file-type')
    browser.element("#file-format-search").type('csv')
    browser.element('a[href="https://www.online-convert.com/ru/file-format/csv"]').click()

    download_url = browser.element('a[href="https://example-files.online-convert.com/spreadsheet/csv/example.csv"]').get(query.attribute("href"))
    content = requests.get(url=download_url).content
    file_path = os.path.join(TMP_DIR, 'example.csv')  # Добавляем имя файла
    with open(file_path, 'wb') as file:
        file.write(content)