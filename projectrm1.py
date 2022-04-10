#Name(ID): Raïssa Musoni(30040481)
#lab: 03

# This program reads a file with a dataset and creates an infographic using SimpleGraphics, generating 3 charts (line chart, bar chart, scatter plot)
# The dataset was created from 2 datasets, one that has data from Canadians and their health characteristics 
# and the other that has an estimate of world population, where the estimates of Canadian population was of interest.

# Canadian Health Characteristics, annual estimates: https://www150.statcan.gc.ca/t1/tbl1/en/cv.action?pid=1310009601
# Total Population - Both Sexes: https://population.un.org/wpp/Download/Standard/Population/ 

#Import SimpleGraphics
from SimpleGraphics import * 

## This function opens the cleaned dataset file, gathers the relevant information in lists, and turns each list into a list of percentage and returns percentage lists 
#  @parameters (None) 
#  @return Dataset, yearslist and the 9 lists of each characteristic in percentage from 2015-2019
def openfile():
    # Open the file
    Dataset = open("Dataset_cleaned.csv", "r")

    # Read line by line from the file and save lists of relevant elements and characteristics
    years = Dataset.readline()
    Years = years.split(';')
    yearslist = []
    for i in range(1,6):
        yearslist.append(Years[i])

    health = Dataset.readline()
    Health = health.split(';')
    healthlist = []
    for i in range(1,6):
        healthlist.append(Health[i])

    mh = Dataset.readline()
    Mh = mh.split(';')
    mhlist = []
    for i in range(1,6):
        mhlist.append(Mh[i])

    stress = Dataset.readline()
    Stress = stress.split(';')
    stresslist = []
    for i in range(1,6):
        stresslist.append(Stress[i])

    overw = Dataset.readline()
    Overw = overw.split(';')
    overwlist = []
    for i in range(1,6):
        overwlist.append(Overw[i])

    obe = Dataset.readline()
    Obe = obe.split(';')
    obeselist = []
    for i in range(1,6):
        obeselist.append(Obe[i])

    diabetes = Dataset.readline()
    Diabetes = diabetes.split(';')
    diabeteslist = []
    for i in range(1,6):
        diabeteslist.append(Diabetes[i])

    highbp = Dataset.readline()
    Highbp = highbp.split(';')
    highbplist = []
    for i in range(1,6):
        highbplist.append(Highbp[i])

    smoke = Dataset.readline()
    Smoke = smoke.split(';')
    smokelist = []
    for i in range(1,6):
        smokelist.append(Smoke[i])

    drink = Dataset.readline()
    Drink = drink.split(';')
    drinklist = []    
    for i in range(1,6):
        drinklist.append(Drink[i])

    estpop = Dataset.readline()
    Estpop = estpop.split(';')
    estpoplist = []
    for i in range(1,6):
        estpoplist.append(Estpop[i])

    # converts the lists to lists of percentage based off of estimated population for respective years
    obesep = []
    overweight = []
    diabetic = []
    hbpressure = []
    smoking = []
    hdrinking = []
    phealth = []
    pmhealth = []
    lifestress = []

    # each element is divided by the population for that year, to return the population percetage of that particular element
    for i in range(5):
        point=(float(obeselist[i])/float(estpoplist[i]))*100
        obesep.append(int(point))
        point1=(float(overwlist[i])/float(estpoplist[i]))*100
        overweight.append(int(point1))
        point2=(float(diabeteslist[i])/float(estpoplist[i]))*100
        diabetic.append(int(point2))
        point3=(float(highbplist[i])/float(estpoplist[i]))*100
        hbpressure.append(int(point3))
        point4=(float(smokelist[i])/float(estpoplist[i]))*100
        smoking.append(int(point4))
        point5=(float(highbplist[i])/float(estpoplist[i]))*100
        hdrinking.append(int(point5))
        point6=(float(healthlist[i])/float(estpoplist[i]))*100
        phealth.append(int(point6))
        point7=(float(mhlist[i])/float(estpoplist[i]))*100
        pmhealth.append(int(point7))
        point8=(float(stresslist[i])/float(estpoplist[i]))*100
        lifestress.append(int(point8))
    
    return Dataset,yearslist,obesep,overweight,diabetic,hbpressure,smoking,hdrinking,phealth,pmhealth,lifestress

