file = open("data4.txt", "w")
le = 0
re = 0
for i in range(100):
    txt = "{0} {1} 45 30 300\n".format(le, re)
    file.write(txt)
    le+=50
    re+=50

for i in range(100):
    txt = "{0} {1} -45 300 30\n".format(le, re)
    file.write(txt)
    le+=50
    re+=50

for i in range(100):
    txt = "{0} {1} -135 40 30\n".format(le, re)
    file.write(txt)
    le+=50
    re+=50

for i in range(100):
    txt = "{0} {1} 135 300 3000\n".format(le, re)
    file.write(txt)
    le+=50
    re+=50