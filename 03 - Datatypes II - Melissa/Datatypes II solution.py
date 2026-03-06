# Exercise 1
# 1
numberlist=[1,10,9,7,8,6,2,3,4,5]
# 2
print(7==numberlist[3])
print(2==numberlist[6])
print(1==numberlist[0])
# 3
numberlist.sort()
print(numberlist.index(10))
# 4
print(len(numberlist))
# 5
numberlist.pop(3)
print(numberlist[3])
# 6
numberlist.insert(3,5)
# 7
print(numberlist[3])
print(numberlist[6])
print(numberlist[0])
#8 
numberlist.pop()
numberlist.append(9000)
print(numberlist)

#Exercise 2
# 1
print(numberlist[2:4])
# 2
print(numberlist[:4])
# 3
print(numberlist[2:])
# 4
print(numberlist[:])
# 5
print('''The ":" character symbolises a range.
The expression x:y creates a range from x - x included - to y - y excluded.
      
The given end index is never included in the range.
Since all arrays in python start indexing at zero, the last index will always be at len(array)-1.
      
If either x or y is left empty (array[x:], array[:y], array[:]), python will take the maximum limits.
[:y] -> "X" is 0
[x:] -> "y" is len(array)
[:] -> "x" is 0, y is len(array)''')
#6
print(numberlist[0:len(numberlist)])
#7
print(numberlist[::2]) #prints out every second value
#8
print(numberlist[2:4:2]) #[start:stop:stepsize]

# Exercise 3
# 1
print(numberlist[0])
# 2
print(numberlist[1])
# 3
print(numberlist[-1])
# 4
print('A negative index takes a position counted from the right')
# 5
print(numberlist[-2:])

#Exercise 4
array1=[1,2,3]
array2=[4,5,6]
array3=[7,8,9]
# 1
array4=list()
array4.append(array1)
array4.append(array2)
#2 
print(array4)
#3
array5=[array1,array2,array3]
#4
print(array5[0][2])
print(array5[1][2])
print(array5[1][0])
print(array5[1][1])
print(array5[2][0])

#Exercise 5
applicant1={'name':'Rob','age':32,'dance partner':True,'experience':0}
applicant2={'name':'Catherin','age':27,'dance partner':False,'experience':2}
applicant3={'name':'Clara','age':27,'dance partner':False,'experience':10}
new_applicants=[applicant1,applicant2,applicant3]

#Exercise 6
# 1
print(new_applicants[0].get('age'))
print(new_applicants[1].get('age'))
print(new_applicants[2].get('age'))
print(new_applicants[0].get('age')==new_applicants[1].get('age')==new_applicants[2].get('age'))
# 2
print(new_applicants[2].get('dance partner'))
# 3
new_applicants.pop(2)
new_applicants.insert(2,{'name':'Catherin','age':27,'dance partner':False,'experience':2})
print(new_applicants)
# 4
new_applicants.pop(0)