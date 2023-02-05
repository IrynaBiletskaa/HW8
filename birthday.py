from collections import defaultdict
from datetime import datetime, timedelta


users = [
    {'name': 'Andry', 'birthday': '2023-02-06'},
    {'name': 'Dima', 'birthday': '2023-02-06'},
    {'name': 'Billy', 'birthday': '2023-03-01'},
    {'name': 'Snow', 'birthday': '2023-02-07'},
    {'name': 'Elena', 'birthday': '2023-02-08'},
    {'name': 'Sasha', 'birthday': '2023-02-06'},
    {'name': 'Diana', 'birthday': '2023-02-10'},
    {'name': 'Kristi', 'birthday': '2023-02-07'},
    {'name': 'Roman', 'birthday': '2023-02-09'},
    {'name': 'Jek', 'birthday': '2023-02-08'},
    {'name': 'Carl', 'birthday': '2023-02-10'},
    {'name': 'Denis', 'birthday': '2023-02-11'},
    {'name': 'Megan', 'birthday': '2023-02-12'},
    {'name': 'Joe', 'birthday': '2023-02-13'},
    {'name': 'Tyler', 'birthday': '2023-02-14'},
    {'name': 'Adriana', 'birthday': '2023-02-15'},
    {'name': 'Nikita', 'birthday': '2023-02-16'},
    {'name': 'Nazar', 'birthday': '2023-02-17'},

]

current_datetime = datetime.now()
week_interval = timedelta(weeks=1)
week = current_datetime + week_interval


def get_birthdays_per_week(users):

    days_dict = {}
    for user in users:
        birth_user = datetime.strptime(user['birthday'], '%Y-%m-%d')
        day_birthday = birth_user.strftime('%A')

        if birth_user > current_datetime and birth_user < week:
            if day_birthday == 'Sunday' or day_birthday == 'Saturday':
                if not 'Monday' in days_dict:
                    days_dict['Monday'] = []
                days_dict['Monday'].append(user['name'])

            elif day_birthday not in days_dict:
                days_dict[day_birthday] = []
                days_dict[day_birthday].append(user['name'])
            else:
                days_dict[day_birthday].append(user['name'])

    for el in days_dict:
        print(f'{el} : {", ".join(days_dict.get(el))}')


# print(el, ':', ', '.join(days_dict.get(el)))


get_birthdays_per_week(users)
