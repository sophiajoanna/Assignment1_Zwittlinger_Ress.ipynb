
"""Assignment1_Zwittlinger_Ress.ipynb


"""



"""This is Assignment1 of Julia Zwittlinger and Sophia Ress

task 1
"""

last = ["Andrea,Barbara", "NotInList", "Bar"]
names = ["Thomas, Michael, Thomas, Andrea, Barbara, Susanne, Michael, Fabian, Hans", "Fabian"]
NotStartingWith = ["A"]
def process(names):
    mainlist = names + last + NotStartingWith
    slicedlist = slice(0,2)
    return mainlist[slicedlist]


process(names)

"""task 2 make a dictionary out of two lists: the names list and a second list, that provides the number of characters of each word"""

def toDict(names):
    return None

#first step create the character list 
names = ["Thomas", "Michael", "Thomas", "Andrea", "Barbara", "Susanne", "Michael", "Fabian", "Hans", "Fabian", "Barbara"]
characters =[]
for i in names:
    characters.append(len(i))
     
# second step requires to convert the two lists to a dictionary in python 
# todict() works if every key has the same value 
# we use zip as we use two lists 

nameDict = dict(zip(names, characters))

print(nameDict)

"""Task 3
 Create a class "Person" that has three attributes (instance variables): "name", "comment" and "id".
 The class shall have a constructor such that a Person-object can be created with "p = Person("aName", 4)", where "aName" is the name of the person and 4 is its id.
 Furthermore, invoking the statement print(p) should lead to the following output "aName (id = 4)".
 Finally, a person shall be renamable by invoking p.rename("newName")
"""

class Person:

  def __init__(self, name, comment, id):      
    self.name = name
    self.comment = comment
    self.id = id


  def printPers(self):
    print("Hi, my name is {} {}. I am {} years old.".format(self.name, self.comment, self.id))

  def rename(self, name):
    self.name = name

p = Person("AName", "AComment", 4)

p.rename("newName")
p.printPers()

"""task 4"""
mynames = ["Lisa", "John", "Paul", "Jim", "Babara"]
myindex = []

class myPerson():
  pass
  def __init__(self, id, name):      
    self.id = id
    self.name = name

def toObj(mynames):
    for list, item in enumerate(mynames):
        myindex.append(list)
        nameDict2 = dict(zip(mynames, myindex))

          #myPerson.id = id
    for idx, val in enumerate(nameDict2):
      myPerson.id = idx
      myPerson.name = val
      print("id: ", myPerson.id)



toObj( ["Lisa", "John", "Paul","Jim", "Babara"])





#   def toObjectList(nameDict2):
#
#   toObjectList(["Lisa", "John", "Paul"])

"""Task 5"""

import collections
list1 = ['Thomas', 'Michael', 'Thomas','Susanne','Michael','Thomas','Alfred','Alfred']
def getDuplicatesofList(list1):
  print(sorted([item for item, count in collections.Counter(list1).items() if count > 1]))

getDuplicatesofList(['Thomas', 'Michael', 'Thomas','Susanne','Michael','Thomas','Alfred','Alfred'])