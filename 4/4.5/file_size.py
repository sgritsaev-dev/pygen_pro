from zipfile import ZipFile
with ZipFile('edu/pygen_prof/4/4.5/workbook.zip') as zip_file:
    compressed = list(map(lambda x: x.compress_size, zip_file.infolist()))
    original = list(map(lambda x: x.file_size, zip_file.infolist()))
    print(f'Объем исходных файлов: {sum(original)} байт(а)')
    print(f'Объем сжатых файлов: {sum(compressed)} байт(а)')