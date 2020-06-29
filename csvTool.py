
class Color():
    def __init__(self, name):
        self.fields = ['name', 'time', 'id', 'category', 'date']
        self.name = name
        self.id = 0
        self.time = 0
        self.cat = '0'
        self.date = '0'
        
    def setId(self, num):
        self.id = num
        
    def setTime(self, time):
        self.time = time
        
    def setCategory(self, cat):
        self.cat = cat
        
    def setDate(self, date):
        self.date = date

    

class csvColorTool:
    def __init__(self):
        self.filename = filename = "statusData.csv"
        self.red = Color('red')
        self.blue = Color('blue')
        self.white = Color('white')
        self.green = Color('green')
        self.yellow = Color('yellow')
        self.fields = self.red.fields
        self.colors = [self.red, self.blue, self.white, self.green, self.yellow]
        self.rows = [[], [], [], [], []] 
        
    def updateRows(self):
        i = 0
        for color in self.colors:
            self.rows[i] = [color.name, color.time, color.id, color.cat, color.date]
            i += 1
        return
    
#end CSVTool
