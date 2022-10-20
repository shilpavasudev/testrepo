#TASK THREE DATA STRUCTURES

#1
#list1=[1,3,'elena',1+2j, 4,2,'damon','stefen',22.2,3.4]
#print(list1)

#2
#list2 = [2,3,4,2,4]
#print(list2[1:4:2])

#3
#from operator import mul


#list3 = [1,4,2,3,2,4]
#print(sum(list3))
#print(mul(list3))

#4

#list4 = [5,4,2,3,2,4]
#print(min(list4))
#print(max(list4))

#5

#list5 = [5,4,2,3,2,4,2,7,1,4,2,8,9]
#for num in list5:
#        if num % 2 != 0:
#            print(num,  end =' ')

#6
#list6= list()
#for i in range(1,30):
#		list6.append(i**2)
#print(list6[:5])
#print(list6[-5:])

#7
#list7 = [1,3,5,9,10]
#list8=[2,4,6,8]
#list7[-1:] = list8 ; #or it can be list7[4:] = list8 
#print (list7)

#8
#from operator import concat

#a = {1:10,2:20}
#b = {3:30,4:40}
#c= a.copy()
#c.update(b)
#print(c)

#9
#n=int(input("enter a number "))
#a = dict()
#for x in range(1,n+1):
#    a[x]=x*x
#print(a) 

#10
#a = input('enter some comma seperated numbers')
#list1 = a.split(",")
#tuple1 = tuple(list)
#print('lists are : ',list1)
#print('tuples are : ',tuple1)

#TASK FOUR TRADITIONAL FUNCTIONS,ANONYMOUS FUNCTIONS & HIGHER ORDER FUNCTIONS

#1
#str1 = "1234abcd"
#str2 = str1[::-1]
#print(str2)

#2
#from curses.ascii import isupper

#def function1(str1): 
#    up1 =0
#    low1= 0
#    for i in str1:
#        if i.isupper() :
#            up1 = up1+1
#        elif i.islower():
#            low1 = low1 +1
#    print("upper letters = : ",up1)
#    print("lower letters = :",low1)
#str1 = input("enter a string:  ")
#s1= function1(str1)

#3
#def function2(list1):
#    newlist = []
#    for i in list1:
#        if i not in newlist:
#            newlist.append(i)
#    print(newlist)

#s1= function2([1,2,2,2,3,4,5,5,6,6])

from functools import reduce
import operator

lists = [[1, 2, 3], [4, 5], [6, 7, 8]]
joinedlist = reduce(operator.add,lists)
 
print(joinedlist)  # prints [1, 2, 3, 4, 5, 6, 7, 8]













