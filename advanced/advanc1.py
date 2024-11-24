#Write a function that calculates the power of a number without using the ** operator


def without_using_operator(number,power):
    if power <= 1:
        number=1/number
        power=-power


    total_num=1
    for a in range(power):
        total_num*= number
    return total_num

number1=int(input("Enter first number:"))
number2=int(input("\tEnter second number: "))


result=without_using_operator(number1,number2)

print("\t\tThe giving numbers:- \n \t\t\tBAse is -->",number1,"\n\t\t\t\tPower is-->",number2)
print("\t\t\t\t\tThe result of your giving numbers--->",result)
