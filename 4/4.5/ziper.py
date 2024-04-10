from zipfile import ZipFile
with ZipFile('edu/pygen_prof/4/4.5/test.zip') as zip_file:
    info = zip_file.infolist()
    print(info[6].file_size)                # размер начального файла в байтах
    print(info[6].compress_size)            # размер сжатого файла в байтах
    print(info[6].filename)                 # имя файла
    print(info[6].date_time) 