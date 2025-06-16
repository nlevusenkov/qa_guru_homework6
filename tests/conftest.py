import os
import pytest
import zipfile

from paths import TMP_DIR, CURRENT_DIRECTORY

TARGET_FILES = ['example.pdf', 'example.xlsx', 'example.csv']
ARCHIVE_PATH = os.path.join(CURRENT_DIRECTORY, 'test_zip.zip')

@pytest.fixture(scope="session", autouse=True)
def operations_with_archive():
    with zipfile.ZipFile(ARCHIVE_PATH, 'w') as zf:
        for file_name in TARGET_FILES:
            file_path = os.path.join(TMP_DIR, file_name)
            zf.write(file_path, arcname=file_name)

    yield