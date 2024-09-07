#Taking total amount form user input
amount = int(input("pls enter amount for withdraw "))

#calculating the number of different notes
note1 = amount // 100
note2 = (amount % 100) // 50
note3 = ((amount%100)%50)//10
print("number of hundred rupess are " , note1)
print("number of fifty   rupess are " , note2)
print("number of  ten    rupess are " , note3)