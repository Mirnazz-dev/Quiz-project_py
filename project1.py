print("________________ [WELCOME TO QUIZ GAME] _________________")
print("*********************************************************")
print("_______________ < Personal information > _______________")
try:
    q1=input("Enter your name:")

    q2=int(input("Enter your age:"))
except ValueError:
      print("ValueError *_*")
      exit()
print(f"Hello {q1}, nice to meet you!")
print("How awesome that you are",q2)
print("*********************************************************")
print("_Let's start our quiz_")
score= 0
print("****{ MATH }*****")
ans=['A','B','C']
Q1=input("""What is 12*3 ?
A.36
B.32
C.30
Your Ans:""").upper()



if Q1==ans[0]:
    print(" Right answer ^_^")
    score+=1
    print("Score:",score)
elif Q1 not in ans:
    print("Invalid choice")

else:
    print("Wrong answer") 
print("*********************************************************")
print("****{ Space }*****")
Q2=input(""" Which planet is known as red planet?
A.Jupiter
B.Mars
C.Earth
Your Ans:""") .upper() 

if Q2==ans[1]:
    print("Right answer ^_^")
    score+=1
    print(" Score:",score)
elif Q2 not in ans:
    print("Invalid choice")

else:
    print("Wrong answer")
print("*********************************************************")
print("****{ Animals }*****")
Q3=input(""" Which is the largest the largest mammal in the world?
A.Elephant
B.Blue whale
C.Giraffe
Your Ans:""") .upper() 

if Q3==ans[1]:
    print("Right answer ^_^")
    score+=1
    print("Score:",score)
elif Q3 not in ans:
    print("Invalid choice")

else:
    print("Wrong answer")
print("*********************************************************")
print("****{ Science }*****")
Q4=input(""" What do plants need to make their own food?
A.Chocolate
B.Toys
C.Sunlight

Your Ans:""") .upper() 

if Q4==ans[2]:
    print("Right answer ^_^")
    score+=1
    print("Score:",score)
elif Q4 not in ans:
    print("Invalid choice")

else:
    print("Wrong answer")
print("*********************************************************")
print(f"[FINAL SCORE:{score}]")
print(f"____________[ Thank you for your answers {q1} ]____________")




