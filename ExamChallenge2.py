maximum = 0
minimum = 0
while True:
    number = input("Enter a number: ")
    if number == "completed":
        break
    try:
        fnumber = float(number)
    except:
        print("Invalid Input")
        continue

    if maximum == 0 or number >= maximum:
        maximum = number
    else:
        maximum = maximum
    if minimum == 0 or number <= minimum:
        minimum = number
    else:
        minimum = minimum
print("Maximum is", maximum)
print("Minimum is", minimum)
