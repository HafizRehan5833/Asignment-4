#Create a function to check if two strings are anagrams


def anagrams(str1,str2):

    str1=str1.replace("","").lower()
    str2=str2.replace("","").lower()

    if sorted(str1) == sorted(str2):
        return  f"{str1} and {str2} are anagrams.."
    else:
        return f"{str1} and {str2} are not anagrams.."
string_1=input("Enter first string: ")    
string_2=input("Enter first string: ")

result=anagrams(string_1,string_2)

print(result)
