fr = open("text/meteo.txt", "r")

#pocet merani
fr_all=fr.read()
count=0
for i in fr_all:
    if i in "\n":
        count+=1
print("pocet merani je:", count)

#namerane teploty ci kieho
with open("text/meteo.txt") as rd:
    items = rd.readlines()
j = [el[21:26] for el in items]
print(*j)

#kod stanice kde bola max temp
fr.seek(0)
zoz = fr.readlines()
zoz_temp = []
for w in range(count):
    teplota, temp  = "", ""
    riadok = zoz[w]
    for w in range(5):
        teplota += riadok[21 + w]
    if riadok[21] == "+":
        for t in range(4):
            if riadok[22 + t] == ",":
                temp += "."
            else:
                temp += riadok[22 + t]
    else:
        for f in range(5):
            if riadok[21 + f] == ",":
                temp += "."
            else:
                temp += riadok[21 + f]
    zoz_temp.append(float(temp))

#max temp itself
zoz_temp.sort()
print("")


#kod stanice
str_max_temp = ""
code = ""
for m in str(zoz_temp[-1]):
    if m == ".":
        str_max_temp += ","
    else:
        str_max_temp += m
for m in zoz:
    if str_max_temp in m:
        for a in range(3):
            code += m[a]
print(zoz_temp[-1],",",code)

#priemer temp = avr
sum = 0
for i in zoz_temp:
    sum += i
avr=sum/len(zoz_temp)
print(avr)



