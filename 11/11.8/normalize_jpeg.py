import re

def normalize_jpeg(filename):
    return re.sub(r'jpeg$|jpg$', r'jpg', filename, flags=re.IGNORECASE)

# INPUT DATA:

# TEST_1:
print(normalize_jpeg('stepik.jPeG'))

# TEST_2:
print(normalize_jpeg('mountains.JPG'))

# TEST_3:
print(normalize_jpeg('windows11.jpg'))

# TEST_4:
print(normalize_jpeg('jepg_file.jPG'))

# TEST_5:
print(normalize_jpeg('file_jepg.jPeG'))

# TEST_6:
print(normalize_jpeg('file.jepg.JPEG'))

# TEST_7:
print(normalize_jpeg('filename.jpg.jpg'))

# TEST_8:
print(normalize_jpeg('stepik.jpeg.jpeg'))

# TEST_9:
print(normalize_jpeg('stepik.jpg.jpeg'))

# TEST_10:
print(normalize_jpeg('stepik.jpeg.jpg'))

# TEST_11:
print(normalize_jpeg('beegeek.JPg'))

# TEST_12:
print(normalize_jpeg('нарусском.JPg'))

# TEST_13:
print(normalize_jpeg('на русском языке.JPG'))

# TEST_14:
print(normalize_jpeg('jpg.jPg.Jpg.JPG'))

# TEST_15:
print(normalize_jpeg('Это тест.JpEg'))