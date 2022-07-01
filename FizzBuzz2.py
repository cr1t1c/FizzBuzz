#Creates a for loop to print the numbers 1-100
for i in range(1,101):
#Tells the program if the number is divisible by 5 and 3 print fizzbuzz
    if (i %3 == 0 and i%5 == 0):
        print("FizzBuzz")
#Tells the program if number is divisible by 3 print Fizz
    elif (i %3 == 0):
        print("Fizz")
#Tells the progam if number is divisible by 5 print Buzz
    elif (i %5 == 0):
        print("Buzz")
#Prints the for loop
    print(i)