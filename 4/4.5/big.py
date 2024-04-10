from zipfile import ZipFile
from datetime import *
with ZipFile('edu/pygen_prof/4/4.5/workbook.zip') as zip_file:
    big=[]
    for el in zip_file.infolist():
        if el.is_dir()==False:
            x={'name': el.filename.split('/')[-1],'date': datetime(*el.date_time),'file_size': el.file_size,'compress_size': el.compress_size}
            big.append(x)
    sorted_big = sorted(big, key=lambda x: x['name'])
    for el in sorted_big:
        print(f'''{el['name']}
  Дата модификации файла: {el['date']}
  Объем исходного файла: {el['file_size']} байт(а)
  Объем сжатого файла: {el['compress_size']} байт(а)\n''')