#6. Write a function to count the vowels in a given string.

def vowels(s):
    vowels_alpha=["a","e","i","o","u","A","E","I","O","U"]
    count=0
    for char in s:
        if char in vowels_alpha:
            count+=1




    return count
user_input=input("Enter the string:  ")
print(f"Numbers of vowels in",user_input,"is : ",vowels(user_input))       
