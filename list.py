#Print the type of a variable and iterate the next letter in a string entered by an user.
s= iter(input("Enter a string:\n>>"))
print(type(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))
print(next(s))

#Remove an item from a list, then insert another item on index [2], and finally sort the list alphabetically
list1 = ["Arrow", "Jewdish", "Balloon", "Zero", "Dynamic", "Fruits"]
list1.remove("Balloon")
list1.append("Jelly")
list1.insert(2,"Ergonomics")
list1.sort()
list1[0:5]
print(list1)


#Print true if all the items in a list is positive or 1
a_list = [1,2,23]
print(all(a_list))

#Ascii to it's corresponding alphabet starting from "a" and skip every other alphabet.
list_of_alphabets = []
for i in range (97,123,2):
    list_of_alphabets.append(chr(i))
print(list_of_alphabets)


'''The included code stub will read an integer "n" from STDIN.
Without using any string methods, try to print the following: "123....n"
Note that "...." represents the consecutive values in between.'''
def values(n):
    for i in range (1,n):
        print(i,end="") 
n = int(input())
values(n)

'''Given a year, determine whether it is a leap year. If it is a leap year, return the Boolean True, otherwise return False.'''
def is_leap(year):
    leap = False
    if (year%4 ==0 and year%100!=0) or year%400==0:
        return True
    return leap

year = int(input("Enter a year:\n>> "))
print(is_leap(year))


#The provided code stub reads and integer "n" from STDIN. For all non-negative integers "i<n", print i^2.
n = int(input("Enter a number:\n>> "))
for i in range (0,n):
    print (i**2)

