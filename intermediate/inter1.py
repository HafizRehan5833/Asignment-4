#. Create a function that takes a list of numbers and returns the largest number.

def user_list():
    li=[2,3,4,5,6]
    if not li:
        return None
    return max(li)

largest= user_list()          

    
print(largest)