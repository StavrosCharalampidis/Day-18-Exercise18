# The first function is print the sum of two args with out using 2 args
def sumOfTwoNum1(*args):
    
    print("The first function")
    print(f'The sum is {args[0] + args[1]}\n')

# The second function is print the sum of two args using 2 args
def sumOfTwoNum2(num1, num2):
    print("The second function")
    print(f'The sum is {num1 + num2}\n')

# The third function is call with out args and only prints
def happyPrint():
    print("The third function") 
    print("Happy Hacking !!!")

# Call the function sumOfTwoNum1 and two values
sumOfTwoNum1(5, 15) 

# Call the function sumOfTwoNum2 and two values
sumOfTwoNum2(5, 5)  

# Call the function happyPrint with out values
happyPrint()