print("Find that which number is greater!!")




a = int(input("Enter first number:   "))
b = int(input("Enter second number:   "))

if a > b:
     print(a, "Is greater than", b)

elif a < b:
     print(a, "Is not greater than", b)

else:
     print(f"{a} is equal to {b}")