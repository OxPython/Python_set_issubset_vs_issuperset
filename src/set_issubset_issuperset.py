'''
Created on Jul 7, 2014

@author: viejoemer

What is the difference between issubset and issuperset in Python?

¿Cuál es la diferencia entre issubset e issuperset en Python?

Really, there are not so different,, each one evaluate the
same in opposite directions.
'''

#Create a set with values.
s = {0,1,2,3,4,5,6,7,8,9}
print(s)

s2 = {1,2}
print(s2)

#Verify if each item from one set is in other.
#All items from s2 are in s
r = s2.issubset(s)
print(r)


#Verify if the items from a other set is in the original set.
#Some items or all from s are in s2.
r = s.issuperset(s2)
print(r)

#This operation are the same but his evaluations are opposite.