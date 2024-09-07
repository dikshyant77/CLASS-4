print("enter the marks obtained in 4 subjects")
maths = int(input("enter maths marks "))
computer = int(input("enter computer marks "))
science= int(input("enter science marks "))
social = int(input("enters social marks "))
totalmarks = maths + computer + science + social
percentage = (totalmarks / 400)* 100
print(percentage)