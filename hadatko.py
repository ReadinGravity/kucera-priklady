#počet zapísaných hier v súbore
f=open('text/hada.txt', 'r')
f_all=f.read()
count=0
for i in f_all:
    if i in '\n':
        count+=1
print('pocet hier je:', count)

#koľko krokov mala najdlhšia hra
f = open('text/hada.txt', 'r')
lines = f.readlines()
longest_line = max(lines, key=len)
print('najdlhsia hra mala:', len(longest_line), 'krokov')

#write
zoz = f.readlines()
fw = open("text/hada_write.txt", "w")
for i in range(3):
    jozkomrkvicka = ""
    count = 1
    por = 0
    riadok = zoz
    while por < len(riadok)-1:
        while riadok[por] == riadok[por+1]:
            count += 1
            por += 1
        jozkomrkvicka += riadok[por] + str(count) + " "
        count = 1
        por += 1
    fw.write(jozkomrkvicka)
    fw.write('\n')

