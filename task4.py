user = str(input("Do you want to reverse? or alphabetically? "))
numbers = [1,2,3,4]

if user == "reverse":
    numbers.reverse()
elif user == "alphabetically":
    numbers.sort()

print(numbers)