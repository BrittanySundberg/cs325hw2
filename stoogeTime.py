# Brittany Sundberg
# CS 325 Fall 2020
# HW1 problem 5


import timeit

setup_code_1 = '''
import random
import math
'''
time_code_1 = '''
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

n_1 = 50
array_1 = []

for i in range(n_1):
    array_1.append(random.randint(0,10000))

new_array_1 = StoogeSort(array_1, 0, len(array_1)-1)
'''
print("Array size n = 50. Time = ", timeit.timeit(setup = setup_code_1,
                    stmt=time_code_1,
                    number=1))


setup_code_2 = '''
import random
import math
'''
time_code_2 = '''
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

n_2 = 100

array_2 = []


for i in range(n_2):
    array_2.append(random.randint(0,10000))

new_array_2 = StoogeSort(array_2, 0, len(array_2)-1)
'''
print("Array size n = 100. Time = ", timeit.timeit(setup = setup_code_2,
                    stmt=time_code_2,
                    number=1))


setup_code_3 = '''
import random
import math
'''
time_code_3 = '''
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
n_3 = 200

array_3 = []


for i in range(n_3):
    array_3.append(random.randint(0,10000))

new_array_3 = StoogeSort(array_3, 0, len(array_3)-1)
'''
print("Array size n = 200. Time = ", timeit.timeit(setup = setup_code_3,
                    stmt=time_code_3,
                    number=1))



setup_code_4 = '''
import random
import math
'''
time_code_4 = '''
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
n_3 = 300

array_3 = []


for i in range(n_3):
    array_3.append(random.randint(0,10000))

new_array_3 = StoogeSort(array_3, 0, len(array_3)-1)
'''
print("Array size n = 300. Time = ", timeit.timeit(setup=setup_code_4,
                                                     stmt=time_code_4,
                                                     number=1))



setup_code_5 = '''
import random
import math
'''
time_code_5 = '''
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

n_3 = 400

array_3 = []


for i in range(n_3):
    array_3.append(random.randint(0,10000))

new_array_3 = StoogeSort(array_3, 0, len(array_3)-1)
'''
print("Array size n = 400. Time = ", timeit.timeit(setup=setup_code_5,
                                                     stmt=time_code_5,
                                                     number=1))


setup_code_6 = '''
import random
import math
'''
time_code_6 = '''
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

n_3 = 500

array_3 = []


for i in range(n_3):
    array_3.append(random.randint(0,10000))

new_array_3 = StoogeSort(array_3, 0, len(array_3)-1)
'''
print("Array size n = 500. Time = ", timeit.timeit(setup=setup_code_6,
                                                     stmt=time_code_6,
                                                     number=1))



setup_code_7 = '''
import random
import math
'''
time_code_7 = '''
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

n_3 = 600

array_3 = []


for i in range(n_3):
    array_3.append(random.randint(0,10000))

new_array_3 = StoogeSort(array_3, 0, len(array_3)-1)
'''
print("Array size n = 600. Time = ", timeit.timeit(setup=setup_code_7,
                                                     stmt=time_code_7,
                                                     number=1))