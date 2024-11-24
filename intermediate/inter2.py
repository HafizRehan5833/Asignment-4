#Write a function to find the nth Fibonacci number using recursion.
# sequence= 0,1,1,2,3,5,8.....


def Fibonacci(user_input):
    if user_input <= 0:
        return "You enter invalid number..."

    elif user_input == 1 :
        return 0
    
    elif user_input==2:
        return 1


    else:
        return Fibonacci(user_input-1)+Fibonacci(user_input-2)

n=int(input("Enter the number: "))        

          

function=Fibonacci(n)
print(function)
