# Exercise 1
# 1
var1 = 5
var2= 10.1
var3 = 5
var4= False
#2
print(type(var1))
print(type(var2))
print(type(var3))
print(type(var4))
# 3
print(var1 == var3)
print(var1 is var3)
print(var2 <= var4)
print(var2 is not var3)
print((var1==var3) and not var4)
print( not var4 or (var1!=var2))
print((var1==var3) or (var2==var1))
print(not (var4 or (var1 == var2)) or (var1<var2))

# Exercise 2
#1
my_string='Melissa Franke'
print(my_string)
print(type(my_string))
#2
pi_string='3.1415'
print(pi_string)
print(type(pi_string))
#3
number_string='3'
print(number_string)
print(type(number_string))
#4
yes=True
print(yes)
print(type(yes))

# Exercise 3
# 1
# print(int(my_string))
# print(float(my_string))
print(bool(my_string))
#2
pi_float=float(pi_string)
print(pi_float)
print(type(pi_float))
pi_int=int(pi_float)
print(pi_int)
print(type(pi_int))
#3
check=pi_int==int(number_string)
print(check)
print(type(check))

# Exercise 4
var5=0
var6=''
var7='0.0'
var8=1
var9=10
var10='Hello World'
print(bool(var5))
print(bool(var6))
print(bool(float(var7)))
print(bool(var8))
print(bool(var9))
print(bool(var10))

# Exercise 5
var11 = 'olfactory bulb, testis'
var12= 'vno'
var13='Spehr Lab research fields:'

print(var11.split(', '))
print(var12.upper())
print(var12.upper() +', '+ var11)