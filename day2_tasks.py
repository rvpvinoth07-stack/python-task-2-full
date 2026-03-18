#Bitwise Operator Tasks
#1
a = 10 
b = 6
print(a&b)

#2
x = 12
y = 5
print(x|y)

#3
num = 8
print(~num)

#4
a = 15
b = 9
print(a^b)

#5
num = 7
print(7 << 2 )

#6
num = 20
print(20 >> 1)

#7
a = int(input("enter first value :- "))
b = int(input("second first value :- "))
print(a&b)

#8
a = int(input("enter first value :- "))
b = int(input("second first value :- "))
print(a^b)

#9
a = "hi"
print(a * 4)

#10
c = "python"
print(c * 3)

#11
str1 = "super"
str2 = "man"
print(str1 + str2)

#12
str3 = "hello"
str4 = "world"
str5 = " "
print(str3 + str5 + str4)

#13
name = input("enter your name :- ")
print(name * 5)

#14
name1 = input("enter first name :- ")
name2 = input("enter second name :- ")
print(name1 + name2)

#15
name =input()
print(name)

#16
age = input("enter your age :- ")
print(age)

#17
num1 = int(input("enter your tamil mark :- "))
num2 = int(input("enter your english mark :- "))
print(num1+num2)

#18
num3 = int(input("enter your Science mark :- "))
num4 = int(input("enter your social mark :- "))
print((num3+num4)/2)

#19
a = int(input("enter your a mark :- "))
b = int(input("enter your b mark :- "))
print(3*a*2+b-2)

#21
num = input()
print(num[len(num)-1])

#22
num1 = int(input())
print(num1%15)

#23
num1 = int(input())
print(num1//10)

#24
num1 = int(input())
print((num1//10)%10)

#25
num1 = int(input())
print(num1%10)

#26
if (10>=5) :
    print("now i think condition true")

#27
num1 = int(input())
if (num1>=50) :
    print(num1>=50)

#28
num1 = int(input())
if (num1>=18) :
    print(num1>=18)


#29
num1 = 110
if (num1>100) :
    print(num1>100)

#30
num1 = 10
if (num1>=0) :
    print(num1>=0)

#31
num1 = int(input("9"))
if num1 % 2 == 0:
    print("9: even")
else :
    print("9: odd")

#32
num1 = int(input())
if num1 >= 35:
    print("pass")
else :
    print("fail")

#33
num1 = int(input())
if num1 > 0:
    print("Positive")
else :
    print("Negative")

#34
num1 = int(input())
if num1 > 10:
    print("Greater than 10")
else :
    print("Not greater than 10")

#35
age = int(input())
height = int(input())
weight = int(input()) 
if(age >=18) :
    if(height >= 160) :
        if(weight >= 60) :
            print("You are selected")

        else :
            ("Your weight is not eligible")
    else :
        ("Your height is not eligible")
else :
    print("Your age is not eligible")

#36
marks = int(input())
age = int(input())
if(marks >= 60) :
    if(age >= 17) :
        print("You got college admission")

    else :
        print("Your age is not eligible")
else :
    print("Your mark is not eligible")

#37
age = int(input())
height = int(input())
weight = int(input()) 

if(age >=16) :
    if(height >= 150) :
        if(weight >= 50) :
            print("You are selected")

        else :
            ("Your weight is not eligible")
    else :
        ("Your height is not eligible")
else :
    print("Your age is not eligible")

#38
day = int(input("enter day number:- "))

match day :
    case 1 :
        print("sunday")
    case 2 :
        print("monday")
    case 3 :
        print("tuesday")
    case 4 :
        print("wednesday")
    case 5 :
        print("thursday")
    case 6 :
        print("friday")
    case 7 :
        print("saturday")