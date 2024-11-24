def repition(num):
    list_1=[]
    for i in range(user_input):
        a=int(input("Enter ssallaries:"))
        list_1.extend(a)
    return list_1

user_input=int(input("Enter number: "))                
        
result=repition(user_input)

print(result)