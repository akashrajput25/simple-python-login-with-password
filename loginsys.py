"""
Created on Fri Mar 20 21:44:25 2020

@author: AKASH RAJPUT
"""
import re
x=input("enter your first name\n")
while not(re.match(re.compile("(^[a-z|A-Z]{4,6})"),x)) :
    x=input("Name error!! enter your first name again\n")
g=input("enter your mid name\n")
while not(re.match(re.compile("(^[a-z|A-Z]{4,6})"),g)) :
    g=input("Name error!! enter your mid name again\n") 
h=input("enter your last name\n")
while not(re.match(re.compile("(^[a-z|A-Z]{4,6})"),h)) :
    h=input("Name error!! enter your last name again\n")
y=int(input("enter your age\n"))
if y>=15 and y<=60:
    print("you are eligible to register\n")
    z=input("enter your DOB\n")
    while not(re.match(re.compile("^([0-2][0-9]|(3)[0-1])(\/)(((0)[0-9])|((1)[0-2]))(\/)\d{4}$"),z)):
         z=input("ERROR!! Enter again your DOB \n")
    q=input("enter your gender: M-male | F-female\n")
    print("\n\n.............................Welcome to Akash Industries.............................\n")
else :
    print("sorry you are not eligible\nVisit when you will be 18 or above ,Thank you :)")
    exit()
def main():
   a=input("Enter password : one of the letter capital with numeric digits and !,@,#,$,%,&,..... signs to keep your credentials as secret and protected\n")                  
   mat = re.search(re.compile("^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,20}$"), a) 
   if mat: 
      print("cool choice of password....\n\n")
      pwdval(a)
   else: 
      print("Password type invalid !!") 
      while not(mat):
          f=input("Do you want to try again\n")
          if f=='y' or f=='Y':
             main()
             if mat:
                pwdval(a)
                exit()
          else:
             print("Goodbye and have a nice day...")
             break
def pwdval(a):
   pwd=a
   if q=="M" or q=="m":
      print("Welcome Mr.",x.capitalize(),"thanks for registering with us\n" )
   if q=="f" or q=="F":
      print("Welcome Mrs.",x.capitalize(),"thanks for registering with us\n" )
   b=input("Do you want to see your credentials Y/N\n")
   if b=='y' or b=='Y':
      print("wait.......")
      c=input("enter your password to see your details \n")
      print("\n\n")
      if c==pwd:
          print("Name :",x.capitalize()," ",g.capitalize()," ",h.capitalize(),"\n","Age :",y,"\n","DOB :",z,"\n","Gender :",q)
      else :
          print("thank you") 
          
   elif b=="n" or b=="N":
       print("Thanks for visiting\n")
       exit()  

main()
