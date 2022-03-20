#Task1:
#Get one string from user
#identify the middle character of the string"

name = input("Please enter the name: ");
Please enter the name: Jyoti
count = len(name)
middle = count//2
print(name[middle])

o/p  = o	
====================================================


#Task1:string1 = ""***python***""
#string2 = "**python********"
#string  = "********java*******"

string1 = "***python***"
string2 = "**python********"
string  = "********java*******"

print(string1.strip("*"))
python
print(string2.lstrip("*"))
python********
print(string.rstrip("*"))
********java	


o/p - python
      python********
      ********java
=====================================================

#Task3: (name<space>float)
#collect three strings from user  name<space>float


name1 = input("Enter Employee name1 & Temp : ")
Enter name and value: Jyoti 10.00
name2 = input("Employee name2 & Temp : ")
Enter your name : Neela 23.00
name3  = input("Employee name3 & Temp: ")
Enter your name : Padma 90.45
val1 = name1.split(" ")
name1 = name1.split()
name2 = name2.split()
name3 = name3.split()
print(float(name1[1])+float(name2[1])+float(name3[1]))

o/p- 123.45
=====================================================

#Task4:
#collect two strings from user
string1: python
String2: java
output ===> jythonpava64hv"


s1 = input("Enter 1st string : ")
Enter 1st string : python
s2 = input("Enter 2nd string : ")
Enter 2nd string : java
c1 = len(s1)
c2 = len(s2)
mid1 = c1//2 
mid2 = c2//2
result = s2[0]+s1[1:]+s1[0]+s2[1:]+str(c1)+str(c2)+s1[mid1]+s2[mid2]
print(result)

jythonpava64hv

=====================================================

#string1: maths
#string2: science
#output ===> sathsmcience57te	


a = input("Pls enter 1st subject name: ")
Pls enter 1st subject name: maths
b = input("Pls enter 2st subject name: ")
Pls enter 2st subject name: science
c1 = len(a)
c2 = len(b)
mid1 = c1//2
mid2 = c2//2
result = b[0]+a[1:]+a[0]+b[1:]+str(c1)+str(c2)+a[mid1]+b[mid2]
print(result)

o/p - sathsmcience57te   
==============================================================


#Task5:
#Collect two strings from user
#string1: wikipedia
#string2: typescript
#output: p  +  c   ===> ascii value of p + ascii value of c  ====>  198
#(ord , chr)


string1 = input("Plz enter the 1st word: ")
Plz enter the 1st word: class
string2 = input("Plz enter the 2nd word: ")
Plz enter the 2nd word: completed
c1 = len(string1)
c2 = len(string2)
mid1 = c1//2
mid2 = c2//2
a = string1[mid1]
b = string2[mid2]
total = ord(a) + ord( b)
result = ""Ascii value of "" + a + "" - "" + str(ord(a)) + "" + "" + ""Ascii value of "" + b + "" - "" + str(ord(b))+ "" = "" + str(total)
print(result)

o/p --  Ascii value of a - 97 + Ascii value of l - 108 = 205

============================================================================================	
#Task6:
#collect one string from user:
#string: computer
#output: c6r	

e = input("Enter the one word: ")
Enter the one word: programming
c = len(e)
first_str = e[0]
last_str = e[c-1]
print(first_str+str(c)+last_str)

o/p -  p11g
=========================================================
Task7
Say hello world with python

print("Hello, World!")

o/p - Hello, World!
=========================================================
Task 8
swapcase

note = "Hello, My name is Jyoti "
sc = note.swapcase()
print(sc)

o/p - hELLO, mY NAME IS jYOTI

=========================================================
Task9
what;s your name

first_name = input()
The Kashamir
second_name = input()
files
print(f" {first_name} {second_name} ! Latest movie in march 2022")

o/p - The Kashamir files ! Latest movie in march 2022
=========================================================
#Task10:
#Mutation

string = input()
asdfghjl
string  = string[:3]+"G"+string[4:]
print(string)


o/p - asdGghjl

=========================================================
#Task11:
#Arithmetic operator

a = input() #3
3
b = input() #2
2

print(a+b)
print(a-b)
print(a*b)

o/p = 5
      1
      6
=========================================================
Task12:
python divison

a = input()
123
b = input()
12

c = a//b
print("int div = " + c)
10
print("Float div = " + c)
10.25



o/p - 10
      10.25
     


==========================================================


