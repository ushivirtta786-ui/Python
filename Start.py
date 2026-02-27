# print("Vishu")

# a = 1
# b = 7
# sum = a + b
# print(sum)
# print("answer is", a + b)

# Data types 
# * Integers
# *   String
# *   Float
# *   Boolean
# *   None

# age = 10
# name = "Vishu"
# height = 5.76
# old = False
# print(type(age))
# print(type(name))
# print(type(height))
# print(type(old))

# Keywords
# and	else	in	return
# as	except	is	True
# assert	finally	lambda	try
# break	False	nonlocal	with
# class	for	None	while
# continue	from	not	yield
# def	global	or	
# del	if	pass	
# elif	import	raise	

# Types of operators
# *   Arithmetic Operators (+,  - , *, /, %, **)
# *   Relational / Comparison Operators (==, !=,  >, < , >=, <=)
# * Logical Operators (not, and, or)
# * Assignment operators (=, +=, -=, /=, %=, **=)

# print(a % b) # modulus operator
# print(a ** b) # a^b operator

# a = 4
# b = 7
# print(a == b)
# print(a != b)

# a += b
# print(a)

# a -= b
# print(a)

# a *= b
# print(a)

# a /= b
# print(a)

# a %= b
# print(a)

# a **= b
# print(a)

# a = 8
# b = 9
# print( not a == b)

# print(a!=b and a<b)
# print(a!=b and a>b)
# print(a==b or a<b)
 
# #Type conversion
# a = 5
# b = 7.54
# # sum = a + b
# # print(type(sum), sum)

# # type casting
# a = int(b)
# c = 6
# sum = a + c 
# print(type (a))
# print(type(sum), sum)

# Input
# * input() statement is used to accept values (using keyboard) from user
# * input() #result for input() is always a str
# * int (input()) #int
# * float (input()) #float

# name = input("What is ur name: ")
# print("Name is:", name)

# * Escape sequence character 
# * \n
# * \t

# a= int(input('a='))
# b= int(input('b='))
# if a>=b:
#     print("True")
# else:
#     print("False")

# # concatenation
# str1 = 'Vishu'
# str2 = 'Attri'
# print(str1+str2)
# print(str1+ "   " +str2)

# # length of string
# len1 = len(str1)
# print(len(str1))
# print(len1)

# # Indexing
# str = "Vishu Attri"
# print(str[3])

# # Slicing
# # +ve
# str= "Vishu Attri"
# print(str[0:5])
# # -ve
# print(str[-5:])

# # String fuctions
# str = 'i am the father of this world'
# print(str.endswith('ld'))
# print(str.capitalize())
# str = str.capitalize()
# print(str)
# print(str.replace('world', 'universe'))
# print(str.find('t')) #tells index of first character
# print(str.find('z')) #-1
# print(str.count('o'))

# name = input('Ur name: ')
# print(len(name))

# a = 'i hv 20$ $is 80 now'
# print(a.count('$'))

# Conditional statements
# if checks every statement
# if-else checks only one statement
# else runs after all statements are false
# a = int(input("Any no: "))
# if a%2 == 0:
#     print("Even")
# else:
#     print("Odd")

# # Grade Students
# marks = int(input('Mrks: '))
# if(marks>=90):
#     print("Grade A")
# elif(marks>=80):
#     print("Grade B")
# elif(marks>=70):
#     print("Grade C")
# else:
#     print("Grade D")

# # Nesting 
# a = int(input("Bisep size: "))
# if a>=10:
#     if a>=15:
#         print("Very Big")
#     else:
#         print("Not that big")
# else:
#     print("Small")

# # Greatest of three nos.
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# if a>=b and a>=c:
#     print("a is greatest")
# elif b>=c:
#     print("b is greatest")
# else:
#     print("c is greatest")

# # Greatest of four nos.
# a = int(input("a: "))
# b = int(input("b: "))
# c = int(input("c: "))
# d = int(input("d: "))
# if a>=b and a>=c and a>=d:
#     print("a is greatest")
# elif b>=c and b>=d:
#     print("b is greatest")
# elif c>=d:
#     print("c is greatest")
# else:
#     print("d is greatest")

# # Mustiple of 7 or not
# a = int(input("Any no: "))
# if a%7 == 0:
#     print("Multiple of 7")
# else:    print("Not a multiple of 7")

# reverse 
a = int(input('a= '))
reverse_a = int(str(a)[::-1])
print('a= ', reverse_a)