debug = True

class basedecoder:
    def __init__(self):
        self.active = ""
        self.temp = ""
        self.temp2 = []
        self.cellmatrix = []
        self.levelwidth = 0
        self.levelheight = 0
    
    def get_height(self):
        code = self.temp
        current = ""
        index = 0
        height = ""
        stop = False
        passed = 0
        while not stop:
            current = code[index]
            if debug:
                print(current)
            if current == ";":
                passed += 1
            if passed == 2:
                stop = True
            index += 1
        
        stop = False

        if debug:
            print("----")
        
        while not stop:
            current = code[index]
            if debug:
                print(current)
            if current == ";":
                stop = True
            else:
                height += current
            index += 1
        if debug:
            print("""
            
            """)
        return(int(height))
    
    def get_width(self):
        code = self.temp
        current = ""
        index = 0
        width = ""
        stop = False
        while not stop:
            current = code[index]
            if debug:
                print(current)
            if current == ";":
                stop = True
            index += 1
        
        stop = False

        if debug:
            print("----")
        
        while not stop:
            current = code[index]
            if debug:
                print(current)
            if current == ";":
                stop = True
            else:
                width += current
            index += 1
        if debug:
            print("""
            
            """)
        return(int(width))

    def set_active(self,code):
        if not code[1] == "1":
            print("Error: Code is not V1.")
        else:
            self.temp = code
            if self.get_width() < 51:
                if self.get_height() < 51:
                    self.active = code
                    self.levelheight = self.get_height()
                    self.levelwidth = self.get_width()
                    self.temp = ""
                else:
                    self.temp = ""
                    print("Level cannot be taller than 50.")
            else:
                print("Level cannot be wider than 50.")
                self.temp = ""

    # gigachad smokes
    def create_cell_matrix(self):
        code = self.active
        current = ""
        index = 0
        stop = False
        passed = 0
        while not stop:
            current = code[index]
            if debug:
                print(current)
            if current == ";":
                passed += 1
            if passed == 4:
                stop = True
            index += 1
        
        print("----")
        stop = False
        currentcell = ""

        while not stop:
            currentcell = ""
            for i in range(7):
                current = code[index]
                if debug:
                    print(current)
                index += 1
                currentcell += current
            if debug:
                print()
                print(currentcell)
            
            self.temp2.append(currentcell)

            if code[index + 1] == ";":
                stop = True
                if debug:
                    print()
                    print("End of cells.")
            else:
                index += 1
            
            if debug:
                print()

        currentcell = ""
        x = ""
        for i in self.temp2:
            x = i[0]
            if debug:
                print(i)
                print(x)
            if x == "0":
                currentcell += "GE"
            elif x == "1":
                currentcell += "CW"
            elif x == "2":
                currentcell += "CC"
            elif x == "3":
                currentcell += "MO"
            elif x == "4":
                currentcell += "SL"
            elif x == "5":
                currentcell += "PU"
            elif x == "6":
                currentcell += "WA"
            elif x == "7":
                currentcell += "EN"
            elif x == "8":
                currentcell += "TR"
            x = i[2]
            if x == "0":
                currentcell += "1"
            elif x == "1":
                currentcell += "2"
            elif x == "2":
                currentcell += "3"
            elif x == "3":
                currentcell += "4"
            self.cellmatrix.append(currentcell)
            currentcell = ""



decoder = basedecoder()

decoder.set_active("V1;3;1;;7.0.0.0,3.2.2.0;;")
decoder.create_cell_matrix()

print(f"""
code: {decoder.active}
width: {decoder.levelwidth}
height: {decoder.levelheight}
matrix: {decoder.cellmatrix}
temp2: {decoder.temp2}
""")