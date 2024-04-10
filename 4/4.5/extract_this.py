from zipfile import ZipFile

def extract_this(zip_name, *args):
    with ZipFile(zip_name) as zip_file:
        if args:
            for el in args:
                zip_file.extract(el)
        else:
            zip_file.extractall()
