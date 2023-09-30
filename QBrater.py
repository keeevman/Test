list1 = [
    "Jalen Hurts", "Patrick Mahomes", "Josh Allen", "Joe Burrow", "Lamar Jackson",
    "Justin Fields", "Trevor Lawrence", "Justin Herbert", "Dak Prescott", "Tua Tagovailoa",
    "Deshaun Watson", "Daniel Jones", "Geno Smith", "Anthony Richardson", "Kirk Cousins",
    "Aaron Rodgers", "Jared Goff", "Russell Wilson", "Derek Carr", "Matthew Stafford",
    "Brock Purdy", "Kenny Pickett", "Jordan Love", "Ryan Tannehill", "Sam Howell",
    "Baker Mayfield", "Kyler Murray", "Desmond Ridder", "Bryce Young", "Jimmy Garoppolo"
]

list2 = [
    "Patrick Mahomes", "Joe Burrow", "Josh Allen", "Justin Fields", "Trevor Lawrence",
    "Jalen Hurts", "Lamar Jackson", "Justin Herbert", "Aaron Rodgers", "Dak Prescott",
    "Russell Wilson", "Daniel Jones", "Kirk Cousins", "Tua Tagovailoa", "Anthony Richardson",
    "Deshaun Watson", "Geno Smith", "Jared Goff", "Derek Carr", "Matthew Stafford",
    "Kyler Murray", "Kenny Pickett", "Bryce Young", "Brock Purdy", "Mac Jones",
    "Jimmy Garoppolo", "Jordan Love", "Ryan Tannehill", "CJ Stroud", "Desmond Ridder",
    "Baker Mayfield", "Sam Howell"
]
list3 = [
    "Patrick Mahomes", "Josh Allen", "Jalen Hurts", "Lamar Jackson", "Joe Burrow",
    "Justin Fields", "Justin Herbert", "Trevor Lawrence", "Deshaun Watson", "Daniel Jones",
    "Dak Prescott", "Tua Tagovailoa", "Kirk Cousins", "Aaron Rodgers", "Geno Smith",
    "Russell Wilson", "Anthony Richardson", "Jared Goff", "Matthew Stafford", "Derek Carr",
    "Matthew Stafford", "Derek Carr", "Kenny Pickett", "Kyler Murray", "Jordan Love",
    "Bryce Young", "Ryan Tannehill"
]
list4 = [
    "Patrick Mahomes", "Josh Allen", "Jalen Hurts", "Lamar Jackson", "Justin Fields",
    "Joe Burrow", "Justin Herbert", "Trevor Lawrence", "Tua Tagovailoa", "Anthony Richardson",
    "Dak Prescott", "Kirk Cousins", "Daniel Jones", "Geno Smith", "Aaron Rodgers",
    "Jared Goff", "Russell Wilson", "Kyler Murray", "Matthew Stafford", "Brock Purdy",
    "Jordan Love", "Bryce Young", "Kenny Pickett", "Sam Howell", "CJ Stroud",
    "Ryan Tannehill", "Derek Carr", "Mac Jones", "Jimmy Garoppolo", "Desmond Ridder",
    "Trey Lance"
]
list5 = [
    "Patrick Mahomes", "Josh Allen", "Jalen Hurts", "Joe Burrow", "Geno Smith",
    "Trevor Lawrence", "Justin Fields", "Kirk Cousins", "Daniel Jones", "Jared Goff",
    "Justin Herbert", "Aaron Rodgers", "Lamar Jackson", "Tua Tagovailoa", "Russell Wilson",
    "Derek Carr", "Dak Prescott", "M. Mariota", "Kyler Murray"
]
list6 = [
    "Jalen Hurts", "Josh Allen", "Patrick Mahomes", "Lamar Jackson", "Joe Burrow",
    "Justin Fields", "Deshaun Watson", "Geno Smith", "Trevor Lawrence", "Justin Herbert",
    "Aaron Rodgers", "Daniel Jones", "Dak Prescott", "Jared Goff", "Kirk Cousins",
    "Russell Wilson", "Tua Tagovailoa", "Mac Jones", "Kenny Pickett", "Jordan Love",
    "Derek Carr", "Anthony Richardson", "Brock Purdy", "Jimmy Garoppolo", "Matthew Stafford",
    "Bryce Young", "CJ Stroud", "Desmond Ridder", "Ryan Tannehill", "Kyler Murray",
    "Baker Mayfield", "Sam Howell"
]


superlist = []
lists = [list1, list2, list3, list4, list5, list6]

for name in list1: 
    superlist.append(name)
for name in list2: 
    if name not in superlist: 
        superlist.append(name)
for name in list3: 
    if name not in superlist: 
        superlist.append(name)
for name in list4: 
    if name not in superlist: 
        superlist.append(name)
for name in list5: 
    if name not in superlist: 
        superlist.append(name)
for name in list6: 
    if name not in superlist: 
        superlist.append(name)


#Function that prints out each quarterback, along with their average ranking. 
def QBrater():
    QBnums = []                                             #poorly named, but very important and will be returned later in the function. 
    for name in superlist:                                  #looping over every name in superlist
        totalIndex = 0                                      #Will be compounded each iteration and will be the sum of each index in each list
        if name in list1:                                   #If their name appears in list1...
            totalIndex += (list1.index(name) + 1)           #totalIndex, now at 0, will be added to by their index within the list (+1 to account for 0th index)
        if name not in list1:                               #If they're not in the list, they're not good, thus +31 to ensure we know they're not good
            totalIndex += 31
        if name in list2: 
            totalIndex += (list2.index(name) + 1)           #totalIndex from the previous list + index from list2
        if name not in list2: 
            totalIndex += 31
        if name in list3: 
            totalIndex += (list3.index(name) + 1)           #totalIndex keeps getting added to by its index within each list (list3 here)
        if name not in list3: 
            totalIndex += 31
        if name in list4: 
            totalIndex += (list4.index(name) + 1)
        if name not in list4: 
            totalIndex += 31
        if name in list5: 
            totalIndex += (list5.index(name) + 1)
        if name not in list5: 
            totalIndex += 31
        if name in list6: 
            totalIndex += (list6.index(name) + 1)
        if name not in list6: 
            totalIndex += 31

        QBnums.append((name, round((totalIndex/len(lists)), 2)))            #each item in QBnums will be a tuple containing the name of the QB and their average index
        #print(name, round((totalIndex/len(lists)), 2)) 
    #print(QBnums)
    sorted_QBnums = sorted(QBnums, key=lambda x: x[1])                      #chatGPT did this weird stuff to sort QBnums so that it is sorted by better players at top. 

    for name, avgIndex in sorted_QBnums:
        print(name, avgIndex)
    
 
#QBrater()                                                                  #Calling this function prints each QB along with their avg index