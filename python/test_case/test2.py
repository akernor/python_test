# список: создание пустого + добавление элеммента в список
# vowels = ['a', 'e', 'i', 'o', 'u']
# word = input("Provide a word to search for vowels: ")
# found = []
# for letter in word:
#     if letter in vowels:
#         if letter not in found:
#             found.append(letter)
# for vowels in found:
#     print(vowels)

# работа со списком: удаление элементов а также добавление + повторение цикла
# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)
# for i in range(4):
#     plist.pop()
# plist.pop(0)
# plist.remove("'")
# plist.extend([plist.pop(), plist.pop()])
# plist.insert(2, plist.pop(3))
# new_phrase = ''.join(plist)
# print(plist)
# print(new_phrase)

# список создание списка и обратная функция
# phrase = "Don't panic!"
# plist = list(phrase)
# print(phrase)
# print(plist)
# new_phrase = ''.join(plist[1:3])
# new_phrase = new_phrase + ''.join([plist[5], plist[4], plist [7], plist[6]])
# print(new_phrase)
# test = list(new_phrase)
# print(test)

# список со срезами + табуляция
paranoid_android = "Marvin, the Paranoid Android"
letters = list(paranoid_android)
for char in letters[:6]:
    print('\t', char)
print()
for char in letters[-7:]:
    print('\t'*2, char)
print()
for char in letters[12:20]:
    print('\t' * 3, char)
print()
