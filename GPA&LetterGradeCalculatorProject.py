def getSum(list1):
    sum=0
    for x in list1:
        sum=sum+x
    return(sum)

def getCount(list1):
    count=0
    for x in list1:
         count=count+1
    return(count)

def getGrade(average):
    if average >= 97:
        print("Your letter grade is A+ and your GPA is 4.0")
    elif average >= 93:
        print("Your letter grade is A and your GPA is 4.0")
    elif average >= 92:
        print("Your letter grade is A- and your GPA is 3.7")
    elif average >= 89:
        print("Your letter grade is B+ and your GPA is 3.3")
    elif average >= 86:
        print("Your letter grade is B and your GPA is 3.0")
    elif average >= 82:
        print("Your letter grade is B- and your GPA is 2.7")
    elif average >= 79:
        print("Your letter grade is C+ and your GPA is 2.3")
    elif average >= 76:
        print("Your letter grade is C and your GPA is 2.0")
    elif average >= 72:
        print("Your letter grade is C- and your GPA is 1.7")
    elif average >= 69:
        print("Your letter grade is D+ and your GPA is 1.3")
    elif average >= 66:
        print("Your letter grade is D and your GPA is 1.0")
    elif average <= 65:
        print("Your letter grade is E/F and your GPA is 0")
    else:
        print("Invalid input")

    

while 1==1:
    list1=input("Please give the list of your grades (seperated by spaces) to calculate the percentage and print the letter grade and GPA accordingly: ")
    listOfMarks = [int(x) for x in list1.split()]
    sum=getSum(listOfMarks)
    count=getCount(listOfMarks)
    average = sum/count
    getGrade(average)
    

        

