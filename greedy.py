import csv

def greedy():
    wordList = open('words.txt', 'r')
    letterFrequency = 'letterPositionFrequency.csv'

    maxValue = 0
    maxWord = []

    letterFreq = {'a':{1:0, 2:0, 3:0, 4:0, 5:0}, 'b':{1:0, 2:0, 3:0, 4:0, 5:0}, 'c':{1:0, 2:0, 3:0, 4:0, 5:0}, 
                'd':{1:0, 2:0, 3:0, 4:0, 5:0}, 'e':{1:0, 2:0, 3:0, 4:0, 5:0}, 'f':{1:0, 2:0, 3:0, 4:0, 5:0}, 
                'g':{1:0, 2:0, 3:0, 4:0, 5:0}, 'h':{1:0, 2:0, 3:0, 4:0, 5:0}, 'i':{1:0, 2:0, 3:0, 4:0, 5:0}, 
                'j':{1:0, 2:0, 3:0, 4:0, 5:0}, 'k':{1:0, 2:0, 3:0, 4:0, 5:0}, 'l':{1:0, 2:0, 3:0, 4:0, 5:0}, 
                'm':{1:0, 2:0, 3:0, 4:0, 5:0}, 'n':{1:0, 2:0, 3:0, 4:0, 5:0}, 'o':{1:0, 2:0, 3:0, 4:0, 5:0}, 
                'p':{1:0, 2:0, 3:0, 4:0, 5:0}, 'q':{1:0, 2:0, 3:0, 4:0, 5:0}, 'r':{1:0, 2:0, 3:0, 4:0, 5:0}, 
                's':{1:0, 2:0, 3:0, 4:0, 5:0}, 't':{1:0, 2:0, 3:0, 4:0, 5:0}, 'u':{1:0, 2:0, 3:0, 4:0, 5:0}, 
                'v':{1:0, 2:0, 3:0, 4:0, 5:0}, 'w':{1:0, 2:0, 3:0, 4:0, 5:0}, 'x':{1:0, 2:0, 3:0, 4:0, 5:0}, 
                'y':{1:0, 2:0, 3:0, 4:0, 5:0}, 'z':{1:0, 2:0, 3:0, 4:0, 5:0}}

    for wline in wordList:
        word = list(wline.rstrip())
        i = 1
        for letter in word:
            if letter in letterFreq:
                letterFreq[letter][i] += 1
            else:
                letterFreq[letter][i] = 1
            i += 1

    with open(letterFrequency, 'w', newline='') as fileWrite:
        
        fieldnames = ['letter', 1, 2, 3, 4, 5]
        writer = csv.DictWriter(fileWrite, fieldnames=fieldnames)
        writer.writeheader()
        for key, val in sorted(letterFreq.items()):
            row = {'letter': key}
            row.update(val)
            writer.writerow(row)

    with open(letterFrequency, 'r') as fileRead:
        reader = csv.reader(fileRead)

        wordList.seek(0)
        for line in wordList:
            
            word = list(line.rstrip())
            wordValue = 0

            i = 1
            for letter in word:
                for row in reader:
                    if (row[0] == letter):
                        wordValue += (float(row[i]) / 12972)
                fileRead.seek(0)
                i += 1

            if wordValue > maxValue:
                maxValue = wordValue
                maxWord = list(line)

    print("best word: ")
    print("".join(maxWord))
    print("best word value: ")
    print(maxValue)
    return "".join(maxWord)