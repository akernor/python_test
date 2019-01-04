# список: рандом(случайное знач. в заданном диапазоне) + повт. цикла + получение текущего времени
# import time
# import random
#
# from datetime import datetime
#
# odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19,
#         21, 23, 25, 27, 29, 31, 33, 35, 37, 39,
#         41, 43, 45, 47, 49, 51, 53, 55, 57, 59]
#
# for i in range(5):
#     right_this_minute = datetime.today().minute
#
#     if right_this_minute in odds:
#         print("This minute seems a little odd.")
#     else:
#         print("Not an odd minute")
#     wait_time = random.randint(1,60)
#     time.sleep(wait_time)

# время
# today = datetime.today().day
# if today == 'Saturday':
#     print('Party!!')
# elif today == 'Sunday':
#     print('Recover.')
# else:
#     print('Work, work, work.')

# повторение в заданном диапазоне
word = "bottles"
for beer_num in range(99, 0, -1):
    print(beer_num, word, "of beer on the wall.")
    print(beer_num, word, "of beer.")
    print("Take one down.")
    print("Pass it around.")
    if beer_num == 1:
        print("No more bottles of beer on the wall.")
    else:
        new_num = beer_num - 1
        if new_num == 1:
            word = "bottle"
        print(new_num, word, "of beer on the wall.")
    print()