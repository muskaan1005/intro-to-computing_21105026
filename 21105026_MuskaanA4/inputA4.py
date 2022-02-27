#Problem1
print('Question1:')
def hanoi_tower(n,present_pos,final_pos,vacant):
    #disk 1 refers to the smallest disc
    if n==0:
        return
    if n==1:
        print(f"Move the disk 1 from {present_pos} to {final_pos}")
        return
    hanoi_tower(n-1,present_pos,vacant,final_pos)
    print(f"Move the disk {n} from {present_pos} to {final_pos}")
    hanoi_tower(n-1,vacant,final_pos,present_pos)

#calling function for 3 disks          
n=3
hanoi_tower(n,'A','B','C')




#Problem2
print('\nQuestion2:')
#taking number of rows as input from user
n=int(input("Enter the number of rows you want in pascal's triangle: "))

#using recursion
print("\nPascal triangle using recursion:")

def pastri(n,org_n=n):
    if n==0:
        return
    
    pastri(n-1,org_n)
    #spaces
    print(' '*(org_n-n),end='')

    #first numbers should be always one
    n1=1
    for i in range(1,n+1):
        print(n1,end=' ')

        #using binomials coeff
        n1=n1*(n-i)//i
    print()
pastri(n)

#using loops
print("\nPascal triangle using loops: ")
for p in range(1,n+1):
    print(' '*(n-p),end='')

    x=1
    for m in range(1,p+1):
        print(x,end=' ')

        x=x*(p-m)//m
    print()

    


#Problem3
print('\nQuestion3:')
a=int(input("enter first integer: "))
b=int(input("enter second integer: "))
while b==0:
    b=int(input("Error! Please enter a non zero integer:"))

qr=divmod(a,b)
quotient=qr[0]
remainder=qr[1]
print(f"Quotient={quotient}")
print(f"Remainder={remainder}")


#a
#checking if function is callable
print('\na)')
s=callable(divmod)
print(s)

#b
print('\nb)')
#checking for nonzero values
print(all(qr))

#c
print('\nc)')
qr=list(qr)
qr.extend([4,5,6])
print(qr)
filtr=filter(lambda n:n>4,qr)
print("Values greater than 4: ",list(filtr))

#d

print('\nd)')
g=set(qr)
print(g)

#e
print('\ne)')
fs = frozenset(g)
print("Immutable set : ", fs)


#f
print('\nf)')
o= max(fs)
print(hash(str(o)))


  

#Problem4
print('\nQuestion4:')

class Student:

    # defining init function
    def __init__(self, name, r_no):
        self.name = name
        self.r_no = r_no
        print("Object created")

    # defining del function
    def __del__(self):
        print("Object deleted")


# storing data in class
s1 = Student("mehak", 234)
s2 = Student("varun", 235)
s3 = Student("arnav", 236)

print() 

# calling del function to destroy object
del s2



# Problem5

print('\nQuestion5:')

class Employees:

    # defining init function
    def __init__(self, Name, Salary):
        self.Name = Name
        self.Salary = Salary

    # defining record function
    def record(self):
        print("Employee Name : ", self.Name)
        print("Employee Salary : ", self.Salary)
        print("\n")


# storing data 
e1 = Employees("Mehak", 40000)
e2 = Employees("Ashok", 50000)
e3 = Employees("Viren", 60000)


print("Record of all employees\n")
e1.record()
e2.record()
e3.record()

#a
print("a)")
#updating mehak's salary
print("updated record\n")
e1.Salary = 70000
e1.record()

#b
print("b)")
#deleting vivek's record
del e3
print("Record deleted.")

#Problem6
print("\nQuestion6:")


m1 = input("Please enter word spoken by first friend : ")
m2 = input("Please enter word spoken by second friend: ")
print()
    


# defining a function
def friendship(w1, w2):

    w1 = w1.lower()
    w2 = w2.lower() 

    # checking whether same letters are used in both words
    if sorted(w1) == sorted(w2):
        print("Your friendship is real.")
    else:
        print("Same letters not used.")

#verifying new word's meaningfulness from shopkeeper
mm=input("Is the new word meaningful?(Y/N)")


if mm.upper()=="N":
    print("Your friendship is fake.")
elif mm.upper()=="Y":
    friendship(m1, m2)
else:
    ("Error!")







