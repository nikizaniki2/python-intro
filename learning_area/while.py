i=0
#Basic while
while i<10:
    i+=1
    print("My first while loop in Python!!!", i)
print("It stopped looping :(")

#Break example
print("Let's do another.")
i=0
while i<10:
    i+=1
    if i==5:
        print("They broke up with me :(")
        break
    print("Look at meee Im Mr.Measeaks Number:", i)
    
#Pretty simple I think, im used to C++ so the only diff for now is syntax.
#Continue Example
print("Im gonna date again.")
i=0
while i<10:
    i+=1
    if i==5:
        print("I'll swipe left on this date.")
        continue
    print("Date number:", i)

#The first actual diff, Python can Else a While loop
#so im gonna do one.
i=0
while i>10:
    print("bla bla bla")
else:
    print("False statement.")

"""
Look at me im a multi
line comment.
"""
_ = 5

while _ < 10:
    print(_, end = ' ')
    _ += 1

print("\n")
temp = 5

while temp < 10:
    print(temp, end = ' ')
    temp += 1

# _ = temp????

#so we use _ as place to store temporary vars?
end = '\n'
million = 1_000_000
print("")
print(million)
#we can use '_' to make numbers
#easier to read
