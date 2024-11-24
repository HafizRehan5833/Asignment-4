#Create a function that takes a list of integers and returns the sum of all even numbers

def sum_of_even(numbers):
    even = 0
    odd=0
    user_input=input("Enter even or odd: ").lower()

    if user_input == "even":


        for num in numbers:
            if num%2==0:
                even+=num
        return even
    else:
        for x in numbers:
           if x%2 != 0:
                odd+=x    
        return odd  

user_list=[1,2,3,4,5,6,7,8,9,10]
print("The list is :",user_list)
result=sum_of_even(user_list)

print("The sum of even number is :",result)