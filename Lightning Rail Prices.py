def totDist(digg1, stopps, dists):
    tote = 0
    for i in range(digg1, digg1+stopps):
        tote += dists[i]
    return tote

allNames = ["Aruldusk", "Atur", "Fairhaven", "Flamekeep", "Fort Zombie", "Gatherhold", "Hatheril", "Irontown", "Korranberg", "Korth", "Krona Peak", "Marketplace", "Passage", "Rekkenmark", "Sharn", "Sigilstar", "Starilaskur", "Sterngate", "Sword Keep", "Thaliost", "Vathirond", "Vedykar", "Vulyar", "Wroat", "Zolanberg"]
thalLine = ["Sharn","Wroat","Hatheril","Sword Keep","Marketplace","Passage","Fairhaven","Thaliost","White_Arch"]
korrLine = ["Sharn","Wroat","Starilaskur","Sterngate","Zolanberg","Korranberg"]
flamLine = ["Sharn","Wroat","Starilaskur","Vathirond","Aruldusk","Sigilstar","Flamekeep"]
eastLine = ["Krona Peak","Irontown","Vulyar"]
karrLine = ["White_Arch","Korth","Rekkenmark","Atur","Vedykar","Fort Zombie","Gatherhold"]

thalDist = [212,735,184,331,322,461,620,620]
korrDist = [212,1007,396,260,271]
flamDist = [212,1007,315,342,164,470,620]
eastDist = [267,509]
karrDist = [0,128,146,248,256,323]
westDist = [620,470,164,342,356,184,331,322,461,620]

bigList = [thalLine, korrLine, flamLine, eastLine, karrLine, westLine]
bigNames = ["Thaliost Line","Korranberg Line","Flamekeep Line","Eastern Line","Karrnath Line","Flamekeep-Thaliost Line"]
bigDist = [thalDist, korrDist, flamDist, eastDist, karrDist, westDist]

conList = ["Sharn", "Wroat", "Starilaskur", "White_Arch"]

while True:
    stop1 = input("Please enter the first stop: ").title()
    while stop1 not in allNames:
        stop1 = input("Unknown station, please try again: ").title()
    print("First stop is: {}".format((stop1).upper()))
    stop2 = input("Please enter the second stop: ").title()
    while stop2 not in allNames:
        stop2 = input("Unknown station, please try again: ").title()
    print("Final stop is: {}\n".format((stop2).upper()))

    startList = []   
    endList = []

    y = 0
    x = 0

    for a in bigList:
        y = 0
        for b in bigList[x]:
            if stop1 in bigList[x][y]:
                startList.append(bigNames[x])
            if stop2 in bigList[x][y]:
                endList.append(bigNames[x])
            y += 1   
        x += 1

    print("Lines that contain origin: {}".format(startList))
    print("Lines that contain destination: {}".format(endList))
 
    for x in endList:
        if x in startList:
            print("route {}".format(x))
            break
        else:
            possCon = []
            z = 0
            for x in endList:
                y = bigNames.index(endList[z])
                z += 1              
                for x in bigList[y]:
                    if x in conList:
                        possCon.append(x)
            conSet = set(possCon)
    print("possible connections: {}".format(conSet))
            
""" 

while True:



    stop1 = input("Please enter the first stop: ").title()

    while stop1 not in allNames:

        stop1 = input("Unknown station, please try again: ").title()

    print("First stop is: {}".format((stop1).upper()))

    stop2 = input("Please enter the second stop: ").title()

    while stop2 not in allNames:

        stop2 = input("Unknown station, please try again: ").title()

    print("Final stop is: {}".format((stop2).upper()))

    

    print("\n")



    startList = []

    endList = []



    y = 0

    x = 0

    for a in bigList:

        y = 0

        for b in bigList[x]:
            if stop1 in bigList[x][y]:
                startList.append(bigNames[x])
            if stop2 in bigList[x][y]:
                endList.append(bigNames[x])
            y += 1
        
        x += 1

    print("Lines that contain origin: {}".format(startList))
    print("Lines that contain destination: {}".format(endList))
    
    
#if sl = el good. else look for connetion station in both
        
"""        
    x += 1



    i = -1



    route = 0







    while True: 



        i += 1        



        if i != len(bigList):



            print("Checking {}".format(bigNames[i]))



            if stop1 and stop2 in bigList[i]:



                line = bigNames[i]



                dig1 = bigList[i].index(stop1)



                dig2 = bigList[i].index(stop2)



                if dig2 < dig1:



                    dig1, dig2 = dig2, dig1



                stops = dig2 - dig1



                distance = totDist(dig1, stops, bigDist[i])



                route = 1

                

                break



        else:



            print("\nSorry, there is no way to travel between "+stop1+" and "+stop2+" via the Lightning Rail.\n")



            break



    if route == 1:



        print("\nThese stops are on the "+line+".")



        print("The distance between "+stop1+" and "+stop2+" is "+str(distance)+" miles. The travel time is "+str(round(distance/30,2))+" hours.")



        print("Steerage Fare: "+str(round(distance*0.03, 2)))



        print("Standard Fare: "+str(round(distance*0.2,2)))



        print("First Class Fare: "+str(round(distance*0.5,2)))
"""
