
# Press the green button in the gutter to run the script.


f = open("EX.txt","w")
f.write("P3\n")
f.write("256 256\n")
c = (256,0,0)
for i in range(256):
    s = ""
    c1=tuple((list(c)).copy())
    for j in range(256):
        c1 = (max(0,c1[0]-1),min(c1[1]+1,255),c1[2])
        s += fff(c1[0])+ " "+fff(c1[1])+ " "+ fff(c1[2]) + "  "

    f.write(s+"\n")
    c = (max(0, c[0] - 1), c[1],min(c[2] + 1, 255))


def writeColor(r,g,b):
    def fff(a):
        a = str(a)
        if len(a) == 2:
            return " " + a
        if len(a) == 3:
            return a
        return "  " + a
    r,g,b = str(r),str(g),str(b)
    rgb = fff(r)+" " + fff(g) + " " + fff(b)
    f = open("EX.txt","w")
    f.write(rgb,"  ")

if __name__ == '__main__':
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/