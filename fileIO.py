

f = open('inputFile.txt', 'r')
passfile = open('passfile.txt', 'w')
failfile = open('failfile.txt', 'w' )
for line in f:
    line_split = line.split()
    if line_split[2] =='P':
        passfile.write(line)
    else:
        failfile.write(line)    
f.close()
passfile.close()
failfile.close()

