operatorList = []
numberList = []

operationAmount = int(input("Please enter the amount of operations: "))

number = 0
ordinalNumber = 0

if abs(number) % 10 == 1 and abs(number) > 3:
    ordinalNumber = f"{number}th"

elif abs(number) % 10 == 1 and abs(number) <= 3:
    ordinalNumber = f"{number}st"

elif abs(number) % 10 == 2 and abs(number) <= 3:
    ordinalNumber = f"{number}nd"

elif abs(number) % 10 == 3 and abs(number) <= 3:
    ordinalNumber = f"{number}rd"

for number in range(operationAmount):
    numberInput = int(input(f"What will your {ordinalNumber} number be?: "))

