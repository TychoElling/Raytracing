import vec3


class PPM:
    def __init__(self):
        self.f = open("EX.txt","w")
        self.f.write("P3\n" + str(x) + " " + str(y), "\n")

    def writeColor(self, rgb):
        def fff(a):
            a = str(a)
            if len(a) == 2:
                return " " + a
            if len(a) == 3:
                return a
            return "  " + a

        r, g, b = str(rgb.e1), str(rgb.e2), str(rgb.e3)
        rgb = fff(r) + " " + fff(g) + " " + fff(b)
        self.f.write(rgb, "  ")

    def writeFile(self,grid, x, y):
       def writeLine(lst):
            for rgb in lst:
                writeColor(rgb)
            self.f.write("\n")
        for lst in grid:
            writLine(lst)




# See PyCharm help at https://www.jetbrains.com/help/pycharm/