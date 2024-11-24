#Write a function to find the factorial of a number 

def fac(n):
    if n<0:
        print("number is less than zero..")
    if n == 0 or n == 1:
        return 1
    return n*fac(n-1)
num=int(input("Enter the number which you want factorial: "))


print("The factorial of the number",num,"is: ",fac(num))
          