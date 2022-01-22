#Problem1
input_1="Python is a case sensitive language"
print('Q1')
#a
print(len(input_1))

#b
reverse=input_1[::-1]
print(reverse)

#c
new_string=input_1[10:26]
print(new_string)

#d
replace1="object oriented"
replaced_string=input_1.replace("a case sensitive",replace1)
print(replaced_string)

#e
index=input_1.find('a')
print('index of a is:',index)

#f
input_new=input_1.replace(" ","")
print(input_new)

#Problem2
print('\nQ2')
name=input("Enter your name:")
SID=int(input("Enter student ID:"))
dept_name=input("Enter department name:")
CGPA=float(input("Enter CGPA:"))

print('Hey, %s Here!'%(name))
print('My SID is %s'%(SID))
print('I am from %s department and my CGPA is %s' %(dept_name,CGPA))


#Problem3
print('\nQ3')
a=56
b=10
#a
print('a&b=',a&b)
#b
print('a|b=',a|b)
#c
print('a^b=',a^b)
#d
print('\nleft shift a by 2 units=',a<<2)
print('left shift b by 2 units=',b<<2)
#e
print('\nright shift a by 2 units=',a>>2)
print('right shift b by 4 units=',b>>4)

#Problem4
print('\nQ4')
numb1=float(input("enter first number=",))
numb2=float(input("enter second number=",))
numb3=float(input("enter third number=",))
maxx=max(numb1,numb2,numb3)
print('Greatest number=',maxx)

#Problem5
print('\nQ5')
sentence=input('enter the string:')
sentence=sentence.lower()
if 'name' in sentence:
     print('Yes')
else:
    print('No')

#Problem6
print('\nQ6')
side1=float(input('enter length of first side='))
side2=float(input('enter length of second side='))
side3=float(input('enter length of third side='))
a=int(side1)
b=int(side2)
c=int(side3)
print('Is the triangle possible?')
if a+b>c:
    print('Yes')
elif b+c>a:
    print('Yes')
elif c+a>b:
    print('Yes')
else:
    print('No')
