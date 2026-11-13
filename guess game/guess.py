import random
rand=random.randint(1,50)
print("_________________{Welcome to guess game}_________________")
print("********************************************************")
try:
   
   
  ''' while choice <1 or choice>50 :
      choice=int(input("guess num between 1 & 50 :"))
  '''
  choice=0
  tries=0
  while choice!= rand:
       choice=int(input("guess num between 1 & 50 :"))
       if  choice <1 or choice>50 :
          print("Invalid number(Enter from 1 to 50).")
          continue
       if(choice<rand):
         tries +=1
         print("False!try a higher num!")
         
       elif(choice>rand):
        tries +=1
        print("False!try a lower num!")
        
       else: 
        print("Congrats!you got it right!")
 
except ValueError:
   print("Value Error")
   exit(1)
if tries<=5:
 print(f"Excellent! your no of tries is [{tries}] ")
elif tries>5  and tries<10:
  print(f"Good!your no of tries is [{tries}] ")
else :
  print(f'''Keep going! you can get it faster ,

 your no of tries is [{tries}] ''')
print(f"Your guess is [{choice}] & random num is [{rand}]")

print("********************************************************")
print("_____________________{ THANK YOU }______________________")
print("********************************************************")
