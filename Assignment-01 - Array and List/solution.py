# Solution for Assignment-1 | Array and List

# Q1. Give an array with some integer type value write a python script to sort array value ?

from array import *

arr = array('i', [14, 212, 332, 4, 545, 66, 7])
arr_list = list(arr)
arr_list.sort()
sorted_arr = sorted(arr_list)
print(sorted_arr)



# Q2. Give a list of hetrogenous elemnets write a python script to remove all the non int value from list ?

list_het = (1, 5, 12, 34, 'Ravikant', 3534, 'Raju', 637, 'Rahul', 12.5, 35.9)
list_int = [i for i in list_het if isinstance(i,  int)]
print(list_int)

# Q3. Write a python script  to calculate average of elements of list ?

list_elements = [87, 45, 66, 23, 67, 34]

total = sum(list_elements)
count = len(list_elements)

avg = total/count

print(avg)


# Q4. Write a python script to create a list to first  n prime numbers ?

n = int(input("Enter how many prime numbers you want: "))

primes = []
num = 2

while len(primes) < n:
    for i in range(2, num):
        if num % i == 0:
            break
    else:
        primes.append(num)
    num += 1

print("First", n, "prime numbers:", primes)

# Q5. Write a python script to create a list to first n term of febonacci series ?

n = int(input("Enter how many Fibonacci terms you want: "))

fibonacci = []

a, b = 0, 1
for _ in range(n):
    fibonacci.append(a)
    a, b = b, a + b

print("First", n, "Fibonacci terms:", fibonacci)
