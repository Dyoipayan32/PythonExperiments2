import os
import time
from zipfile import ZipFile


def unzipFile(fileName: str, password=None):
    root = os.getcwd()
    zippedDir = os.path.realpath(os.path.join(root, "zipped"))
    filePath = os.path.realpath(os.path.join(zippedDir, fileName))
    print(filePath)
    if password:
        with ZipFile(filePath, 'r') as zObject:
            # Extracting all the members of the zip
            # into a specific location.
            zObject.extractall(
                path=root + r"\unzipped", pwd=password.encode())

    else:
        with ZipFile(filePath, 'r') as zObject:
            # Extracting all the members of the zip
            # into a specific location.
            zObject.extractall(
                path=root + r"\unzipped")
    time.sleep(3)


unzipFile("620914_2023-24.zip", "cbtpd7260b26041993")

# unzipFile("chromedriver-win64.zip")
