#Lists to hold operations and numbers
operatorList = []
numberList = []
messyOperationList = []

#Ask for the operation amount
operationAmount = int(input("Please enter the amount of operations: "))

#Ask for the first number
operationNumber = int(input(f"What will be your 1st number?: "))
numberList.append(operationNumber)

for number in range(1, operationAmount + 1):
    #Calculate ordinal numbers
    if number % 10 == 1 and number % 100 != 11:
        ordinalNumber = f"{number}st"

    elif number % 10 == 2 and number % 100 != 12:
        ordinalNumber = f"{number}nd"

    elif number % 10 == 3 and number % 100 != 13:
        ordinalNumber = f"{number}rd"

    else:
        ordinalNumber = f"{number}th"
    
    #Ask for operation
    if ordinalNumber == f"{number}st":
        operator = input(f"What will your {ordinalNumber} operation be?: ")

    else:
        operator = input(f"What about the {ordinalNumber} operation?: ")
    
    #Append the inputted operator into the list
    operatorList.append(operator)

    #Ask for a number and then append it into the list
    operationNumber = int(input(f"What about the {ordinalNumber} number?: "))
    numberList.append(operationNumber)
    
#Assign the numbers and operators into a list
for i in range(len(numberList)):
    messyOperationList.append(numberList[i])
    i+=1

for i in range(len(operatorList)):
    messyOperationList.append(operatorList[i])
    i+=1

#Seperate numbers and operations
numbersForOperation = [x for x in messyOperationList if isinstance(x, int)]
operatorsForOperation = [x for x in messyOperationList if isinstance(x, str)]

#Interleave numbers and operators together in the list 
organizedOperationList = []
for i in range(len(numbersForOperation)):
    organizedOperationList.append(numbersForOperation[i])
    if i < len(operatorsForOperation):
        organizedOperationList.append(operatorsForOperation[i])

#Calculate the operation
operationString = "".join(str(x) for x in organizedOperationList)
result = eval(operationString)

print(f"{operationString}={result}")
