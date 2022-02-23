import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# no_items = len(names)
# random_choice = random.randint(0, no_items - 1)
# person_who_will_pay = names[random_choice]
# print(person_who_will_pay + ' is going to pay the meal today!')
person_who_will_pay= random.choice(names)
print(person_who_will_pay + ' is going to pay the meal today!')