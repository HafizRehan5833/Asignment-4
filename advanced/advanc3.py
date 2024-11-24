#Write a function to flatten a nested list.

def flatten(list_1):
    list_2=[]
    for item in list_1:
        if isinstance(item,list):
            list_2.extend(flatten(item))

        else:
            list_2.append(item)
    return list_2


#def flatten(nested_list):
   # flattened = []
    #for item in nested_list:
    #    if isinstance(item, list):
    #        flattened.extend(flatten(item))  # Recursively flatten the nested list
    #    else:
    #        flattened.append(item)
   # return flattened


list_1=[1,2,[3,4],1,[2,7]]

result=flatten(list_1)
print(result)