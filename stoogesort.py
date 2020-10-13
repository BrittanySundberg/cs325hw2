# Brittany Sundberg
# CS 325 Fall 2020
# HW2 problem 5

import math
infile = open('data.txt', 'r')
all_arrays = []

with open('data.txt', 'r') as infile:
    temp_array = []
    for line in infile:
        string = line.strip()
        list = string.split()
        for i in range(0, len(list)):
            list[i] = int(list[i])
        list.pop(0)
        all_arrays.append(list)


def StoogeSort(array, low, high):
    #if the section we're looking at is only 2 elements and they need to be switched, switch them
    if (high-low+1) == 2 and (array[low] > array[high]):
        temp = array[low]
        array[low] = array[high]
        array[high] = temp
    #if the section we're looking at is more than 2 elements, we need to recursively call the function on smaller subsections
    elif (high-low+1) > 2:
        n = high-low+1
        m = math.ceil((2*n)/3)
        StoogeSort(array, low, low+m-1) #lower third of the currently-looked at portion of the array
        StoogeSort(array, (high-m+1), high) #upper third of the currently-looked at portion of the array
        StoogeSort(array, low, low+m-1) #lower third again to see if it needs to be adjusted.
    return array


for array in all_arrays:
    StoogeSort(array, 0, len(array)-1)



with open('stooge.out', 'w') as outfile:
    for array in all_arrays:
        string_out = ""
        for element in array:
            string_out += str(element)
            string_out += " "
        string_out += '\n'
        outfile.write(string_out)
