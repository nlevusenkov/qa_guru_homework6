import os
import pytest
import zipfile

from paths import TMP_DIR, CURRENT_DIRECTORY

TARGET_FILES = ['example.pdf', 'example.xlsx', 'example.csv']
ARCHIVE_PATH = os.path.join(TMP_DIR, 'test_zip.zip')
@pytest.fixture(scope='function')
def operations_with_archive():
    with zipfile.ZipFile(os.path.join(TMP_DIR, 'test_zip.zip'), 'w') as zf:
        for file_name in ['example.pdf', 'example.xlsx', 'example.csv']:
            file_path = os.path.join(TMP_DIR, file_name)
            if os.path.exists(file_path):
                zf.write(file_path, arcname=file_name)
