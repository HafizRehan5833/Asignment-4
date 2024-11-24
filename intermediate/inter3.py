#3. Write a function to check whether a string is a palindrome.

def palindrome(_input):
   
    return _input[ ::-1]

user_input=input("Enter the string: ")
result=palindrome(user_input)
print(result)    
