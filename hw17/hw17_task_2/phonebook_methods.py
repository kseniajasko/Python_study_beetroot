import json
#indent = int(4)
def opened():
    with open("data_phonebook.json", "r+") as data_ph:
        data = json.load(data_ph)
    return data

def add(number = None, first_name = None, last_name = None,  city = None):
    list_1 = None
    data = {"number": number, "first_name": first_name, "last_name": last_name, "city": city}
    if not data['number'] or len(data['number']) != 10 or not data['first_name'] or not data['last_name']:
        return list_1

    if data['first_name'] is not None and data['last_name'] is not None:
        data['full_name'] = data['first_name'].title() + ' ' + data['last_name'].title()

    list_1 = opened()

    with open('data_phonebook.json', 'r+') as f:
       # list_1 = json.load(f)
        list_1.append(data)
        json.dump(list_1, f, indent =4)

    return list_1

