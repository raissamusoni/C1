#Name(ID): Jeremiah Odagwe(30063630) and Raïssa Musoni(30040481)
#lab: 03
#Jeremiah Odagwe did about 50%. Raïssa Musoni did about 50%.

# This program asks user if they want to create a pie chart or bar chart
# and it asks follow up questions that allows for the creation of the chart 


# import libraries random, Simple Graphics
from SimpleGraphics import * 
import random 

# get user input if it's barchart or piechart
PIECHART = 1
BARCHART = 2
print("Chart Creation Menu")
print("1. Pie Chart")
print("2. Bar Chart")
ChartType = int(input("Select your chart type: "))

# when pie chart is selected
if ChartType == PIECHART:
# get user input for title, # of sectors & total value 
    PieChartTitle = input("Enter the title of the chart: ")
    NumberofSectors = int(input("Enter the number of sectors (2 to 6): "))
    TotalValue = int(input("Enter the total value of all sectors: "))
    ListNumberofSectors = range(1,NumberofSectors+1)
    ListNumberofSectorsV = range(1,NumberofSectors)
    STARTVALUE = 0
    STARTVALUEY = 150
    STARTVALUEYSQ = 160
    TITLEX=getWidth()/2
    TITLEY=getHeight()/8
    X = getWidth()/4
    Y = getHeight()/5
    Z = 400
    
    # Draw Title
    setOutline("Black")
    setFont("New Roman","20", "bold")
    text(TITLEX,TITLEY,PieChartTitle,"c")
    
    # Creating the legend with user input of labels
    for i in ListNumberofSectors:
        h = i
        LabelofSector = input("Label sector %d: " %h)
        
        #colour
        r =  random.randint(0,255)
        g =  random.randint(0,255)
        b =  random.randint(0,255)
        setFill(r,g,b)

        # draw the word
        JGAP = 50
        WORDX = 765
        setOutline("Black")
        setFont("New Roman", "8")
        text(WORDX,STARTVALUEY, LabelofSector, "c") 
        STARTVALUEY = STARTVALUEY + JGAP

        # draw the legend
        WIDTH=30
        HEIGHT = 30
        SQX = WORDX - 15
        rect(SQX, STARTVALUEYSQ, WIDTH, HEIGHT)
        STARTVALUEYSQ = STARTVALUEYSQ + JGAP
        
        # drawing the sectors based off of user input for each value (minus last sector)
        if i<NumberofSectors:
            FULLCIRCLEVALUE = 360
            ValueofSector = int(input("Enter the value of the %s sector: " %LabelofSector))
            EndValue = (ValueofSector/TotalValue)*FULLCIRCLEVALUE
            pieSlice(X,Y,Z,Z,STARTVALUE,EndValue)
            STARTVALUE = STARTVALUE + EndValue

        #drawing the last sector using formula
        else:
            pieSlice(X,Y,Z,Z,STARTVALUE,(FULLCIRCLEVALUE-STARTVALUE))


# when bar chart is selected
else:
    # get user input for title, number of bars, gridline interval and label y-axis
    BarChartTitle = input("Enter the title of the chart: ")
    NumberofBars = int(input("Enter the number of bars (2 to 6): "))
    gridlineinterval = int(input("Enter the gridline interval (10 to 100): "))
    yaxislabel = input("Enter the label for the Y-Axis: ")
    
    # setting values needed for drawing bar chart
    Height = 400//gridlineinterval
    Height2 = 400%gridlineinterval
    grid = range(1,Height+1)
    grid2 = range(1,Height+2)
    StartGridY = getHeight()*.75
    Label = 0
    GridY = StartGridY + gridlineinterval
    GridX = 655
    TITLEX=getWidth()/2
    GRIDWIDTH=500
    bottomofgrid1=StartGridY + gridlineinterval

    # draw the title 
    setOutline("Purple")
    setFont("New Roman","20", "bold")
    TITLEY = bottomofgrid1 - 445
    text(TITLEX,TITLEY,BarChartTitle,"c")

    # draw the label for y-axis
    LABELYAXIS = bottomofgrid1 - 200
    LABELXAXIS = 140
    setFont("New Roman","8", "bold")
    text(LABELXAXIS,LABELYAXIS,yaxislabel,"se")

    # draw gridline
    for i in grid:
        setOutline("Black")
        rect(150,StartGridY,GRIDWIDTH,gridlineinterval)
        StartGridY = StartGridY - gridlineinterval

    # draw gridline values
    for i in grid2:
        setOutline("Black")
        setFont("New Roman", "8")
        text(GridX,GridY, Label, "sw")
        Label = Label + gridlineinterval 
        GridY = GridY - gridlineinterval
    # when gridline interval does not divide evenly into 400
    if Height2 != 0:
        correction = Label # gridlineinterval
        rect(150,StartGridY,GRIDWIDTH,gridlineinterval)
        text(GridX,GridY, correction,"sw")
   
    
    # draw the bars and their value labels, colors 
    listNumberofbars = range(1, NumberofBars+1)
    
    #setting values needed for creating the bars
    barwidth = 50
    barspace = (GRIDWIDTH-(NumberofBars*barwidth))//(NumberofBars+1)
    barposx = barspace+150
    barspace2 = barposx+25
    Xposlabel = barspace2

   
    # drawing the bars
    for i in listNumberofbars:
        h=i 
        barlabel = input("Label bar %d: " %h)
        barvalues = int(input("Enter the value of bar %s: " %barlabel))
        bottomofgrid=StartGridY + gridlineinterval
        
        # drawing scheme for when gridline interval does not divide into 400 evenly
        if Height2 != 0:
            barposy = bottomofgrid1 - barvalues 
        # when gridline interval does divide into 400
        else:
            barposy = (400 - barvalues) + bottomofgrid
        
        #colour
        r =  random.randint(0,255)
        g =  random.randint(0,255)
        b =  random.randint(0,255)
        setFill(r,g,b)

        # function to draw the bars
        rect(barposx,barposy, barwidth, barvalues)
        barposx= barposx + barwidth + barspace 

        #labels for bars
        setOutline("Black")
        setFont("New Roman", "8")
        Yposlabel = barposy + 15 + barvalues
        text(Xposlabel, Yposlabel, barlabel, "c" )

        
        #labels for values of bar 
        setOutline("Black")
        setFont("New Roman", "8", "bold")
        Yposlabel2 = 5 + barposy
        text(Xposlabel, Yposlabel2, barvalues, "c" )
        Xposlabel = Xposlabel + barwidth + barspace
    
# Print completion message
print("Your chart is completed.")

