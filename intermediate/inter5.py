#Write a function to calculate the GCD (Greatest Common Divisor) of two numbers.

def GCD(num_1,num_2):
    while num_2!=0:
        num_1,num_2=num_2,num_1%num_2
    return num_1

number1=int(input("Enter first number:"))
number2=int(input("Enter second number: "))


result=GCD(number1,number2)

print(result)