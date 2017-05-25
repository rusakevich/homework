from datetime import datetime, date
def days_to_year():
    Y = date.today().year #Определеям сегодняшний год
    Tod = datetime.today() #Определеям сегодняшнюю дату
    Dat = datetime(Y,12,31) #Формируем дату конца сегодняшнего года
    return (Dat - Tod).days

print('Количество дней до нового года осталось - {}'.format(days_to_year()))
