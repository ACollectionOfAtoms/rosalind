def main():
    o = open('rosalind_ini5.txt' , 'r')
    o = list(o)
    f = open('output.txt', 'w')
    for line in o:
        line.strip()
    for i in range(1, len(o), 2) :
        f.write(o[i])
main()
