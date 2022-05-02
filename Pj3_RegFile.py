#------------------------------------------------------------
#Project3: Resume parser and downloader (regex file handling)
#-------------------------------------------------------------
import re

out = open("Draft_Resume.txt","r")
print("Resume details: ") 
line = out.readlines()
line = str(line)

#print(line)
print("")
print("")


name = re.findall(r"[A-Za-z]*",line)
#print("Name: ",name)
    

emails = re.findall(r"[a-z0-9\.\-+_]+@[a-z0-9\.\-+_]+\.[a-z]+", line)
print("Email:",emails)

phone = re.findall(r'[\+\(]?[1-9][0-9 .\-\(\)]{8,}[0-9]', line)
print("Moble :",phone)

urls = re.findall('https?://(?:[-\w.]|(?:%[\da-fA-F]{2}))+', line)
count = len(urls)
for i in range(count):
 print(urls[i])



out.close()

