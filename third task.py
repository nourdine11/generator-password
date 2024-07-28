import string
import random

lowercase=list(string.ascii_lowercase)
uppercase=list(string.ascii_uppercase)
ponctuation=list(string.punctuation)
digits=list(string.digits)

char_num=input("Please enter number of character in your password : ")

while True :
    try:
        char_num=int(char_num)
        if char_num < 6 :
            print("You need at least 6 character .")
            char_num=input("Enter number of character again : ")
        else :
            break
    except:
        print("Please enter number only !")
        char_num=input("Please enter number of character in your password :")
random.shuffle(lowercase)
random.shuffle(uppercase)
random.shuffle(ponctuation)
random.shuffle(digits)

part1=round(char_num* 30//100)
part2=round(char_num*20//100)
remaining=char_num-(2*part1 + 2*part2)
password=[]

for i in range(part1):
    password.append(lowercase[i])
    password.append(uppercase[i])

for i in range(part2):
    password.append(ponctuation[i])
    password.append(digits[i])
if remaining>0:

    for i in range(remaining):
        password.append(random.choice(lowercase+ uppercase + ponctuation + digits))
random.shuffle(password)
final_password = ''.join(password)

print("Generated password:", final_password)


