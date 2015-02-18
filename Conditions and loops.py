def main():
    a = 4631
    b = 9285
    c = 0
    for i in range(a  , b + 1):
        if i % 2 != 0:
            c += i
    print c
main()
