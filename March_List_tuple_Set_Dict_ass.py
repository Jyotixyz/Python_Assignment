===================================================================
************** List ***********************************************
===================================================================

#Create an empty list (two ways)
#Concatenate with [5,6,7,8]
#add 8,9,1,5,6,7,8,1 elements to that list
#Find frequency of 8 (count)
#find the mean of the list
#find sum (List) + min + Max 
#Find median of the list
#remove duplicates from list and give output in the format of tuple"
-------------------------------------------------------------------

#Create an empty list (two ways)
empty_ls = []

#Concatenate with [5,6,7,8]
ls = [5,6,7,8]
print(ls)
[5, 6, 7, 8]

#add 8,9,1,5,6,7,8,1 elements to that list
ls.append(8)
ls.append(9)
ls.append(1)
ls.append(5)
ls.append(6)
ls.append(7)
ls.append(8)
ls.append(1)
print(ls)
[5, 6, 7, 8, 8, 9, 1, 5, 6, 7, 8, 1]

#Find frequency of 8 (count)
print(ls.count(8))
3

#find the mean of the list
print(list(set(ls)))
[1, 5, 6, 7, 8, 9]

average = sum(ls)/len(ls)
print(average)
5.916666666666667

#find sum (List) + min + Max 
print(sum(ls))
71
print(min(ls))
1
print(max(ls))
9
print(list(set(ls)))
[1, 5, 6, 7, 8, 9]

#Find median of the list
medain = len(ls)//2
res = (ls[medain]+ls[~medain])/2
print(res)
6.5

#remove duplicates from list and give output in the format of tuple"
tup = tuple(ls)
print(tup)
(1, 1, 5, 5, 6, 6, 7, 7, 8, 8, 8, 9)
print(type(tup))
<class 'tuple'>
=====================================================================

**************** Tuple **********************************************


#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
#Concatenate both tuples and remove duplicates from tuple
#Find the index value of 9 (after concatenation)
#multiply above elements 3 times

---------------------------------------------------------------------
#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
t1 = (1,4,5,6,7,8)
t2 = (5,6,7,8,9)

#Create two tuples (1,4,5,6,7,8) (5,6,7,8,9)
tp_set = set(t1)
tp_set = set(t2)
tp_set1 = set(t1)
tp_set2 = set(t2)
com_ele = (tp_set1 & tp_set2)
print(com_ele)
{8, 5, 6, 7}

#Concatenate both tuples 
print(t1+t2)
(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)

#and remove duplicates from tuple
Non_dup_tup = set(t1+t2)
print(Non_dup_tup)
{1, 4, 5, 6, 7, 8, 9}

#Find the index value of 9 (after concatenation)
print(t1+t2)
(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)
tup = (t1+t2)
print(tup)
(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)
print(tup.index(9))
10

#multiply above elements 3 times"
print(tup*3)
(1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9, 1, 4, 5, 6, 7, 8, 5, 6, 7, 8, 9)
======================================================================================================
*********** Sets ***********
======================================================================================================

#Create two empty sets
#update set1 with 7,8,9,1,2,3,4,5,0
#update set2 with 4,5,6,0
#check whether set2 is subset of set1 or no ?
#check whether both have common elements are no ?
#remove 8 from set 1 and set 2 ==> find the inferences
#discard 0 from set1 and set2 
#find collection of both sets ===> set1 and set2"


#Create two empty sets
set1 = set()
print(type(set1))
<class 'set'>

set2 = set()
print(type(set2))
<class 'set'>

#update set1 with 7,8,9,1,2,3,4,5,0
set1 = { 7,8,9,1,2,3,4,5,0}
set1.update(set1)
print(set1)
{0, 1, 2, 3, 4, 5, 7, 8, 9}

#update set2 with 4,5,6,0
set2 = {4,5,6,0}
set2.update(set2)
print(set2)
{0, 4, 5, 6}

#check whether set2 is subset of set1 or no ?
print(set1.issubset(set2))
False
print(set1.isdisjoint(set2))
False

#remove 8 from set 1 and set 2 ==> find the inferences
set1.remove(8)
print(set1)
{0, 1, 2, 3, 4, 5, 7, 9}


set2.remove(8)
Traceback (most recent call last):
  File ""<pyshell#19>"", line 1, in <module>
    set2.remove(8)
KeyError: 8

#discard 0 from set1 and set2 
set1.discard(0)
print(set1)
{1, 2, 3, 4, 5, 7, 9}
set2.discard(0)
print(set2)
{4, 5, 6}

#find collection of both sets ===> set1 and set2"
set1.update(set2)
print(set1)
{1, 2, 3, 4, 5, 6, 7, 9}

#find collection of both sets ===> set1 and set2"
set1 = { 7,8,9,1,2,3,4,5,0}
print(set1)
{0, 1, 2, 3, 4, 5, 7, 8, 9}
set2 = {0, 4, 5, 6}
print(set2)
{0, 4, 5, 6}
set1.update(set2)
print(set1)
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9}

#check whether both have common elements are no ?
set1 = { 7,8,9,1,2,3,4,5,0}
set2 = {0, 4, 5, 6}
print(set1.isdisjoint(set2))
False
============================================================================
********* dictionary  *****************

#create a dictionary
#{1:[""english"",""maths"",""science""], 2:[10,20,30], 3:[""bio-botany"",""bio-zoology"",""Algebra""]}
#Extract ""bobtn"" from above dictionary
#Extract ""arbeg"" from above dictionary
#print all keys in dictionary and convert it into tuple
#Find the average of all numbers available under key ""2"""

---------------------------------------------------------------------------
#create a dictionary
#{1:[""english"",""maths"",""science""], 2:[10,20,30], 3:[""bio-botany"",""bio-zoology"",""Algebra""]}
dict = {1:[""english"",""maths"",""science""], 2:[10,20,30], 3:[""bio-botany"",""bio-zoology"",""Algebra""]}
print(dict)
{1: ['english', 'maths', 'science'], 2: [10, 20, 30], 3: ['bio-botany', 'bio-zoology', 'Algebra']}

#Extract ""bobtn"" from above dictionary
print(dict[""bobtn""])
Traceback (most recent call last):
  File ""<pyshell#2>"", line 1, in <module>
    print(dict[""bobtn""])
KeyError: 'bobtn'

#Extract ""arbeg"" from above dictionary
print(dict[""arbeg""])
Traceback (most recent call last):
  File ""<pyshell#3>"", line 1, in <module>
    print(dict[""arbeg""])
KeyError: 'arbeg'

#print all keys in dictionary and convert it into tuple
print(dict.keys())
dict_keys([1, 2, 3])
tup = tuple(dict.items())
print(type(tup))
<class 'tuple'>

#Find the average of all numbers available under key ""2"""
values = dict[2]
print(values)
[10, 20, 30]
avg = (sum(values)/len(values))
print(avg)
20.0"

================================================================================





















