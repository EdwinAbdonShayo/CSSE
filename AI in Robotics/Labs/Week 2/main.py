import random
import random
import string
import numpy as np
import matplotlib.pyplot as plt


List1 = [1,2,3,5,2,8,12,6,3,1,8,1,3,0,20,4,4,5,0,1,5,0,4,5,4,3,3,0]

# 1. find the max & min number in the List

print("\n\n1. Maximum and minimum value in a list\n")

print('The List:',List1)

print('\nthis is the maximum,', max(List1))

print('this is the minimum,', min(List1))

# 2. count the occurrences

print("\n\n2. Count Occurrences\n")

print('0 appears', List1.count(0), 'times')

print('3 appears', List1.count(3), 'times')

# 3. Basic Statistics

print("\n\n3. Basic Statistics\n")

sum = 0

for i in List1:
    sum += i

print('the sum of the numbers is', sum)

avg = sum / len(List1)

print('the average of the numbers is', avg)


# 4. Guessing Game

print("\n\n4. Guessing Game\n")

randomNum = random.randint(0,10)

minrand = random.randint(0,(randomNum-1))
maxrand = random.randint((randomNum+1),11)

guessNum = int(input(f"Guess a number\n\nLess than {maxrand} & greater than {minrand}\nInsert number here: "))

if guessNum == randomNum:
    print("You guessed it!")
else:
    print(f"You didn't guess it!, the correct guess was {randomNum}")
    

# 5. Python Dictionary
print("\n\n5. Python Dictionaries")

d1 = {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81, 10: 100, 11: 121, 12:
144, 13: 169, 14: 196, 15: 225}

print("\nHere is the first dictionary:\n", d1)

d2 = {}

for i in d1:
    if (d1[i] % 3) == 0:
        d2[i] = (d1[i])

print("\nHere is the second dictionary (Multiples of 3):\n", d2)


# 6. Sorting Dictionaries

print("\n\n6. Sorting Dictionaries")

# a. Sorted by Key

Dict1 = { '20':'2', '0.5':'1', 'embe':'21wq', '12':'banana', 'juice':'orange'}
sortedDict = {}

keyList = list(Dict1.keys())

for i in keyList:
    minKey = min(Dict1)
    sortedDict[minKey] = Dict1[minKey] 
    del Dict1[minKey] 

print(f'\nThe sorted dictionary with "Key"\n {sortedDict}')

# b. Sorted by Value

Dict1 = { '20':'2', '0.5':'1', 'embe':'21wq', '12':'banana', 'juice':'orange'}

sortedDictByValue = {}

keyList2 = list(Dict1.keys())


while Dict1:
    minKey = min(Dict1, key=lambda k: Dict1[k])

    sortedDictByValue[minKey] = Dict1[minKey]

    del Dict1[minKey]

print(f'\nThe sorted dictionary with "Value"\n {sortedDictByValue}')


# 7. Strings and files

print("\n\n7. Strings & Files\n")

random_text = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=30))

file_path = 'text.txt'

with open(file_path, 'w') as file:
    file.write(random_text)

with open(file_path, 'r') as file:
    content = file.read()

print(f'Here is the random text:\n{content}')


# 8. Multidimensional lists, arrays, matrices and Numpy

print("\n\n8. Multidimensional lists, arrays, matrices and Numpy\n")


# Define two bi-dimensional lists (matrices)
matrix_A = [
    [2, 5, 7, 6],
    [3, 5, 5, 4],
    [9, 7, 1, 0],
    [1, 0, 0, 5]
]

matrix_B = [
    [1, 2, 3, 4],
    [4, 3, 2, 1],
    [0, 1, 0, 1],
    [2, 0, 3, 4]
]

# a. Element-wise sum of two matrices
def matrix_sum(matrix_A, matrix_B):
    return [[matrix_A[i][j] + matrix_B[i][j] for j in range(len(matrix_A[0]))] for i in range(len(matrix_A))]

# b. Matrix product of two matrices
def matrix_product(matrix_A, matrix_B):
    rows_A = len(matrix_A)
    cols_A = len(matrix_A[0])
    cols_B = len(matrix_B[0])

    # Initialize result matrix with zeros
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += matrix_A[i][k] * matrix_B[k][j]
    
    return result

# Perform both operations
sum_result = matrix_sum(matrix_A, matrix_B)
product_result = matrix_product(matrix_A, matrix_B)

print(f'The sum of two bi-dimensional list\n{sum_result}\nThe product of two bi-dimensional list\n{product_result}')


# 9. Plotting with pyplot

print("\n\n9. Plotting with pyplot\n")

# a. Plot the sine function between -pi and pi
x_sine = np.linspace(-np.pi, np.pi, 500)
y_sine = np.sin(x_sine)

# b. Plot the natural logarithm of the square root of values between 0 and 100 with step 0.1
x_log_sqrt = np.arange(0.1, 100, 0.1)  # start from 0.1 to avoid log(0) issue
y_log_sqrt = np.log(np.sqrt(x_log_sqrt))

# Create subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 5))

# Plot a. Sine function
ax1.plot(x_sine, y_sine, label='sin(x)', color='blue')
ax1.set_title('Sine Function')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.grid(True)
ax1.legend()

# Plot b. Natural logarithm of square root
ax2.plot(x_log_sqrt, y_log_sqrt, label='ln(sqrt(x))', color='green')
ax2.set_title('Natural Logarithm of Square Root')
ax2.set_xlabel('x')
ax2.set_ylabel('ln(sqrt(x))')
ax2.grid(True)
ax2.legend()

# Show plots
plt.tight_layout()
plt.show()

print("Plotted\n\n\nThe End!")
