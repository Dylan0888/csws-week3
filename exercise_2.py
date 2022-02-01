
numbers = list(i for i in range(0,100,5))

print("The Multiples of 5 are")
for i in range(0,len(numbers)):
    print(numbers[i])



# FizzBuzz task


userNumberStr = input("-----( Fizz Buzz )-----\n Pick a Number to Play Fizz Buzz!")
userNumber = int(userNumberStr)

for i in range(1,userNumber):
    if(i%10 == 0 and i%5 == 0):
        print("Fizz Buzz")
    elif(i%10 == 0):
        print("Buzz")
    elif(i%5 == 0):
        print("Fizz")
    else:
        print(i)
