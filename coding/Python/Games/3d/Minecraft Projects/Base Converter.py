#Base Converter by Albert Hao
base = int(input("Enter the base of the number to convert to: "))
originalNumber = input("Enter the number to convert: ")
powerList = [1]
for power in range(len(str(originalNumber))):
    powerList.append(base**power)
print(powerList)