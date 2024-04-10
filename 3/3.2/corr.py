from datetime import date

def is_correct(day, month, year):
    try:
        test_date = date(int(year), int(month), int(day))
        return True
    except:
        return False
    
print(is_correct(31, 12, 10051))