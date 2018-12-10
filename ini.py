def main():
    f = open("codigos.txt")
    c = f.readlines()
    c = [x.strip().split("-")[0] for x in c]
    c = list(set(c))

    print(c)

main()