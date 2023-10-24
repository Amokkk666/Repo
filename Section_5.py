first_number = input ("What is the first number? ")
second_number = input ("What is the second number? ")
third_number = input ("What is the third number? ")

if first_number == second_number == third_number:
    print ("Sum is: ",int(first_number)+int(second_number)+int(third_number))
    print ("Sum is: ",int(first_number)+int(second_number)+int(third_number))
    print ("Sum is: ",int(first_number)+int(second_number)+int(third_number))

else:
    print ("Sum is: ",int(first_number)+int(second_number)+int(third_number))


grade_input = input("What is your grade? ")
grade = int(grade_input)
if grade >= 90:
    print("A")
elif grade >=80 and grade<90:
    print ("B")
elif grade >=70 and grade<80:
    print("C")
elif grade >=60 and grade<70:
    print("D")
else:
    print("F")
    