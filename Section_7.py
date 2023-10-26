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
    