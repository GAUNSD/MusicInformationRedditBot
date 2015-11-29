    # Program to read and find the data base of the artists

    import math

    print "Search West Coast Rappers text file"
    print

    filename = "WestCoastHipHop.txt"
    inFile = open (filename,"r")
    line = inFile.readline().rstrip("\n")

    keyword = "N.W.A"
    cLetter = ord(keyword[0])-64

    print cLetter, "c Letter"
    infoMatrix = [0 for x in range(27)]

    i = 0
    found = False
    # 2d Array, elements with each
    while line != "":
        #Get the category 
        category = line.split(":")
        line = inFile.readline().rstrip("\n")

        info = category[1].split(" #")

        
        info[0] = category[0]
        #print i
        #print info

        if (cLetter == i):
            print "test", i
            #Go through the array info and look for the element
            for j in range(0, len(info)):
                elem = info[j]
                print elem
                if (elem == keyword):
                    found = True
        
        i = i + 1

    print found





















        
