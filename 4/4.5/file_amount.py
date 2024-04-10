from zipfile import ZipFile
with ZipFile('edu/pygen_prof/4/4.5/workbook.zip') as zip_file:
    filtered = list(filter(lambda x: x.is_dir()==False, zip_file.infolist()))
    print(len(filtered))