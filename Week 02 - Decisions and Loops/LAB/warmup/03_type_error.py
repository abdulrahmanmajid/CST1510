# BROKEN ON PURPOSE.
# Run it, read the last line, then fix it.

limit = 20
value = float(input("Value: ")) # I had to add a float function to the input so that it would convert the users value from text ( str ) to a numnber ( float

if value > limit:
    print("OVER")
else:
    print("OK")
