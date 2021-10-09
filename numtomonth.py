months = "JanFebMarAprMayJunJulAugSepOctNovDec"

print("Enter the month in numbers")
n = eval(input("Which month? "))

value = (n-1)*3

print("The month is {}.".format(months[value:value+3]))