## This function loads a background image and resizes the window to a 1500 Width and 650 Height
#  @parameters (None)
#  @return (None)
def loadbackgroundimage():
    #resize window to portion of background image
    background = loadImage("background1.png")

    W = getWidth(background)
    H = getHeight(background)-350
    resize(W,H)
    drawImage(background, 0, 0) #1500,650

## This function creates the Project Title
#  @parameters (None)
#  @return (None)
def projectTitle():    
    # Project Title
    OFFSET = 110
    PTITLE_X = (getWidth()/2) - OFFSET
    PTITLE_Y = 40
    ptitle = "Health Highlights for Canadians (2015-2019)"
    setFont("New Roman", "16", "underline") 
    text(PTITLE_X, PTITLE_Y,ptitle,"c")

## This function creates the first chart, line chart
#  @param yearslist: list of the relevant years 2015-2019 
#  @param obesep: list of the obesity numbers for the relevant years, divided by estimated population for those years 
#  @param overweight: list of the overweight numbers for the relevant years, divided by estimated population for those years
#  @param diabetic: list of the diabetic numbers for the relevant years, divided by estimated population for those years
#  @return (None)
def chart1(yearslist,obesep,overweight,diabetic):
    # Chart 1 - estimated percentage of population that are obese, overweight, diabetic - line chart
    # setting local constants and creating the box and the x and y axis lines
    BG1X = 10
    BG1Y = 90
    BG1W = 360  
    BG1H = 280 
    MARGIN1 = 40
    topofY_x = BG1X+MARGIN1
    topofY_y = BG1Y+MARGIN1
    originy = BG1Y+BG1H-MARGIN1
    endofX_x = BG1X+BG1W-MARGIN1
    endofX_y = BG1Y+BG1H-MARGIN1
    rect(BG1X, BG1Y, BG1W, BG1H)
    line(topofY_x,topofY_y,topofY_x,originy,endofX_x,endofX_y)

    # Graph 1 Title 
    title1x = BG1X+(BG1W/2)
    title1y = BG1Y+20
    title1 = "Obesity, Overweight, Diabetic Levels"
    setFont("New Roman", "10", "bold") 
    text(title1x,title1y,title1,"c")

    # Y-scale 
    scale = 0
    for i in range(1,11):
        y=i*20
        line(topofY_x,originy-y,endofX_x,endofX_y-y)
        setFont("New Roman", "7", "bold") 
        scale = scale + 20
        Scale = str(scale)+"%"
        text(topofY_x,originy-y,Scale,"e")

    # X-scale
    space = 70
    YLSPACE = 20
    XLSPACE = 5
    text(topofY_x+XLSPACE,endofX_y+YLSPACE,str(yearslist[0]),"s")
    for i in range(1,5):
        Year = yearslist[i]
        x=i*space
        text(topofY_x+XLSPACE+x,endofX_y+YLSPACE,str(Year),"s")

    # Obese, overweight, diabetic lines for the line chart
    for i in range(len(yearslist)):
        x=i*space
        setOutline("dark salmon")
        line(topofY_x+XLSPACE,originy-(int(obesep[i-1])),topofY_x+XLSPACE+x,originy-(int(obesep[i])))
        setOutline("cyan4")
        line(topofY_x+XLSPACE,originy-(int(overweight[i-1])),topofY_x+XLSPACE+x,originy-(int(overweight[i])))
        setOutline("dark olive green")
        line(topofY_x+XLSPACE,originy-(int(diabetic[i-1])),topofY_x+XLSPACE+x,originy-(int(diabetic[i])))


    # legend #1
    # creating the box for which the legend will be in
    setOutline("black")
    lw1 = BG1W*(1/2)
    lh1 = BG1H*(1/4)
    lx1 = ((BG1X + BG1W)*(1/2))-(lw1*(1/2))
    ly1 = BG1Y + BG1H + (lh1*(1/3))
    rect(lx1,ly1,lw1,lh1)

    # creating the rectangles for the corresponding labels and naming them
    obx = lx1 + 10
    oby = ly1 + 10
    obh = lh1/7
    obw = lh1/7
    legendmargin=lh1/7
    setOutline("black")
    setFill("dark salmon")
    rect(obx,oby,obh,obw)
    setOutline("black")
    text(obx+20,oby,"Obese (Adults)","nw")

    setOutline("black")
    setFill("cyan4")
    rect(obx,oby+(2*legendmargin),obh,obw)
    setOutline("black")
    text(obx+20,oby+(2*legendmargin),"Overweight (Adults)","nw")

    setOutline("black")
    setFill("dark olive green")
    rect(obx,oby+(4*legendmargin),obh,obw)
    setOutline("black")
    text(obx+20,oby+(4*legendmargin),"Diabetes","nw")

