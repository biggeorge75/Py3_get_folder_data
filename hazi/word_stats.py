import collections

textfile = "aslan.txt"

with open(textfile) as file:
    mytext = str(file.read())

    if len(mytext) == 0:
        print("file is empty")
    else:
        numWords = len(mytext.split(" "))
        char = (len(mytext.replace(" ", "")))

        wordLen = 3
        mytext2 = mytext.replace("\n", " ")
        listOfWords = [ word for word in mytext2.split(" ") if len(word)>wordLen]
        listWordNumber = collections.Counter(listOfWords).most_common()

    summary = f'\nSzavak száma: {numWords} \nKarakterek száma: {char} \nA 3 leggyakoribb szó: {listWordNumber[0]}, {listWordNumber[1]}, {listWordNumber[2], }'

    with open("summary.txt", "w") as f:
        f.write(summary)

print(summary)
