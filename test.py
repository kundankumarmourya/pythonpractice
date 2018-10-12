
num1= 30
num2= 40
num3 = num2 + num1
# print ("hello  world" ,  num3)
print("bitwise shift by 2 =" , num1 >> 1)
print("bitwise shift by 2 =" , num2 >> 2)

string1="python"
string2="kundan"

# print("addming string =", string1+string2)

# print("repeating string", string1*4)

# print("string slicing", string1[2:4])

# print(string1.find('p'))
my_list =['kundan', 'manish', 'rahul', 'atul', 'deepak']
my_list.append('coding')
print(my_list)
my_list.extend(['never', 'forget', 'coding' ])
print(my_list)

marks= 76

if (marks>70):
  print("grade A")
elif(marks == 70) and (marks>=70):
 print("Grade B") 
elif(marks < 70) and (marks>60) :
 print("Grade B") 
else:
	print("Fail")