## This function creates the second chart, bar chart
#  @param yearslist: list of the relevant years 2015-2019 
#  @param hbpressure: list of the high blood pressure numbers for the relevant years, divided by estimated population for those years 
#  @param smoking: list of the smoking numbers for the relevant years, divided by estimated population for those years
#  @param hdrinking: list of the heavy drinking numbers for the relevant years, divided by estimated population for those years
#  @return (None)
def chart2(yearslist,hbpressure,smoking,hdrinking):
    # Chart 2 - estimated % of population that have high blood pressure, smoke, are heavy drinkers - bar chart
    # local constants and creating the box and x and y line
    setOutline("black")
    setFill("white")
    BG2X = 460
    BG2Y = 90
    BG2W = 360  
    BG2H = 280   
    MARGIN2 = 40
    topofY2_x = BG2X+MARGIN2
    topofY2_y = BG2Y+MARGIN2
    originy2 = BG2Y+BG2H-MARGIN2
    endofX2_x = BG2X+BG2W-MARGIN2
    endofX2_y = BG2Y+BG2H-MARGIN2
    rect(BG2X, BG2Y, BG2W, BG2H)
    line(topofY2_x,topofY2_y,topofY2_x,originy2,endofX2_x,endofX2_y)

    # Graph 2 Title 
    title2x = BG2X+(BG2W/2)
    title2y = BG2Y+20
    title2 = "HBP, Smoking, Heavy Drinking Levels"
    setFont("New Roman", "10", "bold") 
    text(title2x,title2y,title2,"c")

    #Draw Bar 1,2,3 for the 5 years
    #setting relevant constants to begin the drawing
    SPACETOBAR1=50
    BARWIDTH=10
    bar1x=topofY2_x+SPACETOBAR1
    bar1y=topofY2_y+BG2H-(int(hbpressure[0]))-(8*BARWIDTH)

    bar2x=topofY2_x+SPACETOBAR1+BARWIDTH
    bar2y=topofY2_y+BG2H-(int(smoking[0]))-(8*BARWIDTH)

    bar3x=topofY2_x+SPACETOBAR1+(2*BARWIDTH)
    bar3y=topofY2_y+BG2H-(int(hdrinking[0]))-(8*BARWIDTH)

    #drawing the bars & X-axis labels
    for i in range(len(yearslist)):  
        setOutline("dark salmon")
        setFill("dark salmon")
        rect(bar1x,bar1y,BARWIDTH,(int(hbpressure[i])))

        setOutline("cyan4")
        setFill("cyan4")
        rect(bar2x,bar2y,BARWIDTH,(int(smoking[i])))
        #X-axis labels
        setOutline("black")
        setFont("New Roman", "7", "bold") 
        text(bar2x+5,bar1y+(2*int(hbpressure[i])),yearslist[i],"c")
        
        setOutline("dark olive green")
        setFill("dark olive green")
        rect(bar3x,bar3y,BARWIDTH,(int(hdrinking[i])))
        bar1x= bar1x + (4*BARWIDTH) 
        bar2x= bar2x + (4*BARWIDTH)
        bar3x = bar3x + (4*BARWIDTH)

    # Y-scale 
    setOutline("Black")
    scale = 0
    for i in range(1,15):
        y=i*14
        line(topofY2_x,originy2-y,endofX2_x,endofX2_y-y)
        setFont("New Roman", "7", "bold") 
        scale = scale + 14
        Scale = str(scale)+"%"
        text(topofY2_x,originy2-y,Scale,"e")

    # legend #2
    # setting the box 
    setFill("white")
    lw2 = BG2W*(1/2)
    lh2 = BG2H*(1/4)
    lx2 = (((2*BG2X) + BG2W)*(1/2))-(lw2*(1/2))
    ly2 = BG2Y + BG2H + (lh2*(1/3)) 
    rect(lx2,ly2,lw2,lh2)

    # creating the rectangles for the corresponding labels and naming them
    bx = lx2 + 10
    by = ly2 + 10
    bh = lh2/7
    bw = lh2/7
    legend2margin=lh2/7
    setOutline("black")
    setFill("dark salmon")
    rect(bx,by,bh,bw)
    setOutline("black")
    text(bx+20,by,"High Blood Pressure","nw")

    setOutline("black")
    setFill("cyan4")
    rect(bx,by+(2*legend2margin),bh,bw)
    setOutline("black")
    text(bx+20,by+(2*legend2margin),"Smoker (Daily or Occasional)","nw")

    setOutline("black")
    setFill("dark olive green")
    rect(bx,by+(4*legend2margin),bh,bw)
    setOutline("black")
    text(bx+20,by+(4*legend2margin),"Heavy Drinking","nw")

