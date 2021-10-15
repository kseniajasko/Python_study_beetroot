import random
#ПРИМІТКА: input виводиться як клас string для того, щоб можна було відповісти
#          у випадку введення букв замість числа

#TASK_1
#Write a program that generates a random number between 1 and 10 and lets the user guess what number was generated. The result should be sent back to the user via a print statement.

x_0 = random.randint(0, 10)
while True:
    x_1 = input('Введіть число від 0 до 10: ')
    if x_1.isdigit():
        if x_0 == int(x_1):
            print('Ви вгадали!')
            break
        else:
            print(f'Ви не вгадали. Правильне число: {x_0}')
            break
    else:
        print('Ви ввели не число')

#TASK_2
#Write a program that takes your name as input, and then your age as input and greets you with the following:
#“Hello <name>, on your next birthday you’ll be <age+1> years”

while True:
    name = input('Напишіть Ваше ім\'я:')
    age =  input('Напишіть Ваш вік:')

    if name.strip() and age.isdigit():
        print(f'Hello {name}, on your next birthday you\'ll be {int(age)+1} years')
        break
    else:
        print('User data is incorrect')

#TASK_3
#Create a program that reads an input string and then creates and prints 5 random strings from characters of the input string.
#For example, the program obtained the word ‘hello’, so it should print 5 random strings(words) that combine characters ‘h’, ‘e’, ‘l’, ‘l’, ‘o’ -> ‘hlelo’, ‘olelh’, ‘loleh’ …
#Tips: Use random module to get random char from string)

word = input('Введіть слово: ').strip()
if word and not word.isdigit():
    counter = 0
    while counter < 5:
        list_1 = [random.choice(word) for _ in range(5)]
        print("".join(list_1))
        counter += 1
else:
    print('Слово не введено.')

#TASK_4
#Write a program that asks the answer for a mathematical expression, checks whether the user is right or wrong, and then responds with a message accordingly.
answer_1 = input('Обчислити: 8:2*(5-1) \nВашa відповідь: ').strip()
answer_2 = '16'
if answer_1 == answer_2:
    print('Правильно')
else:
    print('Неправильно')
