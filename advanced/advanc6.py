#. Write a function that takes a list of employee salaries and calculates the average salary.
def average_salary(salleries):
    if not salleries:
        return 0
    return sum(salleries)/len(salleries)

salleries_list=[]
avg_list=[]
print("Your salleries list are -->", salleries_list)
user_input=input("\t\t\tDo you want to  addition or not: ")
num=int(input("How much  salleries number you want to  add in list : "))
if user_input == "add":
    if num == 1:
        add_salary1=int(input("Enter add salary: "))
        
        
        avg=add_salary1/12
        avg_list.extend(add_salary1)
        
        
        
        salleries_list.extend(avg)
        
        
    elif num == 2:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        avg=sum(add_salary1,add_salary2)/12
        avg_list.extend(avg)
        salleries_list.extend([add_salary1,add_salary2])
    elif num == 3:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
       
       
        avg=sum(add_salary1,add_salary2,add_salary3)/12
        avg_list.extend(avg)


        salleries_list.extend([add_salary1,add_salary2,add_salary3])
    elif num == 4:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))

        avg=sum(add_salary1,add_salary2,add_salary3,add_salary4)/12
        avg_list.extend(avg)

        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4])
    elif num == 5:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))

        
        avg=sum(add_salary1,add_salary2,add_salary3,add_salary4,add_salary5)/12
        avg_list.extend(avg)


        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5])

    elif num == 6:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))

        avg=sum(add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6)/12
        avg_list.extend(avg)


        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6])

        

    elif num == 7:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))  

        avg=sum(add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7)/12
        avg_list.extend(avg)

        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7])  
    elif num == 8:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))    
        add_salary8=int(input("\tEnter add salary: "))
        
        
        avg=sum(add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8)/12
        avg_list.extend(avg)


        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8])

    elif num == 9:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))    
        add_salary8=int(input("\tEnter add salary: "))       
        add_salary9=int(input("\tEnter add salary: "))


        avg=sum(add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary7,add_salary9)/12
        avg_list.extend(avg)

        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary7,add_salary9])
    elif num == 10:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))    
        add_salary8=int(input("\tEnter add salary: "))       
        add_salary9=int(input("\tEnter add salary: ")) 
        add_salary10=int(input("\tEnter add salary: "))

        avg=sum(add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8,add_salary9,add_salary10)/12
        avg_list.extend(avg)

        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8,add_salary9,add_salary10])          
        
    elif num == 11:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))    
        add_salary8=int(input("\tEnter add salary: "))       
        add_salary9=int(input("\tEnter add salary: ")) 
        add_salary10=int(input("\tEnter add salary: "))  
        add_salary11=int(input("\tEnter add salary: "))
        

        avg=sum(add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8,add_salary9,add_salary10,add_salary11)/12
        avg_list.extend(avg)


        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8,add_salary9,add_salary10,add_salary11])          
     
    elif num == 11:
        add_salary1=int(input("\tEnter add salary: "))
        add_salary2=int(input("\tEnter add salary: "))
        add_salary3=int(input("\tEnter add salary: "))
        add_salary4=int(input("\tEnter add salary: "))
        add_salary5=int(input("\tEnter add salary: "))
        add_salary6=int(input("\tEnter add salary: "))  
        add_salary7=int(input("\tEnter add salary: "))    
        add_salary8=int(input("\tEnter add salary: "))       
        add_salary9=int(input("\tEnter add salary: ")) 
        add_salary10=int(input("\tEnter add salary: "))  
        add_salary11=int(input("\tEnter add salary: "))
        add_salary12=int(input("\tEnter add salary: "))

        avg=sum(add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8,add_salary9,add_salary10,add_salary11,add_salary12)/12
        avg_list.extend(avg)

        salleries_list.extend([add_salary1,add_salary2,add_salary3,add_salary4,add_salary5,add_salary6,add_salary7,add_salary8,add_salary9,add_salary10,add_salary11,add_salary12])          
                    

else:
    print("invalid")   

print("Your salleries list after addition -->", salleries_list)


#total_sum=sum(salleries_list)

#print("Your",len(avg_list)," month salleries are --->",)

result=average_salary(avg_list)

print(f"Your average salary is {result:.2f}")