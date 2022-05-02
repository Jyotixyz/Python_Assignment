
#-----------------------------------
#------------Project2----------------
#-----------------------------------








import smtplib
import os
import pywhatkit
import datetime

Correct = 0
Wrong = 0
y = 0

hour = datetime.datetime.now().hour
minute = datetime.datetime.now().minute

total_dict = {"Question 1":{"Question":"Addition of two numbers(10+20)","Option1": "10","Option2": "20","Option3": "30","Correct answer": "30"},
              
              "Question 2":{"Question":"Addition of two numbers(100+20)","Option1": "10","Option2": "20","Option3": "120","Correct answer": "120"},
              
              "Question 3":{"Question":"Addition of two numbers(20+20)","Option1": "10","Option2": "20","Option3": "40","Correct answer": "40"},
              
              "Question 4":{"Question":"Addition of two numbers(90+20)","Option1": "110","Option2": "20","Option3": "30","Correct answer": "110"},
              
              "Question 5":{"Question":"Substraction of two numbers(100-20)","Option1": "10","Option2": "80","Option3": "120","Correct answer": "80"},
              
              "Question 6":{"Question":"Substraction of two numbers(100-100)","Option1": "0","Option2": "20","Option3": "120","Correct answer": "0"},
              
              "Question 7":{"Question":"Substraction of two numbers(19-20)","Option1": "10","Option2": "-1","Option3": "120","Correct answer": "-1"},
              
              "Question 8":{"Question":"Substraction of two numbers(80-78)","Option1": "10","Option2": "78","Option3": "120","Correct answer": "78"},
              
              "Question 9":{"Question":"Substraction of two numbers(500-150)","Option1": "350","Option2": "20","Option3": "120","Correct answer": "350"},
              
              "Question 10":{"Question":"Div of two numbers(100%10)","Option1": "10","Option2": "20","Option3": "30","Correct answer": "20"},
              
              "Question 11":{"Question":"Div of two numbers(200%20)","Option1": "Set","Option2": "List","Option3": "Dictionary","Correct answer": "List"},
              
              "Question 12":{"Question":"Div of two numbers(500%50)","Option1": "10","Option2": "20","Option3": "30","Correct answer": "20"},
              
              "Question 13":{"Question":"Div of two numbers(0-0)","Option1": "0","Option2": "1","Option3": "2","Correct answer": "0"},
              
              "Question 14":{"Question":"Mul of two numbers(11*11)","Option1": "11","Option2": "1","Option3": "111","Correct answer": "111"},
              
              "Question 15":{"Question":"Mul of two numbers(90*9)","Option1": "90","Option2": "67","Option3": "00","Correct answer": "90"}}

#Personal info
name = input("Enter the name here: ")
print("welcome quiz")
num = int(input("Number of questions do you want to play ? "))
count = len(total_dict)
print(" ")

for i in total_dict:

   if(y<num): 
        print(i,".",total_dict[i]["Question"])
        print("Options1 : ",total_dict[i]["Option1"])
        print("Options2 : ",total_dict[i]["Option2"])
        print("Options3 : ",total_dict[i]["Option3"])
        print(" ")
        answer = input("please enter anyone option: Options1/Options2/Options3: ")
        
        if answer == total_dict[i]["Correct answer"]:
            print("Answer is correct for Question")
            Correct = Correct+1
            print(" ")
        
        else:
            print("wrong answer")
            Wrong = Wrong+1
            print(" ")
            
        y = y+1
   else:
      break

   
#Score calculation
print(" ")
print("Score Details :")
AvgScore = (Correct/num)*100
strPer = "3.Total Score in % : {}".format(AvgScore)
strC = "1.Number of correct answer is {}".format(Correct)
strW = "2.Number of wrong answer is {}".format(Wrong)
print(" ")

strname = "Player name is:"
strname = strname+name
mail_msg = strname+os.linesep+strC+os.linesep+strW+os.linesep+strPer
print(mail_msg)
print(" ")


#Send msg in watsapp number
minute =  minute+2
pywhatkit.sendwhatmsg('+911234567891',mail_msg,hour,minute) # 10dig phone numbes

#Send mail code
Pwd = input("Please enter your gmail password : ")
s = smtplib.SMTP('smtp.gmail.com',587)
s.starttls()
s.login('abcd123@gmail.com',pwd)
s.sendmail('abcd123@gmail','abcd123@gmail.com',mail_msg) # (enter sender & receiver mail id or same id in both side
print("Mail Sent")
s.quit()






































    
