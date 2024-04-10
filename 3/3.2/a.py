from datetime import date
import locale

florida_hurricane_dates = [date(1987, 11, 15), date(1988, 3, 12), date(1976, 5, 12)]
# присваиваем самую раннюю дату урагана в переменную first_date
first_date = min(florida_hurricane_dates)

# конвертируем дату в ISO и RU формат
iso = 'Дата первого урагана в ISO формате: ' + first_date.isoformat()
ru = 'Дата первого урагана в RU формате: ' + first_date.strftime('%d/%m/%Y')
us = 'Дата первого урагана в US формате: ' + first_date.strftime('%m.%d.%Y')

print(iso)
locale.setlocale(locale.LC_ALL, 'ru_RU.UTF-8')

print(ru)
print(us)