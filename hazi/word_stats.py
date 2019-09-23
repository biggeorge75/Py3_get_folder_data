"""
Ebben a feladatban egy olyan kódot kell írnod ami betölt egy tetszőleges .txt fájlt (mellékelek egyet) és készít egy statisztikát a szövegről amely tartalma:

- Szavak száma
- Karakterek száma szóköz nélkül
- A három leggyakoribb szó (ignoráljuk a 3 betűs vagy rövidebb szavakat)

A végeredményt mentse ki egy word_stats.txt fájlba és opcionálisan készülhet egy excel fájl is az eredeti fájl mellé.
"""

import collections

textfile = "The Adventures of Sherlock Holmes.txt"

with open(textfile) as file:
    text = file.read()

    if len(text) == 0:
        print("file is empty")
    else:
        numWords = len(text.split(" "))
        char = (len(text.replace(" ", "")))

        wordLen = 3
        myText = text.replace("\n", " ")
        listWords = [i for i in myText.split(" ") if len(i) > wordLen]
        listWordNumber = collections.Counter(listWords).most_common(3)

    summary = f'{textfile}\nSzavak száma: {numWords:>9} \nKarakterek száma: {char:>3} \nA ' \
              f'3 leggyakoribb szó: {listWordNumber[0][0]} ' \
              f'({listWordNumber[0][1]}), {listWordNumber[1][0]} ({listWordNumber[1][1]}), ' \
              f'{listWordNumber[2][0]} ({listWordNumber[2][1]})'

    with open("summary.txt", "w", encoding="UTF8") as file:
        file.write(summary)
print('_'*80)
print(summary)
print('_'*80)
