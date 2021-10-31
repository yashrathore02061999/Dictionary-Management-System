'''
create your own dictionary
'''
'''
trim() function removes spaces at the start and end of string value.

Explanation from line 18 to line 44:
We have defined 2 instance data members for class Dictionary1 i.e. dict1 and n. n variable is storing the number of words we want in the dictionary.
The dict1 is a dictionary variable and is storing key value pairs where the keys are the words and the values are nested lists where the 1st element of
the nested list is the meaning of the word, 2nd element is the type of word i.e. noun etc. 3rd element of nested list is another nested list stored in variable list1
which contains the words which are similar to that word.

self.dict1.update({key:[value1,value2,list1]}) stores the key value pair in the dictionary.


Line 47-67:
This will accept word to be searched form user and if word is present then it displays all details of that word i.e. meaning,type and words similar.

Line 76-90:
Displays all the words and their meaning,type and words similar one by one which are all stored in dictionary.

Line 94-111:
Accepts an alphabet from user and displays all words in the dictionary which begin from the alphabet along with their meaning etc.
'''


class Dictionary1:
    def __init__(self):
        self.dict1 = {}
        list1 = []
        cnt = 1
        self.n = int(input("\n Enter how many words to store in dictionary:"))
        n1=0
        cnt1=1


        for i in range(self.n):
            print("\n Enter the word no."+str(cnt))
            key=input()
            print("\n Enter meaning of word "+str(key))
            value1=input()
            print("\n Enter what is the type of the word "+str(key)+". Is it a noun or adjective or verb or adverb etc?")
            value2=input()
            n1=int(input("\n Enter how many words are similar to the word "+str(key)))
            for j in range(0,n1):
                word1=input("\n Enter the word no."+str(cnt1)+" which is similar to"+str(key))
                list1.append(word1)
                cnt1+=1

            self.dict1.update({key:[value1,value2,list1]})

            list1=[]
            cnt1=1
            cnt+=1

    def search_dictionary(self):
        word1=input("\n Enter the word to be searched:")
        word1=word1.lower()
        word1=word1.strip()
        value1=self.dict1[word1]
        cnt=1
        if(value1!=None):
            print("\n The description of the entire word is ")


        for item1 in value1:
            if(cnt==1):
                print("\n The meaning of the word is ",item1)

            elif(cnt==2):
                print("\n The type of the word is ", item1)

            else:
                print("\n The words similar to the word is",item1)

            cnt+=1



    def display_dictionary(self):
        for (key,value) in self.dict1.items():
          print("\n Word:",key)
          cnt=1
          for item1 in value:
              if(cnt==1):
                print("Word Meaning:",item1)

              elif(cnt==2):
                  print("Word type:",item1)

              else:
                  print("List of word similar to that word are ",item1)

              cnt+=1

    def display_dictionary_alphabet(self):
        char1=input("\n Enter the alphabet starting from which you want to display words in dictionary:")

        for (key, value) in self.dict1.items():
            if(key[0]==char1):
                print("\n Word:", key)
                cnt = 1
                for item1 in value:
                  if (cnt == 1):
                    print("Word Meaning:", item1)

                  elif (cnt == 2):
                    print("Word type:", item1)

                  else:
                    print("List of word similar to that word are ", item1)

                  cnt += 1


