
#Problem1
print('Q1')
inp=input("Enter a word or sentence-")
inp=inp.lower().strip()
i=0
dict={}
if " " not in inp:
    #word case
    while i<len(inp):
        count=0
        j=0
        while j<len(inp):
            if inp[i]==inp[j]:
                count=count+1
                j=j+1
            else:
                j=j+1
        dict[f"{inp[i]}"]=count
        i+=1
    for key,value in dict.items():
        print(f"{key}:{value}")
else:
    #sentence case
    list=str.split(inp)
    while i<len(list):
        count=0
        k=0
        while k<len(list):
            if list[i]==list[k]:
                count+=1
                k+=1
            else:
                k+=1
        dict[f"{list[i]}"]=count
        i+=1
    for key,value in dict.items():
        print(f"{key}-{value}")

#Problem2

print("\nQ2")
#Taking input from user
day=int(input('Please enter Day- '))
month=int(input('Please enter Month- '))
year=int(input('Please enter Year- '))


#Removing invalid cases
if day>30 and month in {2,4,6,9,11}:
    condition=False
elif day>31 and month in {1,3,5,7,8,10,12}:
    condition=False
elif (day==29 or day==30) and month==2 and year%4!=0:
    condition=False
elif day==30 and month==2 and year%4==0:
    condition=False
else:
    condition=True


#if-else statement
if condition:
    #checking if new year
    if day==31 and month==12:
        n_year=year+1
    else:
        n_year=year
    if month==12 and day==31:
        n_month=1
    else:
        n_month=month
#changing dates
    #checking for months with 31 days
    if month in {1,3,5,7,8,10,12}:
        if day==31:
            next_day=1
            if month!=12:
                n_month=month+1
            else:
                n_month=1
        else:
            next_day=day+1
    #checking for the month of february
    elif month==2:
        if year%4==0:
            if day==29:
                next_day=1
                n_month=3
            else:
                next_day=day+1
        else:
            if day==28:
                next_day=1
                n_month=3
            else:
                next_day=day+1
                    
    #covering all the remaining cases
    else:
        if day==30:
            next_day=1
            n_month=month+1
        else:
            next_day=day+1
    print(f"Next Date is: {next_day}/{n_month}/{n_year}")
else:
    #gives a warning and ends the program
    print("Invalid date entered.")
    

#Problem3
print('\nQ3')    
#defining empty list to take input from user
list_0=[]
while input("Enter Y to enter data:").lower().strip()=='y':
    list_1=float(input("Enter a number: "))
    list_0.append(list_1)
print(list_0)

#defining empty list to store tuple pairs
list3=[]
for i in list_0:
    tuple1=(i,i**2)
    list3.append(tuple1)
print(list3)    
        

#Problem4
print('\nQ4')
grade=int(input('Enter Grade Points-'))

dictionary={10:{'l_grade':'A+','p_mance':'Outstanding'},
           9:{'l_grade':'A','p_mance':'Excellent'},
           8:{'l_grade':'B+','p_mance':'Very Good'},
           7:{'l_grade':'B','p_mance':'Good'},
           6:{'l_grade':'C+','p_mance':'Average'},
           5:{'l_grade':'C','p_mance':'Below Average'},
           4:{'l_grade':'D','p_mance':'Poor'}}
if 3<grade<11:
    for key in dictionary.keys():
        if key==grade:
            value=dictionary[key]
            print(f"Your Grade is {value['l_grade']} and {value['p_mance']} performance ")
        else:
            continue
else:
    print('Error!')
#Problem5
print('\nQ5')    
list_1=['A','B','C','D','E','F','G','H','I','J','K']
row=1
space=''
while row<=6:
    for k in list_1:
        print(k,end='')
    list_1=list_1[:-2]
    row+=1
    space+=' '
    print('')
    print(space,end='')

#Problem6
print('\nQ6')
dictionary={}
entering_values=True
while entering_values:
    #input
    SID=int(input("Enter SID:"))
    name=str(input("Enter name of the student:"))
    #Storing response in dictionary
    dictionary[SID]=name
    #new entries
    repeat=input("Do you want to enter another entry?(Y/N)")
    if repeat.upper()=="N":
        entering_values=False
    elif repeat.upper()=="Y":
        continue
    else:
        entering_values=False
        print("Error!")
       
print(dictionary)

#a
print("\nPART A")
for SID,name in dictionary.items():
    print(f"SID {SID} is {name}.")

#b
print("\nPART B")    
name_sorted=sorted(dictionary.values())
print(name_sorted)

#c
print("\nPART C")
SID_sorted=sorted(dictionary.keys())
print(SID_sorted)

#d
print("\nPART D")
inpu=int(input("Enter SID of the student:"))
if inpu in dictionary.keys():
     print(f"name:{dictionary[inpu]}")
else:
    print("Invalid SID")

    
#Problem7

print("Q7")
number=int(input("Total elements of Fibonacci sequence that you want(must be greater than 1)- "))

#using the formula of the sum of previous two terms is equal to the present term.
a_n1=1
a_n2=0
n=0
#initializing sum with first two terms
sum=a_n1+a_n2

#initial two terms case(recursion not valid)
print(f"Fibonnaci sequence with {number} terms")
print(a_n2)
print(a_n1)

#remaining fibonnaci terms
while n<number-2:
    a_n=a_n2+a_n1
    a_n2=a_n1
    a_n1=a_n
    print(a_n)
    n=n+1
    sum+=a_n

print(f"Sum of total {number} terms of sequence is {sum}")
average=sum/number
print(f"Average= {average}")
print("End")

#Problem8
print("Q8")
Set1= {1, 2, 3, 4, 5}
Set2= {2, 4, 6, 8}
Set3= {1, 5, 9, 13, 17}

#parta
print("PART A")
set_notboth=Set1^Set2
print(f"set with elements in set1 and set2 but not common: {set_notboth}")

#partb
print("PART B")
set_onlyinone=Set1^Set2^Set3
print(f"Set of elements that are only present in not more than one set: {set_onlyinone}")

#partc
print("PART C")
set_onlyintwo=(Set1|Set2|Set3)- (Set1^Set2^Set3)-(Set1&Set2&Set3)
print(f"Set of elements that are only present in two sets: {set_onlyintwo}")

#partd
print("PART D")
new_set1=set()
for n in range(1,11):
    new_set1.add(n)
not_common_1=new_set1- Set1
print(f"set of all integers in the range 1 to 10 that are not in Set1: {not_common_1}")

#parte
print("PART E")
new_set2=set()
for n in range(1,11):
    new_set2.add(n)
not_common_2=new_set2 - (Set1|Set2|Set3)
print(f"Set of all integers in the range 1 to 10 that are not in Set1 and Set2 and Set3: {not_common_2}")
    
