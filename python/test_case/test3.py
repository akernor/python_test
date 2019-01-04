# словарь0
# person1 = { 'Name': 'Ford Prefect',
#             'Gender': 'Male',
#             'Occupation': 'Researcher',
#             'Home Planet': 'Betelgeuse Seven'}
# print(person1)

# словарь1
# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Provide a word to search for vowels: ")
# found = {}
# found['a'] = 0
# found['e'] = 0
# found['i'] = 0
# found['o'] = 0
# found['u'] = 0
# for letter in word:
#     if letter in vowels:
#         found[letter] += 1
# for k, v in sorted(found.items()):
#     print(k, 'was found', v, 'time(s).')

#словарь2
# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Provide a word to search for vowels: ")
# found = {}
# for letter in word:
#     if letter in vowels:
#         found.setdefault(letter, 0)
#         found[letter] += 1
# for k, v in sorted(found.items()):
#     print(k, 'was found', v, 'time(s).')

#множества: преобразование и вывод общих объектов в множествах
# vowels1 = set('aeiou')
# word = input("Provide a word to search for vowels: ")
# found = vowels1.intersection(set(word))
# for vowels in found:
#     print(vowels)

# кортеж
# a = (1,)
# b = (1, 2, 3)

# комбинирование встроенных структур данных (словарь в словаре)
import pprint


people = {}
people['Ford'] = {  'Name': 'Ford Prefect',
                    'Gender': 'Male',
                    'Occupation': 'Researcher',
                    'Home Planet': 'Betelgeuse Seven'}
people['Artur'] = {  'Name': 'Artur Dent',
                    'Gender': 'Unknown',
                    'Occupation': 'Sandwich-Maker',
                    'Home Planet': 'Earth'}
people['Robot'] = {  'Name': 'Marvin',
                    'Gender': 'Unknown',
                    'Occupation': 'Paranoid Android',
                    'Home Planet': 'Earth'}
people['Trillian'] = {  'Name': 'Tricia McMillan',
                    'Gender': 'Female',
                    'Occupation': 'Mathematician',
                    'Home Planet': 'Unknown'}
pprint.pprint(people)
