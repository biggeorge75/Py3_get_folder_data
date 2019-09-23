"""
Ebben a feladatban egy olyan kódot kell írnod ami betölt egy tetszőleges .txt fájlt (mellékelek egyet) és készít egy statisztikát a szövegről amely tartalma:

- Szavak száma
- Karakterek száma szóköz nélkül
- A három leggyakoribb szó (ignoráljuk a 3 betűs vagy rövidebb szavakat)

A végeredményt mentse ki egy word_stats.txt fájlba és opcionálisan készülhet egy excel fájl is az eredeti fájl mellé.
"""

with open('The Adventures of Sherlock Holmes.txt') as f:
    text = f.read()

word_list = [i for i in text.split() if len(i) > 3]
word_count = len(word_list)

character_count = sum([len(i) for i in word_list])

word_counter = {}
for i in word_list:
    if i in word_counter:
        word_counter[i] += 1
    else:
        word_counter[i] = 1

import operator

sorted_word_counter = sorted(word_counter.items(), key=operator.itemgetter(1), reverse=True)
print(sorted_word_counter[:3])



