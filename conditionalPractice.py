'''
Created on Feb 14, 2020

@author: ITAUser
'''
x = 0
if(x == 1):
    print("Something")
#skips printing because x doesn't equal 1

x = 0
if(x == 0):
    print("Something")
#will print because x does equal 0

if(x == 0):
    print("some")
elif(x == 1):
    print("thing")
#this time only one or the other is going to print

else:
    print("N/A")
#if number falls under neither category, it will print "N/A"


