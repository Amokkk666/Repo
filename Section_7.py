#1. Exercise
a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))
sign = input("Enter the sign (+ or -): ")


def calculation(a,b,sign):
    if sign == "+":
        return a+b
    if sign == "-":
        return a-b
    
result = calculation (a,b,sign)
print(result)

 #2. Exercise

name = input("Enter the employee name: ")
salary = input("Enter the employyee's salary: ")

def showEmployee(name, salary):
   return("Employee" + " " + name +" "+  "salary" +" "+ "is:" +" "+ salary )

result=showEmployee(name, salary)
print(result)

 #3. Exercise

a = int(input("Enter the first integer: "))
b = int(input("Enter the second integer: "))

def outerFun(a, b):
    def innerFun(a, b):
        return a+b
    return innerFun(a, b) + 8

result=outerFun(a,b)
print(result)