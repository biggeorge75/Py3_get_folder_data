# # 1. Definiálj egy str típusú változót és egy int típusú változót majd printeld ki azokat egy mondatban.

# words = 'éves vagyok.'
# nums = 44
# print('1. feladat: ' + str(nums) + ' ' + words)
# print(f'1. feladat: {nums} {words}')
########################################################################################################################
########################################################################################################################
# # 2. Definiálj egy listát tetszőleges adatokkal majd a lista utolsó elemét tedd a lista elejére.

# lista = ['első', 2, 'három', 4, 'utolsó']
# lista[0], lista[-1] = lista[-1], lista[0]
# print(f'2. feladat: {lista}')
########################################################################################################################
########################################################################################################################
# # 3. Definiálj egy dictionary-t tetszőleges adatokkal majd printeld ki a dictionary tartalmát úgy,
# hogy a kulcsok ABC sorrendben legyenek rendezve.

# dict = {'Gyümölcs': 'alma', 'Üdítő' : 'almalé', 'Szeszesital' : 'pálinka'}
# print(f'3.feladat: {sorted(dict.keys())}')
########################################################################################################################
########################################################################################################################
# # 4. Generálj egy 10 számjegyből álló számlistát ahol a számok négyzetükre emelve kerülnek be a listába és
# ezt a list comprehension eljárással egy sorban.

# numlist = [ i**2 for i in range(1,11) ] # vagy i*i
# print(f'4.feladat: {numlist}')
########################################################################################################################
########################################################################################################################
# # 5. Adott egy tetszőleges hosszúságú str. Készíts belőle egy új példányt amelyben minden második karakter nagybetű.

# def big(s):
#     r = ""
#     i = True
#     for char in s:
#         if i:
#             r += char.upper()
#         else:
#             r += char.lower()
#         if char != ' ':
#             i = not i
#     return r
#
# print(f" 5.feladat: {big('minden páros nagybetűvel')}")
########################################################################################################################
########################################################################################################################
# 6. Generálj egy password-ot a felhasználó által megadott adatokból: név, cím, születési idő. A generált password-ben
#    nem lehetnek ékezetek, viszont kis és nagybetűk valamint számok variációit kell tartalmazza.

# lista6 = []
# nev = input('Keresztneved: ')
# cim = input('Melyik városban születtél: ')
# szido = input('Melyik évben születtél: ')
#
# csere = str.maketrans('áéíóöőúüű' 'ÁÉÍÓÖŐÚÜŰ', 'aeiooouuu' 'AEIOOOUUU')
# lista6.append(cim[1].translate(csere) + nev[0].translate(csere) + cim[-1].translate(csere) + nev[-1].translate(csere)
# + szido[2].translate(csere) + szido[0].translate(csere))
#
# print(f'6.feladat: {lista6}')
########################################################################################################################
########################################################################################################################
########################################################################################################################
########################################################################################################################
# # Kondíciók 1. Írj egy feltételt ahol a True ág csak akkor fut le ha a bemenetként megadott változó páros szám.
# num = int(input('Szám: '))
# if num%2 == 0:
#     print(f'Kondíciók 1. feladat: {num}')
########################################################################################################################
########################################################################################################################
# # Kondíciók 2. Írj egy olyan változót amely értéke True ha a felette megadott int változó értéke kisebb 10-nél.
# Ellenkező esetben a változó False lesz.
# a = True
# b = int(input('Szám: '))
# if b < 10:
#     a = True
# else:
#     a = False
# print(f'Kondíciók 2. feladat: {a}')
########################################################################################################################
########################################################################################################################

#################### még nincs készen ##############################################################
# # Kondíciók 3. Írj egy olyan while ciklust amely addig számlál amíg a bemenetként megadott változó kisebb 10-nél,
# majd megfordítja a számlálást, elszámol 0-ig és kilép.
#
#
# x = int(input('Szám: '))
# while True:
#     if x < 10:
#         x += 1
#         print(x)
#     else:
#         break




