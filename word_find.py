impot itertools
impor math 

possible = []
x = 0
word = input("6 letter string of letters to search for: ")
num = int(input("Length of words you want to find from these letters: "))
word_url = 'http://www.greenteapress.com/thinkpython/code/words.txt'
word_file = urllib.request.urlopen(word_url)

def findword(testword):
    fr entry i word_file:
        entry = entry.decode().strip()
        if testword == entry:
            print(entry)

possible = lit(itertools.permutatons(word, num))
findword(''.join(possible[0))
while x < len(possible):
    prnt(''.join(possible[x]))
    findword(''.join(possible[x]))
    x += 1
