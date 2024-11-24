#basic function
#4. Write a function that takes a string and returns it reversed


def string(str):
    user_input=input("Enter the string: ")
    str=user_input
    reverse=str[::-1]
    return reverse
func=string(str)

print(func)