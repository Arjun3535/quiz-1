print("Welcome to Compter Quiz!!")

play = input("Do you want to play?")


if play.lower()!= "yes":
    print("See you soon! Have a Great Day :)")
    quit()

print("Okay! Let's start to play")
score = 0

answer = input(" What does GPU stands for ?  ")
if answer.lower() ==  "graphics processing unit":
    print( "Hurray!! Correct Answer")
    score +=1
    
else:
    print("incorrect!")


answer = input(" What does CPU stands for ?  ")
if answer.lower() ==  "central processing unit":
    print( "Hurray!! Correct Answer")
    score +=1

else:
    print("incorrect!")


answer = input(" What does RAM stands for ?  ")
if answer.lower() ==  "random access memory":
    print( "Hurray!! Correct Answer")
    score +=1
else:
    print("incorrect!")

print(" You got " + str(score)+ "  Question Correct!") 
print("You got "+ str(score/3 *100) + "%")