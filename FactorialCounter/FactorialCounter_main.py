# Define a function named factorial
def factorial():
    number = input("Enter a number for calculating Factorial: ") # Get input as integer from user
    if number == "0" or "." in number or "/" in number or "-" in number:
        print("Error! Enter an natural number ")
        exit()
    else:
        number = int(number)
        i = 1 # This variable is used for futur use in loop
        n = 1 # This variable is used for futur use in loop
        while i <= number:
            n = n * i
            i += 1
    print("Factorial of number " + str(number) + " is " + str(n))


factorial() # calling function


