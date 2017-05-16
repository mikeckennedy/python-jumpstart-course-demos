import datetime

def print_header():
    print('-------------------------------')
    print('        Birthday App'
    print('-------------------------------')

def get_user_birthday():
    user_year = int(input('What year were you born? [YYYY]'))
    user_month = int(input('What month were you born? [MM]'))
    user_day = int(input('What day were you born? [DD]'))
    
    user_birthday = datetime.datetime(user_year, user_month, user_day)
    
    return user_birthday


def compare_dates():
    current_datetime = datetime.now()
    current_year = datetime.year(current_datetime)
    current_month = datetime.month(current_datetime)
    current_day = datetime.day(current_datetime)

def print_delta():
    pass


print_header()

get_user_birthday()

compare_dates()

print_delta()

