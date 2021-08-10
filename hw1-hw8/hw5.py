import random

#TASK_1
#Write a Python program to get the largest number from a list of random numbers with the length of 10
#Constraints: use only while loop and random module to generate numbers
random_list = random.sample(range(-1000, 1000), 10)
print(f'{random_list} \nMax element in list:',  max(random_list))


# TASK_2
#Generate 2 lists with the length of 10 with random integers from 1 to 10, and make a third list containing the common integers between the 2 initial lists without any duplicates.
#Constraints: use only while loop and random module to generate numbers
#ex_1
#елементи в випадково заданих списках МОЖУТЬ повторюватися
def randNumMaxFor(n):
    ret = []
    for i in range(n):
        ret.append(random.randint(1, 10))
    return ret

list_1 = randNumMaxFor(10)
list_2 = randNumMaxFor(10)
print(f'{list_1} \n{list_2}')
print(list(set(list_1).intersection(list_2)))

#ex_2
#елементи в випадково заданих списках НЕ МОЖУТЬ повторюватися
# list_1 = random.sample(range(1, 11), 10)
# list_2 = random.sample(range(1, 11), 10)
# print(f'{list_1} \n{list_2}')
# print(list(set(list_1).intersection(list_2)))


 #TASK_3
#Make a list that contains all integers from 1 to 100, then find all integers from the list that are divisible by 7 but not a multiple of 5, and store them in a separate list. Finally, print the list.
#Constraint: use only while loop for iteration
list_3 = [i for i in range(1, 101) if not i % 7 and i % 5]
#list_3 = [i for i in range(1, 101, 7) if i % 5 !=0]
print(list_3)

