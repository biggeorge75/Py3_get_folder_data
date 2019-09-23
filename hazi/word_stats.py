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
