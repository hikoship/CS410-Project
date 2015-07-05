f = open('postdata.txt')
f2 = open('postdata2.txt', 'w')
i = 1
for line in f:
    if(i % 10 == 0):
        f2.write(line)
    i+=1

