# name = "bilal"
# age = '23'
# is_new = True
# print(name,age,is_new)

# name = input('What is your name? ')
# color = input('What is your favourite color? ')
# print(name + 'Likes' + color)

# birth_year = input('birth year: ')
# print(type(birth_year))
# age = 2019 - int(birth_year)
# print(age)
# print(type(age))

# pounds = input('what is your weight(lbs) ')
# kilo = int(pounds) * 0.45
# #print(type(kg))
# print(kilo)

# kilo = input('what is your weight(kilo): ' )
# pounds = int(kilo) * 2.20
# print(pounds)

# name = "my name is bilal"
# print(len(name))
# print(name.upper())
# print('Name' in name)
# print (name.find('bilal'))

# print (10 ** 2)
# print(20 % 3)
# x = 20
# x += 4
# print(x)

# x = 2.8
# print(round(x))
# print(abs(-2.9))

# is_hot  = False
# is_cold = True
#
# if is_hot:
#     print("It's a hot day")
#     print("drink plenty of water")
# elif is_cold:
#     print("it's a cold day")
#     print("wear warm cloths")
#
# else:
#     print("It's a lovely day")
#     print("Enjoy your day")

# house_price = 1000000
# is_buyer_good = False
# if is_buyer_good:
#     down_payment = 0.1 * house_price
# else:
#     down_payment = 0.2 * house_price
# print(f"down_payment: ${down_payment}")

#name = input("what is your name? ")

# if len(name) < 4:
#     print("character should more then three")
# elif len(name) > 15:
#     print("your name is too long")
# else:
#     print("you have a good name")

u_weight = input("what is your weight: ")
unit = input("(k)ilo or (P)ounds: ")
if unit.upper() == "pounds":
    convert = int(u_weight) * 0.45
    print(f"you are {convert} kilos")
else:
    convert = int(u_weight) / 0.45
    print(f"you are {convert} pounds")
