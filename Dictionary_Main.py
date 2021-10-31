'''
This pgm contains the main pgm

'''
from File2 import Dictionary1

d1=Dictionary1()

while(True):
    option=int(input("\n Enter your choice...1. Searching word   2. Display entire dictionary    3. Searching word using alphabet   4. Exit:"))
    if(option==1):
        d1.search_dictionary()

    elif(option==2):
        d1.display_dictionary()

    elif(option==3):
        d1.display_dictionary_alphabet()

    else:
        break

