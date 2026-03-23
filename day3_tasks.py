#1
for i in range(1,51) :
    print(i)

#2
for i in range(2,101,2) :
    print(i)

#3
for i in range(1,101,2) :
    print(i)

#4
for i in range(1,11) :
    print("7 x", i, "=", 7*i)

#5
total = 0
for i in range(1,101):
    total += i
print("sum:", total)

#6
for i in range(50, 0, -1):
    print(i)

#7
count = 0
for i in range(1,101):
    if i%3 == 0:
        count += 1
print("divisible by 3:", count)

#8
for i in range(1,11):
    print(i*i)

#9
for i in range(1,11):
    print(i**3)

#10
n=int(input())
for i in range(1,n+1):
    print(i)

#11
i = 1
while i <= 20:
    print(i)
    i += 1

#12
num = int(input())
fact = 1
i = 1
while i <= num:
    fact *= i
    i += 1
print(fact)

#13
num = int(input())
rev = 0
while num > 0:
    rev = rev * 10 + num % 10
    num //= 10
print(rev)

#14
num = int(input())
count = 0
if num == 0:
    count = 1
else:
    while num > 0:
        count += 1
        num //=10
print(count)

#15
while True:
    text = input("Enter (stop to end): ")
    if text.lower() == "stop":
        break

#16
for i in range(1, 5):
    for j in range(i):
        print("*", end="")
    print()    