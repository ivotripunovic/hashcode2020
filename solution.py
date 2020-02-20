import random

def scoresSorter(val):
    return val[1]

def libSorter(val):

    N = int(val[0][0])
    T = int(val[0][1])
    M = int(val[0][2])

    fitness = N * M / T

    return fitness

def readFile(filename):
    fp = open(filename)
    line = fp.readline().rstrip().split(' ')
    B = int(line[0])
    L = int(line[1])
    D = int(line[2])
    scores = fp.readline().rstrip().split(' ')
    scores = list(map(int, scores))

    # print(scores)
    # print(scorespair)

    libraries = []
    for i in range(0,L):
        lib = fp.readline().rstrip().split(' ')
        lib.append(i)
        books = fp.readline().rstrip().split(' ')
        books = list(map(int, books))
        
        booksScore = []
        for j in range(0, len(books)):
            booksScore.append([books[j], scores[books[j]]])

        booksScore.sort(key = scoresSorter, reverse = True )

        libraries.append([lib, booksScore])

    #print(libraries)

    libraries.sort(key = libSorter, reverse = True)

    #print(libraries)

    fp.close()
    return B, L, D, scores, libraries

# Library ids = []
# books = {} sa idijem lib-a, i listom knjiga
def writeFile(filename, result):
    fout = filename[:-3] + 'out'
    fp = open(fout, "w")

    fp.write(str(len(result)) + '\n')

    for i in range(0, len(result)):
        # lib id i numBooks
        fp.write(' '.join(map(str,result[i][0])) + '\n')
        # book ids
        fp.write(' '.join(map(str,result[i][1])) + '\n')

    fp.close()

def solve(B, L, D, scores, libraries):
    result = []

    for i in range(0, L):
        booksInLib = int(libraries[i][0][0])
        libID = [libraries[i][0][3], booksInLib]
        books = []
        for j in range(0, booksInLib):
            books.append(libraries[i][1][j][0])

        result.append([libID, books])

    return result


def run(file):
    B, L, D, scores, libraries = readFile(file)

    result = solve(B, L, D, scores, libraries)

    writeFile(file, result)

files = 'a_example.txt  b_read_on.txt  c_incunabula.txt  d_tough_choices.txt  e_so_many_books.txt  f_libraries_of_the_world.txt'.split('  ')
# files = 'a_example.txt  b_read_on.txt'.split('  ')
#files = ['a_example.txt'] 
#files = ['b_read_on.txt']
for f in files:
    print(f)
    run(f)
 