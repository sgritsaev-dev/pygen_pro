from datetime import datetime

with open('C:/VS code pets/edu/pygen_prof/3.3/diary.txt', 'r', encoding='utf-8') as diary:
    diary = sorted(diary.read().split('\n\n'), key=lambda d: datetime.strptime(d[0:17], '%d.%m.%Y; %H:%M'))
print(*diary, sep='\n\n')