f = open('inputFile.txt')
count=0
for line in f:
    print(str(count) + " " + line)
    count = count + 2
f.close()
