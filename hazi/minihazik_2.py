# # 1. Írj egy olyan függvényt amely visszaadja három szám közül a legnagyobbat. A megoldásban nem használhatsz standard lib. függvényeket pl: max()

# def biggest(a, b, c):
#     if a > b and a > c:
#         return a
#     if b > a and b > c:
#         return b
#     if c > a and c > b:
#         return c
#
# print(biggest(40, 43, 161))
########################################################################################################################
########################################################################################################################
# # 2. Írj egy olyan függvényt amely összead minden olyan számot egy listában amely páros szám.

# def add_even_number_list(lista):
#     number = sum(list(filter(lambda x: x % 2 == 0, lista)))
#     return number
#
# lista = [ 2, 4, 3, 5, 4, 11, 8]
# print(add_even_number_list(lista))
########################################################################################################################
########################################################################################################################
# # 3. Írj egy olyan függvényt amely megfordít egy string-et. Pl.:1234abcd >>> dcba4321

# def invert(word):
#     return word[::-1]
#
# print(invert('1234abcd'))
########################################################################################################################
########################################################################################################################
# # 4. Írj egy olyan függvényt amely visszaadja a nagybetűk és kisbetűk számát a paraméterben megadott string-ben.

# import re
#
# def smallbig(word):
#     big = re.findall(r'[A-ZÁÉÍÓÖŐÚÜŰ]', word)
#     small = re.findall(r'[a-záéiíóöőúüű]', word)
#
#     return f'{word}\nNagybetűk: {len(big)}\nKisbetűk: {len(small)}'
#
# print(smallbig('NaGyGyörgy'))
########################################################################################################################
########################################################################################################################
# # 5. Írj egy függvényt amely megvizsgálja, hogy egy szó palindrom vagy sem. Pl. madam >>> True

# def palindrom(word):
#     if word == word[::-1]:
#         return True
#     else:
#         return False
#
# print(palindrom('madam'))
########################################################################################################################
########################################################################################################################
# # 6. Írj egy függvényt amely visszaadja két szám szorzatát.
# # Ha nem kapott paramétert akkor alapértelmezett számokat használ.

# def multiplied(a=2, b=3):
#     return a * b
#
# print(multiplied(5,2))
########################################################################################################################
########################################################################################################################
# # 7. Írj egy függvényt amely terszőleges hosszúságú paraméterlistát fogad.
# # A kapott paramétereket elemzi és visszaad egy dictionary-t a bejövő paraméterek összegével.
# # Pl. (1,2,3,”apple”,”banana”,”lemon”) >>> [6, “applebananalemon”]

# def summarize(*args):
#     int_piece = 0
#     str_piece = ''
#     for i in args:
#         if type(i) == int:
#             int_piece += int(i)
#         elif type(i) == str:
#             str_piece += i
#     return [int_piece, str_piece]
#
# print(summarize(1,2,3, "apple", "banana", "lemon"))
########################################################################################################################
########################################################################################################################
# # 8. Írj egy függvényt amely egy global változó értékét állítja át. Ha a változó False, akkor True és ellenkezőleg.

# name = True
# def init():
#     global name
#     if name == False:
#         name = True
#     else:
#         name = False
#     return name
#
# print(init())
##########################################  REKURZIÓ  ##################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
# # Írj egy rekurzív függvényt a fibonacci szekvencia szemléltetésére.

# fibonacci_cache = {}
# def recursive_fibonacci(n):
#     if n in fibonacci_cache:
#         return fibonacci_cache[n]
#
#     if n == 1:
#         value = 1
#     elif n == 2:
#         value = 1
#     elif n > 2:
#         value = recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
#
#     fibonacci_cache[n] = value
#     return value
#
# for i in range(1, 1001):
#    print(i,':',recursive_fibonacci(i))

########## 2. megoldás ###############
# from functools import lru_cache
#
# @lru_cache(maxsize=1000)
# def recursive_fibonacci(n):
#     if n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     elif n > 2:
#         return recursive_fibonacci(n-1) + recursive_fibonacci(n-2)
#
# for i in range(1, 1001):
#    print(i,':',recursive_fibonacci(i))
########################################################################################################################
########################################################################################################################
# #