import random
n=random.randint(1,100)
a=0
guesses=0

while(a!=n):
    guesses+=1
    a=int(input("enter your number: "))
    if(a>n):
        print("lower please")
    else:
        print("higher please")

print(f"you have guessed th number correctly in {guesses} guesses")


    

