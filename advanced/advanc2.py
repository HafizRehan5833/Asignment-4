#2. Create a function that converts a given temperature from Celsius to Fahrenheit and vice versa.

def temperature(user_temp,unit):
   
    if unit == "far":
        celsius=(user_temp - 32) * 5/9 
        return f"Your temperature in farenheit : {user_temp} \n your temperature in celsius:  {celsius:.2f}"

    elif unit== "cel":
        faren=(user_temp* 9/5) + 32
        return f"Your temperature in celcius: {user_temp}\nI convert your temperature in farenheit: {faren: .2f}"
    else:
        return f"invalid"
temp=float(input("Enter the temperature: ")) 
temp_unit=input("Your temperature in Far or Cel:").lower()

result= temperature(temp,temp_unit)
print(result)