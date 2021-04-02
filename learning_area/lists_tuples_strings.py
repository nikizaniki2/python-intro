a = ['foo', 'bar', 'baz', 'qux', 'quux', 'corge']

#we can use negative numbres to count from the back
print(a[1])
print(a[-5])
print(a[-2])
print(a[4])

#slicing
#this example starts counting from 2 but stops at 4
#slicing starts from the first number but stops before the last.
print(a[2:5])

#Not giving a number at which to start or end the slice
#either starts from the begining of the item or doesn't stop until it's end.
print(a[:5])
print(a[2:])

#Striding
# The third number determines how many elements to skip?
print(a[0:6:2])

#in / not in
#Checks if element is in a list.
print('qux' in a)
print('thud' not in a)

#concatenating (adding/splicing) ( Both do not change 'a')
print(a + ['grault', 'garply'])
#replication
print(a * 2)

#Number of intems in a list
print(len(a))

#Lowest value of an item in list
print(min(a))

#Highest value of an item in a list
print(max(a))

#We can use slicing and striding to flip a list
print(a[::-1])

#List can contain other lists as an element(Nesting) (https://files.realpython.com/media/t.08554d94a1e5.png)
x = ['a', ['bb', ['ccc', 'ddd'], 'ee', 'ff'], 'g', ['hh', 'ii'], 'j']

#(copied from site) To access the items in a sublist, simply append an additional index
print(x[1][0])

#Functions are not recursive when ran on a nestet list
print(len(x))

#Unlike strings lists can easily be edited
print(a)
a[2] = 10
print(a)
a[2] = 'baz'

#You can remove an item using the del list_name[item_number]
print(a)
del a[3]
print(a)

#You can combine slicing and editing

a[1:4] = [1.1, 2.2, 3.3, 4.4, 5.5]
print(a)
#"Python just grows or shrinks the list as needed."

#List methods:
# | .append "Appends object <obj> to the end of list a"
# | .extend "Extends a list with the objects from an iterable."
#\/
#Append adds everything as a single element to a list while extend adds each item as its own element in a list.
# .isert "Inserts an object into a list."
print(a)
a.insert(3,'qux')
print(a)
# .remove "Removes an object from a list."
#Removes an item by Value.
a.remove('qux')
print(a)
# .pop "Removes an element from a list."
#Removes an item by ID. Also returns removed item. (Removes last item if index is not specified.)
a.insert(3,'qux')
print(a)
a.pop(3)
print(a)

############# Python Tuples ############

#Tuples (like strings) are immutable.

t = ('foo', 'bar', 'baz', 'qux', 'quux', 'corge')
print("Tuples\n",t)

#You can still use it like a normal list exept for the fact that you cannot change the items in a tuple in any way.
#"'tuple' object does not support item assignment"
#You can redefine a tuple.
t = "foo"
print(t)

#You can swap items by using a single tuple assignment the following way:
#I don't truly understand how this works yet.
a = 'foo'
b = 'bar'
print(a, b)
a, b = b, a
print(a, b)

############### End of tutorial #################