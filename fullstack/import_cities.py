""" This populates City table with cities. 
"""

import csv
#from smartcity.models import MyCity

with open('data/worldcities.csv', encoding='utf8') as f:  #imports file containing city tables called worldcities.csv
    res = csv.reader(f)                                   #specifies format and reads in the worldcities.csv file
    count = 0
    res = list(res)                                       #processes instruction
    c = 0
    while c < 10:
        print(res[c])                                     #prints the result 'name' of cities read from the city table
        c +=1


    #ends import and polution of city table
 
