user = str(input("what do you want to remove an element? "))
numbers = [1, 2 ,3 ,4]

if user == "yes":
    num = int(input("Select a number: "))
    numbers.pop(num)
elif user == "no":
    num = int(input("Enter a number to remove: "))
    numbers.remove(num)

print(numbers)