## This function creates the third chart, scatter plot
#  @param yearslist: list of the relevant years 2015-2019 
#  @param pmhealth: list of the perceived mental health (poor) numbers for the relevant years, divided by estimated population for those years 
#  @param phealth: list of the perceived health (poor) numbers for the relevant years, divided by estimated population for those years
#  @param lifestress: list of the extreme life stress numbers for the relevant years, divided by estimated population for those years
#  @return (None)
def chart3(yearslist,pmhealth,phealth,lifestress):
    # Chart 3 - estimated % of population that perceive their mental health and health as poor, have extreme life stress - scatterplot
    # setting local constants and relevant variables to be used
    setOutline("black")
    setFill("White")
    BG3X = 910
    BG3Y = 90
    BG3W = 360 
    BG3H = 280  
    MARGIN3 = 40
    topofY3_x = BG3X+MARGIN3
    topofY3_y = BG3Y+MARGIN3
    originy3 = BG3Y+BG3H-MARGIN3
    originy3p = originy3 - 14
    endofX3_x = BG3X+BG3W-MARGIN3
    endofX3_y = BG3Y+BG3H-MARGIN3
    rect(BG3X, BG3Y, BG3W, BG3H)
    line(topofY3_x,topofY3_y,topofY3_x,originy3,endofX3_x,endofX3_y)
    x3space = 50

    # Graph 2 Title 
    title3x = BG3X+(BG3W/2)
    title3y = BG3Y+20
    title3 = "Health, Mental Health, Life Stress Levels"
    setFont("New Roman", "10", "bold") 
    text(title3x,title3y,title3,"c")

    # Y-scale
    setOutline("Black")
    scale = 0
    for i in range(1,15):
        y=i*14
        line(topofY3_x,originy3-y,endofX3_x,endofX3_y-y)
        setFont("New Roman", "7", "bold") 
        scale = scale + 4
        Scale = str(scale)+"%"
        text(topofY3_x,originy3-y,Scale,"e")
    
    # creating the Scatterplot and X-axis labels
    for i in range(len(yearslist)):
        setFill("dark salmon")
        setOutline("dark salmon")
        ellipse(topofY3_x+x3space,originy3p-(int(pmhealth[i])),5,5)

        setFill("cyan4")
        setOutline("cyan4")
        ellipse(topofY3_x+x3space,originy3p-(int(phealth[i])),5,5)

        setFill("dark olive green")
        setOutline("dark olive green")
        ellipse(topofY3_x+x3space,originy3p-(int(lifestress[i])),5,5)

        setOutline("black")
        text(topofY3_x+x3space,originy3+15,yearslist[i])

        x3space = x3space + 50

    # legend #3 - creating the box
    setFill("white")
    setOutline("black")
    lw3 = BG3W*(1/2)
    lh3 = BG3H*(1/4)
    lx3 = (((2*BG3X) + BG3W)*(1/2))-(lw3*(1/2))
    ly3 = BG3Y + BG3H + (lh3*(1/3))
    rect(lx3,ly3,lw3,lh3)

    # creating the rectangles for the respective categories
    sx = lx3 + 10
    sy = ly3 + 10
    sh = lh3/7
    sw = lh3/7
    legend3margin=lh3/7
    setOutline("black")
    setFill("dark salmon")
    rect(sx,sy,sh,sw)
    setOutline("black")
    text(sx+20,sy,"Perceived Mental Health (Poor)","nw")

    setOutline("black")
    setFill("cyan4")
    rect(sx,sy+(2*legend3margin),sh,sw)
    setOutline("black")
    text(sx+20,sy+(2*legend3margin),"Perceived Health (Poor)","nw")

    setOutline("black")
    setFill("dark olive green")
    rect(sx,sy+(4*legend3margin),sh,sw)
    setOutline("black")
    text(sx+20,sy+(4*legend3margin),"Perceived Life Stress (Extreme)","nw")

