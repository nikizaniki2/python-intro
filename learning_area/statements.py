dummy = 0

#Basic if and else statements
if dummy:
    print(True)
else:
    print(False)

#elif (Else if)

if dummy == 1:
    print("Dummy is equal to 1")
elif dummy==3:
    print("Dummy is equal to 3")
else:
    print("Dummy is not equal to either 1 or 3")

#Conditional Expression
r = False
print("Let's go to the", 'beach' if not r else 'library')

#Pass Example

if True:
    pass
print("Skipped indented block")