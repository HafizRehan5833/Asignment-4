#Write a function that takes a list and removes all duplicate elements.

def delete_num(list_1):
    return  list(set(list_1))

list_1=[1,2,3,4,2,1,4,5,6]
print("Your list is -->",list_1)
result=delete_num(list_1)

print("\t\tlist without duplication -->",result)