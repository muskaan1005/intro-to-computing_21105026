#Assignment1
#1st program
numb1=int(input("enter first number: "))
numb2=int(input("enter second number: "))
numb3=int(input("enter third number: "))
avg=(numb1+numb2+numb3)/3
print("The average is ",avg)

#2nd program
GrossIncome=float(input("Gross income: "))
dependents=int(input("Dependents: "))
taxrate=0.2
s_deduction=10000
d_deduction=3000
taxable_income=GrossIncome-s_deduction-(d_deduction*dependents)
tax=taxable_income*taxrate
print("Income tax: ",tax)

#3rd program
print("Student=[SID, Name, Gender, DepartmentName, CGPA]")
Student=[11,'Nikhil','M','Mechanical',8.9]
print("Student=",Student)
Student=[15,'Mudita','F','Electronics',9.0]
print("Student=",Student)

#4th program
Marks=[11,76,34,56,30]
print("Marks unsorted= ",Marks)
Marks.sort()
print("Marks sorted= ",Marks)

#5th program
print("color=['Red','Green','White','Black','Pink','Yellow']")
#a
color=['Red','Green','White','Black','Pink','Yellow']
color.pop(3)
print("color",color)
#b
color=['Red','Green','White','Black','Pink','Yellow']
color[3:5]=['Purple']
print("color",color)
