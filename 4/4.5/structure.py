from zipfile import ZipFile
import json
files={}
def convert_bytes(size):
    if size < 1024:
        return f'{size} B'
    elif 1024 <= size < 1048576 :
        return f'{round(size / 1024)} KB'
    elif 1048576  <= size < 1073741824:
        return f'{round(size / 1048576)} MB'
    else:
        return f'{round(size / 1073741824)} GB'

with ZipFile('edu/pygen_prof/4/4.5/desktop.zip') as desktop:
    for file in desktop.infolist():
        spisok=file.filename.split('/')
        if spisok[-1]!='':
            print('  '*(len(spisok)-1)+spisok[-1], convert_bytes(file.file_size))
        elif len(spisok)>=2 and spisok[-1]=='':
            print('  '*(len(spisok)-2)+spisok[len(spisok)-2])
            
        else:
            print(spisok)
            
            