########################################################################################################################
# Created on Tue 26_01_13   #   Created by Melissa Franke   #   fair use in Chemosensation Coding Workshop
# Last edit: 26_04_07       #   Edited by Melissa Franke
########################################################################################################################

def mystery_function(array: list) ->list:
    swapped=True
    while swapped:
        swapped=True
        for i in range(1,len(array)):
            if array[i-1]>array[i]:
                temp=array[i]
                array[i]=array[i-1]
                array[i-1]=temp
                swapped=True
    return array

my_list=[1,10,9,7,8,6,2,3,4,5]
new_list=mystery_function(my_list)
print(new_list)
            