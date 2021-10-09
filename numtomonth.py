months = "JanFebMarAprMayJunJulAugSepOctNovDec"

print("Enter the month in numbers")
n = eval(input("Enter the Month Number? "))

value = (n-1)*3

print("The month is {}.".format(months[value:value+3]))

