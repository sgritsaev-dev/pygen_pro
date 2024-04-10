from zipfile import ZipFile
with ZipFile('edu/pygen_prof/4/4.5/workbook.zip') as zip_file:
    filtered = list(filter(lambda x: x.file_size>0 and x.compress_size>0, zip_file.infolist()))
    rate={}
    for el in filtered:
        rate.setdefault(el.filename, el.compress_size/el.file_size)
    print(min(rate.items(), key=lambda x: x[1])[0].split('/')[1])