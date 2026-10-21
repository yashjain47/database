# print(-10//3)

'---------------------------------------------------------------------------------'
# a = {}
# print(type(a))
# b = set()
# print(type(b))
# c = []
# print(type(c))
# d = tuple()
# print(type(d))

'----------------------------------------------------------------------------------'

# print('"""Converstion adcaafd "asdadasdad" asjdhayaha"""')
# print("\"\"\"Converstion adcaafd \"asdadasdad\" asjdhayaha \"\"\"")

'----------------------------------------------------------------------------------'

# print(2**3**2)
'''left to right operators for associativity
right to left operators for associativity for exponentialy
so for 2**(3**2)  --> 2**9 --> 512'''


# print("asabdad \\n aanscnac")
'\ --> \ escape character and \\ ---> \ '

# print("/\/\/\/\/\/\/\/\\")

# a = "Shantanu"
# print(a[2:8:-2])

# a ={"jay":23,"yash":12,"yash":122}
# print(len(a),a)

# a = [1,4,7]
# b = [2,5,8]
# c = [3,6,9]

# print(list(zip(a,b,c)))

# print(10.0//3)


# print(type(2E3),2E3)


# print(765<1)
# for i in 765<1:
#     print(i)

# a = "yash jain"
# b = "Yash jain"

# print(ord('Y'),ord('y'))
# print(a == b)


'''Operators Type

UNARY OPERATOR --> works on 1 operator (Eg. Bitwise operator (~))
BINARY OPERATOR --> works on 2 operator (Eg. Add operator (+))
TERNARY OPERATOR --> works on 3 operator 

Ternary operator syntax:
    value if true <condition> value if false 
    if,else are ternary operator in python

    eg. print("Yash") if (a>b)  else print("NO") 

'''

# a,b = 10,20
# print(~a)
# print(a+b)

# print("Yash") if (a>b)  else print("NO") 


'-----------------------------------------------------------------------------------------------------'

'''
PEP8
written by guido van rossum

for readability and consistency.
 

Rule:
1.  Naming conventions of variables, modules, packages.
2.  variable name for constant and class name.

'''


'-----------------------------------------------------------------------------------------------------'

'''
walrus operator

you can assign 
a = 100
a+1

'''
# a = 100
# print(a+1)




a = [3,3,42,4,2,5,67,3,2,46]
b = []

while a:
    min = a[0]
    for i in a:
        if i < min:
            min = i
            b.append(min)
            a.remove(min)
        
print(b)