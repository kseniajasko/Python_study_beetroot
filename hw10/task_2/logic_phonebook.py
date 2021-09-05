
import json
import phonebook_metods
#data_book = phonebook_metods.opened()

while True:
    data_ph = open("data_phonebook.json", "r+")
    data = json.load(data_ph)
    user_choise = input("For using phonebook type: \nfor searching info: 'search' \nfor addind: 'add' \nfor deletind: 'delete' \nfor updating: 'update'\nfor exing: 'exit'\n").lower()
    if user_choise == "search":
        phonebook_metods.search(data, data_ph)
    elif user_choise == "add":
         phonebook_metods.add(data, data_ph)
    elif user_choise == "delete":
         phonebook_metods.delete(data, data_ph)
    elif user_choise == "update":
         phonebook_metods.update(data, data_ph)
    elif user_choise == "exit":
        print('Good bye!')
        break
    else:
        print("Error input")
        continue
