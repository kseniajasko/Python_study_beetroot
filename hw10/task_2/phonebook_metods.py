import json
#indent = int(4)
# def opened():
#     with open("data_phonebook.json", "r+") as data_ph:
#         data = json.load(data_ph)
#     return data

def searchlist(phone, data):
    for p in data:
        for a in p.values():
            if a == phone:
                return p

def search(data, data_ph):
    number_to_read = input("Please, enter key worlds to search: ").strip()
    print(searchlist(number_to_read, data))

def add(data, data_ph):
    number = input("Please enter number: ").strip()
    first_name = input("Please enter first name: ").strip()
    last_name = input("Please enter last name: ").strip()
    full_name = input("Please enter full name: ").strip()
    city = input("Please enter city: ").strip()
    data.append({"number": number, "first_name": first_name, "last_name": last_name, "full_name": full_name, "city": city})
    #data[number] = {"first_name": first_name}
    data_ph.seek(0) #
    json.dump(data, data_ph, indent = 4)

def delete(data, data_ph):
    number_to_delete = input("Please, enter key words to delete: ").strip()
    k = searchlist(number_to_delete, data)
    data.remove(k)
    with open('data_phonebook.json', 'w') as data_ph:
        json.dump(data, data_ph, indent=4)

def update(data, data_ph):
    number_to_update = input("Please, enter key words to update contact: ").strip()
    update1 = searchlist(number_to_update, data)
    number = input("Please enter new number: ").strip()
    first_name = input("Please enter new first name: ").strip()
    last_name = input("Please enter new last name: ").strip()
    full_name = input("Please enter new full name: ").strip()
    city = input("Please enter new city: ").strip()
    data[data.index(update1)] = {
        "number": (update1["number"], number)[bool(number.strip())],
        "first_name": (update1["first_name"], number)[bool(first_name.strip())],
        "last_name": (update1["last_name"], number)[bool(last_name.strip())],
        "full_name": (update1["full_name"], number)[bool(full_name.strip())],
        "city": (update1["city"], number)[bool(city.strip())]}
    with open('data_phonebook.json', 'w') as data_ph:
        json.dump(data, data_ph, indent=4)