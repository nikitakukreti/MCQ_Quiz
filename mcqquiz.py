print("Welcome to the quiz with questions related to Python...")
print("Let's start the quiz..")
score=0
while(True):
    print("1.Given a function that does not return any value, what value is shown when executed at the shell?")
    print("A.int\n B.bool \nC.void \nD.None")
    a=input("enter your choice")
    if (a=="D"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")

    print("2.Which module in Python supports regular expressions?")
    print("A.re \nB.regex\nC.pyregex\nD.None")
    a=input("enter your choice")
    if (a=="A"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")

    print("3.What is the output of the following program : print 0.1 + 0.2 == 0.3")
    print("A)True\nB)False\nC)Machine depedent\nD)None")
    a=input("enter your choice")

    if (a=="B"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")

    print("4.Which of the following is not a complex number?")
    print("A)k = 2 + 3j\nB)k = complex(2, 3)\nC)k = 2 + 3l\nD)k = 2 + 3J")
    a=input("enter your choice")

    if (a=="C"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")

    print("5.What does ~~~~~~5 evaluate to?")
    print("A)+5\nB)-11\nC)+11\nD)-5")
    a=input("enter your choice")

    if (a=="A"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")

    print("6.Given a string s = “Welcome”, which of the following code is incorrect?")
    print("A)print s[0]\nB)print s.lower()\nC)s[1] = ‘r’\nD)print s.strip()")
    a=input("enter your choice")

    if (a=="C"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
    print("7.________ is a simple but incomplete version of a function.")
    print("A)Stub\nB)Function\nC)A function developed using bottom-up approach\nD)A function developed using top-down approach")
    a=input("enter your choice")

    if (a=="A"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")

    print("8.To start Python from the command prompt, use the command ______")
    print("A)execute python\nB)go python\nC)python\nD)run python")
    a=input("enter your choice")

    if (a=="D"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")

    print("9.Which of the following is correct about Python?")
    print("A)It supports automatic garbage collection.\nB)It can be easily integrated with C, C++, COM, ActiveX, CORBA, and Java\nC)Both of the above\nD)None of the above")
    a=input("enter your choice")

    if (a=="C"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")

    print("10.What is the output of the following program : print "Hello World"[::-1]")
    print("A)dlroW olleH\nB)Hello Worl\nC)d\nD)Error")
    a=input("enter your choice")

    if (a=="A"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
    print("11.What is the output of the following code : print 9//2")
    print("A)4.5\nB)4.0\nC)4\nD)Error")
    a=input("enter your choice")

    if (a=="C"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
    print("12.Which function overloads the >> operator?")
    print("A)more()\nB)gt()\nC)ge()\nD)None of the above")
    a=input("enter your choice")

    if (a=="D"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
    print("13.Which operator is overloaded by the or() function?")
    print("A)||\nB)|\nC)//\nD)/")
    a=input("enter your choice")

    if (a=="B"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
    
    print("14.What is the output of the following program :
          i = 0
          while i < 3:
          print i
          i++
          print i+1")
    print("A)0 2 1 3 2 \nB)0 1 2 3 4 5\nC)Error\nD)1 0 2 4 3 5")
    a=input("enter your choice")

    if (a=="C"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
    print("15.What is the output of the following program :
def myfunc(a):
    a = a + 2
        a = a * 2
    return a
 
print myfunc(2)")
    print("A)8\nB)16\nC)Indentation Error\nD) Runtime Error")
    a=input("enter your choice")

    if (a=="C"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
    print("16.What is the output of the expression : 3*1**3")
    print("A)27\nB)9\nC)3\nD)1")
    a=input("enter your choice")

    if (a=="C"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
    print("17.What is the output of the following program : print '{0:.2}'.format(1.0 / 3)")
    print("A)0.333333\nB)0.33\nC)0.333333:-2\nD)Error")
    a=input("enter your choice")

    if (a=="B"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("18.What is the output of the following program : print '{0:-2%}'.format(1.0 / 3)\nA)0.33\nB)0.33%\nC)33.33%\nD)33%")
    a=input("enter your choice")

    if (a=="C"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("19.What is the output of the following program :
i = 0
while i < 3: 
    print i 
    i += 1
else: 
    print 0  \nA)0 1 2 3 0\nB)0 1 2 0\nC)0 1 2\nD)Error")
    a=input("enter your choice")

    if (a=="B"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("20.What is the output of the following program :
i = 0
while i < 5:
    print(i)
    i += 1
    if i == 3:
        break
else:
    print(0)    \nA)0 1 2 0\nB)0 1 2\nC)Error\nD)None of the above")
    a=input("enter your choice")

    if (a=="B"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("21.What is the output of the following program : print 'cd'.partition('cd')\nA)(‘cd’)\nB)(”)\nC)(”)\nD)(”, ‘cd’, ”)")
    a=input("enter your choice")

    if (a=="D"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("22. What is the output of the following program :    print 'abef'.partition('cd')\nA)(‘abef’)\nB)(‘abef’, ‘cd’, ”)\nC)(‘abef’, ”, ”)\nD)None of the above")
    a=input("enter your choice")

    if (a=="C"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("23. What is the output of the following program :
print 'abcefd'.replace('cd', '12')  \nA)ab1ef2\nB)abcefd\nC)ab1efd\nD)ab12ed2")
    a=input("enter your choice")

    if (a=="B"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
    print("24. What will be displayed by the following code?
def f(value, values):
    v = 1
    values[0] = 44
t = 3
v = [1, 2, 3]
f(t, v)
print(t, v[0])  \nA)1 1\nB)1 44\nC3 1\nD)3 44")
    a=input("enter your choice")

    if (a=="D"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")

    print("25.What is the output of the following code? Consider Python 2.7.
print tuple[1:3] if tuple == ( 'abcd', 786 , 2.23, 'john', 70.2 ) else tuple()  \nA)( 'abcd', 786 , 2.23, 'john', 70.2 )\nB)abcd\nC)(786, 2.23)\nD)None of the above")
    a=input("enter your choice")

    if (a=="D"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("26.What will be the output of the following code :
print type(type(int))\n A)type 'int'\nB)type 'int'\nC)Error\nD)0")
    a=input("enter your choice")

    if (a=="B"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("27.What is the output of the following code :
L = ['a','b','c','d']
print "".join(L)\n  A)Error\nB)None\nC)abcd\nD)[‘a’,’b’,’c’,’d’]")
    a=input("enter your choice")

    if (a=="C"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("28.What is the output of the following segment :
chr(ord('A'))   \nA)A\nB)B\nC)a\nD)Error")
    a=input("enter your choice")

    if (a=="A"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("29.What is the output of the following program :
y = 8
z = lambda x : x * y
print z(6)  \nA)48\nB)14\nC)64\nD)	None of the above")
    a=input("enter your choice")

    if (a=="A"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             
    print("30.Which of the following is the use of id() function in python? \nA)Id returns the identity of the object\nB)Every object doesn’t have a unique id\nC)All of the mentioned\nD)None of the mentioned")
    a=input("enter your choice")

    if (a=="A"):
     print("Correct answer!")
     score=score+1
    else:
         print("Incorrect answer!")
             

print("Quiz has completed...")
print("Your final sore is: ",score)
