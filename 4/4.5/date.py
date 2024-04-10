from zipfile import ZipFile
from datetime import *
with ZipFile('edu/pygen_prof/4/4.5/workbook.zip') as zip_file:
    dates={}
    for el in zip_file.infolist():
        if el.is_dir()==False:
            dates.setdefault(el.filename.split('/')[-1], datetime(*el.date_time))
    filtered = dict(filter(lambda x: x[1]>datetime(2021, 11, 30, 14, 22, 00), dates.items()))
    sorted = sorted(filtered.items(), key=lambda x: x[0])
    for el in sorted:
        print(el[0])