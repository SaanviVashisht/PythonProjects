#Part 1: Looping by Elements And Index Exercise

students_list=['Jenna','Erni','Beau','Max','Alex','Ronnie','Candace']
for i in students_list:
  print(i)

for i in range(len(students_list)):
    print(i, students_list[i])

#Part 2: Decide whather you should loop by element or loop by index

students_list=['Jenna','Erni','Beau','Max','Alex','Ronnie','Candace']
for index, value in enumerate(students_list):
  students_list[index]= students_list[index]+"'s potato'"
print(students_list)

#Part  3: Alternating Vegetables

students_list=['Jenna','Erni','Beau','Max','Alex','Ronnie','Candace']
for index, value in enumerate(students_list):
  if index % 2 == 0:
    students_list[index]= students_list[index]+"'s potato'"
  else:
    students_list[index]= students_list[index]+"'s yam'"
print(students_list)