# debug mode


debug = True

class basedecoder:
    def __init__(self):
        self.active = ""
        self.temp = ""
        self.temp2 = []
        self.temp3 = []
        self.cellmatrix = []
        self.celllocs = []
        self.levelwidth = 0
        self.levelheight = 0

    # get height of level from self.temp
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
    
    # get width of level from self.temp
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

    # set self.active if code meets correct criteria
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

    # create a list containing all of the cells in the code
    def create_cell_matrix(self):
        def mapfunc(a,b):
            return((a,b))
        code = self.active
        current = ""
        index = 0
        stop = False
        passed = 0
        while not stop:
            current = code[index]
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
            while True:
                current = code[index]
                index += 1
                if current == "," or current == ";":
                    break
                currentcell += current
            if debug:
                print()
                print(currentcell)
            
            self.temp2.append(currentcell)
            if current == ";":
                stop = True
            else:
                pass
            
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

            print("\n\n")
            
            a = ""
            y = ""
            z = 4
            while True:
                a = i[z]
                if a == ".":
                    break
                else:
                    z += 1
                    y += a
            xloc = int(y) # doesn't work, probably something near line 130
            z += 1
            y = ""
            while True:
                try:
                    a = i[z]
                except IndexError:
                    break
                z += 1
                y += a

            self.cellmatrix.append(currentcell)
            currentcell = ""
            yloc = int(y)
            loc = (xloc,yloc)
            if debug:
                print(loc)
                print("\n\n")
            self.temp3.append(loc)
        self.celllocs = self.temp3.copy()
        self.temp2 = self.temp3 = []



decoder = basedecoder()

decoder.set_active("V1;20;20;;0.0.6.12,0.1.6.11,0.2.5.11,0.3.5.12,1.0.7.10,4.0.10.14,4.1.10.15,4.0.10.16,4.1.10.17,4.0.10.18,4.1.11.14,4.2.11.15,4.3.11.16,4.3.11.17,4.1.11.18,4.0.12.14,4.2.12.15,7.0.12.16,4.0.12.17,4.0.12.18,0.3.13.1,0.3.13.2,0.3.13.3,0.3.13.4,0.3.13.5,0.3.13.6,5.3.13.7,5.3.13.8,5.3.13.9,5.3.13.11,5.3.13.12,5.3.13.13,4.1.13.14,4.1.13.15,4.1.13.16,4.0.13.17,4.1.13.18,0.3.14.1,0.3.14.2,0.3.14.3,0.3.14.4,0.3.14.5,0.3.14.6,5.3.14.7,5.3.14.8,5.3.14.9,5.3.14.10,5.3.14.12,5.3.14.13,4.0.14.14,4.1.14.15,4.0.14.16,4.1.14.17,4.0.14.18,0.3.15.1,0.3.15.2,0.3.15.3,0.3.15.4,0.3.15.5,0.3.15.6,5.3.15.7,5.3.15.9,5.3.15.11,5.3.15.13,0.3.13.0,0.3.14.0,0.3.15.0,8.0.13.19,8.0.14.19,8.0.15.19,2.0.15.8,2.0.15.10,2.0.14.11,2.0.15.12,0.2.13.10,3.0.2.5,0.1.3.5,0.1.3.4,0.1.3.6,3.0.2.6,3.0.1.4,5.0.2.4,6.0.2.17,3.3.2.16,3.0.1.17,3.1.2.18,3.2.3.17;;")
decoder.create_cell_matrix()

print(f"""
code: {decoder.active}
width: {decoder.levelwidth}
height: {decoder.levelheight}
matrix: {decoder.cellmatrix}
celllocs: {decoder.celllocs}
temp2: {decoder.temp2}
temp3: {decoder.temp3}
""")

# TODO:
#     visualise data 🤪