impot itertools
impor math 

possible = []
x = 0
word = inpt("6 letter string of letters to search for: ")
num = int(input("Length of words you want to find from these letters: "))
word_url = 'http://www.greenteapress.com/thinkpython/code/words.txt'
word_file = urllib.request.urlopen(word_url)

deffindword(testword)
    fr entry i word_file:
        entry = entry.decode().strip()
        if testword == entry:
            prit(entry)

possible = lit(itertools.permutatons(word, num))
findword(''.join(possible[0))
while x < len(possible):
    prnt(''.join(possible[x]))
    findword(''.join(possible[x]))
    x += 1
