#multiple day plot
import matplotlib
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from csvTool import csvColorTool


class DataCollect:
    def __init__(self, ct):
        self.header = [ct.red.cat, ct.blue.cat, ct.white.cat, ct.green.cat, ct.yellow.cat]
        self.filename = ct.filename
        self.ct = ct
        
    def readCSV(self):
        self.data_r = pd.read_csv(self.filename, delimiter = ',')
         
    # Takes total data and creates sub arrays for each bar category 
    def gatherData(self, rawData): # make better plz
        dataSize = len(rawData)
        dataR = []
        dataB = []
        dataW = []
        dataG = []
        dataY = []
        
        for i in range(0, 5):
            print rawData.iloc[0].iloc[i]
            
        #        [rawData.iloc[color].iloc[field]] where field == 1 == 'time'
        dataR += [rawData.iloc[0].iloc[1]]
        dataB += [rawData.iloc[1].iloc[1]]
        dataW += [rawData.iloc[2].iloc[1]]
        dataG += [rawData.iloc[3].iloc[1]]
        dataY += [rawData.iloc[4].iloc[1]]
        '''
        for day in range(0, dataSize):
            dataR += [rawData.iloc[day].iloc[0]]
            dataB += [rawData.iloc[day].iloc[1]]
            dataW += [rawData.iloc[day].iloc[2]]
            dataG += [rawData.iloc[day].iloc[3]]
            dataY += [rawData.iloc[day].iloc[4]]
        '''
        
        # Necessary for creating a stacked bar graph
        # This is for the "bottom" parameter of the plot
        dr = np.array(dataR) # dr --> data Red
        db = np.array(dataB) # db --> data Blue
        dw = np.array(dataW) # dw --> data White
        dg = np.array(dataG) # dg --> data Green
        dy = np.array(dataY) # dy --> data Yellow
        return [dr, db, dw, dg, dy]

    
        
       
class BarGraph:
    def __init__(self):
        self.ct = csvColorTool()
        #self.filename = self.ct.filename
        self.dc = DataCollect(self.ct)
        self.dataGrabSize_ = 10
        self.x = self.defineBarCount()
    
        
    def setDataSize(self, num):
        dataGrabSize_ = num
        
        
    def defineBarCount(self):
        x = []
        for i in range(0, self.dataGrabSize_):
            x += [i]
        return x    
        
        
    # Annotate every bar with data
    def labeler(self, rect):
        for rect in rects:
            h = rect.get_height()
            ax.annotate('{}'.format(h),
                        xy = (rect.get_x() + rect.get_width() / 2, h),
                        xytext = (0, 0),
                        textcoords = "offset points",
                        ha = 'center',                    
                        va = 'bottom')
            
            
    # Label every bar
    def labelBars(self, barList):
        for bar in barList:
            self.labeler(bar)
            
            
    # Return x-axis list of days --> [D1, D2, ... , Dn]
    def getDayLabels(self):
        days = []
        for i in range(0, self.dataGrabSize_):
            dayNumber = str(i + 1)
            days += ['D' + dayNumber]
        return days
                
    
    def setVisualCharacteristics(self, barList, ax):
        cats = self.dc.header
        # x-axis
        days = self.getDayLabels()
        ax.set_xticklabels(days)
        ax.set_xticks(self.x)
        
        # y-axis
        ax.set_ylabel('Time')
        
        # Details   
        ax.legend(((barList[0][0]), barList[1][0], barList[2][0], barList[3][0], barList[4][0]), (cats[0], cats[1], cats[2], cats[3], cats[4]))
        ax.set_title('Colors and Time graph')
        #labelBars(barList)
       
        return ax
        
        
    def initStackedPlot(self):
        # Set graph numerical characteristics
        x = self.x
        width = 0.15
        fig, ax = plt.subplots()
        ax.grid(zorder=0)
        
        # Gather raw data into numpy data lists --> Provides data points and 'bottom' parameter for stacked bar graph
        dataLists = self.dc.gatherData(self.dc.data_r)
        
        # Collect data into each bar
        redBar =    ax.bar(x, dataLists[0], width, color ='r', edgecolor = 'black', zorder=3)
        blueBar =   ax.bar(x, dataLists[1], width, bottom = dataLists[0], color = 'b', edgecolor = 'black',zorder=3)
        whiteBar =  ax.bar(x, dataLists[2], width, bottom = dataLists[0] + dataLists[1], color = '#d3d3d3', edgecolor = 'black', zorder=3)
        greenBar =  ax.bar(x, dataLists[3], width, bottom = dataLists[0] + dataLists[1] + dataLists[2], color = 'g', edgecolor = 'black', zorder=3)
        yellowBar = ax.bar(x, dataLists[4], width, bottom = dataLists[0] + dataLists[1] + dataLists[2] + dataLists [3] ,color = 'y', edgecolor = 'black', zorder=3)
        barList = [redBar, blueBar, whiteBar, greenBar, yellowBar]
        
        ax = self.setVisualCharacteristics(barList, ax)
        fig.tight_layout()
        return plt


    def drawPlot(self):
        # Assign <self.dc> a variable for visual simplicity
        dataCollect = self.dc
        
        # Read the CSV provided
        dataCollect.readCSV()
        
        # initialize the plot, and assign it to variable <plt>
        plt = self.initStackedPlot()
        
        # Illustrate the plot to user
        plt.show()



#end barGraphStack