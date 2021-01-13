import math
def get_name():
    name = input('What is your name?')
    print(name)



def reverse_it():
    string = input("Write something to be reversed: ")
    print(string[::-1])


def swap_em(a, b):
     a, b = b, a
     print('a = ',a, 'b = ', b)

def multiply_array(arr):
    print(math.prod(arr))

def fizzbuzz(num):
    if num % (3*5) == 0:
        print('fizzbuzz')
    elif num % 3 == 0:
        print('fizz')
    elif num % 5 == 0:
        print('buzz')
    else:
        print('archer') 

def fibonacci():
    fibs = [1,1]
    index = input('Which fibonacci number do you want?')
    while len(fibs) < int(index):
         length = len(fibs)
         nextFib = fibs[length-2] + fibs[length-1]
         fibs.append(nextFib)
    print(f'{fibs[len(fibs)-1]} is the fibonacci number at position {index}')


def search_array(arr, val):
    if val in arr:
        print('true')
    else:
        print('false')  

  
def palindrome(str):
    rev = str[::-1]
    if str == rev:
        print(str, 'is a palindrome')
    else:
        print(str, 'is not a palindrome')


def has_dupes(arr):
    arr_set = set(arr)

    if len(arr) != len(arr_set):
        print('contains duplicates')
    else:
        print('does not contain duplicates')

