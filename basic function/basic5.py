#Create a function to check if a given number is prime.

def is_prime(n):

    if n<=1:
        return "Invalid"

    else: 
        for num in range(2,int(n**0.5)+1):
            if n%num==0:
                return "\t\tYour number is not prime..."
        return "\t\tYour number is prime..."


num_1=int(input("Enter the number: "))

result=is_prime(num_1)
print(result)