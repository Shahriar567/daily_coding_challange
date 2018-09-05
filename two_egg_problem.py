# A building has 100 floors. One of the floors is the highest floor an egg can be
# dropped from without breaking.
# If an egg is dropped from above that floor, it will break. If it is dropped
# from that floor or below, it will be completely undamaged and you can drop
# the egg again.
#
# Given two eggs, find the highest floor an egg can be dropped
# from without breaking, with as few drops as possible.

import math

def twoEgg(lis, x=80):
    lisLen = len(lis)
    lisLen1 = int(math.floor(0.3 * lisLen))
    lisLen2 = int(math.ceil(0.7 * lisLen))
    found1 = False
    found2 = False
    # print(lis[:lisLen1])
    # print(lis[lisLen2:])
    # print(lis[lisLen1:lisLen2])

    while (found1==False and found2==False):
        print("Is this happening")
        if lisLen1 < x and lisLen2 > x and (lisLen2-lisLen1 == 1) :
            found1 = True
            found2 = True
            return lisLen1, lisLen2
        if (lisLen1 > x):
            twoEgg(lis[:lisLen1])
        elif (lisLen2 < x):
            twoEgg(lis[lisLen2:])
        else:
            twoEgg(lis[lisLen1:lisLen2])




lis = [x for x in range(0,100)]
print(twoEgg(lis))




String commaSeparated = "item1 , item2 , item3";
ArrayList<String> items =
new  ArrayList<String>(Arrays.asList(commaSeparated.split(",")));