## This function creates a blurb of obersvations for each chart
#  @parameters (None)
#  @return (None)
def blurb():
    # Blurb-summary of what the data reveals when they are in charts
    # Creating the Blurb
    setFill("white")
    setOutline("black")
    blurbx = getWidth()*(1/4)
    blurby = getHeight()*(4/5)
    blurbw = 600
    blurbh = blurbw*(1/5)
    rect(blurbx,blurby,blurbw,blurbh)

    # textlines for the blurb
    SPACE = 10
    SPACE1 = 15
    blurbtx = blurbx + SPACE
    blurbty = blurby + SPACE1
    blurbtext = "For Chart 1, we notice that there has been some consistency with respect to obesity (adults), overweight (adults) and diabetic"
    text(blurbtx,blurbty,blurbtext, "nw")
    blurbtext2 = "levels. Notably, a quarter of the population, who are adults, are overweight. This number could be higher when including "
    text(blurbtx,blurbty+SPACE1,blurbtext2,"nw")
    blurbtext3 = "the rest of the population. For Chart 2, the levels are pretty evenly distributed. Same percentage for high blood pressure"
    text(blurbtx,blurbty+(2*SPACE1),blurbtext3,"nw")
    blurbtext4 = "and heavy drinking. There seems to be a drop for smoking, however overall it is around the same percentage: 12-14%."
    text(blurbtx,blurbty+(3*SPACE1),blurbtext4,"nw")
    blurbtext5 = "For Chart 3, the percentage of those who have extreme life stress is more than the percentage of those who perceive their"
    text(blurbtx,blurbty+(4*SPACE1),blurbtext5,"nw")
    blurbtext6 = "health and mental health to be poor. Between 4%-6% of the population perceive their mental health to be poor."
    text(blurbtx,blurbty+(5*SPACE1),blurbtext6,"nw")

## This function closes the cleaned dataset file
#  @param Dataset: the cleaned dataset file
#  @return (None) 
def closefile(Dataset):
    # Close file
    Dataset.close()

## Main logic of program
#  @parameters (None)
#  @return (None)
def main():
    # open the cleaned data file and return relevant lists that will be used to create charts
    Dataset,yearslist,obesep,overweight,diabetic,hbpressure,smoking,hdrinking,phealth,pmhealth,lifestress = openfile()
    # load background image and resize the window
    loadbackgroundimage()
    # draw the project title
    projectTitle()
    # create Chart 1
    chart1(yearslist,obesep,overweight,diabetic)
    # create Chart 2
    chart2(yearslist,hbpressure,smoking,hdrinking)
    # create Chart 3
    chart3(yearslist,pmhealth,phealth,lifestress)
    # create blurb
    blurb()
    #close cleaned data file
    closefile(Dataset)
# Call to main
main()
