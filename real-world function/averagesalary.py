#Write a function that takes a list of employee salaries and calculates the average salary.


def salaries(list_sal) :   
    result=sum(avg_list)
    return result

salleries_list=[]
avg_list=[]

sallery_1=int(input("Entry first employee yearly sallery: "))
salleries_list.append(sallery_1)

sallery_2=int(input("Enter second employee yearly sallery: "))
salleries_list.append(sallery_2)

sallery_3=int(input("Enter third employee yearly sallery: "))
salleries_list.append(sallery_3)

print("Your yearly salleries list are: ",salleries_list)

#input from user  the sallery how much  divide by total sallery
for_yes_or_no=input("\t\t\tDo you want to show your average salary \n\t\t\t\tPlease enter (yes/no): ").lower()
if for_yes_or_no == "yes":
    user_input=int(input("Enter how many month average salary you want:  "))
    avg_1=sallery_1/user_input
    print("The" ,user_input," month salary of first employee: ",avg_1 )
    avg_list.append(avg_1)

    # for second person
    avg_2=sallery_2/user_input
    print("The" ,user_input," month salary of first employee: ",avg_2 )
    avg_list.append(avg_2)

    #for third person
    avg_3=sallery_3/user_input
    print("The" ,user_input," month salary of first employee: ",avg_3 )
    avg_list.append(avg_3)


sum_salry=sum(salleries_list)

print("\t\t\t\tYou need ",sum_salry," rupees for yearly employee salaries..")



func=salaries(avg_list)

print("Your need ",func,"Rupees for monthly employee salaries..")
