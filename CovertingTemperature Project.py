
def convertingCelsiusToFarenheit(C):
    F = (9/5*C)+32
    return(F)

def convertingFarenheitToCelsius(F):
    C= (F-32) * (5/9)
    return(C)


while 1==1:
    user=int(input("Hi there! Please press 1 if you would like to convert Celsius to Farenheit and 2 if you like to convert Farenheit to Celsius and 3 if you want the program to stop:  "))
    if user==1:
        C= int(input("Please enter a number which you would like to be converted to Farenheit: "))
        answer=convertingCelsiusToFarenheit(C)
        print(answer)
    elif user==2:
        F=int(input("Please enter a number you would like to be converted to Celsius: "))
        answer=convertingFarenheitToCelsius(F)
        print(answer)
    elif user==3:
        break
    else:
        print("Invalid input.")








